import cv2
import numpy as np

from pathlib import Path
from PIL import Image

import barcode
from barcode.writer import ImageWriter

from os import listdir
from os.path import isfile, join

import customeFunctions

def stickerMergeFiles(column):
    # Path to where all the individual images are
    path = 'C:/personal-git/aresta-barcode/src/app/images/pallet-done'

    # Save new file to the path below 
    saveToPath = "C:/personal-git/aresta-barcode/src/app/images/pallet-merge-done"

    # Search for all the files in directory
    columnStickerImg = [f for f in listdir(path) if isfile(join(path, f))]
    # list for all the images full path
    allImgFullPath = []
    singleSheet = []

        # Add full path to each file
    for i in range(len(columnStickerImg)):
        # Merge the file name to the rest of the path
        fullPath = join(path,columnStickerImg[i])
        columnStickerImg[i] = fullPath

    for i in range(len(columnStickerImg)):
        if i%column == 0:
            for j in range(column):
                sign = i+j
                singleSheet.append(columnStickerImg[sign])
                # singleSheet.append(sign)
                cityId = singleSheet[0][60:62]
                streetId = singleSheet[0][63:65]
            print("Creating Cidade{}-Rua{}".format(cityId,streetId))
            # print(singleSheet)

            for k in range(len(singleSheet)):
                #Creates image object
                toImg = cv2.imread(singleSheet[k])
                # Saves image object to list
                allImgFullPath.append(toImg)

            # Convers the list to array
            allImgFullPath_array = np.array(allImgFullPath)

            # Combines all the individual column images to one image
            fullImg = cv2.vconcat(allImgFullPath_array)

            # Save the file to path
            cv2.imwrite("{}/{}.PNG".format(saveToPath,"Cidade{}-Rua{}".format(cityId,streetId)), fullImg)
            allImgFullPath.clear()
            singleSheet.clear()

# column = 5
# stickerMergeFiles(column)