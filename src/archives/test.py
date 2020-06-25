import cv2
import numpy as np

path = "C:/personal-git/aresta-barcode/src/app/images/column-blank-pad/column-sticker-row-blank.png"

saveToPath = "C:/personal-git/aresta-barcode/src/app/images/column-blank-pad/"

toImg = cv2.imread(path)

img2 = cv2.hconcat([toImg,toImg])

cv2.imwrite("{}long.png".format(saveToPath),img2)