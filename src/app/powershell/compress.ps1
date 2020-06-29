# All Paths Variables
# $barcodeLibrary = "C:\personal-git\aresta-barcode\src\app\images\barcode_library"

# $aptStickerDoneSingle = "C:\personal-git\aresta-barcode\src\app\images\apt_sticker_done_single"
# $aptStickerDoneRowMerge = "C:\personal-git\aresta-barcode\src\app\images\apt_sticker_done_row_merge"
$aptStickerDoneFullPageMerge = "C:\personal-git\aresta-barcode\src\app\images\apt_sticker_done_full_page_merge"

# $columnDoneSingle = "C:\personal-git\aresta-barcode\src\app\images\column_done_single"
# $columnDoneRowMerge = "C:\personal-git\aresta-barcode\src\app\images\column_done_row_merge"
$columnDoneFullPageMerge = "C:\personal-git\aresta-barcode\src\app\images\column_done_full_page_merge"

# $signDoneSingle = "C:\personal-git\aresta-barcode\src\app\images\sign_done_single"
# $signDoneRowMerge = "C:\personal-git\aresta-barcode\src\app\images\sign_done_row_merge"
$signDoneFullPageMerge = "C:\personal-git\aresta-barcode\src\app\images\sign_done_full_page_merge"

# Temp Name
# $new_barcodeLibrary = "C:\personal-git\aresta-barcode\src\app\images\codigos-de-barra-individual"

# $new_aptStickerDoneSingle = "C:\personal-git\aresta-barcode\src\app\images\apt-individual"
# $new_aptStickerDoneRowMerge = "C:\personal-git\aresta-barcode\src\app\images\apt-linhas"
$new_aptStickerDoneFullPageMerge = "C:\personal-git\aresta-barcode\src\app\images\apt-pagina-completa"

# $new_columnDoneSingle = "C:\personal-git\aresta-barcode\src\app\images\estanteria-individual"
# $new_columnDoneRowMerge = "C:\personal-git\aresta-barcode\src\app\images\estanteria-linhas"
$new_columnDoneFullPageMerge = "C:\personal-git\aresta-barcode\src\app\images\column-pagina-completa"

# $new_signDoneSingle = "C:\personal-git\aresta-barcode\src\app\images\placas-individual"
# $new_signDoneRowMerge = "C:\personal-git\aresta-barcode\src\app\images\placas-linhas"
$new_signDoneFullPageMerge = "C:\personal-git\aresta-barcode\src\app\images\placas-pagina-completa"

#Save to Path
$saveTo = "C:\Users\vinir\OneDrive\Desktop\aresta-share\AllFiles-TLS.Zip"

#Rename files for distribution
# Barcode
# Rename-Item -Path $barcodeLibrary -NewName $new_barcodeLibrary
# Apt
# Rename-Item -Path $aptStickerDoneSingle -NewName $new_aptStickerDoneSingle
# Rename-Item -Path $aptStickerDoneRowMerge -NewName $new_aptStickerDoneRowMerge
Rename-Item -Path $aptStickerDoneFullPageMerge -NewName $new_aptStickerDoneFullPageMerge
# Column
# Rename-Item -Path $columnDoneSingle -NewName $new_columnDoneSingle
# Rename-Item -Path $columnDoneRowMerge -NewName $new_columnDoneRowMerge
Rename-Item -Path $columnDoneFullPageMerge -NewName $new_columnDoneFullPageMerge
# Sign
# Rename-Item -Path $signDoneSingle -NewName $new_signDoneSingle
# Rename-Item -Path $signDoneRowMerge -NewName $new_signDoneRowMerge
Rename-Item -Path $signDoneFullPageMerge -NewName $new_signDoneFullPageMerge

#Compress files
$compress = @{
    # Path             = $new_barcodeLibrary, $new_aptStickerDoneSingle, $new_aptStickerDoneRowMerge, $new_aptStickerDoneFullPageMerge, $new_columnDoneSingle, $new_columnDoneRowMerge, $new_columnDoneFullPageMerge, $new_signDoneSingle, $new_signDoneRowMerge, $new_signDoneFullPageMerge
    Path             = $new_aptStickerDoneFullPageMerge, $new_columnDoneFullPageMerge, $new_signDoneFullPageMerge
    CompressionLevel = "Fastest"
    DestinationPath  = $saveTo
}

Compress-Archive @compress

# Bring the name back to original

# Barcode
# Rename-Item -Path $new_barcodeLibrary -NewName $barcodeLibrary
# Apt
# Rename-Item -Path $new_aptStickerDoneSingle -NewName $aptStickerDoneSingle
# Rename-Item -Path $new_aptStickerDoneRowMerge -NewName $aptStickerDoneRowMerge
Rename-Item -Path $new_aptStickerDoneFullPageMerge -NewName $aptStickerDoneFullPageMerge
# Column
# Rename-Item -Path $new_columnDoneSingle -NewName $columnDoneSingle
# Rename-Item -Path $new_columnDoneRowMerge -NewName $columnDoneRowMerge
Rename-Item -Path $new_columnDoneFullPageMerge -NewName $columnDoneFullPageMerge
# Sign
# Rename-Item -Path $new_signDoneSingle -NewName $signDoneSingle
# Rename-Item -Path $new_signDoneRowMerge -NewName $signDoneRowMerge
Rename-Item -Path $new_signDoneFullPageMerge -NewName $signDoneFullPageMerge

Write-Output "Compress Done"
