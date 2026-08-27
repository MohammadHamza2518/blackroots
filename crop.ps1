
Add-Type -AssemblyName System.Drawing

$srcPath = "C:\Users\moham\.gemini\antigravity\brain\8a3ba400-40f9-42a7-8517-940c250103f9\.user_uploaded\media_1786354548264.jpg"
$assetsDir = "c:\Users\moham\Downloads\blackroots website\assets"
$previewDir = "c:\Users\moham\Downloads\blackroots website\preview\assets"

$img = [System.Drawing.Bitmap]::FromFile($srcPath)
$w = $img.Width
$h = $img.Height

# 1. Front View (Left third)
$rectFront = [System.Drawing.Rectangle]::FromLTRB(0, 0, [int]($w * 0.36), $h)
$cropFront = $img.Clone($rectFront, $img.PixelFormat)
$cropFront.Save("$assetsDir\blackroots-bottle-front-hd.png", [System.Drawing.Imaging.ImageFormat]::Png)
$cropFront.Save("$assetsDir\blackroots-bottle-front-label.png", [System.Drawing.Imaging.ImageFormat]::Png)
$cropFront.Dispose()

# 2. Side View (Center third)
$rectSide = [System.Drawing.Rectangle]::FromLTRB([int]($w * 0.32), 0, [int]($w * 0.68), $h)
$cropSide = $img.Clone($rectSide, $img.PixelFormat)
$cropSide.Save("$assetsDir\blackroots-bottle-side-hd.png", [System.Drawing.Imaging.ImageFormat]::Png)
$cropSide.Dispose()

# 3. Back View (Right third)
$rectBack = [System.Drawing.Rectangle]::FromLTRB([int]($w * 0.64), 0, $w, $h)
$cropBack = $img.Clone($rectBack, $img.PixelFormat)
$cropBack.Save("$assetsDir\blackroots-bottle-back-hd.png", [System.Drawing.Imaging.ImageFormat]::Png)
$cropBack.Dispose()

$img.Dispose()

Copy-Item $srcPath "$assetsDir\blackroots-bottles-trio-hd.jpg" -Force
Copy-Item $srcPath "$assetsDir\blackroots-bottles-trio.jpg" -Force

Write-Host "PowerShell cropping completed successfully!"
