import cv2

import barcodeGenerator
import customeFunctions
# =================================================
# Get Images
# =================================================

IMAGES_PATH = "C:/personal-git/aresta-barcode/src/app/images/"


def createAll(state, city, street, column, level, product, apt, column_start, column_end, even_odd_all):
    def get_digit(index):
        path ="{}apt_sticker_header_digits/resized/apt_sticker_digit_{}.png".format(IMAGES_PATH, index)
        digit = cv2.imread(path)
        return digit

    def get_arrow():
        path = "{}apt_sticker_arrow_up/apt_sticker_arrow_up_black.PNG".format(IMAGES_PATH)
        arrow = cv2.imread(path)
        return arrow

    def get_pad():
        path = "{}apt_sticker_barcode_header_pad/pad.PNG".format(IMAGES_PATH)
        pad = cv2.imread(path)
        return pad

    def get_header(index):
        path ="{}apt_sticker_header/apt_sticker_header_{}.PNG".format(IMAGES_PATH, index)
        header = cv2.imread(path)
        return header

    def get_line(option):
        if option == "side":
            path = "{}lines/stickerSide.png".format(IMAGES_PATH)
        if option == "top":
            path = "{}lines/stickerTop.png".format(IMAGES_PATH)
        line = cv2.imread(path)
        return line

    # =================================================
    # Combine Images
    # =================================================

    def create_single(state, city, street, column, level, product, apt):

        # Generate sectioin images
        arrow = get_arrow()
        pad = get_pad()
        header = get_header(level) #420 x 114
        # barcode = getBarcode(state, city, street, column, level, product)
        barcode = barcodeGenerator.getBarcode(state, city, street, column, level, product)

        # create the product number
        apt = customeFunctions.addZero_twoDigits(apt)
        digit1 = apt[0:1]
        digit2 = apt[1:2]
        first_digit = get_digit(digit1) # 82 x 114
        second_digit = get_digit(digit2)

        # Combine Images
        img1 = cv2.hconcat([header, first_digit, second_digit, pad])
        img2 = cv2.vconcat([img1, barcode])
        img3 = cv2.hconcat([img2, arrow])
        # Side Line
        img4 = cv2.hconcat([img3, get_line("side")])
        # Top Line
        img5 = cv2.vconcat([get_line("top"), img4])

        # Create File Name
        city = customeFunctions.addZero_twoDigits(city)
        street = customeFunctions.addZero_twoDigits(street)
        column = customeFunctions.addZero_threeDigits(column)
        level = customeFunctions.addZero_twoDigits(level)
        product = customeFunctions.addZero_twoDigits(product)
        file_name = "{}.{}.{}.{}.{}.{}-apt-{}.png".format(state, city, street, column, level, product, apt)

        save_path = "{}apt_sticker_done_single/{}".format(IMAGES_PATH, file_name)
        cv2.imwrite(save_path, img5)
        print(save_path)

    if even_odd_all == "all":
        print("Doing all")
        for each_column in range(column_start, column_end+1):
            print("column: ", each_column)
            for each_level in range(1, level+1):
                for each_apt in range(1, apt+1):
                    create_single(state, city, street, each_column, each_level, product, each_apt)
                    
    elif even_odd_all == "even":
        print("Doing even")
        for each_column in range(column_start, column_end+1):
            if each_column%2 == 0:
                print("column: ", each_column)
                for each_level in range(1, level+1):
                    for each_apt in range(1, apt+1):
                        create_single(state, city, street, each_column, each_level, product, each_apt)

    elif even_odd_all == "odd":
        print("Doing odd")
        for each_column in range(column_start, column_end+1):
            if each_column%2 != 0:
                print("column: ", each_column)
                for each_level in range(1, level+1):
                    for each_apt in range(1, apt+1):
                        create_single(state, city, street, each_column, each_level, product, each_apt)


