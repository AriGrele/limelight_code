from dataset import dataset
import os

path='E:/image data/insect_orders'
xprize='C:/Users/Ari/Documents/scripts/xprize/database files/'

data=dataset(f'{path}/Lepidoptera - Copy',
             f'{xprize}/annotations/lep_annotations.json',
             f'{xprize}/image_splits/lepdata')

data.split_set()
data.test_dir=''

for level in [0,4]:
    print(f'{100}% for {["Class","Order","Family","Genus","Species"][level]}')
    data.save(level)
    print(data.total,data.use)

#for percent in [1,2,5,10,25,50,75,100]:
#    data=dataset(test.img_src,test.label,f'{test.dst}/{percent}')
#    data.test,data.test_dir=test.test,test.test_dir
#    data.split_set(use=percent/100)
#    for level in [0]:
#        print(f'{percent}% for {["Class","Order","Family","Genus","Species"][level]}')
#        data.save(level)
#        print(data.total,data.use)
