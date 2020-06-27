import cv2
import numpy as np

from pathlib import Path
from PIL import Image

from os import listdir
from os.path import isfile, join

import barcode
from barcode.writer import ImageWriter

import glob
# https://stackoverflow.com/questions/2225564/get-a-filtered-list-of-files-in-a-directory

import pprint

#My Files
import customeFunctions
import barcodeGenerator
import resize

imagesPath = "C:/personal-git/aresta-barcode/src/app/images/"



# ====== Merge ===============================

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

            print("Generating File: {}".format(fileName))

            # Save the file to path
            cv2.imwrite("{}/{}.PNG".format(saveToPathRow,fileName), fullImg)

            allImgFullPath.clear()
            rowImg.clear()
            

def mergeColumn(state, city, street, printRow, printColumn):

    city = customeFunctions.addZero_twoDigits(city)
    street = customeFunctions.addZero_twoDigits(street)

    def getBlankColumnPath():
        path = "{}column_blank_pad/column-sticker-blank.png".format(imagesPath)
        return path

    perSheet = printRow*printColumn

    blankSingleColumnPath = getBlankColumnPath()
    
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

            print("Generating File: {}".format(fileName))

            # Save the file to path
            cv2.imwrite("{}/{}.PNG".format(saveToPathRow,fileName), fullImg)

            allImgFullPath.clear()
            rowImg.clear()



def mergeApt(state, city, street, printRow, printColumn):

    city = customeFunctions.addZero_twoDigits(city)
    street = customeFunctions.addZero_twoDigits(street)

    def getBlankColumnPath():
        path = "{}apt_sticker_blank_pad/apt-sticker-blank.png".format(imagesPath)
        return path

    perSheet = printRow*printColumn

    blankSingleColumnPath = getBlankColumnPath()
    
    # Path to where all the individual images are
    path = '{}apt_sticker_done_single/'.format(imagesPath)

    # Save new file to the path below 
    saveToPathRow = "{}apt_sticker_done_row_merge".format(imagesPath)

    # files=glob.glob("{}*".format(path))
    files = glob.glob("{}/{}.{}.{}*".format(path, state, city, street))


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
    fullPage = []
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
            fileName = 'adesivo_apt_rua{}_linha{}'.format(street, rowCount)

            print("Generating File: {}".format(fileName))

            rowFile = "{}/{}.PNG".format(saveToPathRow,fileName)

            # Save the file to path
            cv2.imwrite(rowFile, fullImg)

            fullPage.append(rowFile)

            allImgFullPath.clear()
            rowImg.clear()

    pprint.pprint(fullPage)

    fullPageImages = []
    sheetCounter = 0
    if len(fullPage) <= printRow:
        for i in range(len(files)):
            # Creates image object
            toImg = cv2.imread(files[i])
            # Saves image object to list
            fullPageImages.append(toImg)
        sheetCounter = sheetCounter + 1
        
    elif len(fullPage) > printRow:
        print(" !!!!!!!!!!! HEY, ACCOUNT FOR THIS SENARIO !!!!!!!!")
        sheetCounter = sheetCounter + 1



    # # TODO: This only creates one single page per street
    # saveToPathSheet = "{}apt_sticker_done_full_page_merge".format(imagesPath)
    # path = "{}apt_sticker_done_row_merge".format(imagesPath)
    # searchFiles = "{}/adesivo_apt_rua{}*".format(path, street)
    # fileName = 'apartament_rua{}'.format(street)
    
    # def mergeToSheet(state, city, street, printRow, printColumn):
    #     city = customeFunctions.addZero_twoDigits(int(city))
    #     street = customeFunctions.addZero_twoDigits(int(street))
    #     # saveToPathSheet = "{}apt_sticker_done_full_page_merge".format(imagesPath)
    #     # path = "{}apt_sticker_done_row_merge".format(imagesPath)

    #     files = glob.glob(searchFiles)

    #     allImgFullPath_array = []
    #     sheetCounter = 0

    #     if len(files) <= printRow:
    #         for i in range(len(files)):
    #             # Creates image object
    #             toImg = cv2.imread(files[i])

    #             # Saves image object to list
    #             allImgFullPath.append(toImg)
    #             sheetCounter = sheetCounter + 1
    #     elif len(files) > printRow:
    #         print(" !!!!!!!!!!! HEY, ACCOUNT FOR THIS SENARIO !!!!!!!!")
    #         sheetCounter = sheetCounter + 1
            
    #     # Convers the list to array
    #     allImgFullPath_array = np.array(allImgFullPath)

    #     # Combines all the individual column images to one image
    #     fullImg = cv2.vconcat(allImgFullPath_array)

    #     fileNameLocal = '{}_pagina{}'.format(fileName, sheetCounter)

    #     print("Generating File: {}".format(fileName))

    #     # Save the file to path
    #     cv2.imwrite("{}/{}.PNG".format(saveToPathSheet,fileNameLocal), fullImg)

    #     allImgFullPath.clear()
    

    # mergeToSheet(state, city, street, printRow, printColumn)