import cv2
import os
import argparse

from limelight import limelight

def parse_opt():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--camera',       type=int,   default=0,                      help='camera index number')
    parser.add_argument('--yolo_weights', type=str,   default='models/class_full.pt', help='path to localizer model file')
    parser.add_argument('--enet_weights', type=str,   default='models/taxon_full.pt', help='path to classifier model dir')
    parser.add_argument('--dst',          type=str,   default='data',                 help='destination folder for data')
    parser.add_argument('--split_n',      type=tuple, default=(3,3),                  help='x,y splits for input frame')
    parser.add_argument('--resolution',   type=tuple, default=(416,416),              help='resolution for yolo model')

    return(parser.parse_args())
    
def main(opt):
    vision=limelight(opt.camera,opt.yolo_weights,opt.enet_weights,opt.dst,opt.split_n,opt.resolution)
        
    video=cv2.VideoCapture(vision.camera) #capture frames from camera stream, default key = 0

    if video.isOpened():
        while video.isOpened():
            ret,frame=video.read()
            
            if ret:
                vision.split_frames(frame) #split captured frame into columns and rows based on split_n (x,y)
                vision.grab_insects() #collect predicted bounding boxes and classifications 

    else:
        print('error opening video capture')

def run(**kwargs):
    opt = parse_opt()
    for k, v in kwargs.items():
        setattr(opt, k, v)
    main(opt)
    return opt

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)   
