import os

name = '도사견'
file_name = name+'.txt'
folder = './'+name+'/'
os.mkdir(folder)
lines = []
with open(file_name,'r') as f:
    data = f.readlines()
for line in data:
    line = line.strip()
    if '. ' in line:
        for split_line in line.split('. '):
            lines.append(split_line.strip())
    else:
        lines.append(line)
for i in range(len(lines)):
    with open(folder+str(i)+'.txt','w') as f:
        f.write(lines[i])