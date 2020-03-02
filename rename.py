import os

filePath = '/home/dongjun/djplace/n22'
fileNames = os.listdir(filePath)
i = 0
for name in fileNames:
    src = os.path.join(filePath, name)
    dst = os.path.basename(filePath) + '_' + str(i) + '.png'
    dst = os.path.join(filePath, dst)
    os.rename(src, dst)
    i += 1
