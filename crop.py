#!/usr/bin/env python3
import os
import cv2

filePath = '../case3_test'
fileNames = os.listdir(filePath)

for name in fileNames:
    imgFile = os.path.join(filePath, name)
    img = cv2.imread(imgFile)
    cropImg = img[765:985, 1080:1500]
    cv2.imwrite('{}/crop_{}.png'.format(filePath, name), cropImg)
