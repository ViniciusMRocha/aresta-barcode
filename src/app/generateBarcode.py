import cv2
import numpy as np

from pathlib import Path
from PIL import Image

import barcode
from barcode.writer import ImageWriter


# Generates the barcode image
def generateSingleBarcode(barcodeNumber):
    # Select encoding
    bcEcnoding = barcode.get_barcode_class('code128')
    # create the img writer
    barcodeImg = bcEcnoding(barcodeNumber, writer=ImageWriter())
    # Location where the new file will be saved
    savePath = "C:/personal-git/aresta-barcode/src/app/images/barcode-library/"+str(barcodeNumber)
    # Save file and specify styling.
    # File defaults to PNG

    fontPath = "C:/personal-git/aresta-barcode/src/app/Roboto/Roboto-Light.ttf"

    customeOption = {"font_path": fontPath, "font_size": 24, "text_distance": 1.2,}
    
    barcodeImg.save(savePath,options=customeOption)
