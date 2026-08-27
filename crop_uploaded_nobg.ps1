Add-Type -AssemblyName System.Drawing

$gridImgPath = "C:\Users\moham\.gemini\antigravity\brain\0219a2fe-4690-4482-9583-96e83a21bc69\.user_uploaded\media_1786434051569.png"
if (Test-Path $gridImgPath) {
    $img = [System.Drawing.Bitmap]::FromFile($gridImgPath)
    Write-Host "Uploaded Grid Dimensions:" $img.Width "x" $img.Height
    
    $w = $img.Width
    $h = $img.Height
    $cols = 5
    $rows = 4
    
    $cellW = $w / $cols
    $cellH = $h / $rows
    
    # Exact circle diameter in 500x500 grid: ~84px!
    $cropSize = 84
    
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
            
            if ($startX -lt 0) { $startX = 0 }
            if ($startY -lt 0) { $startY = 0 }
            if (($startX + $cropSize) -gt $w) { $startX = $w - $cropSize }
            if (($startY + $cropSize) -gt $h) { $startY = $h - $cropSize }
            
            $crop = New-Object System.Drawing.Bitmap $cropSize, $cropSize
            $g = [System.Drawing.Graphics]::FromImage($crop)
            $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
            $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
            $g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
            
            # Clip circle
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
    Write-Host "PERFECT 84PX INNER CIRCLE CROPPED 20 AVATARS FROM UPLOADED NO-BG IMAGE!"
} else {
    Write-Host "Uploaded file not found"
}
