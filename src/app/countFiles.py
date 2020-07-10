import glob

def getTotalImageCount():
    paths = []

    imagesPath = "C:/personal-git/aresta-barcode/src/app/images/"

    paths.append("{}barcode_library/".format(imagesPath))
    paths.append("{}apt_sticker_done_single/".format(imagesPath))
    paths.append("{}apt_sticker_done_row_merge/".format(imagesPath))
    paths.append("{}apt_sticker_done_full_page_merge/".format(imagesPath))
    paths.append("{}column_done_single/".format(imagesPath))
    paths.append("{}column_done_row_merge/".format(imagesPath))
    paths.append("{}column_done_full_page_merge/".format(imagesPath))
    paths.append("{}sign_done_single/".format(imagesPath))
    paths.append("{}sign_done_row_merge/".format(imagesPath))
    paths.append("{}sign_done_full_page_merge/".format(imagesPath))

    for i in range(len(paths)):
        files=glob.glob("{}*".format(paths[i]))
        total = len(files)
        path = paths[i]
        print("Total: {} ==> {}".format(total,path))

