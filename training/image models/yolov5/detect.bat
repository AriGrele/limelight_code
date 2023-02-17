if not defined in_subprocess (cmd /k set in_subprocess=y ^& %0 %*) & exit )
cd yolov5

python detect.py --weights "C:/Users/Ari/Documents/scripts/xprize/models/image models/yolov5/yolov5/runs/train/exp10/weights/best.pt" --iou-thres .1 --source "C:/Users/Ari/Documents/scripts/xprize/Limelight code/data/frames" --conf-thres 0.01 --img-size 416