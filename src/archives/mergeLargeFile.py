import cv2
import numpy as np

from pathlib import Path
from PIL import Image

saveToPath = "C:/personal-git/aresta-barcode/src/archives"
file1 = "C:/personal-git/aresta-barcode/src/app/images/sign_done_row_merge/rua01_nivelMax8_linha00.PNG"
img1 = cv2.imread(file1)

file2 = "C:/personal-git/aresta-barcode/src/app/images/sign_done_row_merge/rua01_nivelMax8_linha01.PNG"
img2 = cv2.imread(file2)


fullImg = cv2.hconcat(img1, img2)
fileName = "testMerge"

# Save the file to path
cv2.imwrite("{}/{}.PNG".format(saveToPath,fileName), fullImg)