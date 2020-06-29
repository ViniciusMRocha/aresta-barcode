import cv2
import numpy as np

from pathlib import Path
from PIL import Image

import barcode
from barcode.writer import ImageWriter

from os import listdir
from os.path import isfile, join

import glob

import barcodeGenerator
import resize
import customeFunctions
# =================================================
# Get Images
# =================================================

imagesPath = "C:/personal-git/aresta-barcode/src/app/images/"


def createAll(state, city, street, column, level, product, apt, columnStart, columnEnd, evenOddAll):
    def getDigit(index):
        path ="{}apt_sticker_header_digits/resized/apt_sticker_digit_{}.png".format(imagesPath, index)
        digit = cv2.imread(path)
        return digit

    def getArrow():
        path = "{}apt_sticker_arrow_up/apt_sticker_arrow_up_black.PNG".format(imagesPath)
        arrow = cv2.imread(path)
        return arrow

    def getPad():
        path = "{}apt_sticker_barcode_header_pad/pad.PNG".format(imagesPath)
        pad = cv2.imread(path)
        return pad

    def getHeader(index):
        path ="{}apt_sticker_header/apt_sticker_header_{}.PNG".format(imagesPath, index)
        header = cv2.imread(path)
        return header

    def getLine(option):
        if option == "side":
            path = "{}lines/stickerSide.png".format(imagesPath)
        if option == "top":
            path = "{}lines/stickerTop.png".format(imagesPath)
        line = cv2.imread(path)
        return line

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
        # Side Line
        img4 = cv2.hconcat([img3, getLine("side")])
        # Top Line
        img5 = cv2.vconcat([getLine("top"),img4])

        # Create File Name
        city = customeFunctions.addZero_twoDigits(city)
        street = customeFunctions.addZero_twoDigits(street)
        column = customeFunctions.addZero_threeDigits(column)
        level = customeFunctions.addZero_twoDigits(level)
        product = customeFunctions.addZero_twoDigits(product)
        fileName = "{}.{}.{}.{}.{}.{}-apt-{}.png".format(state, city, street, column, level, product, apt)

        savePath = "{}apt_sticker_done_single/{}".format(imagesPath, fileName)
        cv2.imwrite(savePath, img5)
        print(savePath)

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


