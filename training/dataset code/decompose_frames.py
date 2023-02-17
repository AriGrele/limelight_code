import os,cv2

path='E:\camtests\cropped'
dst='../../database files/image_splits/test_sets'

for file in os.listdir(path):
    print(file)
    name=file.replace(".mp4","")
    if not os.path.exists(f'{dst}/{name}'):os.mkdir(f'{dst}/{name}')

    cap=cv2.VideoCapture(f'{path}/{file}')

    c=0
    while(cap.isOpened()):
        c+=1
        ret,frame=cap.read()
        
        if not ret:break

        cv2.imwrite(f'{dst}/{name}/{name}_{c}.jpg',frame)

    cap.release()

    
    
