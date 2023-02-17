import os

paths={'yolov5':'../image models/yolov5/yolov5/runs/detect',
       'yolov6':'../image models/YOLOv6/yolov6/runs/inference/exp',
       'yolov7':'../image models/yolov7/yolov7/runs/detect'}

#paths={'ground':'../../mix'}

names={'exp':'1','exp2':'2','exp3':'5','exp4':'10','exp5':'25','exp6':'50','exp7':'75'}
       
dst='lows.txt'

data=['model experiment image class x y w h']
for model,folder in paths.items():
    for exp in os.listdir(folder):
        print(model,exp)
        
        if exp in names.keys():name=names[exp]
        else:name=exp

        if 'labels' in os.listdir(f'{folder}/{exp}'):exp+='/labels'

        for file in [f for f in os.listdir(f'{folder}/{exp}') if '.txt' in f]:

            with open(f'{folder}/{exp}/{file}','r') as d:
                for row in d:
                    data.append(f'{model} {name} {file} {" ".join(row.strip().split(" ")[:5])}')

with open(dst,'w') as o:o.write('\n'.join(data))

