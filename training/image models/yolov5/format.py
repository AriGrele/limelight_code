import shutil,argparse

def main(opt):
    try:
        shutil.rmtree(opt.dst)
    except:Exception
    shutil.copytree(opt.src,opt.dst)

def parse_opt():
    parser=argparse.ArgumentParser()
    parser.add_argument('src',type=str,default='',help='source folder')
    parser.add_argument('dst',type=str,default='',help='destination folder')
    return parser

if __name__=="__main__":
    opt=parse_opt().parse_args()
    main(opt)



