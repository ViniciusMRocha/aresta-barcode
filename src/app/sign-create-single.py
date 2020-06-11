import cv2
import numpy as np

from pathlib import Path
from PIL import Image

import barcode
from barcode.writer import ImageWriter

import customeFunctions

# Returns the single digit image for the header
def getDigit(digit):
    path ="C:/personal-git/aresta-barcode/src/app/images/sign-header-single-digits/digit{}.PNG".format(digit)
    digitImg = cv2.imread(path)
    return digitImg

def getLabel(index):
    # print("Runnig getLabel")
    path ="C:/personal-git/aresta-barcode/src/app/images/sign-barcode-header/label-{}.PNG".format(index)
    label = cv2.imread(path)
    return label

def getPad():
    # print("Runnig getPad")
    path = "C:/personal-git/aresta-barcode/src/app/images/sign-barcode-header-pad/pad.PNG"
    pad = cv2.imread(path)
    return pad

# Generates the correct arrow given the isle number
def getArrow(isle):
    #pattern repeats for every 4 digits.
    #Current Patters: >> >> << <<
    isle = int(isle)
    total = isle/4
    totalNoRemainder = isle//4
    check = total-totalNoRemainder
    if check == 0.25 or check == 0.5:
        # Arrow: >>> 
        arrow = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/sign-header-arrow/right-arrow.PNG")
    elif check == 0.75 or check == 0.0:
        # Arrow: <<<
        arrow = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/sign-header-arrow/left-arrow.PNG")
    return arrow

def getBarcode(state, city, region, isle, shelf, product):
    # print("Runnig getBarcode")
    city = customeFunctions.addZero_twoDigits(city)
    region = customeFunctions.addZero_twoDigits(region)
    isle = customeFunctions.addZero_threeDigits(isle)
    shelf = customeFunctions.addZero_twoDigits(shelf)
    product = customeFunctions.addZero_twoDigits(product)
    path = "C:/personal-git/aresta-barcode/src/app/images/barcode-library/{}.{}.{}.{}.{}.{}.png".format(state, city, region, isle, shelf, product)
    print(path)
    barcode = cv2.imread(path)
    return barcode

# Generates the barcode image
def generateBarcode(barcodeNumber):
    # Select encoding
    bcEcnoding = barcode.get_barcode_class('code128')
    # create the img writer
    barcodeImg = bcEcnoding(barcodeNumber, writer=ImageWriter())
    # Location where the new file will be saved
    savePath = "C:/personal-git/aresta-barcode/src/app/images/barcode-library/"+str(barcodeNumber)
    # Save file and specify styling.
    # File defaults to PNG
    barcodeFile = barcodeImg.save(savePath,options={"font_size": 24, "text_distance": 1.2,})
    return barcodeFile

# generates the isle label, buy taking a isle number and generating a image from the digit images
def createIsleLable(isle):

    #Makes "1" into "001"
    isle = customeFunctions.addZero_threeDigits(isle)
    #substring the input into 3 digits
    isleDigit1 = isle[0:1]
    isleDigit2 = isle[1:2]
    isleDigit3 = isle[2:3]

    # Gets the digits images for each isle digit 
    firstDigit = getDigit(isleDigit1)
    secondDigit = getDigit(isleDigit2)
    thirdDigit = getDigit(isleDigit3)
    # Create New Isle

    isleImg = cv2.hconcat([getPad(),firstDigit,secondDigit,thirdDigit,getPad()])
    headerImg = cv2.vconcat([getArrow(isle),isleImg])

    return headerImg


# Generates all isle images
def createAllImages(state, city, region, isle, shelfMax, product):
    city = customeFunctions.addZero_twoDigits(city)
    region = customeFunctions.addZero_twoDigits(region)
    product = customeFunctions.addZero_twoDigits(product)
    allBarcodesPath = []

    for isle in range(1, isle):
        isleThreeDigits = customeFunctions.addZero_threeDigits(isle)
        for shelf in range(1, shelfMax):
            shelf = customeFunctions.addZero_twoDigits(shelf) 

            # Generate Barcode
            barcodeNumber = ('{}.{}.{}.{}.{}.{}').format(state, city, region, isleThreeDigits, shelf, product)
            generateBarcode(barcodeNumber)
            barcodeImgPath = "C:/personal-git/aresta-barcode/src/app/images/barcode-library/{}.{}.{}.{}.{}.{}.png".format(state, city, region, isleThreeDigits,shelf,product)
            allBarcodesPath.append(barcodeImgPath)

        # Generates the a single isle image
        createIsleImage(isle, shelf, allBarcodesPath)

        # Clear list for next iteration
        allBarcodesPath.clear()

# Generates the a single isle image
def createIsleImage(isle, shelf, allBarcodesPath):

    labelAndBarcode = []
    isle = int(isle)
    shelf = int(shelf)
    
    if (isle % 2) == 0:
        for i in range(shelf-1,0,-1):
            lable = getLabel(i)
            labelAndBarcode.append(lable)
            barcodeImg = cv2.imread(allBarcodesPath[i-1])
            labelAndBarcode.append(barcodeImg)
    if (isle % 2) > 0:
        for i in range(shelf,0,-1):
            lable = getLabel(i)
            labelAndBarcode.append(lable)
            barcodeImg = cv2.imread(allBarcodesPath[i-1])
            labelAndBarcode.append(barcodeImg)


    # Convers the list to array
    labelAndBarcode_array = np.array(labelAndBarcode)
    
    # Generate Isle Image File
    fullImg = cv2.vconcat(labelAndBarcode_array)
    fullImg = cv2.vconcat([createIsleLable(isle),fullImg])
    # Save file
    isleThreeDigits = customeFunctions.addZero_threeDigits(isle)
    fileName = ('{}.{}.{}.{}').format(state, city, region, isleThreeDigits)
    cv2.imwrite("C:/personal-git/aresta-barcode/src/app/images/sign-single-done/{}.jpeg".format(fileName), fullImg)

    print("Generating Image: {}.jpeg".format(fileName))


# ===============================================================
# USER INPUT 

state = 1
city = 1
region = 2
isle = 5
shelf = 8
product = 1

# ===============================================================

# Apply offset
isle = isle + 1
shelf = shelf + 1

# Generate all images
createAllImages(state, city, region, isle, shelf, product)

