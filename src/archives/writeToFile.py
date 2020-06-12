from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys
import cv2
import numpy as np

path = "C:/personal-git/aresta-barcode/src/app/column-bg.png"
columnNumber = "001"
columnBg = Image.open(path)
font = ImageFont.truetype('Roboto-Bold.ttf',65)
draw = ImageDraw.Draw("001")
draw.text((100, 100), columnNumber, (1, 1, 1), font=font)
columnBg.show()



# # in_file = "C:/personal-git/aresta-barcode/src/app/blank.png"
# in_file = "C:/personal-git/aresta-barcode/src/app/pil_color.png"
# # in_file = "C:/personal-git/aresta-barcode/src/app/blank-small.png"
# text ="002"
# out_file = "column-out.png"
 
# img = Image.open(in_file)
# draw = ImageDraw.Draw(img)
# font = ImageFont.truetype('Roboto-Bold.ttf',20)
# draw.text((0, 0), text, (1, 1, 1), font=font)
# img.save(out_file)
