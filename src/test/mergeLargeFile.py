import cv2
import numpy as np

from pathlib import Path
from PIL import Image

imagesPath = "C:/personal-git/aresta-barcode/src/app/images/"

saveToPath = "C:/personal-git/aresta-barcode/src/archives"

allImgFullPath = []

for i in range(15):
    file1 = "{}sign_blank_pad/blank-sign8.PNG".format(imagesPath)
    img1 = cv2.imread(file1)
    allImgFullPath.append(img1)

print(len(allImgFullPath))


fullImg = cv2.hconcat(allImgFullPath)
# fullImg = cv2.vconcat([img3,fullImg])

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