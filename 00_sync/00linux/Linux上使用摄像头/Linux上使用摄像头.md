sudo apt install ffmpeg

ffmpeg -y -f v4l2 -rtbuf_size 128M -video_size <width>x<height> -i /dev/video0 -frames:v 1 output.png
ffmpeg -y -f v4l2 -i /dev/video0 -frames:v 1 output.png
ffmpeg -y -f v4l2 -rtbuf_size 128M -i /dev/video0 -frames:v 1 output.png