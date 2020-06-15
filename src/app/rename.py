import os

folderPath = "C:/personal-git/aresta-barcode/src/graphics-design/sticker/sticker-pallet-header/sticker-pallet-header/"
fileNameNoNumer = "Slide"
newFileNameNoNumer = "pallet-"
extension = ".PNG"
count = 0
directory = "C:/personal-git/aresta-barcode/src/graphics-design/sticker/sticker-pallet-header/sticker-pallet-header/"

for path in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, path)):
        if path.endswith(extension):
            count += 1 
print ("Total item count",count)

for i in range(1,count+1):
    eachFile = folderPath+fileNameNoNumer+str(i)+extension
    
    newFileName = folderPath+newFileNameNoNumer+str(i)+extension
    os.rename(eachFile,newFileName)


