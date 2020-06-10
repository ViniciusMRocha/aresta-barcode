import os

folderPath = "C:/personal-git/aresta-barcode/src/app/images/sticker-arrow-up/"
fileNameNoNumer = "sticker-arrow-up-a"
newFileNameNoNumer = "sticker-arrow-up-"
extension = ".PNG"
count = 0
directory = "C:/personal-git/aresta-barcode/src/app/images/sticker-arrow-up/"

for path in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, path)):
        if path.endswith(extension):
            count += 1 
print ("Total item count",count)

for i in range(0,count+1):
    eachFile = folderPath+fileNameNoNumer+str(i)+extension
    
    newFileName = folderPath+newFileNameNoNumer+str(i)+extension
    os.rename(eachFile,newFileName)


