import cv2
import numpy as np

from pathlib import Path
from PIL import Image

import barcode
from barcode.writer import ImageWriter

#My Files
import signMergeAll
import aptStickerCreate
import aptStickerMerge
import columnStickerCreate
import columnStickerMerge
import signCreateSingle


'''
# =========== RUA 1 ==================================================
state = 1
city = 1
street = 1
column = 57
level = 9
product = 1
signCreateSingle.createAllImages(state, city, street, column, level, product)
columnStickerCreate.createAllColumnStickers(state, city, street, column, level, product)


# =========== RUA 2 ==================================================
state = 1
city = 1
street = 2
column = 57
level = 9
product = 1
signCreateSingle.createAllImages(state, city, street, column, level, product)
columnStickerCreate.createAllColumnStickers(state, city, street, column, level, product)


# =========== RUA 3 ==================================================
state = 1
city = 1
street = 3
column = 57
level = 9
product = 1
signCreateSingle.createAllImages(state, city, street, column, level, product)
columnStickerCreate.createAllColumnStickers(state, city, street, column, level, product)


# =========== RUA 4 ==================================================
state = 1
city = 1
street = 4
column = 81
level = 9
product = 1

aptLevel = 2
apt = 3
columnStart = 9
columnEnd = 60
evenOddAll = "even"

signCreateSingle.createAllImages(state, city, street, column, level, product)
columnStickerCreate.createAllColumnStickers(state, city, street, column, level, product)
aptStickerCreate.createAllAptSticker(state, city, street, column, aptLevel, product, apt, columnStart, columnEnd, evenOddAll)


# =========== RUA 5 ==================================================
state = 1
city = 1
street = 5
column = 81
level = 9
product = 1

aptLevel = 2
apt = 3
columnStart = 9
columnEnd = 68
evenOddAll = "all"

signCreateSingle.createAllImages(state, city, street, column, level, product)
columnStickerCreate.createAllColumnStickers(state, city, street, column, level, product)
aptStickerCreate.createAllAptSticker(state, city, street, column, aptLevel, product, apt, columnStart, columnEnd, evenOddAll)


# =========== RUA 6 ==================================================
state = 1
city = 1
street = 6
column = 97
level = 9
product = 1

aptLevel = 2
apt = 3
columnStart = 9
columnEnd = 68
evenOddAll = "odds"

signCreateSingle.createAllImages(state, city, street, column, level, product)
columnStickerCreate.createAllColumnStickers(state, city, street, column, level, product)
aptStickerCreate.createAllAptSticker(state, city, street, column, aptLevel, product, apt, columnStart, columnEnd, evenOddAll)

#TODO: Account for the difference of column lengths

# =========== RUA 7 ==================================================
state = 1
city = 1
street = 7
column = 97
level = 9
product = 1
signCreateSingle.createAllImages(state, city, street, column, level, product)
columnStickerCreate.createAllColumnStickers(state, city, street, column, level, product)


# =========== RUA 8 ==================================================
state = 1
city = 1
street = 8
column = 97
level = 9
product = 1
signCreateSingle.createAllImages(state, city, street, column, level, product)
columnStickerCreate.createAllColumnStickers(state, city, street, column, level, product)


# =========== RUA 9 ==================================================
state = 1
city = 1
street = 9
column = 63
level = 9
product = 1
signCreateSingle.createAllImages(state, city, street, column, level, product)
columnStickerCreate.createAllColumnStickers(state, city, street, column, level, product)


# =========== RUA 10 ==================================================
state = 1
city = 2
street = 10
column = 33
level = 7
product = 1
signCreateSingle.createAllImages(state, city, street, column, level, product)
columnStickerCreate.createAllColumnStickers(state, city, street, column, level, product)


# =========== RUA 11 ==================================================
state = 1
city = 2
street = 11
column = 41
level = 8
product = 1
signCreateSingle.createAllImages(state, city, street, column, level, product)
columnStickerCreate.createAllColumnStickers(state, city, street, column, level, product)
#TODO: make it start and end point for 12 level column
'''