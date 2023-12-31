import sys
import getopt

if len(sys.argv)!=7:
    print('incorrect usage')
    print('change -o oldword -n newword -f filename')
    sys.exit(1)
try:
    options,arg=getopt.getopt(sys.argv[1:],'ho:n:f:')
except getopt.GetoptError:
    print('change -o oldword -n newword -f filename')
else:
    for opt,argg in options:
        if opt=='-h':
            print('change -o oldword -n newword -f filename')
            sys.exit(2)
        elif opt=='-o':
            oldword=argg
        elif opt=='-n':
            newword=argg
        elif opt=='-f':
            filename=argg
    else:
            print('old word :',oldword)
            print('new word :',newword)
            print('filename :',filename)
            if oldword and newword and filename:
                f=open(filename,'r')
                data=f.read()
                f.close()
                data=data.replace(oldword,newword)
                f=open(filename,'w')
                f.write(data)
                f.close()