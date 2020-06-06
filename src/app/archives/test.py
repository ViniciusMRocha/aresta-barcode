import cv2
import numpy as np


def getDigit(digit):
    path ="C:/personal-git/aresta-barcode/src/app/images/single-digits/digit{}.PNG".format(digit)
    digitImg = cv2.imread(path)
    print (path)
    return digitImg
getDigit(1)