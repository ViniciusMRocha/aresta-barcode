# All Paths Variables
$aptStickerDoneMerge = "C:\personal-git\aresta-barcode\src\app\images\apt-sticker-done-merge"
$aptStickerDoneSingle = "C:\personal-git\aresta-barcode\src\app\images\apt-sticker-done-single"

$columnDoneMerge = "C:\personal-git\aresta-barcode\src\app\images\column-done-merge"
$columnDoneSingle = "C:\personal-git\aresta-barcode\src\app\images\column-done-single"

$signDoneMerge = "C:\personal-git\aresta-barcode\src\app\images\sign-done-merge"
$signDoneSingle = "C:\personal-git\aresta-barcode\src\app\images\sign-done-single"
$signDoneRowMerge = "C:\personal-git\aresta-barcode\src\app\images\sign-done-row-merge"
$signDoneFullPageMerge = "C:\personal-git\aresta-barcode\src\app\images\sign-done-full-page-merge"

# Temp Name
$new_aptStickerDoneMerge = "C:\personal-git\aresta-barcode\src\app\images\apt-grupo"
$new_aptStickerDoneSingle = "C:\personal-git\aresta-barcode\src\app\images\apt-individual"

$new_columnDoneMerge = "C:\personal-git\aresta-barcode\src\app\images\estanteria-grupo"
$new_columnDoneSingle = "C:\personal-git\aresta-barcode\src\app\images\estanteria-individual"

$new_signDoneMerge = "C:\personal-git\aresta-barcode\src\app\images\placas-grupo"
$new_signDoneSingle = "C:\personal-git\aresta-barcode\src\app\images\placas-individual"
$new_signDoneRowMerge = "C:\personal-git\aresta-barcode\src\app\images\placas-juntas-por-linha"
$new_signDoneFullPageMerge = "C:\personal-git\aresta-barcode\src\app\images\placas-para-imprimir"

#Save to Path
$saveTo = "C:\Users\vinir\OneDrive\Desktop\aresta-share\AllFiles-TLS.Zip"

#Rename files for distribution
Rename-Item -Path $aptStickerDoneMerge -NewName $new_aptStickerDoneMerge
Rename-Item -Path $aptStickerDoneSingle -NewName $new_aptStickerDoneSingle

Rename-Item -Path $columnDoneMerge -NewName $new_columnDoneMerge
Rename-Item -Path $columnDoneSingle -NewName $new_columnDoneSingle

Rename-Item -Path $signDoneMerge -NewName $new_signDoneMerge
Rename-Item -Path $signDoneSingle -NewName $new_signDoneSingle
Rename-Item -Path $signDoneMerge -NewName $new_signDoneRowMerge
Rename-Item -Path $signDoneSingle -NewName $new_signDoneFullPageMerge

#Compress files
$compress = @{
    Path             = $new_aptStickerDoneMerge, $new_aptStickerDoneSingle, $new_columnDoneMerge, $new_columnDoneSingle, $new_signDoneMerge, $new_signDoneSingle, $new_signDoneRowMerge, $new_signDoneFullPageMerge
    CompressionLevel = "Fastest"
    DestinationPath  = $saveTo
}

Compress-Archive @compress


# Bring the name back to original
Rename-Item -Path $new_aptStickerDoneMerge -NewName $aptStickerDoneMerge
Rename-Item -Path $new_aptStickerDoneSingle -NewName $aptStickerDoneSingle
Rename-Item -Path $new_columnDoneMerge -NewName $columnDoneMerge
Rename-Item -Path $new_columnDoneSingle -NewName $columnDoneSingle
Rename-Item -Path $new_signDoneMerge -NewName $signDoneMerge
Rename-Item -Path $new_signDoneSingle -NewName $signDoneSingle
Rename-Item -Path $new_signDoneRowMerge -NewName $signDoneMerge
Rename-Item -Path $new_signDoneFullPageMerge -NewName $signDoneSingle

Write-Output "Compress Done"