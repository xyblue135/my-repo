本篇只有安装，具体使用在其他篇章，例如串流，摄像头，emby jellyfin
# 直接安装
直接安装不加后缀的话，版本是比较落后的
```
sudo apt install ffmpeg
```

```
ffmpeg -version
转码功能也都是可以用的
```
# 手动安装
## WIN
https://ffmpeg.org/
一个是源码二进制文件，一个是安装包
![image-2024115114815.png|450](00_sync/00linux/Linux%E4%B8%8B%E5%AE%89%E8%A3%85ffmpeg/Linux%E4%B8%8B%E5%AE%89%E8%A3%85ffmpeg/image-2024115114815.png)
下面这个是win的，有两位开发者，上面那个有预编译的版本，点进去
精简版和全版本
![image-20241151434386.png|450](00_sync/00linux/Linux%E4%B8%8B%E5%AE%89%E8%A3%85ffmpeg/Linux%E4%B8%8B%E5%AE%89%E8%A3%85ffmpeg/image-20241151434386.png)
这样的话免安装的ffmpeg再加上环境变量，win的就可以了
## Linux
###  手动编译安装【去看我make安装】
https://www.ffmpeg.org/
1.下载FFmpeg压缩包二进制文件，可以从官网下载https://ffmpeg.org/download.html
2.解压压缩包:tar -zxvf ffmpeg-xxx.tar.gz
3.进入解压后的目录：cd ffmpeg-xxx
确保三方库正确安装
```
sudo apt-get update
sudo apt-get install yasm nasm pkg-config
```
4.执行配置命令:   
```
./configure --prefix=/usr/local/ffmpeg --enable-shared --disable-static
```
也可以是下面这个
 ```
./configure \
  --prefix=/home/0000/soft/ffmpeg/bianyi_result \
  --enable-shared \
  --disable-static \
  --enable-gpl \
  --enable-libmfx \
  --enable-vaapi \
  --enable-nonfree \
  --enable-libx264 \
  --enable-libx265 \
  --enable-libvpx \
  --enable-libmp3lame \
  --enable-libvorbis \
  --enable-libopus \
  --enable-libass \
  --enable-libfreetype \
  --enable-libtheora \
  --enable-libwebp \
  --enable-libaom \
  --enable-libvmaf \
  --enable-libvpl
```
LGPL 是 Lesser General Public License（较宽松通用公共许可证）
![image-2024116480256.png|400](00_sync/00linux/Linux%E4%B8%8B%E5%AE%89%E8%A3%85ffmpeg/Linux%E4%B8%8B%E5%AE%89%E8%A3%85ffmpeg/image-2024116480256.png)
5.编译:make
6.安装:sudo make install
7.配置环境变量：将/usr/local/ffmpeg/bin添加到PATH环境变量中，可以通过编辑~/.bashrc文件实现，添加以下内容：
```
export PATH=$PATH:/usr/local/ffmpeg/bin
```
8.source ~/.bashrc
9.验证安装是否成功：ffmpeg -version
![image-2024116481988.png](00_sync/00linux/Linux%E4%B8%8B%E5%AE%89%E8%A3%85ffmpeg/Linux%E4%B8%8B%E5%AE%89%E8%A3%85ffmpeg/image-2024116481988.png)
#### lib问题
如果出现lib问题  我这个是共享库加载路径有问题
![image-20241161458135.png](00_sync/00linux/Linux%E4%B8%8B%E5%AE%89%E8%A3%85ffmpeg/Linux%E4%B8%8B%E5%AE%89%E8%A3%85ffmpeg/image-20241161458135.png)
先判断下文件在不在，如果不在可能需要重新安装或者手动安装lib库
```
find /usr/local/ffmpeg -name "libavdevice.so.61"
```
设置临时变量看看行不行
```
export LD_LIBRARY_PATH=/usr/local/ffmpeg/lib:$LD_LIBRARY_PATH
```
![image-20241161712705.png](00_sync/00linux/Linux%E4%B8%8B%E5%AE%89%E8%A3%85ffmpeg/Linux%E4%B8%8B%E5%AE%89%E8%A3%85ffmpeg/image-20241161712705.png)
添加到~/.bashrc里面去
```
export LD_LIBRARY_PATH=/usr/local/ffmpeg/lib:$LD_LIBRARY_PATH
```
source ~/.bashrc
```
ldd $(which ffmpeg)
```
如果正常就可以了，可以回到步骤
### 安装已经编译好的【推荐】
建议直接
```
sudo dnf install ffmpeg ffmpeg-devel
```
https://www.johnvansickle.com/ffmpeg/
选择合适的架构
![image-20241151923871.png|325](00_sync/00linux/Linux%E4%B8%8B%E5%AE%89%E8%A3%85ffmpeg/Linux%E4%B8%8B%E5%AE%89%E8%A3%85ffmpeg/image-20241151923871.png)
加入环境变量，注意推荐使用export PATH=$PATH:/文件夹
![image-2024116169846.png|475](00_sync/00linux/Linux%E4%B8%8B%E5%AE%89%E8%A3%85ffmpeg/Linux%E4%B8%8B%E5%AE%89%E8%A3%85ffmpeg/image-2024116169846.png)



