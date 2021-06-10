#!/user/bin/env python
# -*- coding:utf-8 -*-


import os, random, shutil
from PIL import Image


def copyFile(fileDir, tarDir1, tarDir2, rate):
    # 1
    pathDir = os.listdir(fileDir)
    num = len(pathDir)
    print(fileDir,num)

    # 2
    sample = random.sample(pathDir, int(num * rate))
    # 3
    for name in pathDir:
        if name in sample:
            #shutil.copyfile(os.path.join(fileDir,name), os.path.join(tarDir1,name))
            saveDir = os.path.join(tarDir1,name)
        else:
            #shutil.copyfile(os.path.join(fileDir,name), os.path.join(tarDir2,name))
            saveDir = os.path.join(tarDir2,name)
            
        #change to jpg
        im = Image.open(os.path.join(fileDir,name))
        name_jpg = os.path.splitext(name)[0]+'.jpg'
        im.save(saveDir)

if __name__ == '__main__':
    folders = ['NORM','TUM']
    rate = 0.8
    for folder in folders:
        fileDir = os.path.join('.','NCT-CRC-HE-100K',folder)
        tarDir1 = os.path.join('.','NCT-CRC-HE-100K','train',folder)
        tarDir2 = os.path.join('.','NCT-CRC-HE-100K', 'val', folder)
        
        for dir in [fileDir,tarDir1,tarDir2]:
            if not os.path.exists(dir):
                os.makedirs(dir)
        copyFile(fileDir, tarDir1, tarDir2, rate) #rate means the percentage of images move to target1
