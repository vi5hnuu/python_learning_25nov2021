import os,sys,getopt

if len(sys.argv)==1:
    print(os.listdir('.'))
    sys.exit(1)

try:
    options,arg=getopt.getopt(sys.argv[1:],'hlw')
    print(options)
    print(arg)
    for opt,arg in options:
        print(opt)
        if opt=='-h':
            print('mydir.py -h -i -w')
            sys.exit(2)
        elif opt=='-l':
            lst=os.listdir('.')
            print(*lst,sep='\n')
        elif opt=='-w':
            lst=os.listdir('.')
            print(*lst,sep='\t')
except getopt.GetoptError:
    print("mydir.p -h -l -w")