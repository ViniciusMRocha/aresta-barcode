from PIL import Image
import os
from resizeimage import resizeimage

def renameLoop():
    for i in range(1,11):
        print(i)
        imagePath = "C:/personal-git/aresta-barcode/src/app/images/sticker-header-digits/Slide{}.PNG".format(i)
        newImagePath = "C:/personal-git/aresta-barcode/src/app/images/sticker-header-digits/resized/sticker-digit-{}.png".format(i-1)
        with open(imagePath, 'r+b') as f:
            with Image.open(f) as image:
                cover = resizeimage.resize_cover(image, [48, 114])
                cover.save(newImagePath, image.format)

def singleFileRename(fileName):
    with open(fileName, 'r+b') as f:
            with Image.open(f) as image:
                cover = resizeimage.resize_cover(image, [68, 114])
                cover.save(fileName, image.format)
