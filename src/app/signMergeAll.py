import cv2
from pathlib import Path
from PIL import Image
import barcode
from barcode.writer import ImageWriter
import numpy as np
from os import listdir
from os.path import isfile, join

#My Files
import customeFunctions

#TODO: Name the file according to the city-rua-00
def mergeSigns(signPerSheet):
    # Path to where all the individual images are
    path = 'C:/personal-git/aresta-barcode/src/app/images/sign-single-done/'

    # Save new file to the path below 
    saveToPath = "C:/personal-git/aresta-barcode/src/app/images/sign-multiple-done"

    # Search for all the files in directory
    # FIXME: join is not working 
    columnImg = [f for f in listdir(path) if isfile(join(path, f))]

    # list for all the images full path
    allImgFullPath = []
    #All Images
    listTest = []

    # Add full path to each file
    for i in range(len(columnImg)):
        # Merge the file name to the rest of the path
        fullPath = join(path,columnImg[i])
        columnImg[i] = fullPath
        # print(columnImg[i])

    streetId = 0
    for i in range(len(columnImg)):
        if i%5 == 0:
            streetId = streetId+1
            for j in range(signPerSheet):
                sign = i+j
                listTest.append(columnImg[sign])
                # listTest.append(sign)
            print("Combining Rua{}: ".format(streetId),listTest)
            for k in range(len(listTest)):
                #Creates image object
                toImg = cv2.imread(listTest[k])
                # Saves image object to list
                allImgFullPath.append(toImg)

            # Convers the list to array
            allImgFullPath_array = np.array(allImgFullPath)

            # Combines all the individual column images to one image
            fullImg = cv2.hconcat(allImgFullPath_array)

            # Save the file to path
            cv2.imwrite("{}/{}.jpeg".format(saveToPath,"Cidade-Rua{}".format(streetId)), fullImg)
            allImgFullPath.clear()
            listTest.clear()


# Testing
# mergeSigns(5)