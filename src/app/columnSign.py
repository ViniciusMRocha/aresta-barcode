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

def getBlankSign(index):
    path = "C:/personal-git/aresta-barcode/src/app/images/sign-blank-pad/blank-sign{}.PNG".format(index)
    blankSign = cv2.imread(path)
    return blankSign

def getBlankSignPath(index):
    path = "C:/personal-git/aresta-barcode/src/app/images/sign-blank-pad/blank-sign{}.PNG".format(index)
    return path

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
def mergeSigns(perSheet, nivelMax, printRow, printColumn):

    blankSign = getBlankSign(nivelMax)
    blankSignPath = getBlankSignPath(nivelMax)

    print("============== Testing mergeSigns ==================")
    print("Per Sheet: {}".format(perSheet))

    # Path to where all the individual images are
    path = 'C:/personal-git/aresta-barcode/src/app/images/sign-done-single'

    # Save new file to the path below 
    saveToPath = "C:/personal-git/aresta-barcode/src/app/images/sign-done-merge/"

    # Gets all files according to pattern
    files=glob.glob("{}/*nivelMax-{}*".format(path,nivelMax))
    
    # lista=[]
    # for i in range(90):
    #     lista.append(i)
    # print(lista)

    #files = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]

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

    # Why 54?
    for i in range(blankFiles):
        files.append(blankSignPath)
    
    # list for all the images full path
    allImgFullPath = []
    temp = []
    newStartPoint = 0
    for i in range(len(files)):
        if i%printColumn == 0:
            for j in range(printColumn):
                newStartPoint = j+i

                # Creates image object
                toImg = cv2.imread(files[newStartPoint])

                # Append Path
                temp.append(files[newStartPoint])

                # Saves image object to list
                allImgFullPath.append(toImg)

            newStartPoint = newStartPoint+1
            # print("Total: ",len(temp))
            # print("Temp: ",temp)
            # print("newStartPoint: ",newStartPoint)

            # Convers the list to array
            allImgFullPath_array = np.array(allImgFullPath)

            # Combines all the individual column images to one image
            fullImg = cv2.hconcat(allImgFullPath_array)

            fileName = 'nivelMax-{}-coluna-{}-{}'.format(nivelMax,newStartPoint-printColumn+1,newStartPoint)

            # Save the file to path
            cv2.imwrite("{}{}.PNG".format(saveToPath,fileName), fullImg)

            allImgFullPath.clear()
            temp.clear()

    # for row in range(printRow):


# https://stackoverflow.com/questions/2225564/get-a-filtered-list-of-files-in-a-directory

