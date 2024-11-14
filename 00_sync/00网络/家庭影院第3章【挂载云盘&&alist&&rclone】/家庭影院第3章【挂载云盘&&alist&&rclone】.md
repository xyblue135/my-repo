在数字时代的今天，云存储已经成为许多人管理和分享个人文件的重要方式。对于家庭影院爱好者来说，将云盘中的媒体资源直接整合进本地播放系统，不仅可以极大地扩展可用的媒体库容量，还可以方便地访问和播放存储在云端的视频、音频等内容。本章节我们将探讨如何通过WebDAV等协议挂载云盘，并将其无缝接入您的家庭影院系统，从而实现更加灵活和便捷的媒体管理与播放体验。

# Alist
https://alist.nn.ci/zh/guide/
具体其它细节需要去alist官网查看并使用
```
version: '3.8'

services:
  alist:
    image: xhofe/alist:latest-ffmpeg  # 换为xhofe/alist:beta 就是非ffmpeg版本
    container_name: alist
    hostname: alist
    volumes:  # 挂载卷
      - /home/0000/docker/alist/data:/opt/alist/data
      - /home/0000/docker/alist/本地:/本地
    environment:  # 设置环境变量
      - PUID=0
      - PGID=0
    restart: unless-stopped  # 重启策略
    network_mode: host  # 使用主机网络模式 主机模式不能映射端口
```
## 设置alist账号密码
```
# 随机生成一个密码
docker exec -it alist ./alist admin random

# 手动设置一个密码,`NEW_PASSWORD`是指你需要设置的密码
docker exec -it alist ./alist admin set 密码

# 查看管理员信息 老版本
docker exec -it alist ./alist admin

# 3.25以上 随机生成一个密码
docker exec -it alist ./alist admin random
```
## 服务端挂载云盘
各家云盘的标准不一样，具体的要看alist文档和实际情况。
`https://alist.nn.ci/zh/`
## WebDav策略
![image-202410213957853.png|350](00_sync/00网络/家庭影院第3章【挂载云盘&&alist&&rclone】/家庭影院第3章【挂载云盘&&alist&&rclone】/image-202410213957853.png)
302收到的数据不会放到磁盘里面，如果有兼容性问题，不要用302重定向
![image-202410215737927.png|425](00_sync/00网络/家庭影院第3章【挂载云盘&&alist&&rclone】/家庭影院第3章【挂载云盘&&alist&&rclone】/image-202410215737927.png)
# 客户端挂载alist
## WIN【Raidrive】
https://www.raidrive.com/download
要确定是http还是https
![image-2024102163483.png|325](00_sync/00网络/家庭影院第3章【挂载云盘&&alist&&rclone】/家庭影院第3章【挂载云盘&&alist&&rclone】/image-2024102163483.png)
![image-202410213145528.png|425](00_sync/00网络/家庭影院第3章【挂载云盘&&alist&&rclone】/家庭影院第3章【挂载云盘&&alist&&rclone】/image-202410213145528.png)
也可以直接使用web进行传输。
![image-20241021531320.png|375](00_sync/00网络/家庭影院第3章【挂载云盘&&alist&&rclone】/家庭影院第3章【挂载云盘&&alist&&rclone】/image-20241021531320.png)
## WIN【rclone】
个人任务rclone比raidrive好用
https://rclone.org/downloads/
你得先看Linux的rclone再回看这个
win是不能直接挂载的，需要个代理。
### WINFSP
WinFsp（Windows File System Proxy）是一个用于 Windows 的文件系统代理软件，类似于 Linux 上的 FUSE（Filesystem in Userspace）。WinFsp 允许开发者在用户模式下创建文件系统，而不是在内核模式下。这种设计简化了文件系统的开发，并降低了出错的风险，因为它不需要直接修改操作系统内核。
https://github.com/winfsp/winfsp
![image-20241194923528.png|291](00_sync/00网络/家庭影院第3章【挂载云盘&&alist&&rclone】/家庭影院第3章【挂载云盘&&alist&&rclone】/image-20241194923528.png)
![image-20241195031603.png|475](00_sync/00网络/家庭影院第3章【挂载云盘&&alist&&rclone】/家庭影院第3章【挂载云盘&&alist&&rclone】/image-20241195031603.png)
```
.\rclone.exe mount alist: G: --vfs-cache-mode full --buffer-size 128M
.\rclone.exe mount alist: G: --vfs-cache-mode full --buffer-size 128M --vfs-disk-space-total-size 9.75T
```
![image-20241195043846.png|475](00_sync/00网络/家庭影院第3章【挂载云盘&&alist&&rclone】/家庭影院第3章【挂载云盘&&alist&&rclone】/image-20241195043846.png)
卸载云盘
```
rclone unmount G:
```
## Linux【rclone】
### 链接云盘
rclone也可以挂载云盘，但是不方便实用，所以用rclone挂载alist整合好的网盘，配合用webdav服务比较方便。
https://github.com/rclone/rclone/releases
```
sudo apt install rclone
```
然后可以使用rclone的命令
```
rclone config
```
![image-20241026442608.png|450](00_sync/00网络/家庭影院第3章【挂载云盘&&alist&&rclone】/家庭影院第3章【挂载云盘&&alist&&rclone】/image-20241026442608.png)
按n回车新建一个远程连接 输入一个链接名字，我命名为alist
![image-20241026619756.png](00_sync/00网络/家庭影院第3章【挂载云盘&&alist&&rclone】/家庭影院第3章【挂载云盘&&alist&&rclone】/image-20241026619756.png)
这里我要是用的为webdav
![image-20241026654676.png|250](00_sync/00网络/家庭影院第3章【挂载云盘&&alist&&rclone】/家庭影院第3章【挂载云盘&&alist&&rclone】/image-20241026654676.png)
我是本机就输入本机地址`http://127.0.0.1:5244/dav`，跟raidrive类似
![image-20241026754902.png|400](00_sync/00网络/家庭影院第3章【挂载云盘&&alist&&rclone】/家庭影院第3章【挂载云盘&&alist&&rclone】/image-20241026754902.png)
使用other
![image-20241026821117.png|386](00_sync/00网络/家庭影院第3章【挂载云盘&&alist&&rclone】/家庭影院第3章【挂载云盘&&alist&&rclone】/image-20241026821117.png)
输入账号密码,也就是alist的
![image-20241026101116.png](00_sync/00网络/家庭影院第3章【挂载云盘&&alist&&rclone】/家庭影院第3章【挂载云盘&&alist&&rclone】/image-20241026101116.png)
然后回车保持默认即可，最后的q回车就可以
![image-20241026119603.png|310](00_sync/00网络/家庭影院第3章【挂载云盘&&alist&&rclone】/家庭影院第3章【挂载云盘&&alist&&rclone】/image-20241026119603.png)

