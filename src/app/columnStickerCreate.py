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


def createAllColumnStickers(state, city, street, column, level, product):
    def getArrow():
        # print("Runnig getArrow")
        path = "C:/personal-git/aresta-barcode/src/app/images/sticker-arrow-up/sticker-arrow-up-black.PNG"
        arrow = cv2.imread(path)
        return arrow

    def getHeader(index):
        # print("Runnig getHeader")
        path = "C:/personal-git/aresta-barcode/src/app/images/pallet-header/pallet-{}.PNG".format(index)
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

    def createColumnSticker(state, city, street, column, level, product):

        # Generate sectioin images
        arrow = getArrow()
        header = getHeader(level) #420 x 114
        barcode = getBarcode(state, city, street, column, level, product)

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

        savePath = "C:/personal-git/aresta-barcode/src/app/images/pallet-done/{}".format(fileName)
        cv2.imwrite(savePath, img2)
        print(savePath)



    print("Creating for street: ",street)
    for c in range(1,column):
        for l in range(1,level):
            # print("img: street-{} column-{} level-{} ".format(street, c, l))
            createColumnSticker(state, city, street, c, l, product)


# ==================================================================

# state = 1
# city = 1
# street = 3
# column = 5 #Give Max Value
# level = 8 #Give Max Value
# product = 1

# createAllColumnStickers(state, city, street, column, level, product)