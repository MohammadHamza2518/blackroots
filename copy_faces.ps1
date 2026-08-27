Add-Type -AssemblyName System.Drawing

$faces = Get-ChildItem "reviews pics\human faces\*.png"
$avatarDir = "assets/reviews"
$demoAvatarDir = "demo_lab/assets/reviews"
$previewAvatarDir = "preview/assets/reviews"

$i = 1
foreach ($f in $faces) {
    $img = [System.Drawing.Bitmap]::FromFile($f.FullName)
    $minDim = [Math]::Min($img.Width, $img.Height)
    
    $startX = [int](($img.Width - $minDim) / 2)
    $startY = [int](($img.Height - $minDim) / 2)
    
    $crop = New-Object System.Drawing.Bitmap $minDim, $minDim
    $g = [System.Drawing.Graphics]::FromImage($crop)
    $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    
    $srcRect = New-Object System.Drawing.Rectangle $startX, $startY, $minDim, $minDim
    $destRect = New-Object System.Drawing.Rectangle 0, 0, $minDim, $minDim
    $g.DrawImage($img, $destRect, $srcRect, [System.Drawing.GraphicsUnit]::Pixel)
    
    $out1 = Join-Path $avatarDir "face-avatar-$i.jpg"
    $out2 = Join-Path $demoAvatarDir "face-avatar-$i.jpg"
    $out3 = Join-Path $previewAvatarDir "face-avatar-$i.jpg"
    
    $crop.Save($out1, [System.Drawing.Imaging.ImageFormat]::Jpeg)
    $crop.Save($out2, [System.Drawing.Imaging.ImageFormat]::Jpeg)
    $crop.Save($out3, [System.Drawing.Imaging.ImageFormat]::Jpeg)
    
    $g.Dispose()
    $crop.Dispose()
    $img.Dispose()
    $i++
}

Write-Host "PROCESSED $i INDIVIDUAL FACE AVATARS!"
