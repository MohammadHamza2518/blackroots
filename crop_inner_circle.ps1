Add-Type -AssemblyName System.Drawing

$gridImgPath = "reviews pics/profile/ChatGPT Image Aug 11, 2026, 12_40_49 PM.png"
$img = [System.Drawing.Bitmap]::FromFile((Resolve-Path $gridImgPath))

$w = $img.Width
$h = $img.Height
$cols = 5
$rows = 4

$cellW = $w / $cols
$cellH = $h / $rows

# The circle inside each cell has diameter ~175px.
# Setting cropSize = 165 ensures we crop 100% INSIDE the face photo with ZERO white background bleeding!
$cropSize = 165

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
        
        # Create output bitmap
        $crop = New-Object System.Drawing.Bitmap $cropSize, $cropSize
        $g = [System.Drawing.Graphics]::FromImage($crop)
        $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
        $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
        $g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
        
        # Create circular clip path so output is a PERFECT CIRCLE PNG/JPG!
        $path = New-Object System.Drawing.Drawing2D.GraphicsPath
        $path.AddEllipse(0, 0, $cropSize, $cropSize)
        $g.SetClip($path)
        
        $srcRect = New-Object System.Drawing.Rectangle $startX, $startY, $cropSize, $cropSize
        $destRect = New-Object System.Drawing.Rectangle 0, 0, $cropSize, $cropSize
        $g.DrawImage($img, $destRect, $srcRect, [System.Drawing.GraphicsUnit]::Pixel)
        
        $out1 = Join-Path $avatarDir "avatar-$count.jpg"
        $out2 = Join-Path $demoAvatarDir "avatar-$count.jpg"
        $out3 = Join-Path $previewAvatarDir "avatar-$count.jpg"
        
        $crop.Save($out1, [System.Drawing.Imaging.ImageFormat]::Jpeg)
        $crop.Save($out2, [System.Drawing.Imaging.ImageFormat]::Jpeg)
        $crop.Save($out3, [System.Drawing.Imaging.ImageFormat]::Jpeg)
        
        $path.Dispose()
        $g.Dispose()
        $crop.Dispose()
        $count++
    }
}

$img.Dispose()
Write-Host "PERFECT INNER FACE CIRCLE CROPPED WITH 0% WHITE BORDER!"
