import cv2
import numpy as np

from pathlib import Path
from PIL import Image

imagesPath = "C:/personal-git/aresta-barcode/src/app/images/"

saveToPath = "C:/personal-git/aresta-barcode/src/app/images/sign_blank_pad"

allImgFullPath = []

file1 = "{}sign_blank_pad/blank-sign12.PNG".format(imagesPath)
img1 = cv2.imread(file1)

file2 = "{}lines/signSideLine12.png".format(imagesPath)
img2 = cv2.imread(file2)

file3 = "{}lines/signTop.png".format(imagesPath)
img3 = cv2.imread(file3)

allImgFullPath.append(img1)
allImgFullPath.append(img2)
allImgFullPath.append(img3)

# allImgFullPath_array = np.array(allImgFullPath)

fullImg = cv2.hconcat([img1,img2])
fullImg = cv2.vconcat([img3,fullImg])

fileName = "signAndLine6"

# Save the file to path
cv2.imwrite("{}/{}.PNG".format(saveToPath,fileName), fullImg)