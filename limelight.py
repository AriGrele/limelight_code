import cv2
import torch
import time
import os
import re

from models import yolo
from efficientnet_pytorch import EfficientNet

class limelight:
    def __init__(self,camera,yolo_weights,enet_weights,dst,split_n,resolution,classifier):
        self.camera       = camera
        self.yolo_weights = yolo_weights
        self.enet_weights = enet_weights
        self.dst          = dst
        self.split_n      = split_n
        self.resolution   = resolution

        with open(f'{enet_weights}/params') as params: #number of classes in each taxonomic level
            self.nclass=[int(row.strip()) for row in params]

        self.frame  = []
        self.frames = []
        self.boxes  = []
        self.errors = 'errors.txt'
        self.stamp  = 'none'
        self.levels = ['Class','Order','Family','Genus','Species'] #taxonomic level labels

        self.yolo = torch.load(yolo_weights) #object localizer
        self.yolo.eval()

        if classifier == 'yolo': #species level yolo classifier
            self.enet = [torch.load(re.sub('/.+\\.pt$','/species.y.pt',yolo_weights))]
        else: #hierarchical classifier
            self.enet = [EfficientNet.from_pretrained(file, num_classes=self.nclass[i]) for i,file in enumerate(os.listdir(enet_weights))]

        self.enet.eval()
        
        if not os.path.exists(self.errors): #error logging
            with open(self.errors,'w') as e:e.write('errors\n')

        for folder in [dst,f'{dst}/images',f'{dst}/frames']: #create output folders
            if not os.path.exists(folder):
                os.mkdir(folder)

    def save_frames(self): #save split frames and original image for debug purposes
        for i,im in enumerate(self.frames):
            cv2.imwrite(f'{self.dst}/frames/{i}.jpg',im)

    def save_img(self): #save cropped images with filenames of timestamp / index
        for i,im in enumerate(self.insects):
            cv2.imwrite(f'{self.dst}/images/{self.stamp}_{i}.jpg',im)

    def save_cls(self): #save taxon predicitons with row names of taxonomic level / timestamp / index
        with open(f'{dst}/data.txt','a') as out:
            for i,dat in enumerate(self.classes):
                name=self.levels[i]
                for j,obj in enumerate(dat):
                    out.write(f'{name} {self.stamp}_{j} {" ".join(dat)}')

    def split_frames(self,img): #split frame into columns and rows based on split_n (x,y)

        def cumsum(x): #cumulative summation to generate start - stop indeces for image splitting
            out=[0]
            for v in x:out.append(v+out[-1])
            return(out)
        
        try:
            n=(int(self.split_n[0]),int(self.split_n[1]))
            
            h, w, channels = img.shape

            if h*w >0:
                x = cumsum([w//n[0]]*n[0])
                y = cumsum([h//n[1]]*n[1])

                self.frame =img #store original image and list of [original, split images]
                self.frames=[img]+[img[splity:y[j+1],splitx:x[i+1]] for i, splitx in enumerate(x) if i != n[0] for j, splity in enumerate(y) if j != n[1]]               

                self.save_frames()
                
        except Exception as e:
            print(e)
            with open(self.errors,'a') as log:
                log.write(f'{time.localtime()} {e}\n')
                          
    def grab_insects(self): #for list of frames, localize insects, classify insects, store images and predictions
        try:
            self.stamp=time.localtime()

            self.boxes=self.yolo(self.frame)
            self.insects=[self.frame[int(b[1]):int(b[3]),int(b[0]):int(b[2])] for box in self.boxes.xyxy for b in box]
            self.classes=[model(self.insects) for model in self.enet]

            self.save_img()
            self.save_cls()
            
        except Exception as e:
            print(e)
            with open(self.errors,'a') as log:
                log.write(f'{time.localtime()} {e}\n')
