import cv2
import numpy as np

# Header
# Add Arrow
# Add BIG isle number

# Barcodes
barcode1 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/barcode-library/1.01.02.001.01.01.png")
barcode2 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/barcode-library/1.01.02.001.02.01.png")
barcode3 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/barcode-library/1.01.02.001.03.01.png")
barcode4 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/barcode-library/1.01.02.001.04.01.png")
barcode5 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/barcode-library/1.01.02.001.05.01.png")
barcode6 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/barcode-library/1.01.02.001.06.01.png")
barcode7 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/barcode-library/1.01.02.001.07.01.png")

# Labels
label1 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/number-labels/label-1.PNG")
label2 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/number-labels/label-2.PNG")
label3 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/number-labels/label-3.PNG")
label4 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/number-labels/label-4.PNG")
label5 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/number-labels/label-5.PNG")
label6 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/number-labels/label-6.PNG")
label7 = cv2.imread("C:/personal-git/aresta-barcode/src/app/images/number-labels/label-7.PNG")

#Combine images
fullImg = cv2.vconcat([label1, barcode1, label2, barcode2, label3, barcode3, label4, barcode4, label5, barcode5, label6, barcode6, label7, barcode7])

#Save file
cv2.imwrite("C:/personal-git/aresta-barcode/src/app/images/print-folder/conbined.jpeg", fullImg)
