# 软解码
```
ffmpeg -i input.mp4 -c:v libx264 -b:v 1000k output_video.mp4
```
# 硬解码
只硬解，不转码
```
ffmpeg -hwaccel qsv -i input.mp4 -c:v copy output_video.mp4
ffmpeg -hwaccel qsv -i input.mkv -c:v copy output_video.mkv
ffmpeg -hwaccel qsv -i input.mkv -c:v copy output_video.mp4

ffmpeg -hwaccel qsv -i input.mkv -c:v h264_qsv -f null -benchmark output_hardware.mp4

```
ffmpeg -init_hw_device qsv=hw -hwaccel qsv -i input.mp4 -c:v h264_qsv -b:v 1000k output_video.mp4

# 故障1
![image-202411131532591.png|400](00_sync/00%E5%9B%BE%E7%89%87%E8%A7%86%E9%A2%91%E5%A4%84%E7%90%86/ffmpeg%E7%9A%84%E5%91%BD%E4%BB%A4%E4%BD%BF%E7%94%A8/ffmpeg%E7%9A%84%E5%91%BD%E4%BB%A4%E4%BD%BF%E7%94%A8/image-202411131532591.png)
```
ffmpeg -hwaccel cuvid -c:v h264_cuvid -i LaLaLand_cafe_4K.mkv -c:v h264_nvenc -b:v 2000k -c:a copy -extra_hw_frames 32 output.mp4
```
这里的`-extra_hw_frames 32`参数增加了额外的解码表面数量,就不会出现这个报错了