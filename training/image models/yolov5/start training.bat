if not defined in_subprocess (cmd /k set in_subprocess=y ^& %0 %*) & exit )
cd yolov5

//python ../format.py "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/1/0/labels" "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/1/labels"
//python train.py --batch 64 --epochs 10 --data "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/1/bugnet_0.yaml" --img 416 --workers 1

python ../format.py "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/lepdata/0/labels" "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/lepdata/labels"
python train.py --batch 64 --epochs 50 --data "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/lepdata/bugnet_0.yaml" --img 416 --workers 1

python ../format.py "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/lepdata/4/labels" "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/lepdata/labels"
python train.py --batch 64 --epochs 50 --data "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/lepdata/bugnet_4.yaml" --img 416 --workers 1