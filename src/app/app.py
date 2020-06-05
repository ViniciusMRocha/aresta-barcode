from pathlib import Path
from PIL import Image
import barcode
from barcode.writer import ImageWriter

# Limits
num1Limit = 1
num2Limit = 2
num3Limit = 4
num4Limit = 2  # Enter one more then needed
num5Limit = 8  # Enter one more then needed
num6Limit = 2  # Enter one more then needed

num1 = '1'  # State
num2 = '01'  # Region
num3 = '02'  # City
num4 = 000  # Isle
num5 = 00  # Shelf
num6 = 00  # Product

prefix = ('{}.{}.{}.').format(num1, num2, num3)


# TODO: Extract 0 adding function
def addZero(check):
    if check <= 9:
        check = '0' + str(check)
    elif check <= 99:
        check = '0' + str(check)
    return check


allFileName = []

for num4 in range(1, num4Limit):
    if num4 <= 9:
        num4 = '00' + str(num4)
    elif num4 <= 99:
        num4 = '0' + str(num4)
    for num5 in range(1, num5Limit):
        if num5 <= 9:
            num5 = '0' + str(num5)
        for num6 in range(1, num6Limit):
            if num6 <= 9:
                num6 = '0' + str(num6)
            barcodeNumber = ('{}.{}.{}.{}.{}.{}').format(
                num1, num2, num3, num4, num5, num6)
            bcEcnoding = barcode.get_barcode_class('code128')
            barcodeImg = bcEcnoding(barcodeNumber, writer=ImageWriter())
            savePath = "C:/personal-git/aresta-barcode/src/app/images/barcode-library/"+str(barcodeNumber)
            barcodeFile = barcodeImg.save(savePath)
            allFileName.append(savePath+str('.png'))

print('Files Created')
