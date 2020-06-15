import cv2
import numpy as np

from pathlib import Path
from PIL import Image

import barcode
from barcode.writer import ImageWriter

#My Files
import customeFunctions
import signMergeAll
import aptStickerCreate
import aptStickerMerge
import columnStickerCreate
import columnStickerMerge
import generateBarcode

# Returns the single digit image for the header
def getDigit(digit):
    path ="C:/personal-git/aresta-barcode/src/app/images/sign-header-single-digits/digit{}.PNG".format(digit)
    digitImg = cv2.imread(path)
    return digitImg

def getLabel(index):
    path ="C:/personal-git/aresta-barcode/src/app/images/sign-barcode-header/label-{}.PNG".format(index)
    label = cv2.imread(path)
    return label

def getPad():
    path = "C:/personal-git/aresta-barcode/src/app/images/sign-barcode-header-pad/pad.PNG"
    pad = cv2.imread(path)
    return pad

# Generates the correct arrow given the column number
def getArrow(column):
    #pattern repeats for every 4 digits.
    #Current Patters: >> >> << <<
    column = int(column)
    total = column/4
    totalNoRemainder = column//4
    check = total-totalNoRemainder
    if check == 0.25 or check == 0.5:
        # Arrow: >>> 
        arrow = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/sign-header-arrow/right-arrow.PNG")
    elif check == 0.75 or check == 0.0:
        # Arrow: <<<
        arrow = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/sign-header-arrow/left-arrow.PNG")
    return arrow

def getBarcode(state, city, street, column, level, product):
    city = customeFunctions.addZero_twoDigits(city)
    street = customeFunctions.addZero_twoDigits(street)
    column = customeFunctions.addZero_threeDigits(column)
    level = customeFunctions.addZero_twoDigits(level)
    product = customeFunctions.addZero_twoDigits(product)
    path = "C:/personal-git/aresta-barcode/src/app/images/barcode-library/{}.{}.{}.{}.{}.{}.png".format(state, city, street, column, level, product)
    print(path)
    barcode = cv2.imread(path)
    return barcode

# Generates the column label, buy taking a column number and generating a image from the digit images
def createColumnLable(column):

    #Makes "1" into "001"
    column = customeFunctions.addZero_threeDigits(column)

    #substring the input into 3 digits
    columnDigit1 = column[0:1]
    columnDigit2 = column[1:2]
    columnDigit3 = column[2:3]

    # Gets the digits images for each column digit 
    firstDigit = getDigit(columnDigit1)
    secondDigit = getDigit(columnDigit2)
    thirdDigit = getDigit(columnDigit3)

    # Create New column
    columnImg = cv2.hconcat([getPad(),firstDigit,secondDigit,thirdDigit,getPad()])
    headerImg = cv2.vconcat([getArrow(column),columnImg])

    return headerImg


# Generates all column images
def createAllImages(state, city, street, column, levelMax, product):
    city = customeFunctions.addZero_twoDigits(city)
    street = customeFunctions.addZero_twoDigits(street)
    product = customeFunctions.addZero_twoDigits(product)
    allBarcodesPath = []

    for column in range(1, column):
        columnThreeDigits = customeFunctions.addZero_threeDigits(column)
        for level in range(1, levelMax):
            level = customeFunctions.addZero_twoDigits(level) 
            
            # Generate Barcode
            barcodeNumber = ('{}.{}.{}.{}.{}.{}').format(state, city, street, columnThreeDigits, level, product)
            print("Barcode Number: "+barcodeNumber)
            generateBarcode.generateSingleBarcode(barcodeNumber)
            barcodeImgPath = "C:/personal-git/aresta-barcode/src/app/images/barcode-library/{}.{}.{}.{}.{}.{}.png".format(state, city, street, columnThreeDigits, level, product)
            allBarcodesPath.append(barcodeImgPath)

        # Generates the a single column image
        createColumnImage(street, column, level, allBarcodesPath)

        # Clear list for next iteration
        allBarcodesPath.clear()

# Generates the a single column image
def createColumnImage(street, column, level, allBarcodesPath):

    labelAndBarcode = []
    column = int(column)
    level = int(level)

    for i in range(level,0,-1):
        lable = getLabel(i)
        labelAndBarcode.append(lable)
        barcodeImg = cv2.imread(allBarcodesPath[i-1])
        labelAndBarcode.append(barcodeImg)

    # Convers the list to array
    labelAndBarcode_array = np.array(labelAndBarcode)
    
    # Generate column Image File
    fullImg = cv2.vconcat(labelAndBarcode_array)
    fullImg = cv2.vconcat([createColumnLable(column),fullImg])

    # Save file
    columnThreeDigits = customeFunctions.addZero_threeDigits(column)
    cityThreeDigits = customeFunctions.addZero_twoDigits(city)

    fileName = ("C:/personal-git/aresta-barcode/src/app/images/sign-single-done/{}.{}.{}.{}.PNG".format(state, cityThreeDigits, street, columnThreeDigits))

    cv2.imwrite(fileName, fullImg)

    print("Generating Image: {}.PNG".format(fileName))


# =======================================   RUAS 1-11   =======================================

state = 1
city = 1
street = 11
column = 5
level = 8
product = 1

# Apply offset
column = column + 1
level = level + 1
street = street + 1

# Crete street
for i in range (1,street):
    createAllImages(state, city, i, column, level, product)

state = 1
city = 1
street = 3
column = 5
level = 2
product = 1
apt = 3
aptStickerCreate.createAllAptSticker(state, city, street, column, level, product, apt)
aptStickerMerge.aptMergeFiles(column, level, apt)
# =======================================   RUAS 10   =======================================

state = 1
city = 2
street = 1
column = 5
level = 6
product = 1

# Apply offset
column = column + 1
level = level + 1
street = street + 1

# Creates 
for i in range (1,street):
    createAllImages(state, city, i, column, level, product)

# fix ofset
signPerPage = column-1
signMergeAll.mergeSigns(signPerPage)

# =======================================   Pallet Sticker   =======================================

state = 1
city = 1
street = 3
column = 5 #Give Max Value
level = 8 #Give Max Value
product = 1

columnStickerCreate.createAllColumnStickers(state, city, street, column, level, product)

# ======================================= Top Column Headers =======================================
column = 5
columnStickerMerge.stickerMergeFiles(column)