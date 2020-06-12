from pathlib import Path
from PIL import Image
import barcode
from barcode.writer import ImageWriter

# Limits
num1Limit = 1
num2Limit = 2
num3Limit = 4
num4Limit = 4  # Enter one more then needed
num5Limit = 8  # Enter one more then needed

num1 = '1'  # State
num2 = '01'  # street
num3 = '02'  # City
num4 = 0  # column
num5 = 0  # level
num6 = 1  # Product

prefix = ('{}.{}.{}.').format(num1, num2, num3)



def addZero_threeDigits(check):
    if check <= 9:
        check = '00' + str(check)
    elif check <= 99:
        check = '0' + str(check)
    else:
        #Force to be string by adding ''
        check = '' + str(check)
    return check

def addZero_twoDigits(check):
    if check <= 9:
        check = '0' + str(check)
    else:
        check = '' + str(check)
    return check


allFileName = []

# Add 0 to product if less then 10
if num6 <= 9:
    num6 = '0' + str(num6)

for num4 in range(1, num4Limit):
    if num4 <= 9:
        num4 = '00' + str(num4)
    elif num4 <= 99:
        num4 = '0' + str(num4)
    for num5 in range(1, num5Limit):
        if num5 <= 9:
            num5 = '0' + str(num5)
            barcodeNumber = ('{}.{}.{}.{}.{}.{}').format(
                num1, num2, num3, num4, num5, num6)
            bcEcnoding = barcode.get_barcode_class('code128')
            barcodeImg = bcEcnoding(barcodeNumber, writer=ImageWriter())
            savePath = "C:/personal-git/aresta-barcode/src/app/images/barcode-library/"+str(barcodeNumber)
            barcodeFile = barcodeImg.save(savePath)
            allFileName.append(savePath+str('.png'))

print('Files Created')
