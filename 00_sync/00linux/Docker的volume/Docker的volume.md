# 引入
volume作为docker和宿主机间桥梁一般的存在
```
docker volume create
docker volume ls
docker rm
docker volume inspect
docker volume prune  危险
```
# 关于卷volume的命名
我是非常不希望看到这种随机生成的名字的，管理起来确实是不太方便。但绑定bind挂载没有办法去改卷的命令，因为那是一个路径
![image-202410305842146.png|475](00_sync/00linux/Docker的volume/Docker的volume/image-202410305842146.png)
# 持久化部署
## 绑定挂载【推荐】 显示local
```
 -v /home/0000/docker/jellyfin/config:/config \
```

```
version: '3.8'

services:
  jellyfin:
    image: jellyfin/jellyfin
    container_name: jellyfin
    hostname: jellyfin
    volumes:  # 挂载卷
      - /home/0000/docker/jellyfin/config:/config
      - /home/xyblue_smb/jellyfin/media:/media
    environment:  # 设置环境变量
      - PUID=1000
      - PGID=1000
    restart: unless-stopped  # 重启策略
    network_mode: host  # 使用主机网络模式 主机模式不能映射端口
```
这个数据都是在宿主机的，只有删除容器才能删除这个假的数据卷。
![image-20241030575723.png](00_sync/00linux/Docker的volume/Docker的volume/image-20241030575723.png)
而且存在一个哈希自动生成的volume，文件夹里面是空的
![image-2024103032067.png|475](00_sync/00linux/Docker的volume/Docker的volume/image-2024103032067.png)
## Docker 管理的卷【不推荐】
这种就直接在var里面了，如果删除卷，持久化部署也就被删除了  如果还有其他内容，也会生成一个哈希自动生成的volume，这个如果把数据卷删除了，就都没了。
```
 -v media123:/media \
```

```
version: '3.8'

volumes:
  config-volume: {}  # 声明名为 config-volume 的卷
  media-volume: {}   # 声明名为 media-volume 的卷

services:
  jellyfin:
    image: jellyfin/jellyfin
    container_name: jellyfin
    hostname: jellyfin
    volumes:  # 挂载卷
      - config-volume:/config  # 将名为 config-volume 的卷挂载到容器的 /config 目录  看情况使用
      - media-volume:/media    # 将名为 media-volume 的卷挂载到容器的 /media 目录  看情况使用
    environment:  # 设置环境变量
      - PUID=1000
      - PGID=1000
    restart: unless-stopped  # 重启策略
    network_mode: host  # 使用主机网络模式
```
# 扩展
## DEIVER模式
![image-20241031626903.png](00_sync/00linux/Docker的volume/Docker的volume/image-20241031626903.png)
这个允许多种格式，如一下，但我还是认为webdav协议配合rclone挂载到本地，再由local挂载比较靠谱
1. **Local**: 默认的存储驱动，用于创建本地文件系统的卷。
2. **NFS (Network File System)**: 允许您挂载网络上的文件系统作为 Docker 卷。这种方式适合需要跨多台机器共享数据的情况。
3. **iSCSI**: 提供块级别的存储访问，通常用于高性能的数据存储需求。
4. **Flocker**: 是一个集群管理系统，支持容器间的数据迁移和跨主机的数据复制。
5. **CephFS**: Ceph 是一个分布式存储系统，CephFS 可以作为一个文件系统挂载到 Docker 容器中。
6. **Azure File Storage**: 微软 Azure 提供的文件存储服务，可以作为一个存储驱动集成到 Docker 中。
7. **Amazon Elastic File System (EFS)**: AWS 的可伸缩文件存储服务，也可以作为 Docker 卷来使用。
8. **Google Cloud Storage**: 谷歌云平台提供的对象存储服务，也有相应的插件支持 Docker 卷的使用。