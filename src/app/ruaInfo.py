# My Files
import columnSign
import columnSticker
import aptSticker
import deleteExtras
import countFiles
import merge

def rua1():
    # =========== RUA 1 =====================================================
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


def rua2():
    # =========== RUA 2 =====================================================
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


def rua3():
    # =========== RUA 3 =====================================================
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



def rua4():
    # =========== RUA 4 =====================================================
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

def rua5():
    # =========== RUA 5 =====================================================
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



def rua6():
    # =========== RUA 6 =====================================================
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

def rua7():
    # =========== RUA 7 =====================================================
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

def rua8():
    # =========== RUA 8 =====================================================
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

def rua9():
    # =========== RUA 9 =====================================================
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



def rua10():
    # =========== RUA 10 =====================================================
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

def rua11():
    # =========== RUA 11 =====================================================
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

def allApt():
    # =========== ALL APT STICKERS =====================================================
    printRow = 40
    printColumn = 10
    # merge.mergeColumn(printRow, printColumn)