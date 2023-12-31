import os
def convert(num):
    for x in ['bytes','KB','MB','GB','TB']:
        if num<1024.0:
            return "%3.1f %s" %(num,x)
        num/=1024.0

def filesize(filepath):
    if os.path.isfile(filepath):
        fileinfo=os.stat(filepath)
        return convert(fileinfo.st_size)

filepath=r'.\problem_23.2.py'
print(filesize(filepath))