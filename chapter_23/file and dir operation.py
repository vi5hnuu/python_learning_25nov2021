import os
import shutil

print(os.name)
print(os.getcwd())
print(os.listdir('.'))
print(os.listdir('..'))

if os.path.exists('sampledata'):
    print('File already exists')
else:
    os.mkdir('sampledata')

#os.chdir('chapter_23')
#os.makedirs('\\dir\\dir\\dir')

curpath=os.path.abspath('.')
os.path.join(curpath,'sampledata')
if os.path.isfile(curpath):
    print('your file exist')
else:
    print('ypur file not exist')