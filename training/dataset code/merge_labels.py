import os,json

path='C:/Users/Ari/Documents/scripts/bugfinder/inat2017/data/labels'
dst='C:/Users/Ari/Documents/scripts/xprize/database files/annotations/inat2017.json'

lines={}

if '.txt' in path:
    with open(f'{path}/{folder}/{file}') as data:
                    line=[row.strip().split(' ') for row in data]
                    line={row[0]:row[1:] for row in line if row[2]!='0' and row[3]!='0'}

                    for i,box in enumerate(line):
                        lines[file][i+1]={'box':[float(n) for n in box.split(' ')[1:]]}

else:
    for folder in os.listdir(path):
        for count,file in enumerate(os.listdir(f'{path}/{folder}')):
            if count%1000==0:print(count)
            
            if '.txt' in file:
                with open(f'{path}/{folder}/{file}') as data:
                    line=[row.strip() for row in data]

                    file=file.replace('.txt','.jpg')
                    
                    if not file in lines.keys():lines[file]={}
                    for i,box in enumerate(line):
                        lines[file][i+1]={'box':[float(n) for n in box.split(' ')[1:]]}
                    

with open(dst,'w') as f:
  json.dump(lines,f,ensure_ascii=False)


