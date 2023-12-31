import sys
import threading
import os
import shutil

def copy_file(input_file,output_file):
    shutil.copy(input_file,output_file)
    s=input_file+' copied!\n'
    print(s)

source=sys.argv[1]
target=sys.argv[2]

if not os.path.exists(source):
    print('source path do not exist')
    exit()
if not os.path.exists(target):
    os.mkdir(target)
os.chdir(source)
lst=os.listdir('.')
tharr=[]
for file in lst:
    sourcefilepath=source+'\\'+file
    targetfilepath=target+'\\'+file
    th=threading.Thread(target=copy_file,args=(sourcefilepath,targetfilepath))
    th.start()
    tharr.append(th)

for th in tharr:
    th.join()