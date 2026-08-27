Add-Type -AssemblyName System.Drawing

$gridImgPath = "C:\Users\moham\.gemini\antigravity\brain\0219a2fe-4690-4482-9583-96e83a21bc69\.user_uploaded\media_1786434051569.png"

if (Test-Path $gridImgPath) {
    $img = [System.Drawing.Bitmap]::FromFile($gridImgPath)
    Write-Host "Image Size:" $img.Width "x" $img.Height
    
    # 20 Face Coordinates mapped exactly to head/face centers!
    # (x, y, cropSize)
    $faceCoords = @(
        # Row 0
        @{ x = 16; y = 15; size = 68; name = "face_0_0_male_glasses" },
        @{ x = 116; y = 18; size = 68; name = "face_0_1_female_longhair" },
        @{ x = 216; y = 18; size = 68; name = "face_0_2_male_beard" },
        @{ x = 316; y = 18; size = 68; name = "face_0_3_female_glasses" },
        @{ x = 416; y = 18; size = 68; name = "face_0_4_male_white" },
        
        # Row 1
        @{ x = 16; y = 138; size = 68; name = "face_1_0_female_trad" },
        @{ x = 116; y = 138; size = 68; name = "face_1_1_male_selfie" },
        @{ x = 216; y = 138; size = 68; name = "face_1_2_female_specs" },
        @{ x = 316; y = 138; size = 68; name = "face_1_3_male_polo" },
        @{ x = 416; y = 138; size = 68; name = "face_1_4_female_pink" },

        # Row 2
        @{ x = 16; y = 265; size = 68; name = "face_2_0_male_sunglasses" },
        @{ x = 116; y = 265; size = 68; name = "face_2_1_female_mature_bindi" },
        @{ x = 216; y = 265; size = 68; name = "face_2_2_male_phone" },
        @{ x = 316; y = 265; size = 68; name = "face_2_3_female_glasses" },
        @{ x = 416; y = 265; size = 68; name = "face_2_4_male_mask" },

        # Row 3
        @{ x = 16; y = 390; size = 68; name = "face_3_0_male_senior" },
        @{ x = 116; y = 390; size = 68; name = "face_3_1_female_green" },
        @{ x = 216; y = 390; size = 68; name = "face_3_2_male_beach" },
        @{ x = 316; y = 390; size = 68; name = "face_3_3_female_yellow_saree" },
        @{ x = 416; y = 390; size = 68; name = "face_3_4_male_jacket" }
    )

    $avatarDir = "assets/reviews"
    $demoAvatarDir = "demo_lab/assets/reviews"
    $previewAvatarDir = "preview/assets/reviews"

    $idx = 1
    foreach ($f in $faceCoords) {
        $cropSize = $f.size
        $startX = $f.x
        $startY = $f.y
        
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
        
        $out1 = Join-Path $avatarDir "custom-avatar-$idx.jpg"
        $out2 = Join-Path $demoAvatarDir "custom-avatar-$idx.jpg"
        $out3 = Join-Path $previewAvatarDir "custom-avatar-$idx.jpg"
        
        $crop.Save($out1, [System.Drawing.Imaging.ImageFormat]::Jpeg)
        $crop.Save($out2, [System.Drawing.Imaging.ImageFormat]::Jpeg)
        $crop.Save($out3, [System.Drawing.Imaging.ImageFormat]::Jpeg)
        
        $path.Dispose()
        $g.Dispose()
        $crop.Dispose()
        $idx++
    }

    $img.Dispose()
    Write-Host "CROPPED 20 CUSTOM PERFECT FACE AVATARS!"
}