### 挂载磁盘
挂载webdav的地方  rclone的log  rclone的视频缓存
提前创建要用到的文件夹
```
mkdir -p /home/0000/soft/rclone/log
touch /home/0000/soft/rclone/log/rclone_mount.log
mkdir -p /home/0000/soft/rclone//tmp/rclone_cache
mkdir -p /home/xyblue_smb/jellyfin/media/rclone_alist_webdav
```

```
rclone mount \
  alist: \
  /home/xyblue_smb/jellyfin/media/rclone_alist_webdav \
  --cache-dir /home/0000/soft/rclone/tmp/rclone_cache \
  --log-file /home/0000/soft/rclone/log/rclone_mount_log \
  --allow-other \
  --allow-non-empty \
  --vfs-cache-mode full \
  --daemon
```

```
#!/bin/bash

# 直接使用提供的命令
rclone mount \
  alist: \
  /home/xyblue_smb/jellyfin/media/rclone_alist_webdav \
  --cache-dir /home/0000/soft/rclone/tmp/rclone_cache \
  --log-file /home/0000/soft/rclone/log/rclone_mount_log \
  --allow-other \
  --allow-non-empty \
  --vfs-cache-mode full \
  --daemon

# 检查 rclone mount 是否成功
if [ $? -eq 0 ]; then
  echo "rclone mount 成功"
else
  echo "rclone mount 失败"
fi
```

# 总结
## 检查挂载状态
```
rclone lsd alist:  【注意冒号】
ps aux | grep rclone  【推荐】
tail -f /log/rclone-mount.log
```
![image-20241026241801.png|450](00_sync/00网络/家庭影院第3章【挂载云盘&&alist&&rclone】/家庭影院第3章【挂载云盘&&alist&&rclone】/image-20241026241801.png)
## 解除挂载
```
rclone config 后直接删除 【推荐】
ps aux | grep rclone 【先查看】
fusermount -u /home/xyblue_smb/jellyfin/media/rclone_alist_webdav  #先强制 卸载 不行的话kill进程 不然会出问题
fusermount -uz /home/xyblue_smb/jellyfin/media/rclone_alist_webdav  # 强制卸载， 适用于异常的情况
```
![image-202410264221335.png|475](00_sync/00网络/家庭影院第3章【挂载云盘&&alist&&rclone】/家庭影院第3章【挂载云盘&&alist&&rclone】/image-202410264221335.png)
## 挂载参数
```
--cache-dir /tmp \    指定缓存目录
--allow-other \  #允许其他用户访问挂载点，这对于在多用户环境中非常有用。



--umask 0022 \ `umask` 是一个用来确定新创建的文件和目录默认权限的掩码
- **文件**：`0666` & `~umask`，例如 `0666` & `0022` = `0644`（即 `-rw-r--r--`）。
- **目录**：`0777` & `~umask`，例如 `0777` & `0022` = `0755`（即 `drwxr-xr-x`）。

--no-subdir  不创建子目录

--buffer-size`**：设置读写缓冲区的大小。例如：
--buffer-size 1M

