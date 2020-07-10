import cv2
import numpy as np

from pathlib import Path
from PIL import Image

from os import listdir
from os.path import isfile, join

import barcode
from barcode.writer import ImageWriter

import glob

import pprint

#My Files
import customeFunctions
import barcodeGenerator
import resize

imagesPath = "C:/personal-git/aresta-barcode/src/app/images/"

def getStreetSeparator():
    path ="{}lines/signBreak.png".format(imagesPath)
    img = cv2.imread(path)
    return img


def getStickerSeparator():
    path ="{}lines/stickerBreak.png".format(imagesPath)
    img = cv2.imread(path)
    return img

def getBlankStickerPath():
    path = "{}column_blank_pad/column-sticker-blank.png".format(imagesPath)
    return path

def mergeSign(state, city, street, level, printRow, printColumn):

    def getBlankSignPath(index):
        path = "{}sign_blank_pad/blank-sign{}.PNG".format(imagesPath, index)
        return path
    
    # Got the steet to search the directory
    city = customeFunctions.addZero_twoDigits(city)
    street = customeFunctions.addZero_twoDigits(street)
    
    # Total columns per role
    perSheet = printRow*printColumn

    # Get blank sign images - nivelMax
    blankSignPath = getBlankSignPath(level)

    # Path to where all the individual images are
    path = '{}sign_done_single'.format(imagesPath)

    # Save new file to the path below 
    saveToPathRow = "{}sign_done_row_merge".format(imagesPath)

    # Gets all the columns for a certain street
    files = glob.glob("{}/{}.{}.{}*nivelMax-{}*".format(path, state, city, street, level))

    # Information about print page
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
        # All blank spaces to end of print sheet
        blankFiles = perSheet-leftOver
        # Total of blank rows
        blankRow = blankFiles // printColumn
        # unit count of total blank signs
        blankRow = blankRow * printColumn
        # Total blank files to fill out the last line
        blankFiles = blankFiles-blankRow

        print("Blank Files: {}".format(blankFiles))
       
        for i in range(blankFiles):
            files.append(blankSignPath)
    
    # list for all the images full path
    allImgFullPath = []
    rowImg = []
    savedFiles = []
    newStartPoint = 0
    for i in range(len(files)):
        if i%printColumn == 0:
            for j in range(printColumn):
                newStartPoint = j+i

                # Creates image object
                toImg = cv2.imread(files[newStartPoint])

                # Append Path
                rowImg.append(files[newStartPoint])

                # Saves image object to list
                allImgFullPath.append(toImg)

            newStartPoint = newStartPoint+1
            # print("Total: ",len(rowImg))
            # print("Row Image: ",rowImg)
            # print("newStartPoint: ",newStartPoint)

            # Convers the list to array
            allImgFullPath_array = np.array(allImgFullPath)

            # Combines all the individual column images to one image
            fullImg = cv2.hconcat(allImgFullPath_array)

            pageCount = customeFunctions.addZero_twoDigits(int(i/printColumn))
            fileName = 'rua{}_nivelMax{}_linha{}'.format(street, level, pageCount)
            savedFiles.append(fileName)

            print("Generating File: {}".format(fileName))

            # Save the file to path
            cv2.imwrite("{}/{}.PNG".format(saveToPathRow,fileName), fullImg)

            allImgFullPath.clear()
            rowImg.clear()
    
    # Adding red line to the end of the last row
    # Get the last row file name
    lastImage = savedFiles[len(savedFiles)-1]
    # Get the last row file path
    lastRowPath = "{}/{}.PNG".format(saveToPathRow,lastImage)
    # makes lastRowPath image into a img object
    lastRowImg = cv2.imread(lastRowPath)
    # append the lastRowImg to the line
    lastImage = cv2.vconcat([lastRowImg,getStreetSeparator()])
    # save file
    cv2.imwrite(lastRowPath, lastImage)
     

