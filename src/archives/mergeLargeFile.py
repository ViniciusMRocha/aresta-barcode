import cv2
import numpy as np

from pathlib import Path
from PIL import Image

imagesPath = "C:/personal-git/aresta-barcode/src/app/images/"

saveToPath = "C:/personal-git/aresta-barcode/src/archives"

allImgFullPath = []

file1 = "{}column_done_row_merge/adesivo_inventario_rua04_linha00.PNG".format(imagesPath)
img1 = cv2.imread(file1)

file2 = "{}column_done_row_merge/adesivo_inventario_rua04_linha01.PNG".format(imagesPath)
img2 = cv2.imread(file2)

allImgFullPath.append(img1)
allImgFullPath.append(img2)

allImgFullPath_array = np.array(allImgFullPath)

fullImg = cv2.vconcat(allImgFullPath_array)
fileName = "testMerge"

# Save the file to path
cv2.imwrite("{}/{}.PNG".format(saveToPath,fileName), fullImg)