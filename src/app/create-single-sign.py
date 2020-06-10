import cv2
import numpy as np

from pathlib import Path
from PIL import Image

import barcode
from barcode.writer import ImageWriter

#TODO: Create variables for location of files. DO NOT hardcode file paths

# Adds "00" to a 1 digit number or "0" to a 2 digit number
def addZero_threeDigits(check):
    if check <= 9:
        check = '00' + str(check)
    elif check <= 99:
        check = '0' + str(check)
    return check

# Adds a "0" to a 2 digit number
def addZero_twoDigits(check):
    if check <= 9:
        check = '0' + str(check)
    else:
        #Force to be string by adding ''
        check = '' + str(check)
    return check

# Returns the single digit image for the header
def getDigit(digit):
    path ="C:/personal-git/aresta-barcode/src/app/images/sign-header-single-digits/digit{}.PNG".format(digit)
    digitImg = cv2.imread(path)
    return digitImg

# Generates the barcode image
def getBarcode(barcodeNumber):
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

# generates the isle label, buy taking a isle number and generating a image from the digit images
def createIsleLable(isle):

    #Makes "1" into "001"
    isle = addZero_threeDigits(isle)
    
    #substring the input into 3 digits
    isleDigit1 = isle[0:1]
    isleDigit2 = isle[1:2]
    isleDigit3 = isle[2:3]

    # Padding
    pad = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/sign-barcode-header-pad/pad.PNG")
    
    
    # Gets the digits images for each isle digit 
    firstDigit = getDigit(isleDigit1)
    secondDigit = getDigit(isleDigit2)
    thirdDigit = getDigit(isleDigit3)

    # Create New Isle
    isleImg = cv2.hconcat([pad,firstDigit,secondDigit,thirdDigit,pad])
    headerImg = cv2.vconcat([getArrow(isle),isleImg])

    return headerImg


# Generates all isle images
def createAllImages(state, city, region, isle, shelfMax, product):
    city = addZero_twoDigits(city)
    region = addZero_twoDigits(region)
    product = addZero_twoDigits(product)
    allBarcodesPath = []

    for isle in range(1, isle):
        isleThreeDigits = addZero_threeDigits(isle)
        for shelf in range(1, shelfMax):
            shelf = addZero_twoDigits(shelf) 

            # Generate Barcode
            barcodeNumber = ('{}.{}.{}.{}.{}.{}').format(state, city, region, isleThreeDigits, shelf, product)
            getBarcode(barcodeNumber)
            barcodeImgPath = "C:/personal-git/aresta-barcode/src/app/images/barcode-library/{}.{}.{}.{}.{}.{}.png".format(state, city, region, isleThreeDigits,shelf,product)
            allBarcodesPath.append(barcodeImgPath)

        # Generates the a single isle image
        createIsleImage(isle, shelf, allBarcodesPath)

        # Clear list for next iteration
        allBarcodesPath.clear()

# Generates the a single isle image
def createIsleImage(isle, shelf, allBarcodesPath):

    # Labels
    label1 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/sign-barcode-header/label-1.PNG")
    label2 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/sign-barcode-header/label-2.PNG")
    label3 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/sign-barcode-header/label-3.PNG")
    label4 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/sign-barcode-header/label-4.PNG")
    label5 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/sign-barcode-header/label-5.PNG")
    label6 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/sign-barcode-header/label-6.PNG")
    label7 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/sign-barcode-header/label-7.PNG")

    # TODO: Dynamicaly generate the barcode
    # allBarcodeImg = []

    # for i in range(len(allBarcodesPath)):
    #     barcodeImg = cv2.imread(allBarcodesPath[i])
    #     allBarcodeImg.append(barcodeImg)

    # allBarcodeImg_array = np.array(allBarcodeImg)
    # fullImg = cv2.vconcat(createIsleLable(isle),allBarcodeImg_array)

    # Each barcode for the isle image
    i=0
    barcodeImg1 = cv2.imread(allBarcodesPath[i])
    barcodeImg2 = cv2.imread(allBarcodesPath[i+1])
    barcodeImg3 = cv2.imread(allBarcodesPath[i+2])
    barcodeImg4 = cv2.imread(allBarcodesPath[i+3])
    barcodeImg5 = cv2.imread(allBarcodesPath[i+4])
    barcodeImg6 = cv2.imread(allBarcodesPath[i+5])
    barcodeImg7 = cv2.imread(allBarcodesPath[i+6])

    # Generate Isle Image File
    fullImg = cv2.vconcat([createIsleLable(isle), label7, barcodeImg7, label6, barcodeImg6, label5, barcodeImg5, label4, barcodeImg4, label3, barcodeImg3, label2, barcodeImg2, label1, barcodeImg1])

    # Save file
    isleThreeDigits = addZero_threeDigits(isle)
    fileName = ('{}.{}.{}.{}').format(state, city, region, isleThreeDigits)
    cv2.imwrite("C:/personal-git/aresta-barcode/src/app/images/sign-single-done/{}.jpeg".format(fileName), fullImg)

    print('\n')
    print("Generating Image: {}.jpeg".format(fileName))
    print ('Isle: {} \nMax Shelf: {} \nBarcodes List: {}'.format(isle,shelf,allBarcodesPath))

# ===============================================================
# USER INPUT 

state = 1
city = 1
region = 2
isle = 10
shelf = 7
product = 2

# ===============================================================

# Apply offset
isle = isle + 1
shelf = shelf + 1

# Generate all images
createAllImages(state, city, region, isle, shelf, product)