def mergeColumn(state, city, street, printRow, printColumn):

    city = customeFunctions.addZero_twoDigits(city)
    street = customeFunctions.addZero_twoDigits(street)

    perSheet = printRow*printColumn

    blankSingleColumnPath = getBlankStickerPath()
    
    # Path to where all the individual images are
    path = '{}column_done_single/'.format(imagesPath)

    # Save new file to the path below 
    saveToPathRow = "{}column_done_row_merge".format(imagesPath)

    files = glob.glob("{}/inv-{}.{}.{}*".format(path, state, city, street))

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
        # All blank spaces to end of print sheet
        blankFiles = perSheet-leftOver
        # Total of blank rows
        blankRow = blankFiles // printColumn
        # unit count of total blank signs
        blankRow = blankRow * printColumn
        # Total blank files to fill out the last line
        blankFiles = blankFiles-blankRow

        print("Blank Files: {}".format(blankFiles))

        for i in range(blankFiles):
            files.append(blankSingleColumnPath)
 

    allImgFullPath = []
    rowImg = []
    savedFiles = []
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
            fileName = 'adesivo_inventario_rua{}_linha{}'.format(street, rowCount)
            savedFiles.append(fileName)

            print("Generating File: {}".format(fileName))

            # Save the file to path
            cv2.imwrite("{}/{}.PNG".format(saveToPathRow,fileName), fullImg)

            allImgFullPath.clear()
            rowImg.clear()

    # Adding red line to the end of the last row
    # Get the last row file name
    lastImage = savedFiles[len(savedFiles)-1]
    # Get the last row file path
    lastRowPath = "{}/{}.PNG".format(saveToPathRow,lastImage)
    # makes lastRowPath image into a img object
    lastRowImg = cv2.imread(lastRowPath)
    # append the lastRowImg to the line
    lastImage = cv2.vconcat([lastRowImg,getStickerSeparator()])
    # save file
    cv2.imwrite(lastRowPath, lastImage)

def mergeApt(state, city, street, printRow, printColumn):

    city = customeFunctions.addZero_twoDigits(city)
    street = customeFunctions.addZero_twoDigits(street)

    blankSingleColumnPath = getBlankStickerPath()
    
    # Path to where all the individual images are
    path = '{}apt_sticker_done_single/'.format(imagesPath)

    # Save new file to the path below 
    saveToPathRow = "{}apt_sticker_done_row_merge".format(imagesPath)

    # files=glob.glob("{}*".format(path))
    files = glob.glob("{}/{}.{}.{}*".format(path, state, city, street))

    # print("Per Sheet: {}".format(perSheet))

    totalFiles = len(files)
    print("Total files: {}".format(totalFiles))

    fullRows = totalFiles//printColumn
    print("Full Rows: {}".format(fullRows))

    totalFilesInFullSheet = printColumn*fullRows
    print("Total Files In Full Sheet: {}".format(totalFilesInFullSheet))

    leftOver = totalFiles-totalFilesInFullSheet 
    print("Left Over: {}".format(leftOver))

    if leftOver != 0:
        # All blank spaces to end of print sheet
        blankFiles = printColumn-leftOver
        # Total of blank rows
        blankRow = blankFiles // printColumn
        # unit count of total blank signs
        blankRow = blankRow * printColumn
        # Total blank files to fill out the last line
        blankFiles = blankFiles-blankRow

        print("Blank Files: {}".format(blankFiles))

        for i in range(blankFiles):
            files.append(blankSingleColumnPath)

    allImgFullPath = []
    rowImg = []
    savedFiles = []

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

            pprint.pprint(rowImg)
            newStartPoint = newStartPoint+1

            # Convers the list to array
            allImgFullPath_array = np.array(allImgFullPath)

            # Combines all the individual column images to one image
            fullImg = cv2.hconcat(allImgFullPath_array)

            rowCount = customeFunctions.addZero_twoDigits(int(i/printColumn))
            fileName = 'adesivo_apt_rua{}_linha{}'.format(street, rowCount)
            savedFiles.append(fileName)
            
            print("Generating File: {}".format(fileName))

            rowFile = "{}/{}.PNG".format(saveToPathRow,fileName)

            # Save the file to path
            cv2.imwrite(rowFile, fullImg)

            allImgFullPath.clear()
            rowImg.clear()

    # Adding red line to the end of the last row
    # Get the last row file name
    lastImage = savedFiles[len(savedFiles)-1]
    # Get the last row file path
    lastRowPath = "{}/{}.PNG".format(saveToPathRow,lastImage)
    # makes lastRowPath image into a img object
    lastRowImg = cv2.imread(lastRowPath)
    # append the lastRowImg to the line
    lastImage = cv2.vconcat([lastRowImg,getStickerSeparator()])
    # save file
    cv2.imwrite(lastRowPath, lastImage)


