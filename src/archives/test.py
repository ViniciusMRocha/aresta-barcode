import cv2
import numpy as np
from pathlib import Path
from PIL import Image
import glob


imagePathSingle = "C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.01.01.001.nivelMax-8.PNG"

image = Image.open(imagePathSingle)
width, height = image.size
print("width:",width)
print("height:",height)


imagePathRow = "C:/personal-git/aresta-barcode/src/app/images/sign-done-row-merge/nivelMax-8-linha-00.PNG"

image = Image.open(imagePathRow)
width, height = image.size
print("width:",width)
print("height:",height)