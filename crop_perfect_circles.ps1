Add-Type -AssemblyName System.Drawing

$gridImgPath = "reviews pics/profile/ChatGPT Image Aug 11, 2026, 12_40_49 PM.png"
$img = [System.Drawing.Bitmap]::FromFile((Resolve-Path $gridImgPath))

$w = $img.Width
$h = $img.Height
$cols = 5
$rows = 4

$cellW = $w / $cols
$cellH = $h / $rows

# Diameter of circle in pixels (tight 1:1 square crop around face!)
$cropSize = 210

$avatarDir = "assets/reviews"
$demoAvatarDir = "demo_lab/assets/reviews"
$previewAvatarDir = "preview/assets/reviews"

$count = 1
for ($r = 0; $r -lt $rows; $r++) {
    for ($c = 0; $c -lt $cols; $c++) {
        $centerX = ($c + 0.5) * $cellW
        $centerY = ($r + 0.5) * $cellH
        
        $startX = [int]($centerX - ($cropSize / 2))
        $startY = [int]($centerY - ($cropSize / 2))
        
        # Ensure inside bounds
        if ($startX -lt 0) { $startX = 0 }
        if ($startY -lt 0) { $startY = 0 }
        if (($startX + $cropSize) -gt $w) { $startX = $w - $cropSize }
        if (($startY + $cropSize) -gt $h) { $startY = $h - $cropSize }
        
        $crop = New-Object System.Drawing.Bitmap $cropSize, $cropSize
        $g = [System.Drawing.Graphics]::FromImage($crop)
        $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
        $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
        $g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
        
        $srcRect = New-Object System.Drawing.Rectangle $startX, $startY, $cropSize, $cropSize
        $destRect = New-Object System.Drawing.Rectangle 0, 0, $cropSize, $cropSize
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
Write-Host "PERFECT 1:1 SQUARE CROPPED 20 AVATARS!"
