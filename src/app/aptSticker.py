import cv2
import numpy as np

from pathlib import Path
from PIL import Image

import barcode
from barcode.writer import ImageWriter

from os import listdir
from os.path import isfile, join

import barcodeGenerator
import resize
import customeFunctions
# =================================================
# Get Images
# =================================================

def createAll(state, city, street, column, level, product, apt, columnStart, columnEnd, evenOddAll):
    def getDigit(index):
        path ="C:/personal-git/aresta-barcode/src/app/images/apt-sticker-header-digits/resized/apt-sticker-digit-{}.png".format(index)
        digit = cv2.imread(path)
        return digit

    def getArrow():
        path = "C:/personal-git/aresta-barcode/src/app/images/apt-sticker-arrow-up/apt-sticker-arrow-up-black.PNG"
        arrow = cv2.imread(path)
        return arrow

    def getPad():
        path = "C:/personal-git/aresta-barcode/src/app/images/apt-sticker-barcode-header-pad/pad.PNG"
        pad = cv2.imread(path)
        return pad

    def getHeader(index):
        path ="C:/personal-git/aresta-barcode/src/app/images/apt-sticker-header/apt-sticker-header-{}.PNG".format(index)
        header = cv2.imread(path)
        return header

    # =================================================
    # Combine Images
    # =================================================

    def createSingle(state, city, street, column, level, product, apt):

        # Generate sectioin images
        arrow = getArrow()
        pad = getPad()
        header = getHeader(level) #420 x 114
        # barcode = getBarcode(state, city, street, column, level, product)
        barcode = barcodeGenerator.getBarcode(state, city, street, column, level, product)

        # create the product number
        apt = customeFunctions.addZero_twoDigits(apt)
        digit1 = apt[0:1]
        digit2 = apt[1:2]
        firstDigit = getDigit(digit1) # 82 x 114
        secondDigit = getDigit(digit2)

        # Combine Images
        img1 = cv2.hconcat([header,firstDigit,secondDigit,pad])
        img2 = cv2.vconcat([img1,barcode])
        img3 = cv2.hconcat([img2,arrow])

        # Create File Name
        city = customeFunctions.addZero_twoDigits(city)
        street = customeFunctions.addZero_twoDigits(street)
        column = customeFunctions.addZero_threeDigits(column)
        level = customeFunctions.addZero_twoDigits(level)
        product = customeFunctions.addZero_twoDigits(product)
        fileName = "{}.{}.{}.{}.{}.{}-apt-{}.png".format(state, city, street, column, level, product, apt)

        savePath = "C:/personal-git/aresta-barcode/src/app/images/apt-sticker-done-single/{}".format(fileName)
        cv2.imwrite(savePath, img3)
        print(savePath)

        width = 378
        height = 189
        resize.singleFileResize(savePath,width,height)

    if evenOddAll == "all":
        print("Doing all")
        for c in range(columnStart,columnEnd+1):
            print("column: ",c)
            for l in range(1,level+1):
                for a in range(1,apt+1):
                    # print("street-{} column-{} level-{} apt-{}".format(street,c,l,a))
                    createSingle(state, city, street, c, l, product, a)
    elif evenOddAll == "even":
        print("Doing even")
        for c in range(columnStart,columnEnd+1):
            if c%2 == 0:
                print("column: ",c)
                for l in range(1,level+1):
                    for a in range(1,apt+1):
                        # print("street-{} column-{} level-{} apt-{}".format(street,c,l,a))
                        createSingle(state, city, street, c, l, product, a)

    elif evenOddAll == "odd":
        print("Doing odd")
        for c in range(columnStart,columnEnd+1):
            if c%2 != 0:
                print("column: ",c)
                for l in range(1,level+1):
                    for a in range(1,apt+1):
                        # print("street-{} column-{} level-{} apt-{}".format(street,c,l,a))
                        createSingle(state, city, street, c, l, product, a)



# state = 1
# city = 1
# street = 1
# column = 12 #Give Max Value
# level = 2 #Give Max Value
# product = 1
# apt = 3
# columnStart = 9
# columnEnd = 57
# evenOddAll = "even"
# evenOddAll = "odd" 
# evenOddAll = "all"

# createAll(state, city, street, column, level, product, apt, columnStart, columnEnd, evenOddAll)

# columnStart = 9
# columnEnd = 68


# def merge(column,level,apt):
#     # Path to where all the individual images are
#     path = 'C:/personal-git/aresta-barcode/src/app/images/apt-sticker-done-single/'

#     # Save new file to the path below 
#     saveToPath = "C:/personal-git/aresta-barcode/src/app/images/apt-sticker-done-merge"

#     # Search for all the files in directory
#     columnStickerImg = [f for f in listdir(path) if isfile(join(path, f))]

#     for i in range(len(columnStickerImg)):
#         print(columnStickerImg[i])

#     singleSheet = []
#     for i in range(1,column+1):
#         print("\nColumn: ",i)
#         total = i/4
#         totalNoRemainder = i//4
#         check = total-totalNoRemainder
#         if check == 0.25 or check == 0.5:
#             print("Normal")
#             #define start point
#             for j in range(apt):
#                 singleSheet.append(columnStickerImg[j])
#                 print(singleSheet)
#                 singleSheet.clear()              
        
#         elif check == 0.75 or check == 0.0:
#             print("Inverted")
#             for j in range(apt-1,-1,-1):
#                 singleSheet.append(columnStickerImg[j])
#                 print(singleSheet)
#                 singleSheet.clear()