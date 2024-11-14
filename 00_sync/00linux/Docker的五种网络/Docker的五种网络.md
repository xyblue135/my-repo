配有思维导图
# 初见
想必使用docker的我们 随着时间推移网卡越来越多，非常臃肿，需要解决掉
![image-202410303357148.png|400](00_sync/00linux/Docker%E7%9A%84%E4%BA%94%E7%A7%8D%E7%BD%91%E7%BB%9C/Docker%E7%9A%84%E4%BA%94%E7%A7%8D%E7%BD%91%E7%BB%9C/image-202410303357148.png)
# 三种基础网络类型
brige和host和none
![image-202410285121318.png](00_sync/00linux/Docker%E7%9A%84%E4%BA%94%E7%A7%8D%E7%BD%91%E7%BB%9C/Docker%E7%9A%84%E4%BA%94%E7%A7%8D%E7%BD%91%E7%BB%9C/image-202410285121318.png)
安装docker后先自带一张docker0网卡
![image-2024103043687.png|475](00_sync/00linux/Docker%E7%9A%84%E4%BA%94%E7%A7%8D%E7%BD%91%E7%BB%9C/Docker%E7%9A%84%E4%BA%94%E7%A7%8D%E7%BD%91%E7%BB%9C/image-2024103043687.png)
## 桥接brige【默认】
【但这个按我理解就是nat】
增加一张网卡情况→veth开头
而我们进入容器内部或者inspect可以看到容器的ip地址且容器网络名字为eth0@if12名字跟宿主机网络名位veth8942279@if11
![image-20241030033667.png|500](00_sync/00linux/Docker%E7%9A%84%E4%BA%94%E7%A7%8D%E7%BD%91%E7%BB%9C/Docker%E7%9A%84%E4%BA%94%E7%A7%8D%E7%BD%91%E7%BB%9C/image-20241030033667.png)
增加两张网卡情况→veth开头以及br-开头 可以看到network ls多了一张 且容器是这张br的ip段的
![image-202410302848432.png|350](00_sync/00linux/Docker%E7%9A%84%E4%BA%94%E7%A7%8D%E7%BD%91%E7%BB%9C/Docker%E7%9A%84%E4%BA%94%E7%A7%8D%E7%BD%91%E7%BB%9C/image-202410302848432.png)
![image-202410302813163.png|325](00_sync/00linux/Docker%E7%9A%84%E4%BA%94%E7%A7%8D%E7%BD%91%E7%BB%9C/Docker%E7%9A%84%E4%BA%94%E7%A7%8D%E7%BD%91%E7%BB%9C/image-202410302813163.png)

## host网络 【推荐】
共享宿主机的网络空间，网络性能最高 但是安全性能可能要差一点
```
docker run -it ——network=host  ——name=可选起容器名字  镜像
```
示例
```
network_mode: host  # 使用宿主机网络
```

```
version: '3.8'

services:
  jellyfin:
    image: jellyfin/jellyfin
    container_name: jellyfin
    network_mode: host  # 使用主机网络模式
#    networks:
#      - docker1
#    ports:  # 映射端口
#      - "8096:8096"
#      - "8920:8920"
    volumes:  # 挂载卷
      - /home/0000/docker/jellyfin/config:/config
      - /home/xyblue_smb/jellyfin/media:/media
    environment:  # 设置环境变量
      - PUID=1000
      - PGID=1000
    restart: unless-stopped  # 重启策略

# 定义或引用网络
#networks:
#  docker1:
#    external: true # 指定使用外部已存在的 docker1 网络 避免重复创建网络
# 定义卷
volumes:
  # 定义一个名为alist_volumes的卷，但是在这个例子中并没有实际使用
  jellyfin_volumes:
```
## none网络
只有本地回环，没有网络模式，不能上网
在host的基础上将
docker-compose
```
    network_mode: host  # 使用主机网络模式
    改为
    network_mode: none  # 使用主机网络模式
```
## custom network 自定义网络
用户自定义网络 各个容器之间可以基于容器名称进行通讯
```
docker network create --subnet=192.168.4.0/24 docker1
```
然后会生成一个192.168.4.0网段的网卡，docker network ls名字为docker1 但是ip a里面就是个br网桥   的跟docker0平起平坐
## container网络 共享容器网络
共享其它容器网络，在k8s中pod用的多
首先inspect 看看要被共享网络的连接 然后断开他
![image-20241030548888.png|550](00_sync/00linux/Docker%E7%9A%84%E4%BA%94%E7%A7%8D%E7%BD%91%E7%BB%9C/Docker%E7%9A%84%E4%BA%94%E7%A7%8D%E7%BD%91%E7%BB%9C/image-20241030548888.png)
```
docker network connect docker1网络名 xunlei容器名&ID
```
# 新的 [还没写完，多网段， 加入网络]
![image-202410314418446.png](00_sync/00linux/Docker%E7%9A%84%E4%BA%94%E7%A7%8D%E7%BD%91%E7%BB%9C/Docker%E7%9A%84%E4%BA%94%E7%A7%8D%E7%BD%91%E7%BB%9C/image-202410314418446.png)

# 清理删除
```
docker inspect 12be036c4393
docker inspect 12be036c4393 |grep -A 100 Containers
```
检查此字段
![image-202410303130945.png|425](00_sync/00linux/Docker%E7%9A%84%E4%BA%94%E7%A7%8D%E7%BD%91%E7%BB%9C/Docker%E7%9A%84%E4%BA%94%E7%A7%8D%E7%BD%91%E7%BB%9C/image-202410303130945.png)


