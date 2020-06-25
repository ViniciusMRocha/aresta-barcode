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


imagePath = "C:/personal-git/aresta-barcode/src/app/images/"


# =================================================
# Get Images
# =================================================

def createAll(state, city, street, column, level, product, apt, columnStart, columnEnd, evenOddAll):
    def getDigit(index):
        path ="{}apt-sticker-header-digits/resized/apt-sticker-digit-{}.png".format(imagePath,index)
        digit = cv2.imread(path)
        return digit

    def getArrow():
        path = "{}apt-sticker-arrow-up/apt-sticker-arrow-up-black.PNG".format(imagePath)
        arrow = cv2.imread(path)
        return arrow

    def getPad():
        path = "{}apt-sticker-barcode-header-pad/pad.PNG".format(imagePath)
        pad = cv2.imread(path)
        return pad

    def getHeader(index):
        path ="{}apt-sticker-header/apt-sticker-header-{}.PNG".format(imagePath,index)
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

        savePath = "{}apt-sticker-done-single/{}".format(imagePath,fileName)
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


def getBlankColumnPath():
    path = "{}apt-sticker-blank-pad/apt-sticker-blank.png".format(imagePath)
    return path

def getBlankColumnRowPath():
    path = "{}apt-sticker-blank-pad/apt-sticker-row-blank.png".format(imagePath)
    return path

def merge(printRow, printColumn):
    
    perSheet = printRow*printColumn

    blankSingleColumnPath = getBlankColumnPath()
    blankColumnRowPath = getBlankColumnRowPath()
    
    print("testing")
    # Path to where all the individual images are
    path = '{}apt-sticker-done-single/'.format(imagePath)

    # Save new file to the path below 
    saveToPathRow = "{}apt-sticker-done-row-merge".format(imagePath)

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

    if leftOver != 0:
        blankFiles = perSheet-leftOver
        print("Blank Files: {}".format(blankFiles))

        for a in range(blankFiles):
            files.append(blankSingleColumnPath)

    allImgFullPath = []
    rowImg = []
    newStartPoint = 0
    for i in range(len(files)):
        if i%printColumn == 0:
            for j in range(printColumn):
                newStartPoint = j+i

                # Append Path
                rowImg.append(files[newStartPoint])

                # Creates image object
                toImg = cv2.imread(files[newStartPoint])

                # Saves image object to list
                allImgFullPath.append(toImg)

            # print(rowImg)
            newStartPoint = newStartPoint+1

            # Convers the list to array
            allImgFullPath_array = np.array(allImgFullPath)

            # Combines all the individual column images to one image
            fullImg = cv2.hconcat(allImgFullPath_array)

            rowCount = customeFunctions.addZero_twoDigits(int(i/printColumn))
            fileName = 'aptSticker-row-{}'.format(rowCount)

            print("Generating File: {}".format(fileName))

            # Save the file to path
            cv2.imwrite("{}/{}.PNG".format(saveToPathRow,fileName), fullImg)

            allImgFullPath.clear()
            rowImg.clear()


    # Save new file to the path below 
    saveToPathFullPage = "{}apt-sticker-done-full-page-merge".format(imagePath)

    rows=glob.glob("{}/*".format(saveToPathRow))

    totalRows = len(rows)
    print("Total rows: {}".format(totalRows))

    fullSheets = totalRows//printRow
    print("Total Full Sheets: {}".format(fullSheets))

    totalRowsInFullSheet = printRow*fullSheets
    print("Total Rows In Full Sheet: {}".format(totalRowsInFullSheet))

    leftOver = totalRows-totalRowsInFullSheet 
    print("Left Over Rows: {}".format(leftOver))

    if leftOver != 0:
        blankRows = printRow-leftOver
        print("Blank Rows: {}\n".format(blankRows))

        for a in range(blankRows):
            rows.append(blankColumnRowPath)

    sheetImg = []
    allImgFullPath = []
    newStartPoint = 0

    print("Total in rows: ",len(rows))
    rounds = int(len(rows)/printRow)
    for i in range(rounds):
        for j in range(printRow):
            
            individualRow = newStartPoint+j

            # print(individualRow)
            sheetImg.append(rows[individualRow])
            # sheetImg.append(individualRow)

            # Creates image object
            toImg = cv2.imread(rows[individualRow])

            # Saves image object to list
            allImgFullPath.append(toImg)

        newStartPoint = individualRow+1

        # Convers the list to array
        allImgFullPath_array = np.array(allImgFullPath)

        # Combines all the individual column images to one image
        fullImg = cv2.vconcat(allImgFullPath_array)

        pageCount = customeFunctions.addZero_twoDigits(i)
        fileName = 'apt-pagina-{}'.format(pageCount)

        print("Generating File: {}".format(fileName))
        # Save the file to path
        cv2.imwrite("{}/{}.PNG".format(saveToPathFullPage,fileName), fullImg)        

        sheetImg.clear()
        allImgFullPath.clear()
