import os
import shutil
print(os.name)
print(os.listdir('.'))
print(os.listdir('..'))

if os.path.exists('mydir'):
    print('mydir exist')
else:
    os.mkdir('mydir')

os.chdir('mydir')
os.makedirs('.\\dir1\\dir2\\dir3')
f=open('myfile','w')
f.write('visnu kumar\n')
f.write('visnu kumar\n')
os.chdir('.\\dir1')
g=open('myfile','w')
g.write('visnu kumar\n')
f.close()
g.close()
