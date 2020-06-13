import cv2
from pathlib import Path
from PIL import Image
import barcode
from barcode.writer import ImageWriter
import numpy as np
from os import listdir
from os.path import isfile, join
import customeFunctions

def aptMergeFiles(column,level,apt):
    # Path to where all the individual images are
    path = 'C:/personal-git/aresta-barcode/src/app/images/sticker-apt-single-done/'

    # Save new file to the path below 
    saveToPath = "C:/personal-git/aresta-barcode/src/app/images/sticker-apt-merge-done"

    # Search for all the files in directory
    columnStickerImg = [f for f in listdir(path) if isfile(join(path, f))]

    # list for all the images full path
    allImgFullPath = []
    singleSheet = []

    #Total 16

    rounds = column*apt*2

    for i in range(rounds):
        if i%apt == 0:
            for j in range(apt):
                sign = i+j
                singleSheet.append(columnStickerImg[sign])
                # singleSheet.append(sign)
                columnId = singleSheet[0][8:11]
                levelId = singleSheet[0][12:14]
            
            for k in range(len(singleSheet)):
                # print(singleSheet[k])
                #Creates image object
                toImg = cv2.imread(path+singleSheet[k])
                # Saves image object to list
                allImgFullPath.append(toImg)

            for l in range(len(singleSheet)-1,-1,-1):
                print(singleSheet[l])
                #Creates image object
                toImg = cv2.imread(path+singleSheet[l])
                # Saves image object to list
                allImgFullPath.append(toImg)

            print("Creating Column{}-Nivel{}".format(columnId,levelId))
            # Convers the list to array
            allImgFullPath_array = np.array(allImgFullPath)

            # Combines all the individual column images to one image
            fullImg = cv2.hconcat(allImgFullPath_array)
            
            # Save the file to path
            cv2.imwrite("{}/{}.PNG".format(saveToPath,"Column{}-Nivel{}".format(columnId,levelId)), fullImg)
            allImgFullPath.clear()
            singleSheet.clear()    


# column = 5
# level = 2
# apt = 3

# aptMergeFiles(column,level,apt)
