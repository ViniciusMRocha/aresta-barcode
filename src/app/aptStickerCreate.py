import cv2
import numpy as np

from pathlib import Path
from PIL import Image

import barcode
from barcode.writer import ImageWriter

import customeFunctions

# =================================================
# Get Images
# =================================================

def createAllAptSticker(state, city, street, column, level, product, apt, columnStart, columnEnd, evenOddAll):
    def getDigit(index):
        # print("Runnig getDigit")
        path ="C:/personal-git/aresta-barcode/src/app/images/sticker-header-digits/resized/sticker-digit-{}.png".format(index)
        digit = cv2.imread(path)
        return digit

    def getArrow(index):
        # print("Runnig getArrow")
        # path = "C:/personal-git/aresta-barcode/src/app/images/sticker-arrow-up/sticker-arrow-up-{}.PNG".format(index)
        path = "C:/personal-git/aresta-barcode/src/app/images/sticker-arrow-up/sticker-arrow-up-black.PNG"
        arrow = cv2.imread(path)
        return arrow

    def getPad():
        # print("Runnig getPad")
        path = "C:/personal-git/aresta-barcode/src/app/images/sticker-barcode-header-pad/pad.PNG"
        pad = cv2.imread(path)
        return pad

    def getHeader(index):
        # print("Runnig getHeader")
        path ="C:/personal-git/aresta-barcode/src/app/images/sticker-header/sticker-header-{}.PNG".format(index)
        header = cv2.imread(path)
        return header

    def getBarcode(state, city, street, column, level, product):
        # print("Runnig getBarcode")
        city = customeFunctions.addZero_twoDigits(city)
        street = customeFunctions.addZero_twoDigits(street)
        column = customeFunctions.addZero_threeDigits(column)
        level = customeFunctions.addZero_twoDigits(level)
        product = customeFunctions.addZero_twoDigits(product)
        path = "C:/personal-git/aresta-barcode/src/app/images/barcode-library/{}.{}.{}.{}.{}.{}.png".format(state, city, street, column, level, product)
        barcode = cv2.imread(path)
        return barcode

    # =================================================
    # Combine Images
    # =================================================

    def createSingleAptSticker(state, city, street, column, level, product, apt):

        # Generate sectioin images
        arrow = getArrow(level)
        pad = getPad()
        header = getHeader(level) #420 x 114
        barcode = getBarcode(state, city, street, column, level, product)

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

        savePath = "C:/personal-git/aresta-barcode/src/app/images/sticker-apt-single-done/{}".format(fileName)
        cv2.imwrite(savePath, img3)
        print(savePath)

    if evenOddAll == "all":
        print("Doing all")
        for c in range(columnStart,columnEnd):
            print("column: ",c)
            for l in range(1,level+1):
                for a in range(1,apt+1):
                    # print("street-{} column-{} level-{} apt-{}".format(street,c,l,a))
                    createSingleAptSticker(state, city, street, c, l, product, a)
    elif evenOddAll == "even":
        print("Doing even")
        for c in range(columnStart,columnEnd):
            if c%2 == 0:
                print("column: ",c)
                for l in range(1,level+1):
                    for a in range(1,apt+1):
                        # print("street-{} column-{} level-{} apt-{}".format(street,c,l,a))
                        createSingleAptSticker(state, city, street, c, l, product, a)

    elif evenOddAll == "odd":
        print("Doing odd")
        for c in range(columnStart,columnEnd):
            if c%2 != 0:
                print("column: ",c)
                for l in range(1,level+1):
                    for a in range(1,apt+1):
                        # print("street-{} column-{} level-{} apt-{}".format(street,c,l,a))
                        createSingleAptSticker(state, city, street, c, l, product, a)



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

# createAllAptSticker(state, city, street, column, level, product, apt, columnStart, columnEnd, evenOddAll)

# columnStart = 9
# columnEnd = 68
