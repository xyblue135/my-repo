# 示例
# GCC
必须确保gcc的安装
GCC（GNU Compiler Collection）或类似的C/C++编译器。GCC是最常用的编译器之一，用于将C和C++源代码编译成机器码。FFmpeg主要是用C语言编写的，所以你需要一个C编译器来编译它的源代码。
## ffmpeg
1.下载FFmpeg压缩包二进制文件，可以从官网下载https://ffmpeg.org/download.html
2.解压压缩包:tar -zxvf ffmpeg-xxx.tar.gz
3.进入解压后的目录：cd ffmpeg-xxx
![image-20241165534138.png|475](00_sync/00linux/Linux下编译make安装/Linux下编译make安装/image-20241165534138.png)
确保三方库正确安装
```
sudo apt-get update
sudo apt-get install yasm nasm pkg-config
```
4.执行配置命令:   
--prefix=/usr/local/ffmpeg 安装路径 --enable-shared 启动共享库（生成 `.so` 文件）。 --disable-static禁用静态库（不生成 `.a` 文件）。
```
./configure --prefix=/usr/local/ffmpeg --enable-shared --disable-static
```
【这个配置命令挺关键的，这个会决定make 安装时候的位置】
![image-2024116426444.png|475](00_sync/00linux/Linux下编译make安装/Linux下编译make安装/image-2024116426444.png)
5.编译:make 【有的时候多线程可能会不稳定】【make -j6 六线程运行】
![image-2024116439703.png|475](00_sync/00linux/Linux下编译make安装/Linux下编译make安装/image-2024116439703.png)
![image-2024116837975.png](00_sync/00linux/Linux下编译make安装/Linux下编译make安装/image-2024116837975.png)
6.安装:sudo make install  【安装到/usr/local/ffmpeg】
我设定的目录在这里，去bin里面可以看到正常运行
![image-2024116138713.png|475](00_sync/00linux/Linux下编译make安装/Linux下编译make安装/image-2024116138713.png)
7.配置环境变量：将/usr/local/ffmpeg/bin或者自定义目录添加到PATH环境变量中
可以通过编辑~/.bashrc文件实现，添加以下内容：
```
export PATH=$PATH:/usr/local/ffmpeg/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/ffmpeg/lib # 如果丢了动态链接库也加上
```
8.source ~/.bashrc
9.验证安装是否成功：ffmpeg -version

# 问题
指定动态链接器,如果在本地和加环境变量发现不能用且提示lib的问题， 可能是少东西了
```
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/ffmpeg/lib
LD_LIBRARY_PATH 是一个环境变量，用于告诉动态链接器（ld.so 或 ld-linux.so）在哪些目录中查找共享库。当你设置 LD_LIBRARY_PATH 时，你实际上是在扩展或覆盖现有的 LD_LIBRARY_PATH 环境变量。
```
![image-20241114302962.png](00_sync/00linux/Linux%E4%B8%8B%E7%BC%96%E8%AF%91make%E5%AE%89%E8%A3%85/Linux%E4%B8%8B%E7%BC%96%E8%AF%91make%E5%AE%89%E8%A3%85/image-20241114302962.png)