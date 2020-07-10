import cv2
import numpy as np

from pathlib import Path
from PIL import Image

import barcode
from barcode.writer import ImageWriter
import customeFunctions

imagesPath = "C:/personal-git/aresta-barcode/src/app/images/"

# Generates the barcode image
def generateSingleBarcode(barcodeNumber):
    # Select encoding
    bcEcnoding = barcode.get_barcode_class('code128')
    # create the img writer
    barcodeImg = bcEcnoding(barcodeNumber, writer=ImageWriter())
    # Location where the new file will be saved
    savePath = "{}barcode_library/".format(imagesPath)+str(barcodeNumber)
    # Save file and specify styling.
    # File defaults to PNG

    customeOption = {"font_size": 24, "text_distance": 1.2,}
    barcodeImg.save(savePath,options=customeOption)


def getBarcode(state, city, street, column, level, product):
    city = customeFunctions.addZero_twoDigits(city)
    street = customeFunctions.addZero_twoDigits(street)
    column = customeFunctions.addZero_threeDigits(column)
    level = customeFunctions.addZero_twoDigits(level)
    product = customeFunctions.addZero_twoDigits(product)
    path = "{}barcode_library/{}.{}.{}.{}.{}.{}.png".format(imagesPath, state, city, street, column, level, product)
    barcode = cv2.imread(path)
    return barcode