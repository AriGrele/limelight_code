if not defined in_subprocess (cmd /k set in_subprocess=y ^& %0 %*) & exit )
git clone https://github.com/WongKinYiu/yolov7
cd yolov7
pip install -r requirements.txt