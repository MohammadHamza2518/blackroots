Add-Type -AssemblyName System.Drawing

$gridImgPath = "reviews pics/profile/ChatGPT Image Aug 11, 2026, 12_40_49 PM.png"
$img = [System.Drawing.Bitmap]::FromFile((Resolve-Path $gridImgPath))
Write-Host "Width:" $img.Width "Height:" $img.Height

# We have 5 columns and 4 rows of circles
# Let's crop tight inside each cell (e.g. padding 10-12% from each side to remove white background!)
$w = $img.Width
$h = $img.Height
$cols = 5
$rows = 4

$cellW = $w / $cols
$cellH = $h / $rows

# Add inset padding inside cell to crop ONLY the circle face!
$padX = [int]($cellW * 0.12)
$padY = [int]($cellH * 0.12)
$cropW = [int]($cellW - (2 * $padX))
$cropH = [int]($cellH - (2 * $padY))

Write-Host "Cell Size:" $cellW "x" $cellH
Write-Host "Tight Crop Size:" $cropW "x" $cropH

$avatarDir = "assets/reviews"
$demoAvatarDir = "demo_lab/assets/reviews"
$previewAvatarDir = "preview/assets/reviews"

$count = 1
for ($r = 0; $r -lt $rows; $r++) {
    for ($c = 0; $c -lt $cols; $c++) {
        $startX = [int](($c * $cellW) + $padX)
        $startY = [int](($r * $cellH) + $padY)
        
        $crop = New-Object System.Drawing.Bitmap $cropW, $cropH
        $g = [System.Drawing.Graphics]::FromImage($crop)
        $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
        $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
        $g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
        
        $srcRect = New-Object System.Drawing.Rectangle $startX, $startY, $cropW, $cropH
        $destRect = New-Object System.Drawing.Rectangle 0, 0, $cropW, $cropH
        $g.DrawImage($img, $destRect, $srcRect, [System.Drawing.GraphicsUnit]::Pixel)
        
        $out1 = Join-Path $avatarDir "avatar-$count.jpg"
        $out2 = Join-Path $demoAvatarDir "avatar-$count.jpg"
        $out3 = Join-Path $previewAvatarDir "avatar-$count.jpg"
        
        $crop.Save($out1, [System.Drawing.Imaging.ImageFormat]::Jpeg)
        $crop.Save($out2, [System.Drawing.Imaging.ImageFormat]::Jpeg)
        $crop.Save($out3, [System.Drawing.Imaging.ImageFormat]::Jpeg)
        
        $g.Dispose()
        $crop.Dispose()
        $count++
    }
}

$img.Dispose()
Write-Host "TIGHT CROPPED 20 AVATARS PERFECTLY WITHOUT WHITE MARGINS!"
