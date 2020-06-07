import cv2
from pathlib import Path
from PIL import Image
import barcode
from barcode.writer import ImageWriter

import numpy as np
from os import listdir
from os.path import isfile, join

path = 'C:/personal-git/aresta-barcode/src/app/images/print-folder/'
fileName = "mergeAll"
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
allImg = []

print("Merging the following files: ")
for i in range(len(onlyfiles)):
    fullPath = join(path,onlyfiles[i])
    onlyfiles[i] = fullPath
    print(onlyfiles[i])
    toImg = cv2.imread(onlyfiles[i])
    allImg.append(toImg)

allImg_array = np.array(allImg)
fullImg = cv2.hconcat(allImg_array)
cv2.imwrite("C:/personal-git/aresta-barcode/src/app/images/mergeAll/{}.jpeg".format(fileName), fullImg)