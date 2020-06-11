import cv2
import numpy as np

from pathlib import Path
from PIL import Image

import barcode
from barcode.writer import ImageWriter

import customeFunctions

# =================================================
# Get Images
# =================================================



def getArrow():
    # print("Runnig getArrow")
    path = "C:/personal-git/aresta-barcode/src/app/images/sticker-arrow-up/sticker-arrow-up-black.PNG"
    arrow = cv2.imread(path)
    return arrow


def getHeader(index):
    # print("Runnig getHeader")
    path = "C:/personal-git/aresta-barcode/src/app/images/pallet-header/pallet-{}.PNG".format(index)
    header = cv2.imread(path)
    return header

def getBarcode(state, city, region, isle, shelf, product):
    # print("Runnig getBarcode")
    city = customeFunctions.addZero_twoDigits(city)
    region = customeFunctions.addZero_twoDigits(region)
    isle = customeFunctions.addZero_threeDigits(isle)
    shelf = customeFunctions.addZero_twoDigits(shelf)
    product = customeFunctions.addZero_twoDigits(product)
    path = "C:/personal-git/aresta-barcode/src/app/images/barcode-library/{}.{}.{}.{}.{}.{}.png".format(state, city, region, isle, shelf, product)
    barcode = cv2.imread(path)
    return barcode

# =================================================
# Combine Images
# =================================================

def createPallet(state, city, region, isle, shelf, product, pallet):

    # Generate sectioin images
    arrow = getArrow()
    header = getHeader(pallet) #420 x 114
    barcode = getBarcode(state, city, region, isle, shelf, product)

    # Combine Images
    img1 = cv2.vconcat([header,barcode])
    img2 = cv2.hconcat([img1,arrow])

    # Create File Name
    city = customeFunctions.addZero_twoDigits(city)
    region = customeFunctions.addZero_twoDigits(region)
    isle = customeFunctions.addZero_threeDigits(isle)
    shelf = customeFunctions.addZero_twoDigits(shelf)
    fileName = "{}.{}.{}.{}.{}.{}-pallet-{}.png".format(state, city, region, isle, shelf, product, pallet)

    savePath = "C:/personal-git/aresta-barcode/src/app/images/pallet-done/{}".format(fileName)
    cv2.imwrite(savePath, img2)
    print(savePath)


state = 1
city = 1
region = 2
isle = 3 #Give Max Value
shelf = 2 #Give Max Value
product = 1
pallet = 2

# createPallet(state, city, region, isle, shelf, product, pallet)

for i in range(1,isle+1):
    print("Isle: ",i)
    for s in range(1,shelf+1):
        for a in range(1,pallet+1):
            # print("isle-{} floor-{} pallet-{}".format(i,s,a))
            createPallet(state, city, region, i, s, product, a)




