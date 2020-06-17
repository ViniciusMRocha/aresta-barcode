from PIL import Image
import os
from resizeimage import resizeimage


def singleFileResize(fileName,width,height):
    with open(fileName, 'r+b') as f:
            with Image.open(f) as image:
                cover = resizeimage.resize_cover(image, [width, height])
                cover.save(fileName, image.format)

'''
# ====== APT ==========================================
fileName = "C:/Users/vinir/OneDrive/Desktop/aresta-share/resize/apt.png"
width = 378
height = 189
singleFileResize(fileName,width,height)

# ====== INV ==========================================
fileName = "C:/Users/vinir/OneDrive/Desktop/aresta-share/resize/inv.PNG"
width = 378
height = 189
singleFileResize(fileName,width,height)

# ====== PLACA 1-6 ==========================================
fileName = "C:/Users/vinir/OneDrive/Desktop/aresta-share/resize/placa1-6.PNG"
width = 246
height = 1118
singleFileResize(fileName,width,height)

# ====== PLACA 1-8 ==========================================
fileName = "C:/Users/vinir/OneDrive/Desktop/aresta-share/resize/placa1-8.PNG"
width = 246
height = 1437
singleFileResize(fileName,width,height)

# ====== PLACA 1-12 ==========================================
fileName = "C:/Users/vinir/OneDrive/Desktop/aresta-share/resize/placa1-12.PNG"
width = 246
height = 2075
singleFileResize(fileName,width,height)
'''
