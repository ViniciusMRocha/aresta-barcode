import cv2
import numpy as np

from pathlib import Path
from PIL import Image

import barcode
from barcode.writer import ImageWriter

from os import listdir
from os.path import isfile, join

#My Files
import customeFunctions
import barcodeGenerator
import resize

# =================================================
# Get Images
# =================================================


def createAll(state, city, street, column, level, product):
    def getArrow():
        # print("Runnig getArrow")
        path = "C:/personal-git/aresta-barcode/src/app/images/apt-sticker-arrow-up/apt-sticker-arrow-up-black.PNG"
        arrow = cv2.imread(path)
        return arrow

    def getHeader(index):
        # print("Runnig getHeader")
        path = "C:/personal-git/aresta-barcode/src/app/images/column-header/header-{}.PNG".format(index)
        header = cv2.imread(path)
        return header

    # =================================================
    # Combine Images
    # =================================================

    def createColumnSticker(state, city, street, column, level, product):

        # Generate sectioin images
        arrow = getArrow()
        header = getHeader(level) #420 x 114
        barcode = barcodeGenerator.getBarcode(state, city, street, column, level, product)

        # Combine Images
        img1 = cv2.vconcat([header,barcode])
        img2 = cv2.hconcat([img1,arrow])

        # Create File Name
        city = customeFunctions.addZero_twoDigits(city)
        street = customeFunctions.addZero_twoDigits(street)
        column = customeFunctions.addZero_threeDigits(column)
        level = customeFunctions.addZero_twoDigits(level)
        product = customeFunctions.addZero_twoDigits(product)

        fileName = "inv-{}.{}.{}.{}.{}.{}.PNG".format(state, city, street, column, level, product)

        savePath = "C:/personal-git/aresta-barcode/src/app/images/column-done-single/{}".format(fileName)
        cv2.imwrite(savePath, img2)
        print(savePath)

        width = 378
        height = 189
        resize.singleFileRename(savePath,width,height)


    print("Creating for street: ",street)
    for c in range(1,column+1):
        for l in range(1,level+1):
            # print("img: street-{} column-{} level-{} ".format(street, c, l))
            createColumnSticker(state, city, street, c, l, product)


# ==================================================================

# state = 1
# city = 1
# street = 3
# column = 5 #Give Max Value
# level = 8 #Give Max Value
# product = 1

# createAll(state, city, street, column, level, product)



def merge(column,level):
    # Path to where all the individual images are
    path = 'C:/personal-git/aresta-barcode/src/app/images/column-done-single/'

    # Save new file to the path below 
    saveToPath = "C:/personal-git/aresta-barcode/src/app/images/column-done-merge"

    # Search for all the files in directory
    columnStickerImg = [f for f in listdir(path) if isfile(join(path, f))]
    # list for all the images full path
    allImgFullPath = []
    singleSheet = []

    # Add full path to each file
    for i in range(len(columnStickerImg)):
        # Merge the file name to the rest of the path
        fullPath = path+columnStickerImg[i]
        columnStickerImg[i] = fullPath

    for i in range(len(columnStickerImg)):
        if i%level == 0:
            for j in range(level):
                sign = i+j
                singleSheet.append(columnStickerImg[sign])
                # singleSheet.append(sign)
                cityId = singleSheet[0][60:62]
                streetId = singleSheet[0][63:65]
                columnId = singleSheet[0][66:69]
            print("Creating Cidade{}-Rua{}-Coluna{}".format(cityId,streetId,columnId))
            print(singleSheet)

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
            cv2.imwrite("{}/{}.PNG".format(saveToPath,"Cidade{}-Rua{}-Coluna{}".format(cityId,streetId,columnId)), fullImg)
            


            allImgFullPath.clear()
            singleSheet.clear()

# column = 5
# level = 8
# merge(column,level)