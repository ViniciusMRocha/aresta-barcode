import cv2
import numpy as np

from pathlib import Path
from PIL import Image

import os
from os.path import isfile, join

import glob

import barcode
from barcode.writer import ImageWriter

#My Files
import aptSticker
import columnSticker
import columnSign
import customeFunctions
import barcodeGenerator
import resize


#C:/personal-git/aresta-barcode/src/app/images/column_done_single/inv-1.01.04.010.01.01.PNG
#C:/personal-git/aresta-barcode/src/app/images/column_done_single/inv-1.01.04.010.02.01.PNG

def removeColumnSticker(state, city, street, column, aptLevelMax, product, apt, startDelete, endDelete, sideRemove):
    print("Remove Column Sticker")

    cityTwoDigits = customeFunctions.addZero_twoDigits(city)
    streetTwoDigits = customeFunctions.addZero_twoDigits(street)
    productTwoDigits = customeFunctions.addZero_twoDigits(product)

    deleteList = []
    path = "C:/personal-git/aresta-barcode/src/app/images/column_done_single/inv-{}.PNG"

    if sideRemove == "even":
        for c in range(startDelete,endDelete+1):
            if c%2 == 0:
                print("\n ---------- Deleting column: {}".format(c))
                columnThreeDigits = customeFunctions.addZero_threeDigits(c)
                for i in range(1,aptLevelMax+1):
                    levelTwoDigits = customeFunctions.addZero_twoDigits(i)
                    search = '{}.{}.{}.{}.{}.{}'.format(state, cityTwoDigits, streetTwoDigits, columnThreeDigits, levelTwoDigits, productTwoDigits)

                    deletePath = path.format(search)
                    deleteList.append(deletePath)

                    if os.path.exists(deletePath):
                        os.remove(deletePath)
                        print("Deleted: {}".format(deletePath))
                    else:
                        print("Do not exist: {}".format(deletePath))

        # List of deletes
        # for i in range(len(deleteList)):
        #     print(deleteList[i])
                
    elif sideRemove == "odd":
        for c in range(startDelete,endDelete+1):
            if c%2 != 0:
                print("\n ---------- Deleting column: {}".format(c))
                columnThreeDigits = customeFunctions.addZero_threeDigits(c)
                for i in range(1,aptLevelMax+1):
                    levelTwoDigits = customeFunctions.addZero_twoDigits(i)
                    search = '{}.{}.{}.{}.{}.{}'.format(state, cityTwoDigits, streetTwoDigits, columnThreeDigits, levelTwoDigits, productTwoDigits)

                    deletePath = path.format(search)
                    deleteList.append(deletePath)

                    if os.path.exists(deletePath):
                        os.remove(deletePath)
                        print("Deleted: {}".format(deletePath))
                    else:
                        print("Do not exist: {}".format(deletePath))
                

    elif sideRemove == "all":
        for c in range(startDelete,endDelete+1):
            print("\n ---------- Deleting column: {}".format(c))
            columnThreeDigits = customeFunctions.addZero_threeDigits(c)
            for i in range(1,aptLevelMax+1):
                levelTwoDigits = customeFunctions.addZero_twoDigits(i)
                search = '{}.{}.{}.{}.{}.{}'.format(state, cityTwoDigits, streetTwoDigits, columnThreeDigits, levelTwoDigits, productTwoDigits)

                deletePath = path.format(search)
                deleteList.append(deletePath)

                if os.path.exists(deletePath):
                    os.remove(deletePath)
                    print("Deleted: {}".format(deletePath))
                else:
                    print("Do not exist: {}".format(deletePath))



