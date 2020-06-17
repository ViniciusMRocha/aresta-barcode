import cv2
import numpy as np

from pathlib import Path
from PIL import Image

import os
from os.path import isfile, join

import barcode
from barcode.writer import ImageWriter

#My Files
import aptSticker
import columnSticker
import columnSign
import customeFunctions
import barcodeGenerator
import resize

def remove(state, city, street, column, level, product, startDelet, sideRemove):

    cityTwoDigits = customeFunctions.addZero_twoDigits(city)
    streetTwoDigits = customeFunctions.addZero_twoDigits(street)
    columnThreeDigits = customeFunctions.addZero_threeDigits(column)
    levelTwoDigits = customeFunctions.addZero_twoDigits(level)
    productTwoDigits = customeFunctions.addZero_twoDigits(product)

    # print("\nDeleting sign: ")
    # signPath = "C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.{}.{}.{}.PNG".format(cityTwoDigits,streetTwoDigits,columnThreeDigits)
    # print(signPath)
    # if os.path.exists(signPath):
    #     os.remove(signPath)
    #     print("Deleted: {}".format(signPath))
    # else:
    #     print("Do not exist: {}".format(signPath))


    if sideRemove == "even":
        print("\nDeleting barcode-library: ")
        for c in range(startDelet,column+1):
            if c%2 == 0:
                print("\nDeleting sign: ")
                columnThreeDigits = customeFunctions.addZero_threeDigits(c)
                signPath = "C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.{}.{}.{}.PNG".format(cityTwoDigits,streetTwoDigits,columnThreeDigits)
                print(signPath)
                if os.path.exists(signPath):
                    os.remove(signPath)
                    print("Deleted: {}".format(signPath))
                else:
                    print("Do not exist: {}".format(signPath))

                for i in range(1,level+1):
                    levelTwoDigits = customeFunctions.addZero_twoDigits(i)
                    columnThreeDigits = customeFunctions.addZero_threeDigits(c)
                    print("\nDeleting level: ")
                    barcodePath = "C:/personal-git/aresta-barcode/src/app/images/barcode-library/1.{}.{}.{}.{}.{}.PNG".format(cityTwoDigits,streetTwoDigits,columnThreeDigits,levelTwoDigits,productTwoDigits)
                    print(barcodePath)
                    if os.path.exists(barcodePath):
                        os.remove(barcodePath)
                        print("Deleted: {}".format(barcodePath))
                    else:
                        print("Do not exist: {}".format(barcodePath))
                
                print("\nDeleting column: ")
                for i in range(1,level+1):
                    levelTwoDigits = customeFunctions.addZero_twoDigits(i)
                    columnPath = "C:/personal-git/aresta-barcode/src/app/images/column-done-single/inv-1.{}.{}.{}.{}.{}.PNG".format(cityTwoDigits,streetTwoDigits,columnThreeDigits,levelTwoDigits,productTwoDigits)
                    print(columnPath)
                    if os.path.exists(columnPath):
                        os.remove(columnPath)
                        print("Deleted: {}".format(columnPath))
                    else:
                        print("Do not exist: {}".format(columnPath))

    elif sideRemove == "odd":
        print("\nDeleting barcode-library: ")
        for c in range(startDelet,column+1):
            if c%2 != 0:
                print("\nDeleting sign: ")
                columnThreeDigits = customeFunctions.addZero_threeDigits(c)
                signPath = "C:/personal-git/aresta-barcode/src/app/images/sign-done-single/1.{}.{}.{}.PNG".format(cityTwoDigits,streetTwoDigits,columnThreeDigits)
                print(signPath)
                if os.path.exists(signPath):
                    os.remove(signPath)
                    print("Deleted: {}".format(signPath))
                else:
                    print("Do not exist: {}".format(signPath))
                print("\nDeleting level: ")
                for i in range(1,level+1):
                    levelTwoDigits = customeFunctions.addZero_twoDigits(i)
                    columnThreeDigits = customeFunctions.addZero_threeDigits(c)
                    barcodePath = "C:/personal-git/aresta-barcode/src/app/images/barcode-library/1.{}.{}.{}.{}.{}.PNG".format(cityTwoDigits,streetTwoDigits,columnThreeDigits,levelTwoDigits,productTwoDigits)
                    print(barcodePath)
                    if os.path.exists(barcodePath):
                        os.remove(barcodePath)
                        print("Deleted: {}".format(barcodePath))
                    else:
                        print("Do not exist: {}".format(barcodePath))
                
                print("\nDeleting column: ")
                for i in range(1,level+1):
                    levelTwoDigits = customeFunctions.addZero_twoDigits(i)
                    columnPath = "C:/personal-git/aresta-barcode/src/app/images/column-done-single/inv-1.{}.{}.{}.{}.{}.PNG".format(cityTwoDigits,streetTwoDigits,columnThreeDigits,levelTwoDigits,productTwoDigits)
                    print(columnPath)
                    if os.path.exists(columnPath):
                        os.remove(columnPath)
                        print("Deleted: {}".format(columnPath))
                    else:
                        print("Do not exist: {}".format(columnPath))
