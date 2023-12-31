import os
import shutil
import os
import shutil
import stat

print(os.name)
print(os.listdir('.'))
print(os.listdir('..'))

if os.path.exists('mydirr'):
    print('mydir exist')
else:
    os.mkdir('mydirr')

os.chdir('mydirr')
os.makedirs('.\\dirr1\\dirr2\\dirr3')
f=open('mmyfile','w')
f.write('visnu kumar\n')
f.write('visnu kumar\n')
f.close()
stats=os.stat('mmyfile')
print('size= ',stats.st_size)

os.rename('mmyfile','yourfile')
shutil.copyfile('yourfile','ourfile')
os.remove('yourfile')

curpath=os.path.abspath('.')
os.path.join(curpath,'yourfile')
if os.path.isfile(curpath):
    print('file exist')
else:
    print('not exist')