def removeColumn(state, city, street, column, level, product, startDelete, endDelete, sideRemove):

    cityTwoDigits = customeFunctions.addZero_twoDigits(city)
    streetTwoDigits = customeFunctions.addZero_twoDigits(street)
    columnThreeDigits = customeFunctions.addZero_threeDigits(column)
    levelTwoDigits = customeFunctions.addZero_twoDigits(level)
    productTwoDigits = customeFunctions.addZero_twoDigits(product)

    if sideRemove == "even":
        for c in range(startDelete,endDelete+1):
            if c%2 == 0:
                print("\n ---------- Deleting column: {}".format(c))
                columnThreeDigits = customeFunctions.addZero_threeDigits(c)
                signPath = "C:/personal-git/aresta-barcode/src/app/images/sign_done_single/1.{}.{}.{}.PNG".format(cityTwoDigits,streetTwoDigits,columnThreeDigits)
                if os.path.exists(signPath):
                    os.remove(signPath)
                    print("Deleted: {}".format(signPath))
                else:
                    print("Do not exist: {}".format(signPath))

                for i in range(1,level+1):
                    levelTwoDigits = customeFunctions.addZero_twoDigits(i)
                    columnThreeDigits = customeFunctions.addZero_threeDigits(c)
                    barcodePath = "C:/personal-git/aresta-barcode/src/app/images/barcode_library/1.{}.{}.{}.{}.{}.PNG".format(cityTwoDigits,streetTwoDigits,columnThreeDigits,levelTwoDigits,productTwoDigits)
                    if os.path.exists(barcodePath):
                        os.remove(barcodePath)
                        print("Deleted: {}".format(barcodePath))
                    else:
                        print("Do not exist: {}".format(barcodePath))
                
                for i in range(1,level+1):
                    levelTwoDigits = customeFunctions.addZero_twoDigits(i)
                    columnPath = "C:/personal-git/aresta-barcode/src/app/images/column_done_single/inv-1.{}.{}.{}.{}.{}.PNG".format(cityTwoDigits,streetTwoDigits,columnThreeDigits,levelTwoDigits,productTwoDigits)
                    if os.path.exists(columnPath):
                        os.remove(columnPath)
                        print("Deleted: {}".format(columnPath))
                    else:
                        print("Do not exist: {}".format(columnPath))

    elif sideRemove == "odd":
        for c in range(startDelete,endDelete+1):
            if c%2 != 0:
                print("\n ---------- Deleting column: {}".format(c))
                columnThreeDigits = customeFunctions.addZero_threeDigits(c)
                signPath = "C:/personal-git/aresta-barcode/src/app/images/sign_done_single/1.{}.{}.{}.PNG".format(cityTwoDigits,streetTwoDigits,columnThreeDigits)
                print(signPath)
                if os.path.exists(signPath):
                    os.remove(signPath)
                    print("Deleted: {}".format(signPath))
                else:
                    print("Do not exist: {}".format(signPath))

                for i in range(1,level+1):
                    levelTwoDigits = customeFunctions.addZero_twoDigits(i)
                    columnThreeDigits = customeFunctions.addZero_threeDigits(c)
                    barcodePath = "C:/personal-git/aresta-barcode/src/app/images/barcode_library/1.{}.{}.{}.{}.{}.PNG".format(cityTwoDigits,streetTwoDigits,columnThreeDigits,levelTwoDigits,productTwoDigits)
                    print(barcodePath)
                    if os.path.exists(barcodePath):
                        os.remove(barcodePath)
                        print("Deleted: {}".format(barcodePath))
                    else:
                        print("Do not exist: {}".format(barcodePath))
                
                for i in range(1,level+1):
                    levelTwoDigits = customeFunctions.addZero_twoDigits(i)
                    columnPath = "C:/personal-git/aresta-barcode/src/app/images/column_done_single/inv-1.{}.{}.{}.{}.{}.PNG".format(cityTwoDigits,streetTwoDigits,columnThreeDigits,levelTwoDigits,productTwoDigits)
                    if os.path.exists(columnPath):
                        os.remove(columnPath)
                        print("Deleted: {}".format(columnPath))
                    else:
                        print("Do not exist: {}".format(columnPath))

    elif sideRemove == "all":
        for c in range(startDelete,endDelete+1):
            print("\n ---------- Deleting column: {}".format(c))
            columnThreeDigits = customeFunctions.addZero_threeDigits(c)
            signPath = "C:/personal-git/aresta-barcode/src/app/images/sign_done_single/1.{}.{}.{}.PNG".format(cityTwoDigits,streetTwoDigits,columnThreeDigits)
            if os.path.exists(signPath):
                os.remove(signPath)
                print("Deleted: {}".format(signPath))
            else:
                print("Do not exist: {}".format(signPath))
                
            for i in range(1,level+1):
                levelTwoDigits = customeFunctions.addZero_twoDigits(i)
                columnThreeDigits = customeFunctions.addZero_threeDigits(c)
                barcodePath = "C:/personal-git/aresta-barcode/src/app/images/barcode_library/1.{}.{}.{}.{}.{}.PNG".format(cityTwoDigits,streetTwoDigits,columnThreeDigits,levelTwoDigits,productTwoDigits)
                if os.path.exists(barcodePath):
                    os.remove(barcodePath)
                    print("Deleted: {}".format(barcodePath))
                else:
                    print("Do not exist: {}".format(barcodePath))
            
            for i in range(1,level+1):
                levelTwoDigits = customeFunctions.addZero_twoDigits(i)
                columnPath = "C:/personal-git/aresta-barcode/src/app/images/column_done_single/inv-1.{}.{}.{}.{}.{}.PNG".format(cityTwoDigits,streetTwoDigits,columnThreeDigits,levelTwoDigits,productTwoDigits)
                if os.path.exists(columnPath):
                    os.remove(columnPath)
                    print("Deleted: {}".format(columnPath))
                else:
                    print("Do not exist: {}".format(columnPath))