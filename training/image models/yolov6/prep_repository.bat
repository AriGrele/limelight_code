if not defined in_subprocess (cmd /k set in_subprocess=y ^& %0 %*) & exit )
git clone https://github.com/meituan/YOLOv6
cd YOLOv6
pip install -r requirements.txt