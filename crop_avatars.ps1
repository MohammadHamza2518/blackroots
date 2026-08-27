Add-Type -AssemblyName System.Drawing

$avatarDir = "assets/reviews"
$demoAvatarDir = "demo_lab/assets/reviews"
$previewAvatarDir = "preview/assets/reviews"

New-Item -ItemType Directory -Force -Path $avatarDir, $demoAvatarDir, $previewAvatarDir | Out-Null

$gridImgPath = "reviews pics/profile/ChatGPT Image Aug 11, 2026, 12_40_49 PM.png"

if (Test-Path $gridImgPath) {
    $grid = [System.Drawing.Bitmap]::FromFile((Resolve-Path $gridImgPath))
    $w = $grid.Width
    $h = $grid.Height
    $cols = 5
    $rows = 4
    $cellW = [int]($w / $cols)
    $cellH = [int]($h / $rows)
    
    $count = 1
    for ($r = 0; $r -lt $rows; $r++) {
        for ($c = 0; $c -lt $cols; $c++) {
            $crop = New-Object System.Drawing.Bitmap $cellW, $cellH
            $g = [System.Drawing.Graphics]::FromImage($crop)
            $srcRect = New-Object System.Drawing.Rectangle ($c * $cellW), ($r * $cellH), $cellW, $cellH
            $destRect = New-Object System.Drawing.Rectangle 0, 0, $cellW, $cellH
            $g.DrawImage($grid, $destRect, $srcRect, [System.Drawing.GraphicsUnit]::Pixel)
            
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
    $grid.Dispose()
    Write-Host "CROPPED $count AVATAR CIRCLES SUCCESSFULLY!"
}

# Copy customer review photos
$photos = Get-ChildItem "reviews pics\*.png"
$pCount = 1
foreach ($p in $photos) {
    Copy-Item $p.FullName "assets/reviews/review-photo-$pCount.jpg" -Force
    Copy-Item $p.FullName "demo_lab/assets/reviews/review-photo-$pCount.jpg" -Force
    Copy-Item $p.FullName "preview/assets/reviews/review-photo-$pCount.jpg" -Force
    $pCount++
}
Write-Host "COPIED $pCount REVIEW PHOTOS!"

# Copy human face photos
$faces = Get-ChildItem "reviews pics\human faces\*.png"
$fCount = 1
foreach ($f in $faces) {
    Copy-Item $f.FullName "assets/reviews/face-photo-$fCount.jpg" -Force
    Copy-Item $f.FullName "demo_lab/assets/reviews/face-photo-$fCount.jpg" -Force
    Copy-Item $f.FullName "preview/assets/reviews/face-photo-$fCount.jpg" -Force
    $fCount++
}
Write-Host "COPIED $fCount FACE PHOTOS!"
