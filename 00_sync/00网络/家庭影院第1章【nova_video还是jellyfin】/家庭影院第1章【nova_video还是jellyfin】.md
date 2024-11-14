随着科技的进步，越来越多的家庭开始追求高品质的家庭影院体验。一个精心打造的家庭影院不仅能够提供震撼的视听享受，还能让您足不出户就能享受到电影院般的观影感受。而在构建这样一个系统的过程中，选择一款合适的播放器则是至关重要的一步。在众多可选方案之中，利用网络附加存储作为多媒体中心的核心组成部分，正逐渐成为许多影音爱好者的首选方案之一。
# nova_video
nova要想好用，就必须要全屋科学上网，且封面数据和介绍数据是存放在服务端的。数据量大的时候会非常缓慢，用了一周我就弃坑了。
![image-202410194011964.png|89](00_sync/00网络/家庭影院第1章【nova_video还是jellyfin】/家庭影院第1章【nova_video还是jellyfin】/image-202410194011964.png)
# jellyfin
## 安装
### 非docker安装
https://jellyfin.org/docs/general/installation/linux#repository-automatic
### docker安装
```
记得换源，记得代理
docker pull jellyfin/jellyfin
```
![image-202410181211899.png|425](00_sync/00网络/家庭影院第1章【nova_video还是jellyfin】/家庭影院第1章【nova_video还是jellyfin】/image-202410181211899.png)
请确保将`/path/to/config`替换为实际配置文件的路径，`/path/to/media`替换为媒体文件的路径。`PUID`和`PGID`是运行容器的用户和组ID，通常设置为1000。【注意，这里只是简单配置，家庭影院优化我写了很多】
```
sudo docker run -d \
  --name jellyfin \
  -p 8096:8096 \
  -p 8920:8920 \
  -v /home/0000/docker/jellyfin/config:/config \
  -v /home/xyblue_smb:/media \
  -e PUID=1000 \
  -e PGID=1000 \
  jellyfin/jellyfin
```

```
version: '3.8'  # 使用Docker Compose文件格式版本3.8

services:
  jellyfin:
    image: jellyfin/jellyfin  # 指定使用的Docker镜像
    container_name: jellyfin  # 容器名称
    ports:
      - "8096:8096"  # 映射宿主机端口到容器端口
      - "8920:8920"  # 映射另一个端口
    volumes:
      - /home/0000/docker/jellyfin/config:/config  # 挂载配置目录
      - /home/xyblue_smb:/media  # 挂载媒体目录
    environment:
      - PUID=1000  # 设置PUID环境变量
      - PGID=1000  # 设置PGID环境变量
    restart: unless-stopped  # 除非停止，否则重启容器
```

docker内部链接外部，用持久化来运行。
TVDB需要科学上网来运行
![image-202410184610542.png|475](00_sync/00网络/家庭影院第1章【nova_video还是jellyfin】/家庭影院第1章【nova_video还是jellyfin】/image-202410184610542.png)
勾选存储nfo数据。
![image-202410184741609.png|475](00_sync/00网络/家庭影院第1章【nova_video还是jellyfin】/家庭影院第1章【nova_video还是jellyfin】/image-202410184741609.png)
关于解码设置，需要配合正确的驱动
![image-202410183532879.png|350](00_sync/00网络/家庭影院第1章【nova_video还是jellyfin】/家庭影院第1章【nova_video还是jellyfin】/image-202410183532879.png)
视频成功被识别到
![image-20241018573315.png|325](00_sync/00网络/家庭影院第1章【nova_video还是jellyfin】/家庭影院第1章【nova_video还是jellyfin】/image-20241018573315.png)
## 刮削海报极其介绍
### 手动刮削
需要配合host的定期更新维护来访问对应api，不然会有dns污染，很难受，且这个一个一个添加也不太方便。
https://www.tinymediamanager.org/download/
![image-20241018233256.png|350](00_sync/00网络/家庭影院第1章【nova_video还是jellyfin】/家庭影院第1章【nova_video还是jellyfin】/image-20241018233256.png)
可以直接使用共享的位置
![image-20241018430164.png|350](00_sync/00网络/家庭影院第1章【nova_video还是jellyfin】/家庭影院第1章【nova_video还是jellyfin】/image-20241018430164.png)
开始搜刮
![image-20241018441178.png|425](00_sync/00网络/家庭影院第1章【nova_video还是jellyfin】/家庭影院第1章【nova_video还是jellyfin】/image-20241018441178.png)
### 自动搜刮
#### Metashark
https://github.com/cxfksword/jellyfin-plugin-metashark
把下载的文件解压，然后将 Douban 文件夹放到 Jellyfin 的 "plugins" 目录下。
    - 对于 Linux, plugins 目录在 "$HOME/.local/share/jellyfin/plugins"
    - 对于 Mac 系统, 在 "~/.local/share/jellyfin/plugins"
    - 对于 Docker, 在 Docker 中的 "/config/plugins" 目录下。 相应的宿主机目录请查阅自己 的目录映射配置
    - 对于 Windows 10, 如果使用管理员权限启动的话，在 "C:\ProgramData\Jellyfin\Server\plugins" 目录下。
    - 对于其他系统，如果你找不到位置，请提 issue 或者与我联系。
放到配置文件的plugs下
![image-202410182028554.png|475](00_sync/00网络/家庭影院第1章【nova_video还是jellyfin】/家庭影院第1章【nova_video还是jellyfin】/image-202410182028554.png)
检查是否启用插件
![image-202410181945902.png|400](00_sync/00网络/家庭影院第1章【nova_video还是jellyfin】/家庭影院第1章【nova_video还是jellyfin】/image-202410181945902.png)
![image-202410182129749.png|400](00_sync/00网络/家庭影院第1章【nova_video还是jellyfin】/家庭影院第1章【nova_video还是jellyfin】/image-202410182129749.png)
#### TMDB
最好用的刮削器，就是不规范化命名可能会错误，且需要搭配科学上网。
# 结果
![image-20241018940539.png|375](00_sync/00网络/家庭影院第1章【nova_video还是jellyfin】/家庭影院第1章【nova_video还是jellyfin】/image-20241018940539.png)
![image-20241018932869.png|350](00_sync/00网络/家庭影院第1章【nova_video还是jellyfin】/家庭影院第1章【nova_video还是jellyfin】/image-20241018932869.png)
![image-20241018952598.png|350](00_sync/00网络/家庭影院第1章【nova_video还是jellyfin】/家庭影院第1章【nova_video还是jellyfin】/image-20241018952598.png)
小笔记本当个nas还挺好用的  外部测功率 赛扬N5095处理器也就 10W 的样子  也算是能秒开4K 远程观影了~
体验下来,jellyfin的界面很好看，多用户控制很好用，解码器基本都支持，可以跨设备断点播放，无缝双语切换，字母切换，自定义码率这些都挺好的。插件metashark链接豆瓣搜刮海波封面挺好用的。