```
docker network ls
docker network rm 网卡
```

```
docker container prune
docker image prune

docker network prune

#- 并不是所有的容器都需要使用卷。有些容器可能仅使用内存中的数据或不需要持久化的存储。
- 卷通常是用来持久化容器内的数据，例如数据库数据、配置文件、下载文件等。
docker volume prune  


docker system prune
```
解压
![image-20241030582696.png|475](00_sync/00linux/Docker%E7%9A%84%E4%BA%94%E7%A7%8D%E7%BD%91%E7%BB%9C/Docker%E7%9A%84%E4%BA%94%E7%A7%8D%E7%BD%91%E7%BB%9C/image-20241030582696.png)
# 网络模版
## host网络
切记早没了端口映射了
```
version: '3.8'

services:
  qbittorrent:
    image: helloz/qbittorrent
    container_name: qbittorrent
    network_mode: host  # 使用宿主机网络
    volumes:
      -  /home/0000/nas_tv/qbittorrent/config:/etc/qBittorrent
      -  /home/xyblue_smb/jellyfin/media/qBittorrent_downloads:/downloads
    restart: unless-stopped
volumes:
  qbittorrent_volumes:
```
## bridge网络
```
version: '3.3'

services:
  alist:
    image: 'xhofe/alist:latest-ffmpeg'
    container_name: alist
    networks:
      - docker1  # 指定使用 docker1 网络
    volumes:
      - '/home/0000/docker/alist/data:/opt/alist/data'
      - '/home/0000/docker/alist/本地:/本地'
    ports:
      - '5244:5244'
    environment:
      - PUID=0
      - PGID=0
      - UMASK=022
    restart: unless-stopped

networks:
  docker1:
    external: true  # 指定使用外部已存在的 docker1 网络 避免重复创建网络
volumes:
  alist_volumes:
```

## 自定义网络
```
version: '3.8'  # 使用 Docker Compose 文件格式版本 3.8

services:
  xunlei:
    image: cnk3x/xunlei
    container_name: xunlei
    privileged: true  # 启用特权模式
    volumes:
      - /home/0000/nas_tv/xunlei/data:/xunlei/data  # 挂载数据目录
      - /home/xyblue_smb/jellyfin/media/xunlei_downloads:/xunlei/downloads  # 挂载下载目录
    --network 
    ports:
      - "2345:2345"  # 映射端口
    restart: unless-stopped  # 除非手动停止，否则总是重启容器
volumes:
  xunlei_volumes:
```
# 究极模板
```
version: '3.8'

services:
  jellyfin:
#=====================================================镜像名字和容器名和主机名（里面那个）
    image: jellyfin/jellyfin
    container_name: jellyfin
    hostname: jellyfin
#=====================================================挂载卷的位置
    volumes:  # 挂载卷
      - /home/0000/docker/jellyfin/config:/config
      - /home/xyblue_smb/jellyfin/media:/media

#=====================================================设置环境变量
    environment:  # 设置环境变量 部分情况可能需要改为0
      - PUID=1000
      - PGID=1000
#=====================================================重启的策略，还有no   on-failure[:max-retry]      always
    restart: unless-stopped  # 重启策略


#=====================================================主机模式
    network_mode: host  # 使用主机网络模式 主机模式不能映射端口

#=====================================================桥接模式 其实nat更为贴切 到自定义网络docker1

#    networks:
#      - docker1
#=====================================================端口映射，如果不桥接到自定义网络，有的默认到docker0 有的再新建个br再进行桥接,所以可以直接写端口

#    ports:  # 映射端口
#      - "8096:8096"
#      - "8920:8920"


#=====================================================    定义或引用网络 下面三行判断是否存在docker1网络的 也就用自定义网络要解除这个注释，防止写错又生成个网络
#networks:
#  docker1:
#    external: true # 指定使用外部已存在的 docker1 网络 避免重复创建网络

#=====================================================  创建新卷名，没啥意义
#volumes:
#  /home/0000/docker/jellyfin/config: 
#  /home/xyblue_smb/jellyfin/media:


#==============================特权模式
#    privileged: true  # 启用特权模式
```

# 补充
## 附件
![image-202410312154327.png](00_sync/00linux/Docker%E7%9A%84%E4%BA%94%E7%A7%8D%E7%BD%91%E7%BB%9C/Docker%E7%9A%84%E4%BA%94%E7%A7%8D%E7%BD%91%E7%BB%9C/image-202410312154327.png)
## host网络中找不到开放端口怎么办
使用 lsof -i 命令 lsof -i :端口   lsof -i |grep alist
需要注意 command 截取不全，比如qbittorrent只有qbittorre
![image-20241031424170.png](00_sync/00linux/Docker%E7%9A%84%E4%BA%94%E7%A7%8D%E7%BD%91%E7%BB%9C/Docker%E7%9A%84%E4%BA%94%E7%A7%8D%E7%BD%91%E7%BB%9C/image-20241031424170.png)
名字应该是和这个有关系
![image-202410314145447.png](00_sync/00linux/Docker%E7%9A%84%E4%BA%94%E7%A7%8D%E7%BD%91%E7%BB%9C/Docker%E7%9A%84%E4%BA%94%E7%A7%8D%E7%BD%91%E7%BB%9C/image-202410314145447.png)