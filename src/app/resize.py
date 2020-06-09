from PIL import Image
import os
from resizeimage import resizeimage


for i in range(1,11):
    print(i)
    imagePath = "C:/personal-git/aresta-barcode/src/app/images/sticker-header-digits/Slide{}.PNG".format(i)
    newImagePath = "C:/personal-git/aresta-barcode/src/app/images/sticker-header-digits/resized/sticker-digit-{}.png".format(i)
    with open(imagePath, 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [84, 114])
            cover.save(newImagePath, image.format)