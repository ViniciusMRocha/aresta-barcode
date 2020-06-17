from PIL import Image
import os
from resizeimage import resizeimage


def singleFileRename(fileName,width,height):
    with open(fileName, 'r+b') as f:
            with Image.open(f) as image:
                cover = resizeimage.resize_cover(image, [width, height])
                cover.save(fileName, image.format)


# def multipleFileRename(rootName,width,height,start,end):
 m

'''
# ====== APT ==========================================
fileName = "C:/Users/vinir/OneDrive/Desktop/aresta-share/resize/apt.png"
width = 378
height = 189
singleFileRename(fileName,width,height)

# ====== INV ==========================================
fileName = "C:/Users/vinir/OneDrive/Desktop/aresta-share/resize/inv.PNG"
width = 378
height = 189
singleFileRename(fileName,width,height)

# ====== PLACA 1-6 ==========================================
fileName = "C:/Users/vinir/OneDrive/Desktop/aresta-share/resize/placa1-6.PNG"
width = 246
height = 1118
singleFileRename(fileName,width,height)

# ====== PLACA 1-8 ==========================================
fileName = "C:/Users/vinir/OneDrive/Desktop/aresta-share/resize/placa1-8.PNG"
width = 246
height = 1437
singleFileRename(fileName,width,height)

# ====== PLACA 1-12 ==========================================
fileName = "C:/Users/vinir/OneDrive/Desktop/aresta-share/resize/placa1-12.PNG"
width = 246
height = 2075
singleFileRename(fileName,width,height)
'''
