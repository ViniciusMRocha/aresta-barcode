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


# =========== RUA 1 ==================================================
state = 1
city = 1
street = 1
column = 56
level = 8
product = 1
columnSign.createAll(state, city, street, column, level, product)
columnSticker.createAll(state, city, street, column, level, product)


# =========== RUA 2 ==================================================
state = 1
city = 1
street = 2
column = 56
level = 8
product = 1
columnSign.createAll(state, city, street, column, level, product)
columnSticker.createAll(state, city, street, column, level, product)


# =========== RUA 3 ==================================================
state = 1
city = 1
street = 3
column = 56
level = 8
product = 1
columnSign.createAll(state, city, street, column, level, product)
columnSticker.createAll(state, city, street, column, level, product)


# =========== RUA 4 ==================================================
state = 1
city = 1
street = 4
column = 80
level = 8
product = 1

aptLevelMax = 2
apt = 3
columnStart = 10
columnEnd = 60
evenOddAll = "even"

columnSign.createAll(state, city, street, column, level, product)
columnSticker.createAll(state, city, street, column, level, product)
aptSticker.createAll(state, city, street, column, aptLevelMax, product, apt, columnStart, columnEnd, evenOddAll)
deleteExtras.removeColumnSticker(state, city, street, column, aptLevelMax, product, apt, columnStart, columnEnd, evenOddAll)


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
columnSticker.createAll(state, city, street, column, level, product)
aptSticker.createAll(state, city, street, column, aptLevelMax, product, apt, columnStart, columnEnd, evenOddAll)
deleteExtras.removeColumnSticker(state, city, street, column, aptLevelMax, product, apt, columnStart, columnEnd, evenOddAll)


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
columnEnd = 67
evenOddAll = "odd"

startDelete = 81
endDelete = column
sideRemove="odd"

columnSign.createAll(state, city, street, column, level, product)
columnSticker.createAll(state, city, street, column, level, product)
aptSticker.createAll(state, city, street, column, aptLevelMax, product, apt, columnStart, columnEnd, evenOddAll)
deleteExtras.removeColumn(state, city, street, column, level, product, startDelete, endDelete, sideRemove)
deleteExtras.removeColumnSticker(state, city, street, column, aptLevelMax, product, apt, columnStart, columnEnd, evenOddAll)

# =========== RUA 7 ==================================================
state = 1
city = 1
street = 7
column = 96
level = 8
product = 1
columnSign.createAll(state, city, street, column, level, product)
columnSticker.createAll(state, city, street, column, level, product)


# =========== RUA 8 ==================================================
state = 1
city = 1
street = 8
column = 96
level = 8
product = 1
columnSign.createAll(state, city, street, column, level, product)
columnSticker.createAll(state, city, street, column, level, product)


# =========== RUA 9 ==================================================
state = 1
city = 1
street = 9
column = 62
level = 8
product = 1
columnSign.createAll(state, city, street, column, level, product)
columnSticker.createAll(state, city, street, column, level, product)


# =========== RUA 10 ==================================================
state = 1
city = 2
street = 10
column = 32
level = 6
product = 1
columnSign.createAll(state, city, street, column, level, product)
columnSticker.createAll(state, city, street, column, level, product)


# =========== RUA 11 ==================================================
state = 1
city = 2
street = 11
product = 1

startColumn = 1
endColumn = 11
level = 8
columnSign.createAllRange(state, city, street, startColumn, level, product, endColumn)
columnSticker.createAllRange(state, city, street, level, product, startColumn, endColumn)

startColumn = 12
endColumn = 14
level = 12
columnSign.createAllRange(state, city, street, startColumn, level, product, endColumn)
columnSticker.createAllRange(state, city, street, level, product, startColumn, endColumn)

startColumn = 15
endColumn = 24
level = 8
columnSign.createAllRange(state, city, street, startColumn, level, product, endColumn)
columnSticker.createAllRange(state, city, street, level, product, startColumn, endColumn)

startColumn = 25
endColumn = 31
level = 12
columnSign.createAllRange(state, city, street, startColumn, level, product, endColumn)
columnSticker.createAllRange(state, city, street, level, product, startColumn, endColumn)

startColumn = 32
endColumn = 40
level = 8
columnSign.createAllRange(state, city, street, startColumn, level, product, endColumn)
columnSticker.createAllRange(state, city, street, level, product, startColumn, endColumn)

# =========== LEVEL 8 ==================================================
nivelMax = 8
printRow = 5
printColumn = 15 
columnSign.mergeSigns(nivelMax, printRow, printColumn)


# =========== LEVEL 6 ==================================================
nivelMax = 6
printRow = 6
printColumn = 15 
columnSign.mergeSigns(nivelMax, printRow, printColumn)


# =========== LEVEL 12 ==================================================
nivelMax = 12
printRow = 3
printColumn = 15 
columnSign.mergeSigns(nivelMax, printRow, printColumn)

# =========== ALL COLUMN STICKERS ==================================================
printRow = 40
printColumn = 10
columnSticker.merge(printRow, printColumn)

# =========== ALL APT STICKERS ==================================================
printRow = 40
printColumn = 10
columnSticker.merge(printRow, printColumn)

# =========== ALL APT STICKERS ==================================================
printRow = 40
printColumn = 10
aptSticker.merge(printRow, printColumn)