--low-level-retries`**：设置低级别重试次数。例如：
--low-level-retries 3

--max-read-ahead`**：设置最大预读取字节数。例如：
--max-read-ahead 1M

--read-ahead-threshold`**：设置预读取阈值。例如：
--read-ahead-threshold 100K
```

```
日志存放位置
--log-file /var/log/rclone-mount.log

设置日志记录级别
--log-level DEBUG

设置统计信息的输出间隔。例如：
--stats 1h
```
## crontab开机脚本
我喜欢crontab  当然也可以用systemctl 和rc 和 /etc/profile
```
#!/bin/bash

# 直接使用提供的命令
rclone mount \
  alist: \
  /home/xyblue_smb/jellyfin/media/rclone_alist_webdav \
  --cache-dir /home/0000/soft/rclone/tmp/rclone_cache \
  --log-file /home/0000/soft/rclone/log/rclone_mount_log \
  --allow-other \
  --allow-non-empty \
  --vfs-cache-mode full \
  --daemon

# 检查 rclone mount 是否成功
if [ $? -eq 0 ]; then
  echo "rclone mount 成功"
else
  echo "rclone mount 失败"
fi
```
crontab -e
```
@reboot /home/0000/soft/rclone/crontab_start.sh > /home/soft/rclone/start_sh.log 2>&1 &
```
# alist定时更新·
```
crontab -e
0 6 * * * docker restart xiaoya
```
## ntp时间问题【已解决】
需要保持时间同步
![image-20241111131332.png](00_sync/00网络/家庭影院第3章【挂载云盘&&alist&&rclone】/家庭影院第3章【挂载云盘&&alist&&rclone】/image-20241111131332.png)

## 播放错误排错
用raidriver竟然出现了两个厂家网盘无法上传，但是rclone只有一家厂家无法上传，于是我仔细看了一下下webdav策略。在看到webdav策略后，修改为本地或者代理即可。可以成功使用了
![image-20241125244908.png](00_sync/00网络/家庭影院第3章【挂载云盘&&alist&&rclone】/家庭影院第3章【挂载云盘&&alist&&rclone】/image-20241125244908.png)
## WEBDAV策略图
![image-20241122059639.png|650](00_sync/00网络/家庭影院第3章【挂载云盘&&alist&&rclone】/家庭影院第3章【挂载云盘&&alist&&rclone】/image-20241122059639.png)


![image-2024112122985.png|475](00_sync/00网络/家庭影院第3章【挂载云盘&&alist&&rclone】/家庭影院第3章【挂载云盘&&alist&&rclone】/image-2024112122985.png)


## rclone缓存
如果不对缓存容量进行限制的话，系统会崩溃的
```
清除名为alist的缓存
rclone cache-clear alist:
```
  --vfs-cache-mode full \这个参数默认一小时清理一次算法计算出来该被清理的
  如果去掉这个参数 就是无缓存文件
  至于用哪个要依据网盘来决定
  也可配合参数
  --vfs-cache-max-size 30G --vfs-cache-max-age 2h --vfs-cache-mode full
```
#!/bin/bash

# 使用提供的命令并添加 --poll-interval 30s 参数
rclone mount \
  alist: \
  /home/xyblue_smb/jellyfin/media/rclone_alist_webdav \
  --cache-dir /home/0000/soft/rclone/tmp/rclone_cache \
  --log-file /home/0000/soft/rclone/log/rclone_mount_log \
  --allow-other \
  --allow-non-empty \
  --poll-interval 3000s \
  --daemon

# 检查 rclone mount 是否成功
if [ $? -eq 0 ]; then
  echo "rclone mount 成功"
else
  echo "rclone mount 失败"
fi
```
## Jellyfin缓存
jellyfin的缓存是cache目录，挂载网盘必须持久化缓存目录，不然预览图什么的不从本地局域网主机加载会非常缓慢且难受