我觉得配合ffmpeg转码我觉得是最方便的测试方法了，如果不会安装ffmpeg的话，我有写，可以去找找看
# 软
```
ffmpeg -i "input.mp4" -c:v libx264 -b:v 100k -c:a aac -b:a 64k -movflags +faststart "output.mp4"
```
# 英特尔
可以使用 `qsv` 来进行硬件加速
```
ffmpeg -hwaccel qsv -hwaccel_output_format qsv -i input.mp4 -c:v h264_qsv -crf 23 -preset fast -c:a copy output.mp4
ffmpeg -hwaccel qsv -hwaccel_output_format qsv -i input.mp4 -c:v h264_qsv -crf 23 -preset fast -c:a copy output.mkv
```
# 英伟达
```
ffmpeg -i LaLaLand_cafe_4K.mkv -vf "scale=-2:1080,format=yuv420p10le" -c:v hevc_nvenc -b:v 60M -color_trc smpte2084 -color_primaries bt2020 -colorspace bt2020nc -c:a copy output_1080p_60mbps.mkv
```