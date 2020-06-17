import cv2
import numpy as np

from pathlib import Path
from PIL import Image

from os import listdir
from os.path import isfile, join

import barcode
from barcode.writer import ImageWriter

import glob

#My Files
import customeFunctions
import barcodeGenerator
import resize

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
    # TODO: Arrows are wrong
    if check == 0.0 or check == 0.75:
        # Arrow 1 - 2: >>> 
        arrow = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/sign-header-arrow/right-arrow.PNG")
    elif check == 0.25 or check == 0.5:
        # Arrow 3 - 4: <<<
        arrow = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/sign-header-arrow/left-arrow.PNG")
    return arrow

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
def createAll(state, city, street, column, levelMax, product):
    check = levelMax
    city = customeFunctions.addZero_twoDigits(city)
    street = customeFunctions.addZero_twoDigits(street)
    product = customeFunctions.addZero_twoDigits(product)
    allBarcodesPath = []

    for column in range(1, column+1):
        columnThreeDigits = customeFunctions.addZero_threeDigits(column)
        for level in range(1, levelMax+1):
            level = customeFunctions.addZero_twoDigits(level) 
            
            # Generate Barcode
            barcodeNumber = ('{}.{}.{}.{}.{}.{}').format(state, city, street, columnThreeDigits, level, product)
            print("Barcode Number: "+barcodeNumber)
            barcodeGenerator.generateSingleBarcode(barcodeNumber)
            barcodeImgPath = "C:/personal-git/aresta-barcode/src/app/images/barcode-library/{}.{}.{}.{}.{}.{}.png".format(state, city, street, columnThreeDigits, level, product)
            allBarcodesPath.append(barcodeImgPath)

        # Generates the a single column image
        createColumnImage(state, city, street, column, level, allBarcodesPath, check)

        # Clear list for next iteration
        allBarcodesPath.clear()

# Generates the a single column image
def createColumnImage(state, city, street, column, level, allBarcodesPath, check):

    labelAndBarcode = []
    city = int(city)
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
    cityTwoDigits = customeFunctions.addZero_twoDigits(city)

    fileName = ("C:/personal-git/aresta-barcode/src/app/images/sign-done-single/{}.{}.{}.{}.nivelMax-{}.PNG".format(state, cityTwoDigits, street, columnThreeDigits,check))

    cv2.imwrite(fileName, fullImg)

    if check == 6:
        width = 246
        height = 1118
        resize.singleFileResize(fileName,width,height)
    elif check == 8:
        width = 246
        height = 1437
        resize.singleFileResize(fileName,width,height)
    elif check == 12:
        width = 246
        height = 2075
        resize.singleFileResize(fileName,width,height)

    print("Generating Image: {}".format(fileName))






# Generates all column images
def createAllRange(state, city, street, startColumn, levelMax, product, endColumn):
    check = levelMax
    city = customeFunctions.addZero_twoDigits(city)
    street = customeFunctions.addZero_twoDigits(street)
    product = customeFunctions.addZero_twoDigits(product)
    allBarcodesPath = []

    for column in range(startColumn, endColumn+1):
        columnThreeDigits = customeFunctions.addZero_threeDigits(column)
        for level in range(1, levelMax+1):
            level = customeFunctions.addZero_twoDigits(level) 
            
            # Generate Barcode
            barcodeNumber = ('{}.{}.{}.{}.{}.{}').format(state, city, street, columnThreeDigits, level, product)
            print("Barcode Number: "+barcodeNumber)
            barcodeGenerator.generateSingleBarcode(barcodeNumber)
            barcodeImgPath = "C:/personal-git/aresta-barcode/src/app/images/barcode-library/{}.{}.{}.{}.{}.{}.png".format(state, city, street, columnThreeDigits, level, product)
            allBarcodesPath.append(barcodeImgPath)

        # Generates the a single column image
        createColumnImage(state, city, street, column, level, allBarcodesPath, check)

        # Clear list for next iteration
        allBarcodesPath.clear()
















# C:\personal-git\aresta-barcode\src\app\images\sign-done-single\1.01.01.001.PNG
# 

# ====== Merge ===============================

#TODO: Name the file according to the city-rua-00
def mergeSigns(perSheet, nivelMax):

    print("============== Testing mergeSigns ==================")
    print("Per Sheet: {}".format(perSheet))

    # Path to where all the individual images are
    path = 'C:/personal-git/aresta-barcode/src/app/images/sign-done-single'

    # Save new file to the path below 
    saveToPath = "C:/personal-git/aresta-barcode/src/app/images/sign-done-merge/"

    # Gets all files according to pattern
    files=glob.glob("{}/*nivelMax-{}*".format(path,nivelMax))
    
    # for i in range(len(files)):
    #     print(files[i])

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

    






# https://stackoverflow.com/questions/2225564/get-a-filtered-list-of-files-in-a-directory

# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.001.PNG
# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.002.PNG
# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.004.PNG
# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.005.PNG
# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.006.PNG
# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.007.PNG
# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.009.PNG
# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.010.PNG
# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.011.PNG
# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.012.PNG
# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.013.PNG
# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.014.PNG
# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.015.PNG
# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.016.PNG
# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.017.PNG
# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.019.PNG
# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.020.PNG
# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.021.PNG
# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.022.PNG
# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.023.PNG
# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.024.PNG
# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.025.PNG
# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.026.PNG
# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.027.PNG
# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.029.PNG
# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.030.PNG
# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.031.PNG
# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.032.PNG
# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.034.PNG
# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.035.PNG
# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.036.PNG
# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.037.PNG
# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.038.PNG
# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.039.PNG
# C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.02.11.040.PNG














#     # Search for all the files in directory
#     # FIXME: join is not working 
#     columnImg = [f for f in listdir(path) if isfile(join(path, f))]

#     # list for all the images full path
#     allImgFullPath = []

#     #All Images
#     singleSheet = []

#     # Add full path to each file
#     for i in range(len(columnImg)):
#         # Merge the file name to the rest of the path
#         fullPath = join(path,columnImg[i])
#         columnImg[i] = fullPath

#     streetId = 0
#     for i in range(len(columnImg)):
#         if i%signPerRow == 0:
#             for j in range(signPerRow):
#                 sign = i+j
#                 singleSheet.append(columnImg[sign])
#                 # Gets the city and street from the file name
#                 cityId = singleSheet[0][65:67]
#                 streetId = singleSheet[0][68:70]
#             print("Creating Cidade{}-Rua{}".format(cityId,streetId))
            
#             for k in range(len(singleSheet)):
#                 #Creates image object
#                 toImg = cv2.imread(singleSheet[k])
#                 # Saves image object to list
#                 allImgFullPath.append(toImg)

#             # Convers the list to array
#             allImgFullPath_array = np.array(allImgFullPath)

#             # Combines all the individual column images to one image
#             fullImg = cv2.hconcat(allImgFullPath_array)

#             # Save the file to path
#             cv2.imwrite("{}/{}.PNG".format(saveToPath,"Cidade{}-Rua{}".format(cityId,streetId)), fullImg)
#             allImgFullPath.clear()
#             singleSheet.clear()


# # Testing
# # mergeSigns(5)