from PIL import Image
import barcode
from barcode.writer import ImageWriter

# Generate barcodes

num1 = '1'
num2 = '01'
num3 = '02'
num4 = '059'
num5 = '07'
num6 = '01'

barcodeNumber = ('{}.{}.{}.{}.{}.{}').format(num1,num2,num3,num4,num5,num6)
bcEcnoding=barcode.get_barcode_class('code39')
barcodeImg=bcEcnoding(barcodeNumber,writer=ImageWriter())
barcodeFile=barcodeImg.save(barcodeNumber)

bg = Image.open("bg.png")
leftArrow = Image.open("leftArrow.png")
rightArrow = Image.open("rightArrow.png")
barcode1 = Image.open(bcFile1)
barcode2 = Image.open(bcFile2)
barcode3 = Image.open(bcFile3)
barcode4 = Image.open(bcFile4)
barcode5 = Image.open(bcFile5)
barcode6 = Image.open(bcFile6)
barcode7 = Image.open(bcFile7)


# TODO: Areas

# val = '1.01.02.059.07.01'
# Code 39
# 6.7cm x 40cm
# 250 x 1500
# 1.01.02.059.07.01 - 12 digits
# <<>><<>> - Arrow



# areaArrow = (0,0,512,512)

# bg.paste(arrow,areaArrow)

# bg.show()