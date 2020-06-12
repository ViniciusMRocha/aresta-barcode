import cv2
from pathlib import Path
from PIL import Image
import barcode
from barcode.writer import ImageWriter
import numpy as np
from os import listdir
from os.path import isfile, join
import customeFunctions

def mergeFiles(inputcolumn,level):
    # Path to where all the individual images are
    path = 'C:/personal-git/aresta-barcode/src/app/images/sticker-single-done/'

    # New file name
    inputcolumnThreeDigits = customeFunctions.addZero_threeDigits(inputcolumn)
    newFileName = "sticker-{}".format(inputcolumnThreeDigits)

    # Save new file to the path below 
    saveToPath = "C:/personal-git/aresta-barcode/src/app/images/sticker-multiple-done"

    # Search for all the files in directory
    # FIXME: join is not working 
    columnStickerImg = [f for f in listdir(path) if isfile(join(path, f))]

    # list for all the images full path
    allImgFullPath = []

    for i in range(0,level):
        inputcolumnThreeDigits = customeFunctions.addZero_threeDigits(inputcolumn)
        beforecolumn = columnStickerImg[i][0:16]
        aftercolumn = columnStickerImg[i][19:31]

        columnGroup = beforecolumn+inputcolumnThreeDigits+aftercolumn
        fullPath = join(path,columnGroup)

        #Creates image object
        toImg = cv2.imread(fullPath)
        # Saves image object to list
        allImgFullPath.append(toImg)

        # Convers the list to array
        allImgFullPath_array = np.array(allImgFullPath)

        # Combines all the individual column images to one image
        fullImg = cv2.vconcat(allImgFullPath_array)

        # Save the file to path
        newFilePath="{}/{}.PNG".format(saveToPath,newFileName)
        cv2.imwrite(newFilePath, fullImg)

def createAll(column, level):
    for i in range(1, column+1):
        if (i % 2) == 0:
            mergeFiles(i,level-1)
        elif (i % 2) > 0:
            mergeFiles(i,level) 

column = 10
level = 8

createAll(column, level)
