import cv2
import numpy as np

from pathlib import Path
from PIL import Image

import barcode
from barcode.writer import ImageWriter

from os import listdir
from os.path import isfile, join

import glob


#My Files
import customeFunctions
import barcodeGenerator
import resize


imagePath = "C:/personal-git/aresta-barcode/src/app/images/"

# Return a blank sticker
def getBlankColumnPath():
    path = "{}column-blank-pad/column-sticker-blank.png".format(imagePath)
    return path

# Return a blank sticker row
def getBlankColumnRowPath():
    path = "{}column-blank-pad/column-sticker-row-blank.png".format(imagePath)
    return path

# =================================================
# Get Images
# =================================================

# create all column sticker
def createAll(state, city, street, column, level, product):
    def getArrow():
        # print("Runnig getArrow")
        path = "{}apt-sticker-arrow-up/apt-sticker-arrow-up-black.PNG".format(imagePath)
        arrow = cv2.imread(path)
        return arrow

    def getHeader(index):
        # print("Runnig getHeader")
        path = "{}column-header/header-{}.PNG".format(imagePath,index)
        header = cv2.imread(path)
        return header

    # =================================================
    # Combine Images
    # =================================================

    def createColumnSticker(state, city, street, column, level, product):

        # Generate sectioin images
        arrow = getArrow()
        header = getHeader(level) #420 x 114
        barcode = barcodeGenerator.getBarcode(state, city, street, column, level, product)

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

        savePath = "{}column-done-single/{}".format(imagePath,fileName)
        cv2.imwrite(savePath, img2)
        print(savePath)

        width = 378
        height = 189
        resize.singleFileResize(savePath,width,height)


    print("Creating for street: ",street)
    for c in range(1,column+1):
        for l in range(1,level+1):
            # print("img: street-{} column-{} level-{} ".format(street, c, l))
            createColumnSticker(state, city, street, c, l, product)



# createAllRange
def createAllRange(state, city, street, level, product, startColumn, endColumn):
    def getArrow():
        # print("Runnig getArrow")
        path = "{}apt-sticker-arrow-up/apt-sticker-arrow-up-black.PNG".format(imagePath)
        arrow = cv2.imread(path)
        return arrow

    def getHeader(index):
        # print("Runnig getHeader")
        path = "{}column-header/header-{}.PNG".format(imagePath,index)
        header = cv2.imread(path)
        return header

    # =================================================
    # Combine Images
    # =================================================

    def createColumnSticker(state, city, street, column, level, product):

        # Generate sectioin images
        arrow = getArrow()
        header = getHeader(level) #420 x 114
        barcode = barcodeGenerator.getBarcode(state, city, street, column, level, product)

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

        savePath = "{}column-done-single/{}".format(imagePath,fileName)
        cv2.imwrite(savePath, img2)
        print(savePath)

        width = 378
        height = 189
        resize.singleFileResize(savePath,width,height)


    print("Creating for street: ",street)
    for c in range(startColumn,endColumn+1):
        for l in range(1,level+1):
            # print("img: street-{} column-{} level-{} ".format(street, c, l))
            createColumnSticker(state, city, street, c, l, product)



def merge(printRow, printColumn):
    
    perSheet = printRow*printColumn

    blankSingleColumnPath = getBlankColumnPath()
    blankColumnRowPath = getBlankColumnRowPath()
    
    print("testing")
    # Path to where all the individual images are
    path = "{}column-done-single/".format(imagePath)

    # Save new file to the path below 
    saveToPathRow = "{}column-done-row-merge".format(imagePath)

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
            fileName = 'columSticker-row-{}'.format(rowCount)

            print("Generating File: {}".format(fileName))

            # Save the file to path
            cv2.imwrite("{}/{}.PNG".format(saveToPathRow,fileName), fullImg)

            allImgFullPath.clear()
            rowImg.clear()


    # Save new file to the path below 
    saveToPathFullPage = "C:/personal-git/aresta-barcode/src/app/images/column-done-full-page-merge"

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
        fileName = 'pallet-pagina-{}'.format(pageCount)

        print("Generating File: {}".format(fileName))
        # Save the file to path
        cv2.imwrite("{}/{}.PNG".format(saveToPathFullPage,fileName), fullImg)        

        sheetImg.clear()
        allImgFullPath.clear()
