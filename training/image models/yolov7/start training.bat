if not defined in_subprocess (cmd /k set in_subprocess=y ^& %0 %*) & exit )
cd yolov7

python ../format.py "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/1/0/labels" "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/1/labels"
python train.py --device 0 --batch-size 16 --epochs 10 --data "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/1/bugnet_0.yaml" --img 416 416 --workers 1 --weights "" --cfg cfg/training/yolov7.yaml

python ../format.py "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/2/0/labels" "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/2/labels"
python train.py --device 0 --batch-size 16 --epochs 10 --data "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/2/bugnet_0.yaml" --img 416 416 --workers 1 --weights "" --cfg cfg/training/yolov7.yaml

python ../format.py "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/5/0/labels" "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/5/labels"
python train.py --device 0 --batch-size 16 --epochs 10 --data "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/5/bugnet_0.yaml" --img 416 416 --workers 1 --weights "" --cfg cfg/training/yolov7.yaml

python ../format.py "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/10/0/labels" "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/10/labels"
python train.py --device 0 --batch-size 16 --epochs 10 --data "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/10/bugnet_0.yaml" --img 416 416 --workers 1 --weights "" --cfg cfg/training/yolov7.yaml

python ../format.py "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/25/0/labels" "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/25/labels"
python train.py --device 0 --batch-size 16 --epochs 10 --data "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/25/bugnet_0.yaml" --img 416 416 --workers 1 --weights "" --cfg cfg/training/yolov7.yaml

python ../format.py "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/50/0/labels" "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/50/labels"
python train.py --device 0 --batch-size 16 --epochs 10 --data "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/50/bugnet_0.yaml" --img 416 416 --workers 1 --weights "" --cfg cfg/training/yolov7.yaml

python ../format.py "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/75/0/labels" "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/75/labels"
python train.py --device 0 --batch-size 16 --epochs 10 --data "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/75/bugnet_0.yaml" --img 416 416 --workers 1 --weights "" --cfg cfg/training/yolov7.yaml