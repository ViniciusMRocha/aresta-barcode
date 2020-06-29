import cv2
import numpy as np

from pathlib import Path
from PIL import Image

imagesPath = "C:/personal-git/aresta-barcode/src/app/images/"

saveToPath = "C:/personal-git/aresta-barcode/src/archives"

allImgFullPath = []

file1 = "{}column_done_single/inv-1.01.01.001.01.01.PNG".format(imagesPath)
img1 = cv2.imread(file1)

file2 = "{}lines/stickerSide.png".format(imagesPath)
img2 = cv2.imread(file2)

file3 = "{}lines/stickerTop.png".format(imagesPath)
img3 = cv2.imread(file3)

# allImgFullPath.append(img1)
# allImgFullPath.append(img2)
# allImgFullPath.append(img3)

fullImg = cv2.hconcat([img1,img2])
fullImg = cv2.vconcat([img3,fullImg])

fileName = "testImage"

# Save the file to path
cv2.imwrite("{}/{}.PNG".format(saveToPath,fileName), fullImg)


# def getLine(option):
#     if option == "side":
#         path = "{}lines/stickerSide.png".format(imagesPath)
#     if option == "top":
#         path = "{}lines/stickerTop.png".format(imagesPath)
#     line = cv2.imread(path)
#     return line