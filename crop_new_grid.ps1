Add-Type -AssemblyName System.Drawing

$gridImgPath = "C:\Users\moham\.gemini\antigravity\brain\0219a2fe-4690-4482-9583-96e83a21bc69\.user_uploaded\media_1786437509977.jpg"
$img = [System.Drawing.Bitmap]::FromFile($gridImgPath)
Write-Host "New Grid:" $img.Width "x" $img.Height

$cols = 5
$rows = 5
$w = $img.Width
$h = $img.Height
$cellW = $w / $cols
$cellH = $h / $rows

# Slightly inset to avoid white borders
$cropSize = [int]($cellW * 0.82)

$dirs = @("assets/reviews", "demo_lab/assets/reviews", "preview/assets/reviews")

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

        $path = New-Object System.Drawing.Drawing2D.GraphicsPath
        $path.AddEllipse(0, 0, $cropSize, $cropSize)
        $g.SetClip($path)

        $srcRect = New-Object System.Drawing.Rectangle $startX, $startY, $cropSize, $cropSize
        $destRect = New-Object System.Drawing.Rectangle 0, 0, $cropSize, $cropSize
        $g.DrawImage($img, $destRect, $srcRect, [System.Drawing.GraphicsUnit]::Pixel)

        foreach ($dir in $dirs) {
            $outPath = Join-Path $dir "new-avatar-$count.jpg"
            $crop.Save($outPath, [System.Drawing.Imaging.ImageFormat]::Jpeg)
        }

        $path.Dispose()
        $g.Dispose()
        $crop.Dispose()
        $count++
    }
}

$img.Dispose()
Write-Host "CROPPED 25 NEW AVATARS FROM 5x5 GRID!"
