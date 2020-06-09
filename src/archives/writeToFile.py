from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys
import cv2
import numpy as np

path = "C:/personal-git/aresta-barcode/src/app/isle-bg.png"
isleNumber = "001"
isleBg = Image.open(path)
font = ImageFont.truetype('Roboto-Bold.ttf',65)
draw = ImageDraw.Draw("001")
draw.text((100, 100), isleNumber, (1, 1, 1), font=font)
isleBg.show()



# # in_file = "C:/personal-git/aresta-barcode/src/app/blank.png"
# in_file = "C:/personal-git/aresta-barcode/src/app/pil_color.png"
# # in_file = "C:/personal-git/aresta-barcode/src/app/blank-small.png"
# text ="002"
# out_file = "isle-out.png"
 
# img = Image.open(in_file)
# draw = ImageDraw.Draw(img)
# font = ImageFont.truetype('Roboto-Bold.ttf',20)
# draw.text((0, 0), text, (1, 1, 1), font=font)
# img.save(out_file)