'''



# =========================================================================================
# ============================== Sample Column = 20 =======================================
# =========================================================================================
state = 9
city = 1
street = 4
column = 20
level = 8
product = 1

aptLevelMax = 2
apt = 3
columnStart = 10
columnEnd = 60
evenOddAll = "even"

columnSign.createAll(state, city, street, column, level, product)
columnSticker.createAll(state, city, street, column, level, product)
aptSticker.createAll(state, city, street, column, aptLevelMax, product, apt, columnStart, columnEnd, evenOddAll)
deleteExtras.removeColumnSticker(state, city, street, column, aptLevelMax, product, apt, columnStart, columnEnd, evenOddAll)



# =========== RUA 1 ==================================================
state = 9
city = 1
street = 1
column = 20
level = 8
product = 1
columnSign.createAll(state, city, street, column, level, product)
columnSticker.createAll(state, city, street, column, level, product)


# =========== RUA 2 ==================================================
state = 9
city = 1
street = 2
column = 20
level = 8
product = 1
columnSign.createAll(state, city, street, column, level, product)
columnSticker.createAll(state, city, street, column, level, product)


# =========== RUA 3 ==================================================
state = 9
city = 1
street = 3
column = 20
level = 8
product = 1
columnSign.createAll(state, city, street, column, level, product)
columnSticker.createAll(state, city, street, column, level, product)


# =========== RUA 4 ==================================================
state = 9
city = 1
street = 4
column = 20
level = 8
product = 1

aptLevelMax = 2
apt = 3
columnStart = 10
columnEnd = 60
evenOddAll = "even"

columnSign.createAll(state, city, street, column, level, product)
columnSticker.createAll(state, city, street, column, level, product)
aptSticker.createAll(state, city, street, column, aptLevelMax, product, apt, columnStart, columnEnd, evenOddAll)
deleteExtras.removeColumnSticker(state, city, street, column, aptLevelMax, product, apt, columnStart, columnEnd, evenOddAll)


# =========== RUA 5 ==================================================
state = 9
city = 1
street = 5
column = 20
level = 8
product = 1

aptLevelMax = 2
apt = 3
columnStart = 9
columnEnd = 68
evenOddAll = "all"

columnSign.createAll(state, city, street, column, level, product)
columnSticker.createAll(state, city, street, column, level, product)
aptSticker.createAll(state, city, street, column, aptLevelMax, product, apt, columnStart, columnEnd, evenOddAll)
deleteExtras.removeColumnSticker(state, city, street, column, aptLevelMax, product, apt, columnStart, columnEnd, evenOddAll)


# =========== RUA 6 ==================================================
state = 9
city = 1
street = 6
column = 20
level = 8
product = 1

aptLevelMax = 2
apt = 3
columnStart = 9
columnEnd = 67
evenOddAll = "odd"

startDelete = 81
endDelete = column
sideRemove="odd"

columnSign.createAll(state, city, street, column, level, product)
columnSticker.createAll(state, city, street, column, level, product)
aptSticker.createAll(state, city, street, column, aptLevelMax, product, apt, columnStart, columnEnd, evenOddAll)
deleteExtras.removeColumn(state, city, street, column, level, product, startDelete, endDelete, sideRemove)
deleteExtras.removeColumnSticker(state, city, street, column, aptLevelMax, product, apt, columnStart, columnEnd, evenOddAll)

# =========== RUA 7 ==================================================
state = 9
city = 1
street = 7
column = 20
level = 8
product = 1
columnSign.createAll(state, city, street, column, level, product)
columnSticker.createAll(state, city, street, column, level, product)


# =========== RUA 8 ==================================================
state = 9
city = 1
street = 8
column = 20
level = 8
product = 1
columnSign.createAll(state, city, street, column, level, product)
columnSticker.createAll(state, city, street, column, level, product)


# =========== RUA 9 ==================================================
state = 9
city = 1
street = 9
column = 20
level = 8
product = 1
columnSign.createAll(state, city, street, column, level, product)
columnSticker.createAll(state, city, street, column, level, product)


# =========== RUA 10 ==================================================
state = 9
city = 2
street = 10
column = 20
level = 6
product = 1
columnSign.createAll(state, city, street, column, level, product)
columnSticker.createAll(state, city, street, column, level, product)


# =========== RUA 11 ==================================================
state = 9
city = 2
street = 11
product = 1

startColumn = 1
endColumn = 11
level = 8
columnSign.createAllRange(state, city, street, startColumn, level, product, endColumn)
columnSticker.createAllRange(state, city, street, level, product, startColumn, endColumn)

startColumn = 12
endColumn = 14
level = 12
columnSign.createAllRange(state, city, street, startColumn, level, product, endColumn)
columnSticker.createAllRange(state, city, street, level, product, startColumn, endColumn)

startColumn = 15
endColumn = 20
level = 8
columnSign.createAllRange(state, city, street, startColumn, level, product, endColumn)
columnSticker.createAllRange(state, city, street, level, product, startColumn, endColumn)

# =========== LEVEL 8 ==================================================
nivelMax = 8
printRow = 5
printColumn = 15 
columnSign.mergeSigns(nivelMax, printRow, printColumn)


# =========== LEVEL 6 ==================================================
nivelMax = 6
printRow = 6
printColumn = 15 
columnSign.mergeSigns(nivelMax, printRow, printColumn)


# =========== LEVEL 12 ==================================================
nivelMax = 12
printRow = 3
printColumn = 15 
columnSign.mergeSigns(nivelMax, printRow, printColumn)

# =========== ALL COLUMN STICKERS ==================================================
printRow = 40
printColumn = 10
columnSticker.merge(printRow, printColumn)

# =========== ALL APT STICKERS ==================================================
printRow = 40
printColumn = 10
columnSticker.merge(printRow, printColumn)

# =========== ALL APT STICKERS ==================================================
printRow = 40
printColumn = 10
aptSticker.merge(printRow, printColumn)


'''