import torch

yolo.c = torch.hub.load('ultralytics/yolov5','custom','models/class.pt') #load and save yolov5 class model architecture 
torch.save(yolo.c, "models/class_full.pt")

yolo.s = torch.hub.load('ultralytics/yolov5','custom','models/species.y.pt') #load and save yolov5 species model architecture 
torch.save(yolo.s, "models/species.y_full.pt")

