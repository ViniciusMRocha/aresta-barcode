from PIL import Image
import barcode
from barcode.writer import ImageWriter

# Limits
num1Limit = 1
num2Limit = 2
num3Limit = 4
num4Limit = 2 # Enter one more then needed 
num5Limit = 8 # Enter one more then needed 
num6Limit = 2 # Enter one more then needed 

num1 = '1' # State
num2 = '01' # Region
num3 = '02' # City
num4 = 000 # Isle
num5 = 00 # Shelf
num6 = 00 # Product

prefix = ('{}.{}.{}.').format(num1,num2,num3)


#TODO: Extract 0 adding function
def addZero (check):
    if check <= 9:
        check = '0' + str(check)
    elif check <= 99:
        check = '0' + str(check)
    return check

allFileName = []

for num4 in range (1,num4Limit):
    if num4 <= 9:
            num4 = '00' + str(num4)
    elif num4 <= 99:
            num4 = '0' + str(num4)
    for num5 in range(1,num5Limit):
            if num5 <= 9:
                num5 = '0' + str(num5)
            for num6 in range (1,num6Limit):
                if num6 <= 9:
                    num6 = '0' + str(num6)
                barcodeNumber = ('{}.{}.{}.{}.{}.{}').format(num1,num2,num3,num4,num5,num6)
                bcEcnoding=barcode.get_barcode_class('code128')
                barcodeImg=bcEcnoding(barcodeNumber,writer=ImageWriter())
                savePath = "barcode-library/"+str(barcodeNumber)
                barcodeFile=barcodeImg.save(savePath)
                allFileName.append(savePath+str('.png'))

print('Files Created')


# TODO: Add files to the bg file

# bg = Image.open("bg.png")
# barcode1 = Image.open(allFileName[1])
# barcode2 = Image.open(allFileName[2])
# barcode3 = Image.open(allFileName[3])
# barcode4 = Image.open(allFileName[4])
# barcode5 = Image.open(allFileName[5])
# barcode6 = Image.open(allFileName[6])
# barcode7 = Image.open(allFileName[7])


# x1 = 0
# x2 = 0
# y1 = 584
# y2 = 280

# for x in range(1,8):
#     pasteArea = (x1,x2,y1,y2)
#     bg.paste(barcode1,pasteArea)
#     x1 = x1 + 584
#     x2 = x2 + 280
#     y1 = y1 + 584
#     y2 = y2 + 280 

# bg.show()













# ----------------------------------------------------------------------------------------------------------------------------------------
# NOTES

# val = '1.01.02.059.07.01'
# 1.01.02.059.07.01 - 12 digits
# <<>><<>> - Arrow Order


# with open('barcode-library/1.01.02.001.01.01.png', 'r+b') as f:
#     with Image.open(f) as image:
#         cover = resizeimage.resize_cover(image, [200, 100],validate=False)
#         cover.save('test-image-cover.jpeg', image.format)

# Messuares
# 600px - 3565px
# 15.8cm x 94.32835821cm
# 6.7cm x 40cm

# ----------------------------------------------------------------------------------------------------------------------------------------