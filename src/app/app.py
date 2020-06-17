import cv2
import numpy as np

from pathlib import Path
from PIL import Image

import barcode
from barcode.writer import ImageWriter

#My Files
import columnSign
import columnSticker
import aptSticker
import deleteExtras

# =========== MERGE TEST ==================================================

perSheet = 75
nivelMax = 8
columnSign.mergeSigns(perSheet, nivelMax)



'''
# =========== RUA 1 ==================================================
state = 1
city = 1
street = 1
column = 56
level = 8
product = 1
columnSign.createAll(state, city, street, column, level, product)
# columnSticker.createAll(state, city, street, column, level, product)


# =========== RUA 2 ==================================================
state = 1
city = 1
street = 2
column = 56
level = 8
product = 1
columnSign.createAll(state, city, street, column, level, product)
# columnSticker.createAll(state, city, street, column, level, product)


# =========== RUA 3 ==================================================
state = 1
city = 1
street = 3
column = 56
level = 8
product = 1
columnSign.createAll(state, city, street, column, level, product)
# columnSticker.createAll(state, city, street, column, level, product)


# =========== RUA 4 ==================================================
state = 1
city = 1
street = 4
column = 80
level = 8
product = 1

aptLevelMax = 2
apt = 3
columnStart = 9
columnEnd = 60
evenOddAll = "even"

columnSign.createAll(state, city, street, column, level, product)
# columnSticker.createAll(state, city, street, column, level, product)
# aptSticker.createAll(state, city, street, column, aptLevelMax, product, apt, columnStart, columnEnd, evenOddAll)


# =========== RUA 5 ==================================================
state = 1
city = 1
street = 5
column = 80
level = 8
product = 1

aptLevelMax = 2
apt = 3
columnStart = 9
columnEnd = 68
evenOddAll = "all"

columnSign.createAll(state, city, street, column, level, product)
# columnSticker.createAll(state, city, street, column, level, product)
# aptSticker.createAll(state, city, street, column, aptLevelMax, product, apt, columnStart, columnEnd, evenOddAll)


# =========== RUA 6 ==================================================
state = 1
city = 1
street = 6
column = 96
level = 8
product = 1

aptLevelMax = 2
apt = 3
columnStart = 9
columnEnd = 68
evenOddAll = "odd"

startDelete = 81
endDelete = column
sideRemove="odd"

columnSign.createAll(state, city, street, column, level, product)
# columnSticker.createAll(state, city, street, column, level, product)
# aptSticker.createAll(state, city, street, column, aptLevelMax, product, apt, columnStart, columnEnd, evenOddAll)
# deleteExtras.remove(state, city, street, column, level, product, startDelete, endDelete, sideRemove)

# =========== RUA 7 ==================================================
state = 1
city = 1
street = 7
column = 96
level = 8
product = 1
columnSign.createAll(state, city, street, column, level, product)
# columnSticker.createAll(state, city, street, column, level, product)


# =========== RUA 8 ==================================================
state = 1
city = 1
street = 8
column = 96
level = 8
product = 1
columnSign.createAll(state, city, street, column, level, product)
# columnSticker.createAll(state, city, street, column, level, product)


# =========== RUA 9 ==================================================
state = 1
city = 1
street = 9
column = 62
level = 8
product = 1
columnSign.createAll(state, city, street, column, level, product)
# columnSticker.createAll(state, city, street, column, level, product)


# =========== RUA 10 ==================================================
state = 1
city = 2
street = 10
column = 32
level = 6
product = 1
columnSign.createAll(state, city, street, column, level, product)
# columnSticker.createAll(state, city, street, column, level, product)


# =========== RUA 11 ==================================================
state = 1
city = 2
street = 11
product = 1

startColumn = 1
endColumn = 11
level = 8
columnSign.createAllRange(state, city, street, startColumn, level, product, endColumn)
# columnSticker.createAllRange(state, city, street, level, product, startColumn, endColumn)

startColumn = 12
endColumn = 31
level = 12
columnSign.createAllRange(state, city, street, startColumn, level, product, endColumn)
# columnSticker.createAllRange(state, city, street, level, product, startColumn, endColumn)

startColumn = 32
endColumn = 40
level = 8
columnSign.createAllRange(state, city, street, startColumn, level, product, endColumn)
# columnSticker.createAllRange(state, city, street, level, product, startColumn, endColumn)



'''

