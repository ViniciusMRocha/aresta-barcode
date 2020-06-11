import cv2
from pathlib import Path
from PIL import Image
import barcode
from barcode.writer import ImageWriter
import numpy as np
from os import listdir
from os.path import isfile, join
import customeFunctions

# Path to where all the individual images are
path = 'C:/personal-git/aresta-barcode/src/app/images/sign-single-done/'

# New file name
newFileName = "isle-1-10"

# Save new file to the path below 
saveToPath = "C:/personal-git/aresta-barcode/src/app/images/sign-multiple-done"

# Search for all the files in directory
# FIXME: join is not working 
isleImg = [f for f in listdir(path) if isfile(join(path, f))]

# list for all the images full path
allImgFullPath = []

print("Merging the following files: ")
for i in range(len(isleImg)):
    # Merge the file name to the rest of the path
    fullPath = join(path,isleImg[i])
    isleImg[i] = fullPath
    print(isleImg[i])
    #Creates image object
    toImg = cv2.imread(isleImg[i])
    # Saves image object to list
    allImgFullPath.append(toImg)

# Convers the list to array
allImgFullPath_array = np.array(allImgFullPath)

# Combines all the individual isle images to one image
fullImg = cv2.hconcat(allImgFullPath_array)

# Save the file to path
cv2.imwrite("{}/{}.jpeg".format(saveToPath,newFileName), fullImg)