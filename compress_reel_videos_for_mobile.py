import os
import subprocess
import imageio_ffmpeg

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
print(f"Using FFmpeg at: {ffmpeg_exe}")

reel_files = [
    r"c:\Users\moham\Downloads\blackroots website\assets\reel-1.mp4",
    r"c:\Users\moham\Downloads\blackroots website\assets\reel-2.mp4",
    r"c:\Users\moham\Downloads\blackroots website\assets\reel-3.mp4",
    r"c:\Users\moham\Downloads\blackroots website\assets\reel-4.mp4",
    r"c:\Users\moham\Downloads\blackroots website\assets\reel-5.mp4",
]

print("=== COMPRESSING AND STREAM-OPTIMIZING REEL VIDEOS FOR MOBILE (60FPS BUTTER SMOOTH) ===")

for rpath in reel_files:
    if os.path.exists(rpath):
        old_size_mb = os.path.getsize(rpath) / (1024 * 1024)
        temp_out = rpath.replace('.mp4', '_fast.mp4')
        
        # FFmpeg command: H.264 yuv420p, crf 26, faststart for instant mobile streaming, max 540x960 9:16
        cmd = [
            ffmpeg_exe,
            '-y',
            '-i', rpath,
            '-c:v', 'libx264',
            '-preset', 'fast',
            '-crf', '26',
            '-pix_fmt', 'yuv420p',
            '-vf', 'scale=540:960:force_original_aspect_ratio=decrease,pad=540:960:(ow-iw)/2:(oh-ih)/2',
            '-c:a', 'aac',
            '-b:a', '96k',
            '-movflags', '+faststart',
            temp_out
        ]
        
        try:
            res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if os.path.exists(temp_out) and os.path.getsize(temp_out) > 1000:
                os.replace(temp_out, rpath)
                new_size_mb = os.path.getsize(rpath) / (1024 * 1024)
                print(f"SUCCESS: {os.path.basename(rpath)} compressed from {old_size_mb:.2f} MB -> {new_size_mb:.2f} MB ({((old_size_mb-new_size_mb)/old_size_mb)*100:.1f}% smaller!)")
            else:
                print(f"Failed to compress {rpath}: {res.stderr[:200]}")
        except Exception as e:
            print(f"Error compressing {rpath}: {e}")
