from oauth2client.service_account import ServiceAccountCredentials
import gspread
import json
import glob
import re
import os
import pandas as pd
import html

scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'api_key.json', scope)
gc = gspread.authorize(credentials)

# 자신이 만든 구글 시트 이름
sh = gc.open('반려동물_데이터셋생성')
sheet = sh.worksheet('시트1')

# tagtog
#폴더 경로
folder_name = "./"

#context list
context_name_list = os.listdir(folder_name + "ann.json/master/pool")

#relation 폴더 경로
relation_folder_paths = glob.glob(folder_name + "ann.json/master/pool/*")

#context 폴더 경로
contexts_folders_paths = glob.glob(folder_name + "plain.html/pool")
# contexts_folders_paths = [folder_name + "plain.html/pool/" + c for c in context_name_list]


#anntation_lenged 정보
annotation_legend = folder_name + "annotations-legend.json"
with open(annotation_legend,"r") as f:
    annotation_legend = json.load(f)

def get_needed_relation_data(tmp_relation):
    subject_token = re.findall("\(+(.+)+\)",annotation_legend[tmp_relation["relations"][0]['classId']])[0].split("|")[0]
    print(len(tmp_relation["entities"]))
    if subject_token == tmp_relation['entities'][0]['classId']:
        sub_entity, obj_entity = tmp_relation['entities']
    else:
        obj_entity, sub_entity  = tmp_relation['entities']
    # get preprocessed entities
    def _get_entity(entity):
        outputs = entity['offsets'][0]
        outputs['type'] = annotation_legend[entity['classId']].split("-")[1].lower()
        return outputs
    
    output_subject = _get_entity(sub_entity)
    output_object = _get_entity(obj_entity)
    return output_subject, output_object

def get_label(relation_json):
    label_tag = relation_json['relations'][0]['classId'] #r_6
    try:
        _,sub_type, label = annotation_legend[re.findall("\(+(.+)+\|",annotation_legend[label_tag])[0]].split("-")
        return f"{sub_type}:{label}"
    except:
        _,sub_type, = annotation_legend[re.findall("\(+(.+)+\|",annotation_legend[label_tag])[0]].split("-")
        return f"{sub_type}:no_relation"

def get_context_from_html(html_file):
    html_file = re.sub(r"\n","", html_file)
    html_file = html.unescape(html_file) # 21-11-17 추가, &quot; 등 제거
    return re.findall("(<pre.+>)(.+)(</pre>)",html_file)[0][1]

def get_sentence_with_entites(subject_entity, object_entity, sentence):
    if subject_entity['start'] < object_entity['start']:
        entity1,entity2 = subject_entity, object_entity
    else:
        entity1,entity2 = object_entity, subject_entity
    
    #entity 시작 위치 및 길이 
    ett1_stt, ett1_len = entity1['start'], len(entity1['text'])
    ett2_stt, ett2_len = entity2['start'], len(entity2['text'])
    
    #문장 분리
    bf, ett1, mid, ett2, af = sentence[:ett1_stt], \
                            sentence[ett1_stt:ett1_stt+ett1_len], \
                            sentence[ett1_stt+ett1_len:ett2_stt], \
                            sentence[ett2_stt:ett2_stt+ett2_len], \
                            sentence[ett2_stt+ett2_len:]

    
    if subject_entity['start'] < object_entity['start']:
        ett1,ett2 = f"<sbj:{ett1}>", f"<obj:{ett2}>"
    else:
        ett1,ett2 = f"<obj:{ett1}>", f"<sbj:{ett2}>"
    
    return "".join([bf, ett1, mid, ett2, af])

#dataframe column
# id : context title(e.g : 카카오게임, 11번가 등)
# sentence w/o entity
# sentence w entity
# subject_entity
# object_entity
# class

id_list = []
sentence_list = []
sentence_with_entities_list = []
subject_entity_list = []
object_entity_list = []
relation_list = []


# tagtog 데이터를 CSV 형태로 변경
for context_name, relation_folder, contexts_folder in zip(context_name_list, relation_folder_paths, contexts_folders_paths):
    # relation files와 context files 리스트 출력
    file_ids = [file_name.split(".txt.")[0] for file_name in os.listdir(relation_folder)]
    file_nums = [ids.split("-")[1] for ids in file_ids]
    relation_files = [relation_folder + "/"+ file_id + ".txt.ann.json" for file_id in file_ids]
    context_files = [contexts_folder + "/"+ file_id + ".txt.plain.html" for file_id in file_ids]
    #json으로 된 relation data와 html로 된 context 데이터 읽기
    for relation_file, context_file, file_num in zip(relation_files,context_files, file_nums):
        #subject, object 정보 추출
        with open(relation_file, "r") as f:
            relation_json = json.load(f)
        try:
            tmp_subject, tmp_object = get_needed_relation_data(relation_json) #subject, object
            tmp_label = get_label(relation_json)
        except:
            continue
        print(f'tmp : {tmp_subject}, {tmp_object}, {tmp_label}')
        #sentence, sentence with entities 정보 추출
        with open(context_file, "r") as f:
            context_json = f.read()
        print(f'context : {context_json}')
        tmp_sentence = get_context_from_html(context_json)
        tmp_sentence_w_entities = get_sentence_with_entites(tmp_subject,tmp_object,tmp_sentence)
        
        #각 list에 데이터 저장
        id_list.append(f"{context_name}_{file_num}")
        sentence_list.append(tmp_sentence)
        sentence_with_entities_list.append(tmp_sentence_w_entities)
        subject_entity_list.append(tmp_subject)
        object_entity_list.append(tmp_object)
        relation_list.append(tmp_label.lower())
print(f'id_list:{id_list}')
# 구글시트에 입력
values = sheet.get_all_values()

header, rows = values[0], values[1:]
data = pd.DataFrame(rows, columns=header)

column_list = ["id","sentence","sentence_with_entity","subject_entity","object_entity","class"]
data = data[column_list]

sen_list =  list(data.sentence_with_entity.values)
print(len(sen_list))

sheet.resize(len(id_list)+1,10)
list_range = f"a2:f{len(id_list)+1}"
cell_list = sheet.range(list_range)

for i in range(len(cell_list)//len(column_list)):
    cell_list[(6*i)].value = id_list[i]
    cell_list[(6*i)+1].value = sentence_list[i]
    cell_list[(6*i)+2].value = sentence_with_entities_list[i]
    cell_list[(6*i)+3].value = str(subject_entity_list[i])
    cell_list[(6*i)+4].value = str(object_entity_list[i])
    cell_list[(6*i)+5].value = relation_list[i]
sheet.update_cells(cell_list)