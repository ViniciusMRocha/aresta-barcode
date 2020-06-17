$compress = @{
    Path             = "C:\personal-git\aresta-barcode\src\app\images\barcode-library",
    "C:\personal-git\aresta-barcode\src\app\images\apt-sticker-done-merge",
    "C:\personal-git\aresta-barcode\src\app\images\apt-sticker-done-single",
    "C:\personal-git\aresta-barcode\src\app\images\column-done-merge",
    "C:\personal-git\aresta-barcode\src\app\images\column-done-single",
    "C:\personal-git\aresta-barcode\src\app\images\sign-done-merge",
    "C:\personal-git\aresta-barcode\src\app\images\sign-done-single"
    CompressionLevel = "Fastest"
    DestinationPath  = "C:\Users\vinir\OneDrive\Desktop\aresta-share\AllFiles-Fast.Zip"
}
Compress-Archive @compress

echo "Compress Done"