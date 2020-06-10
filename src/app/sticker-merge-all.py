import cv2
from pathlib import Path
from PIL import Image
import barcode
from barcode.writer import ImageWriter
import numpy as np
from os import listdir
from os.path import isfile, join


# Adds a "0" to a 2 digit number
def addZero_twoDigits(check):
    if check <= 9:
        check = '0' + str(check)
    else:
        # Force to be string by adding ''
        check = '' + str(check)
    return check

# Adds "00" to a 1 digit number or "0" to a 2 digit number
def addZero_threeDigits(check):
    if check <= 9:
        check = '00' + str(check)
    elif check <= 99:
        check = '0' + str(check)
    else:
        #Force to be string by adding ''
        check = '' + str(check)
    return check

def mergeFiles(inputIsle,shelf):
    # Path to where all the individual images are
    path = 'C:/personal-git/aresta-barcode/src/app/images/sticker-single-done/'

    # New file name
    inputIsleThreeDigits = addZero_threeDigits(inputIsle)
    newFileName = "sticker-{}".format(inputIsleThreeDigits)

    # Save new file to the path below 
    saveToPath = "C:/personal-git/aresta-barcode/src/app/images/sticker-multiple-done"

    # Search for all the files in directory
    # FIXME: join is not working 
    isleStickerImg = [f for f in listdir(path) if isfile(join(path, f))]

    # list for all the images full path
    allImgFullPath = []

    for i in range(0,shelf):
        inputIsleThreeDigits = addZero_threeDigits(inputIsle)
        beforeIsle = isleStickerImg[i][0:16]
        afterIsle = isleStickerImg[i][19:31]

        isleGroup = beforeIsle+inputIsleThreeDigits+afterIsle
        fullPath = join(path,isleGroup)

        #Creates image object
        toImg = cv2.imread(fullPath)
        # Saves image object to list
        allImgFullPath.append(toImg)

        # Convers the list to array
        allImgFullPath_array = np.array(allImgFullPath)

        # Combines all the individual isle images to one image
        fullImg = cv2.vconcat(allImgFullPath_array)

        # Save the file to path
        newFilePath="{}/{}.PNG".format(saveToPath,newFileName)
        cv2.imwrite(newFilePath, fullImg)

def createAll(isle, shelf):
    for i in range(1, isle+1):
        if (i % 2) == 0:
            mergeFiles(i,shelf-1)
        elif (i % 2) > 0:
            mergeFiles(i,shelf) 

isle = 10
shelf = 8

createAll(isle, shelf)
