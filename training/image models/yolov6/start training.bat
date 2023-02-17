if not defined in_subprocess (cmd /k set in_subprocess=y ^& %0 %*) & exit )
cd YOLOv6

python ../format.py "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/1/0/labels" "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/1/labels"
python tools/train.py --eval-final-only --batch-size 64 --epochs 10 --data-path "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/1/bugnet_0.yaml" --img 416 --workers 1

python ../format.py "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/2/0/labels" "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/2/labels"
python tools/train.py --eval-final-only --batch-size 64 --epochs 10 --data-path "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/2/bugnet_0.yaml" --img 416 --workers 1

python ../format.py "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/5/0/labels" "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/5/labels"
python tools/train.py --eval-final-only --batch-size 64 --epochs 10 --data-path "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/5/bugnet_0.yaml" --img 416 --workers 1

python ../format.py "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/10/0/labels" "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/10/labels"
python tools/train.py --eval-final-only --batch-size 64 --epochs 10 --data-path "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/10/bugnet_0.yaml" --img 416 --workers 1

python ../format.py "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/25/0/labels" "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/25/labels"
python tools/train.py --eval-final-only --batch-size 64 --epochs 10 --data-path "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/25/bugnet_0.yaml" --img 416 --workers 1

python ../format.py "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/50/0/labels" "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/50/labels"
python tools/train.py --eval-final-only --batch-size 64 --epochs 10 --data-path "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/50/bugnet_0.yaml" --img 416 --workers 1

python ../format.py "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/75/0/labels" "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/75/labels"
python tools/train.py --eval-final-only --batch-size 64 --epochs 10 --data-path "C:/Users/Ari/Documents/scripts/xprize/database files/image_splits/inat2017/75/bugnet_0.yaml" --img 416 --workers 1
