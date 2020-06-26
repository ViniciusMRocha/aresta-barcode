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


def getBlankSignPath(index):
    path = "{}sign_blank_pad/blank-sign{}.PNG".format(imagesPath, index)
    return path

# ====== Merge ===============================

def mergeSign(state, city, street, level, printRow, printColumn):

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