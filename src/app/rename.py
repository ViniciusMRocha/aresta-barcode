import os

folderPath = "C:/personal-git/aresta-barcode/src/graphics-design/sign/sign-barcode-header/sign-barcode-header/"
fileNameNoNumer = "Slide"
newFileNameNoNumer = "label-"
extension = ".PNG"
count = 0


for path in os.listdir(folderPath):
    if os.path.isfile(os.path.join(folderPath, path)):
        if path.endswith(extension):
            count += 1 
print ("Total item count",count)

for i in range(1,count+1):
    eachFile = folderPath+fileNameNoNumer+str(i)+extension
    
    newFileName = folderPath+newFileNameNoNumer+str(i)+extension
    os.rename(eachFile,newFileName)


