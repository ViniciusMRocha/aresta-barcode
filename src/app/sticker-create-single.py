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

def getBarcode(state, city, region, isle, shelf, product):
    # print("Runnig getBarcode")
    city = customeFunctions.addZero_twoDigits(city)
    region = customeFunctions.addZero_twoDigits(region)
    isle = customeFunctions.addZero_threeDigits(isle)
    shelf = customeFunctions.addZero_twoDigits(shelf)
    product = customeFunctions.addZero_twoDigits(product)
    path = "C:/personal-git/aresta-barcode/src/app/images/barcode-library/{}.{}.{}.{}.{}.{}.png".format(state, city, region, isle, shelf, product)
    barcode = cv2.imread(path)
    return barcode

# =================================================
# Combine Images
# =================================================

def createSticker(state, city, region, isle, shelf, product, apt):

    # Generate sectioin images
    arrow = getArrow(shelf)
    pad = getPad()
    header = getHeader(shelf) #420 x 114
    barcode = getBarcode(state, city, region, isle, shelf, product)

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
    region = customeFunctions.addZero_twoDigits(region)
    isle = customeFunctions.addZero_threeDigits(isle)
    shelf = customeFunctions.addZero_twoDigits(shelf)
    fileName = "{}.{}.{}.{}.{}.{}-andar-{}-apt-{}.png".format(state, city, region, isle, shelf, product,shelf, apt)

    savePath = "C:/personal-git/aresta-barcode/src/app/images/sticker-single-done/{}".format(fileName)
    cv2.imwrite(savePath, img3)
    print(savePath)


state = 1
city = 1
region = 2
isle = 3 #Give Max Value
shelf = 2 #Give Max Value
product = 1
apt = 3

# createSticker(state, city, region, isle, shelf, product, apt)

for i in range(1,isle+1):
    print("Isle: ",i)
    for s in range(1,shelf+1):
        for a in range(1,apt+1):
            # print("isle-{} floor-{} apt-{}".format(i,s,a))
            createSticker(state, city, region, i, s, product, a)


#Loop all apt options
# for i in range(1,isle+1):
#     print("Isle: ",i)
#     for s in range(1,shelf+1):
#         for a in range(1,apt+1):
#             print("isle-{} floor-{} apt-{}".format(i,s,a))
#         for a in range(apt,0,-1):
#             print("isle-{} floor-{} apt-{}".format(i,s,a))









