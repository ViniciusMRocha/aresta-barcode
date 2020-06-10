import cv2
import numpy as np

from pathlib import Path
from PIL import Image

import barcode
from barcode.writer import ImageWriter

# Define file paths

# Adds "00" to a 1 digit number or "0" to a 2 digit number
def addZero_threeDigits(check):
    if check <= 9:
        check = '00' + str(check)
    elif check <= 99:
        check = '0' + str(check)
    return check

# Adds a "0" to a 2 digit number
def addZero_twoDigits(check):
    if check <= 9:
        check = '0' + str(check)
    else:
        # Force to be string by adding ''
        check = '' + str(check)
    return check

# =================================================
# Get Images
# =================================================

def getDigit(index):
    print("Runnig getDigit")
    path ="C:/personal-git/aresta-barcode/src/app/images/sticker-header-digits/resized/sticker-digit-{}.png".format(index)
    digit = cv2.imread(path)
    return digit

def getArrow(index):
    print("Runnig getArrow")
    # path = "C:/personal-git/aresta-barcode/src/app/images/sticker-arrow-up/sticker-arrow-up-{}.PNG".format(index)
    path = "C:/personal-git/aresta-barcode/src/app/images/sticker-arrow-up/sticker-arrow-up-black.PNG"
    arrow = cv2.imread(path)
    return arrow

def getPad():
    print("Runnig getArrow")
    path = "C:/personal-git/aresta-barcode/src/app/images/sticker-barcode-header-pad/pad.PNG"
    pad = cv2.imread(path)
    return pad

def getHeader(index):
    print("Runnig getHeader")
    path ="C:/personal-git/aresta-barcode/src/app/images/sticker-header/sticker-header-{}.PNG".format(index)
    header = cv2.imread(path)
    return header

def getBarcode(state, city, region, isle, shelf, product):
    print("Runnig getBarcode")
    
    city = addZero_twoDigits(city)
    region = addZero_twoDigits(region)
    isle = addZero_threeDigits(isle)
    shelf = addZero_twoDigits(shelf)
    product = addZero_twoDigits(product)
    path = "C:/personal-git/aresta-barcode/src/app/images/barcode-library/{}.{}.{}.{}.{}.{}.png".format(state, city, region, isle, shelf, product)
    print(path)
    barcode = cv2.imread(path)
    return barcode

# =================================================
# Combine Images
# =================================================

def createSticker(state, city, region, isle, shelf, product):

    # Generate sectioin images
    arrow = getArrow(shelf)
    pad = getPad()
    header = getHeader(shelf) #420 x 114
    barcode = getBarcode(state, city, region, isle, shelf, product)

    # create the product number
    product = addZero_twoDigits(product)
    digit1 = product[0:1]
    digit2 = product[1:2]
    firstDigit = getDigit(digit1) # 82 x 114
    secondDigit = getDigit(digit2)
    print("digit1: ",digit1)
    print("digit2: ",digit2)

    # Combine Images
    img1 = cv2.hconcat([header,firstDigit,secondDigit,pad])
    img2 = cv2.vconcat([img1,barcode])
    img3 = cv2.hconcat([img2,arrow])

    # Create File Name
    city = addZero_twoDigits(city)
    region = addZero_twoDigits(region)
    isle = addZero_threeDigits(isle)
    shelf = addZero_twoDigits(shelf)
    fileName = "sticker-{}.{}.{}.{}.{}.{}.png".format(state, city, region, isle, shelf, product)

    cv2.imwrite("C:/personal-git/aresta-barcode/src/app/images/sticker-single-done/{}".format(fileName), img3)

state = 1
city = 1
region = 2
isle = 3 #Give Max Value
shelf = 8 #Give Max Value
product = 2

# isleMax = 9
# shelfMax = 9

for i in range(1, isle+1):
    isleThreeDigits = addZero_threeDigits(i)
    if (i % 2) == 0:
        print("Is even - Top 7")
        for j in range(1, shelf):
            shelfThreeDigits = addZero_twoDigits(j)
            stickerInfo = isleThreeDigits+"."+shelfThreeDigits
            createSticker(state, city, region, i, j, product)
            print(stickerInfo)
    if (i % 2) > 0:
        print("Is odd - Top 8")
        for j in range(1, shelf+1):
            shelfThreeDigits = addZero_twoDigits(j)
            stickerInfo = isleThreeDigits+"."+shelfThreeDigits
            # create level 8
            createSticker(state, city, region, i, j, product)
            print(stickerInfo)