def mergeStickerPrintPage(folderPath, saveToPathRow, filePrefix, printRow, printColumn, levelorColumn):

    def getBlankRow(levelorColumn):
        if levelorColumn == 0:
            path = "{}column_blank_pad/column-sticker-row-blank.png".format(imagesPath)
            return path
        elif levelorColumn == 6:
            path = "{}sign_blank_pad/blank-sign-row6.PNG".format(imagesPath)
            return path
        elif levelorColumn == 8:
            path = "{}sign_blank_pad/blank-sign-row8.PNG".format(imagesPath)
            return path
        elif levelorColumn == 12:
            path = "{}sign_blank_pad/blank-sign-row12.PNG".format(imagesPath)
            return path

    # Path to save file
    saveToPath = "{}{}".format(imagesPath,saveToPathRow)
    # Appends full Path to the parameter folder

    foldeFullPath = "{}{}".format(imagesPath,folderPath)

    if levelorColumn != 0:
        files = glob.glob("{}/*nivelMax{}*".format(foldeFullPath,levelorColumn))
    else:
        # all files in the directory
        files = glob.glob("{}/*".format(foldeFullPath))

    print("Per Sheet: {}".format(printRow))

    totalFiles = len(files)
    print("Total files: {}".format(totalFiles))

    fullSheets = totalFiles//printRow
    print("Full Sheets: {}".format(fullSheets))

    totalFilesInFullSheet = printRow*fullSheets
    print("Total Files In Full Sheet: {}".format(totalFilesInFullSheet))

    leftOver = totalFiles-totalFilesInFullSheet 
    print("Left Over: {}".format(leftOver))

    if leftOver != 0:
        # All blank rows to end of print sheet
        blankFiles = printRow-leftOver
        print("Blank Files: {}".format(blankFiles))

        for i in range(blankFiles):
            files.append(getBlankRow(levelorColumn))

        # pprint.pprint(files)


    allImgFullPath = []
    newStartPoint = 0
    for i in range(len(files)):
        if i%printRow == 0:
            for j in range(printRow):
                newStartPoint = j+i
                
                # Creates image object
                toImg = cv2.imread(files[newStartPoint])

                # Saves image object to list
                allImgFullPath.append(toImg)

            newStartPoint = newStartPoint+1

            # Combines all the individual column images to one image
            fullImg = cv2.vconcat(allImgFullPath)

            pageCount = customeFunctions.addZero_twoDigits(int(i/printRow))
            fileName = '{}{}'.format(filePrefix,pageCount)

            print("Generating File: {}".format(fileName))

            # Save the file to path
            cv2.imwrite("{}/{}.PNG".format(saveToPath,fileName), fullImg)

            allImgFullPath.clear()


# printRow = 40
# printColumn = 10
# levelorColumn = 0 #determines if it is a sign or sticker | 0 = column 6,8,12 level o sign
# folderPath = "apt_sticker_done_row_merge"
# saveToPathRow = "apt_sticker_done_full_page_merge"
# filePrefix = "adesivo_apartamento_pagina"

# mergeStickerPrintPage(folderPath, saveToPathRow, filePrefix, printRow, printColumn, levelorColumn)

# folderPath = "column_done_row_merge"
# saveToPathRow = "column_done_full_page_merge"
# filePrefix = "adesivo_paletes_pagina"

# mergeStickerPrintPage(folderPath, saveToPathRow, filePrefix, printRow, printColumn, levelorColumn)


# printRow = 5
# printColumn = 5
# levelorColumn = 8
# folderPath = "sign_done_row_merge"
# saveToPathRow = "sign_done_full_page_merge"
# filePrefix = "placa_paletes_nivel{}_pagina".format(levelorColumn)
# mergeStickerPrintPage(folderPath, saveToPathRow, filePrefix, printRow, printColumn, levelorColumn)

# printRow = 5
# printColumn = 5
# levelorColumn = 6
# folderPath = "sign_done_row_merge"
# saveToPathRow = "sign_done_full_page_merge"
# filePrefix = "placa_paletes_nivel{}_pagina".format(levelorColumn)
# mergeStickerPrintPage(folderPath, saveToPathRow, filePrefix, printRow, printColumn, levelorColumn)

# printRow = 5
# printColumn = 5
# levelorColumn = 12
# folderPath = "sign_done_row_merge"
# saveToPathRow = "sign_done_full_page_merge"
# filePrefix = "placa_paletes_nivel{}_pagina".format(levelorColumn)
# mergeStickerPrintPage(folderPath, saveToPathRow, filePrefix, printRow, printColumn, levelorColumn)