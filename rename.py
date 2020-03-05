#!/usr/bin/env python3
import os
from datetime import datetime
today = datetime.today().strftime('%m%d')

def rename():
    filePath = input("Enter the path of the directory: i.e.(case1/cycles or case1/cycles_denoise) \n")
    #filePath = '/home/dongjun/djplace/synth-ml/examples/hello_world/synth_ml_data/case1/cycles'
    filePath = '/home/dongjun/djplace/synth-ml/examples/hello_world/synth_ml_data/{}'.format(filePath)
    fileNames = os.listdir(filePath)
    i = 0
    for name in fileNames:
        src = os.path.join(filePath, name)
        dst = os.path.basename(filePath) + '_' + today + '_' + str(i) + '.png'
        dst = os.path.join(filePath, dst)
        os.rename(src, dst)
        i += 1

try:
    rename()
except Exception as e:
    print(e)
finally:
    print("Finished.")
