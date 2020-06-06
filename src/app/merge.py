import cv2
import numpy as np
from pathlib import Path
from PIL import Image
import barcode
from barcode.writer import ImageWriter


def addZero_threeDigits(check):
    if check <= 9:
        check = '00' + str(check)
    elif check <= 99:
        check = '0' + str(check)
    return check

def addZero_twoDigits(check):
    if check <= 9:
        check = '0' + str(check)
    else:
        check = '' + str(check)
    return check

def getDigit(digit):
    path ="C:/personal-git/aresta-barcode/src/app/images/single-digits/digit{}.PNG".format(digit)
    digitImg = cv2.imread(path)
    return digitImg

def getBarcode(barcodeNumber):
    bcEcnoding = barcode.get_barcode_class('code128')
    barcodeImg = bcEcnoding(barcodeNumber, writer=ImageWriter())
    savePath = "C:/personal-git/aresta-barcode/src/app/images/barcode-library/"+str(barcodeNumber)
    barcodeFile = barcodeImg.save(savePath)
    return barcodeFile


def createIsleLable(isle):
    isle = addZero_threeDigits(isle)
    isleDigit1 = isle[0:1]
    isleDigit2 = isle[1:2]
    isleDigit3 = isle[2:3]

    # Pad
    pad = cv2.imread("C:/personal-git/aresta-barcode/graphics-design/pads-labels/pad.PNG")
    
    # Arrow
    rightArrow = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/arrows/right-arrow.PNG")
    leftArrow = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/arrows/left-arrow.PNG")

    firstDigit = getDigit(isleDigit1)
    secondDigit = getDigit(isleDigit2)
    thirdDigit = getDigit(isleDigit3)

    # Create New Isle
    isleImg = cv2.hconcat([pad,firstDigit,secondDigit,thirdDigit,pad])
    headerImg = cv2.vconcat([rightArrow,isleImg])

    return headerImg




# Generate Barcode Number
def gerateBarCode(state, city, region, product):
    state = state
    city = addZero_twoDigits(city)
    region = addZero_twoDigits(region)
    product = addZero_twoDigits(product)

    allBarcodesImg = []

    isleMax = 4  # Enter one more then needed
    shelfMax = 8  # Enter one more then needed

    # Labels
    label1 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/number-labels/label-1.PNG")
    label2 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/number-labels/label-2.PNG")
    label3 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/number-labels/label-3.PNG")
    label4 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/number-labels/label-4.PNG")
    label5 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/number-labels/label-5.PNG")
    label6 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/number-labels/label-6.PNG")
    label7 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/number-labels/label-7.PNG")

    for isle in range(1, isleMax):
        createIsleLable(isle)
        isleThreeDigits = addZero_threeDigits(isle)
        for shelf in range(1, shelfMax):
            shelf = addZero_twoDigits(shelf)  

            # Generate Barcode         
            barcodeNumber = ('{}.{}.{}.{}.{}.{}').format(state, city, region, isleThreeDigits, shelf, product)
            barcodeNum = getBarcode(barcodeNumber)
            allBarcodesImg.append(barcodeNum)
            
        # TODO: Make it dinamic
        # barcodeImgPath = "C:/personal-git/aresta-barcode/src/app/images/barcode-library/1.01.02.{isleThreeDigits}.01.01.png".format()
        barcodeImg1 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/barcode-library/1.01.02.001.01.01.png")
        barcodeImg2 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/barcode-library/1.01.02.001.02.01.png")
        barcodeImg3 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/barcode-library/1.01.02.001.03.01.png")
        barcodeImg4 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/barcode-library/1.01.02.001.04.01.png")
        barcodeImg5 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/barcode-library/1.01.02.001.05.01.png")
        barcodeImg6 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/barcode-library/1.01.02.001.06.01.png")
        barcodeImg7 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/barcode-library/1.01.02.001.07.01.png")
  
        # Generate File
        fullImg = cv2.vconcat([createIsleLable(isle), label1, barcodeImg1, label2, barcodeImg2, label3, barcodeImg3, label4, barcodeImg4, label5, barcodeImg5, label6, barcodeImg6, label7, barcodeImg7])

        # Save file
        fileName = ('{}.{}.{}.{}.{}').format(state, city, region, isleThreeDigits, shelf)
        cv2.imwrite("C:/personal-git/aresta-barcode/src/app/images/print-folder/{}.jpeg".format(fileName), fullImg)


# Header - Inputs

state = 1
city = 1
region = 2 
product = 1

gerateBarCode(state, city, region, product)








