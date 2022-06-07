# Pet Relation Extraction Dataset
- Naver Boostcamp AI Tech 3
- NLP Data Annotation Project
- 한국어 위키피디아에서 추출한 반려동물 관련 원시 데이터를 활용한 Relation Extraction Dataset 제작

## [Solution Presentation](https://github.com/boostcampaitech3/level2-data-annotation_nlp-level2-nlp-08/blob/main/assets/08_presentation.pdf)

## [Wrapup Report](https://github.com/boostcampaitech3/level2-data-annotation_nlp-level2-nlp-08/blob/main/assets/Data_Annotation_NLP_%ED%8C%80_%EB%A6%AC%ED%8F%AC%ED%8A%B8(8%EC%A1%B0).pdf)

## [Guideline](https://github.com/boostcampaitech3/level2-data-annotation_nlp-level2-nlp-08/blob/main/assets/08_guideline.pdf)

## [Relation Map](https://github.com/boostcampaitech3/level2-data-annotation_nlp-level2-nlp-08/blob/main/assets/08_relation.xlsx)

## About Us

임동진|정재윤|조설아|허치영|이보림|
:-:|:-:|:-:|:-:|:-:
<img src='https://avatars.githubusercontent.com/u/72785706?v=4' height=80 width=80px></img>|<img src='https://avatars.githubusercontent.com/u/71070496?v=4' height=80 width=80px></img>|<img src='https://avatars.githubusercontent.com/u/90924434?v=4' height=80 width=80px></img>|<img src='https://avatars.githubusercontent.com/u/69616444?v=4' height=80 width=80px></img>|<img src='https://avatars.githubusercontent.com/u/55435898?v=4' height=80 width=80px></img>|
[Github](https://github.com/idj7183)|[Github](https://github.com/kma7574)|[Github](https://github.com/jarammm)|[Github](https://github.com/mooncy0421)|[Github](https://github.com/bo-lim)

### Contribution  

`임동진` &nbsp; : &nbsp; Data Annotation • Calculate IAA <br>
`정재윤` &nbsp; : &nbsp; Data Annotation • Make Relation Map <br>
`조설아` &nbsp; : &nbsp; Data Annotation • Make Guideline <br>
`허치영` &nbsp; : &nbsp; Data Annotation • Modeling <br>
`이보림` &nbsp; : &nbsp; Data Annotation • Make Guideline <br>

## Data Overview
- Train data : 1579
- Test data : 176
- Number of class : 10
    ```
    '동물:서식지' '동물:대체표현' '동물:신체적특징' '동물:비신체적특징' '동물:사냥감' '동물:역할' '동물:유래' '동물:개체수' 
    '집단:하위집단' '관계 없음' 
    ```

## Results (KLUE/BERT-base)
- **Fleiss' Kappa** : 0.79
- **Micro F1** : 57.2581
- **AUPRC** : 60.4493
-  Selected as **Novel King**
