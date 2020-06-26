import cv2
import numpy as np

from pathlib import Path
from PIL import Image

import barcode
from barcode.writer import ImageWriter

import time
#https://stackoverflow.com/questions/3620943/measuring-elapsed-time-with-the-time-module/46544199

# My Files
import columnSign
import columnSticker
import aptSticker
import deleteExtras
import countFiles
import merge

# Start function timer
startTime = time.time()

try:


    # =========== RUA 4 ====================================================================================================
    state = 1
    city = 1
    street = 4
    column = 80
    level = 8
    product = 1
    # columnSign.createAll(state, city, street, column, level, product)
    # columnSticker.createAll(state, city, street, column, level, product)

    aptLevelMax = 2
    apt = 3
    columnStart = 10
    columnEnd = 60
    evenOddAll = "even"
    # aptSticker.createAll(state, city, street, column, aptLevelMax, product, apt, columnStart, columnEnd, evenOddAll)
    # deleteExtras.removeColumnSticker(state, city, street, column, aptLevelMax, product, apt, columnStart, columnEnd, evenOddAll)

    # === Merge Signs ===============
    printRow = 5
    printColumn = 15 
    # merge.mergeSign(state, city, street, level, printRow, printColumn)

    # === Merge Column Sticker ===============
    printRow = 40
    printColumn = 10
    # merge.mergeColumn(state, city, street, printRow, printColumn)

    # === Merge Apt Sticker ===============
    printAptRow = 40
    printAptColumn = 10
    merge.mergeApt(state, city, street, printAptRow, printAptColumn)

    street = 5
    merge.mergeApt(state, city, street, printAptRow, printAptColumn)

    street = 6
    merge.mergeApt(state, city, street, printAptRow, printAptColumn)

    

    '''

    # =========== RUA 1 ====================================================================================================
    state = 1
    city = 1
    street = 1
    column = 56
    level = 8
    product = 1
    columnSign.createAll(state, city, street, column, level, product)
    columnSticker.createAll(state, city, street, column, level, product)

    # === Merge Signs ===============
    printRow = 5
    printColumn = 15 
    merge.mergeSign(state, city, street, level, printRow, printColumn)

    # === Merge Column Sticker ===============
    printRow = 40
    printColumn = 10
    merge.mergeColumn(state, city, street, printRow, printColumn)

    
    # =========== RUA 2 ====================================================================================================
    state = 1
    city = 1
    street = 2
    column = 56
    level = 8
    product = 1
    columnSign.createAll(state, city, street, column, level, product)
    columnSticker.createAll(state, city, street, column, level, product)

    # === Merge Signs ===============
    printRow = 5
    printColumn = 15 
    merge.mergeSign(state, city, street, level, printRow, printColumn)

    # === Merge Column Sticker ===============
    printRow = 40
    printColumn = 10
    merge.mergeColumn(state, city, street, printRow, printColumn)

    
    # =========== RUA 3 ====================================================================================================
    state = 1
    city = 1
    street = 3
    column = 56
    level = 8
    product = 1
    columnSign.createAll(state, city, street, column, level, product)
    columnSticker.createAll(state, city, street, column, level, product)

    # === Merge Signs ===============
    printRow = 5
    printColumn = 15 
    merge.mergeSign(state, city, street, level, printRow, printColumn)

    # === Merge Column Sticker ===============
    printRow = 40
    printColumn = 10
    merge.mergeColumn(state, city, street, printRow, printColumn)


    
    # =========== RUA 4 ====================================================================================================
    state = 1
    city = 1
    street = 4
    column = 80
    level = 8
    product = 1
    columnSign.createAll(state, city, street, column, level, product)
    columnSticker.createAll(state, city, street, column, level, product)

    aptLevelMax = 2
    apt = 3
    columnStart = 10
    columnEnd = 60
    evenOddAll = "even"
    aptSticker.createAll(state, city, street, column, aptLevelMax, product, apt, columnStart, columnEnd, evenOddAll)
    deleteExtras.removeColumnSticker(state, city, street, column, aptLevelMax, product, apt, columnStart, columnEnd, evenOddAll)

    # === Merge Signs ===============
    printRow = 5
    printColumn = 15 
    merge.mergeSign(state, city, street, level, printRow, printColumn)

    # === Merge Column Sticker ===============
    printRow = 40
    printColumn = 10
    merge.mergeColumn(state, city, street, printRow, printColumn)

    # === Merge Apt Sticker ===============
    printAptRow = 40
    printAptColumn = 10
    merge.mergeApt(state, city, street, printAptRow, printAptColumn)
    
    # =========== RUA 5 ====================================================================================================
    state = 1
    city = 1
    street = 5
    column = 80
    level = 8
    product = 1
    columnSign.createAll(state, city, street, column, level, product)
    columnSticker.createAll(state, city, street, column, level, product)

    aptLevelMax = 2
    apt = 3
    columnStart = 9
    columnEnd = 68
    evenOddAll = "all"
    aptSticker.createAll(state, city, street, column, aptLevelMax, product, apt, columnStart, columnEnd, evenOddAll)
    deleteExtras.removeColumnSticker(state, city, street, column, aptLevelMax, product, apt, columnStart, columnEnd, evenOddAll)

    # === Merge Signs ===============
    printRow = 5
    printColumn = 15 
    merge.mergeSign(state, city, street, level, printRow, printColumn)

    # === Merge Column Sticker ===============
    printRow = 40
    printColumn = 10
    merge.mergeColumn(state, city, street, printRow, printColumn)
    
    # === Merge Apt Sticker ===============
    printAptRow = 40
    printAptColumn = 10
    merge.mergeApt(state, city, street, printAptRow, printAptColumn)



    # =========== RUA 6 ====================================================================================================
    state = 1
    city = 1
    street = 6
    column = 96
    level = 8
    product = 1
    columnSign.createAll(state, city, street, column, level, product)
    columnSticker.createAll(state, city, street, column, level, product)

    aptLevelMax = 2
    apt = 3
    columnStart = 9
    columnEnd = 67
    evenOddAll = "odd"
    startDelete = 81
    endDelete = column
    sideRemove="odd"
    aptSticker.createAll(state, city, street, column, aptLevelMax, product, apt, columnStart, columnEnd, evenOddAll)
    deleteExtras.removeColumn(state, city, street, column, level, product, startDelete, endDelete, sideRemove)
    deleteExtras.removeColumnSticker(state, city, street, column, aptLevelMax, product, apt, columnStart, columnEnd, evenOddAll)

    # === Merge Signs ===============
    printRow = 5
    printColumn = 15 
    merge.mergeSign(state, city, street, level, printRow, printColumn)

    # === Merge Column Sticker ===============
    printRow = 40
    printColumn = 10
    merge.mergeColumn(state, city, street, printRow, printColumn)

    # === Merge Apt Sticker ===============
    printAptRow = 40
    printAptColumn = 10
    merge.mergeApt(state, city, street, printAptRow, printAptColumn)
    
    # =========== RUA 7 ====================================================================================================
    state = 1
    city = 1
    street = 7
    column = 96
    level = 8
    product = 1
    columnSign.createAll(state, city, street, column, level, product)
    columnSticker.createAll(state, city, street, column, level, product)

    # === Merge Signs ===============
    printRow = 5
    printColumn = 15 
    merge.mergeSign(state, city, street, level, printRow, printColumn)

    # === Merge Column Sticker ===============
    printRow = 40
    printColumn = 10
    merge.mergeColumn(state, city, street, printRow, printColumn)
    
    # =========== RUA 8 ====================================================================================================
    state = 1
    city = 1
    street = 8
    column = 96
    level = 8
    product = 1
    columnSign.createAll(state, city, street, column, level, product)
    columnSticker.createAll(state, city, street, column, level, product)

    # === Merge Signs ===============
    printRow = 5
    printColumn = 15 
    merge.mergeSign(state, city, street, level, printRow, printColumn)

    # === Merge Column Sticker ===============
    printRow = 40
    printColumn = 10
    merge.mergeColumn(state, city, street, printRow, printColumn)
    
    # =========== RUA 9 ====================================================================================================
    state = 1
    city = 1
    street = 9
    column = 62
    level = 8
    product = 1
    columnSign.createAll(state, city, street, column, level, product)
    columnSticker.createAll(state, city, street, column, level, product)

    # === Merge Signs ===============
    printRow = 5
    printColumn = 15 
    merge.mergeSign(state, city, street, level, printRow, printColumn)

    # === Merge Column Sticker ===============
    printRow = 40
    printColumn = 10
    merge.mergeColumn(state, city, street, printRow, printColumn)

    
    
    # =========== RUA 10 ====================================================================================================
    state = 1
    city = 2
    street = 10
    column = 32
    level = 6
    product = 1
    columnSign.createAll(state, city, street, column, level, product)
    columnSticker.createAll(state, city, street, column, level, product)

    # === Merge Signs ===============
    printRow = 6
    printColumn = 15 
    merge.mergeSign(state, city, street, level, printRow, printColumn)
    
    # === Merge Column Sticker ===============
    printRow = 40
    printColumn = 10
    merge.mergeColumn(state, city, street, printRow, printColumn)

    # =========== RUA 11 ====================================================================================================
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

    # === Merge Signs ===============
    level = 8
    printRow = 5
    printColumn = 15 
    merge.mergeSign(state, city, street, level, printRow, printColumn)
    
    level = 12
    printRow = 4
    printColumn = 15 
    merge.mergeSign(state, city, street, level, printRow, printColumn)

    # === Merge Column Sticker ===============
    printRow = 40
    printColumn = 10
    merge.mergeColumn(state, city, street, printRow, printColumn)


    # =========== ALL APT STICKERS ====================================================================================================
    printRow = 40
    printColumn = 10
    merge.mergeColumn(printRow, printColumn)

    '''
    
except:
    print("\n!!!!!!! Error Found !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    raise Exception


# =========== COUNT ALL FILES ====================================================================================================
print("\n======= Total Images Report ==================================")
countFiles.getTotalImageCount()

print("\n======= Elapsed Time ==================================")
endTime = time.time() - startTime
time.strftime("%H:%M:%S", time.gmtime(endTime))
print(time.strftime("%H:%M:%S", time.gmtime(endTime)))

