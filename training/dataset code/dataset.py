import os,math,shutil,cv2,json

class dataset:
    def __init__(self,img_src,label_src,dst):
        self.img_src=img_src
        self.img={}
        self.label=label_src
        self.dst=dst
        self.test=[]
        self.train=[]
        self.val=[]

        self.label_data=labels(label_src)
        self.taxa={}
        label_names=list(self.label_data)
        print(len(label_names))
        
        files=list(set(os.listdir(img_src)).intersection(label_names))
        if len(files)>=400:
            self.img=files

            for img in self.img:
                taxon='_'.join(img.split('_')[3:5])
                if not '_' in taxon:taxon='insect'
                
                    
                if not taxon in self.taxa.keys():self.taxa[taxon]=[]
                self.taxa[taxon].append(img)

    def test_set(self,count):
        print('Splitting test data')
        self.test_dir=f'{self.dst}/images/test/'
        self.test=[]
        
        for i,tax in enumerate(self.taxa.keys()):         
            self.test+=[(tax,img) for i,img in enumerate(self.taxa[tax]) if i<count]
            
            progress((i+1)/len(self.img))

    def split_set(self,percent=.7,use=1):
        print('Splitting training and validation data')
        self.train_dir,self.val_dir=f'{self.dst}/images/train/',f'{self.dst}/images/val/'
        self.train,self.val=[],[]
        self.total,self.use=0,0
        
        files=remove(self.img,[img[1] for img in self.test])
        self.total+=len(files)
        files=files[:math.ceil(len(files)*use)]
        self.use+=len(files)

        taxa=invert(self.taxa)
        
        for j,img in enumerate(files):
            taxon=taxa[img]
            
            if j<math.floor(len(files)*percent):
                self.train.append((taxon,img))
            else:
                self.val.append((taxon,img))


    def save_test(self):
        if not os.path.exists(self.test_dir):new_folder(self.test_dir)

        print('Saving testing images')
        for i,img in enumerate(self.test):
            shutil.copy(f'{self.img_src}/{img[1]}',f'{self.test_dir}/{img[1]}')
            progress((i+1)/len(self.test))

    def save_split(self):
        if not os.path.exists(self.train_dir):new_folder(self.train_dir)
        if not os.path.exists(self.val_dir):new_folder(self.val_dir)

        print('Saving training images')
        for i,img in enumerate(self.train):
            shutil.copy(f'{self.img_src}/{img[1]}',f'{self.train_dir}/{img[1]}')
            progress((i+1)/len(self.train))

        print('Saving validation images')
        for i,img in enumerate(self.val):
            shutil.copy(f'{self.img_src}/{img[1]}',f'{self.val_dir}/{img[1]}')
            progress((i+1)/len(self.val))

    def save_labels(self,level):
        self.level=level
        self.key=[]
        
        new_folder(f'{self.dst}/{level}/labels/test/')
        new_folder(f'{self.dst}/{level}/labels/train/')
        new_folder(f'{self.dst}/{level}/labels/val/')

        with open(f'{self.dst}/data.txt','w') as output:output.write('set taxon x y w h\n')

        for img in self.test:self.save_box(img,'test')
        for img in self.train:self.save_box(img,'train')
        for img in self.val:self.save_box(img,'val')

        with open(f'{self.dst}/bugnet_{level}.yaml','w') as y:
            y.write('\n'.join([f'train: {self.dst}/images/train',
                               f'val: {self.dst}/images/val',
                               f'nc: {len(self.key)}',
                               f'names: {self.key}']))

    def show_boxes(self):
        for img in list(set(self.test+self.train+self.val)):
            image=cv2.imread(f'{self.img_src}/{img[1]}')
            
            rows=self.label_data[img[1]]
            
            for row in rows:
                center,dim=(float(row[0]),float(row[1])),(float(row[2]),float(row[3]))
                    
                p1,p2=unbox(center,dim)
                center,dim=box([clamp(p1[0],0,1),clamp(p1[1],0,1)],[clamp(p2[0],0,1),clamp(p2[1],0,1)])
                p1,p2=unbox(center,dim,size=image.shape)
                
                image = cv2.rectangle(image,(math.floor(p1[0]),math.floor(p1[1])),(math.floor(p2[0]),math.floor(p2[1])),(0,0,0),2)
                print(f'{self.img_src}/{img[1]}\n{row}\n{center} {dim} {p1} {p2}')
                print(image.shape)
                cv2.imshow(f'{self.img_src}/{img[0]}/{img[1]}',image)
                cv2.waitKey(0)
                if input('Break?')=='y':break 

    def save_box(self,img,mode):
        taxon='_'.join(img[1].split('_')[:(1+self.level)])
        if not '_' in taxon:taxon='insect'

        
        if not taxon in self.key:self.key.append(taxon)

        taxon=self.key.index(taxon)
            
        rows=self.label_data[img[1]]
        data,labels=[],[]
        
        for row in rows:
            center,dim=(float(row[0]),float(row[1])),(float(row[2]),float(row[3]))
            p1,p2=unbox(center,dim)
            center,dim=box([clamp(p1[0],0,1),clamp(p1[1],0,1)],[clamp(p2[0],0,1),clamp(p2[1],0,1)])

            labels.append(f'{taxon} {center[0]} {center[1]} {dim[0]} {dim[1]}')
            data.append(f'{mode} {self.key[taxon]} {center[0]} {center[1]} {dim[0]} {dim[1]}')
            
        with open(f'{self.dst}/{self.level}/labels/{mode}/{img[1].replace("jpg","txt")}','w') as output:
            output.write('\n'.join(labels))
        with open(f'{self.dst}/data.txt','a') as output:
            output.write('\n'.join(data))
        

    def save(self,level):
        self.save_test()
        self.save_split()
        self.save_labels(level=level)

def invert(dic):
    out={}
    for k,i in dic.items():
        for new in i:out[new]=k
    return(out)

def new_folder(path):
    text=''
    for word in path.split('/'):
        text+=f'{word}/'
        if not os.path.exists(text):os.mkdir(text)

def remove(v1,v2):return [item for item in v1 if not item in v2]

def labels(path):
    print("Extracting label data")
    with open(path,'r') as labels:
        datadict=json.load(labels)

    data={}
    for key,item in datadict.items():
        if len(item.keys())>0:
            data[key]=[box['box'] for n,box in item.items() if type(box)==type({})]
    
    return(data)        
    
def clamp(x,l,u):
    if x<l:return(l)
    if x>u:return(u)
    return x

def box(pos1,pos2):
    mid = [(pos2[0]+pos1[0])/2,(pos2[1]+pos1[1])/2]
    dim = [pos2[0]-pos1[0],pos2[1]-pos1[1]]
    return mid,dim
            
def unbox(center,dims,size=(1,1)):
    p1 = ((center[0]-dims[0]/2)*size[1],(center[1]-dims[1]/2)*size[0])
    p2 = ((center[0]+dims[0]/2)*size[1],(center[1]+dims[1]/2)*size[0])
    return p1,p2

def progress(percent,char='=',length=50):
    print(f'|{math.floor(percent*length)*char}{math.ceil((1-percent)*length)*" "}| {round(percent*100,2)}%     ',end='\r')
    if percent==1:print()

