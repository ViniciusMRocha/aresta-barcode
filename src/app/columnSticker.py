import cv2
import numpy as np

from pathlib import Path
from PIL import Image

import barcode
from barcode.writer import ImageWriter

from os import listdir
from os.path import isfile, join

import glob


#My Files
import customeFunctions
import barcodeGenerator
import resize




def getBlankColumnPath():
    path = "C:/personal-git/aresta-barcode/src/app/images/column-blank-pad/column-sticker-blank.png"
    return path

def getBlankColumnRowPath():
    path = "C:/personal-git/aresta-barcode/src/app/images/column-blank-pad/column-sticker-row-blank.png"
    return path

# =================================================
# Get Images
# =================================================


# createAllRange
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
        resize.singleFileResize(savePath,width,height)


    print("Creating for street: ",street)
    for c in range(1,column+1):
        for l in range(1,level+1):
            # print("img: street-{} column-{} level-{} ".format(street, c, l))
            createColumnSticker(state, city, street, c, l, product)



# createAllRange
def createAllRange(state, city, street, level, product, startColumn, endColumn):
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
        resize.singleFileResize(savePath,width,height)


    print("Creating for street: ",street)
    for c in range(startColumn,endColumn+1):
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



def merge(printRow, printColumn):

    perSheet = printRow*printColumn

    print("testing")
    # Path to where all the individual images are
    path = 'C:/personal-git/aresta-barcode/src/app/images/column-done-single/'

    # Save new file to the path below 
    saveToPathRow = "C:/personal-git/aresta-barcode/src/app/images/column-done-row-merge"

    files=glob.glob("{}*".format(path))

    print("Per Sheet: {}".format(perSheet))

    totalFiles = len(files)
    print("Total files: {}".format(totalFiles))

    fullSheets = totalFiles//perSheet
    print("Full Sheets: {}".format(fullSheets))

    totalFilesInFullSheet = perSheet*fullSheets
    print("Total Files In Full Sheet: {}".format(totalFilesInFullSheet))

    leftOver = totalFiles-totalFilesInFullSheet 
    print("Left Over: {}".format(leftOver))

    blankFiles = perSheet-leftOver
    print("Blank Files: {}".format(blankFiles))