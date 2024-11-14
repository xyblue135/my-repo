我选用容器portainer，不过不建议新手就用可视化，会不熟悉每个选项的因果
需要用特权模式和持久化部署的位置为var的docker.sock 不然不会显示其它容器状态
```
version: '3.8'

services:
  portainer:
#=====================================================镜像名字和容器名和主机名（里面那个）
    image: 6053537/portainer-ce:latest
    container_name: portainer
    hostname: portainer
#=====================================================挂载卷的位置
    volumes:
      - /home/0000/docker/portainer/data:/data
      - /var/run/docker.sock:/var/run/docker.sock
            # 这里是容器环境目录映射，可以解决无法读取本地环境的问题，无需更改
#=====================================================设置环境变量
    environment:  # 设置环境变量
      - PUID=0
      - PGID=0
#=====================================================重启的策略，还有no   on-failure[:max-retry]      always
    restart: unless-stopped  # 重启策略


#=====================================================主机模式
    network_mode: host  # 使用主机网络模式 主机模式不能映射端口

#=====================================================桥接模式 其实nat更为贴切 到自定义网络docker1

#    networks:
#      - docker1
#=====================================================端口映射，如果不桥接到自定义网络，有的默认到docker0 有的再新建个br再进行桥接,所以可以直接写端口

#    ports:  # 映射端口
#      - "9003:9000"



#=====================================================    定义或引用网络 下面三行判断是否存在docker1网络的 也就用自定义网络要解除这个注释，防止写错又生成个网络
#networks:
#  docker1:
#    external: true # 指定使用外部已存在的 docker1 网络 避免重复创建网络

#=====================================================  创建新卷名，没啥意义
#volumes:
#  /home: 
#  /home:


#==============================特权模式
    privileged: true  # 启用特权模式
```
![image-2024111234148.png](00_sync/00linux/Linux下的docker可视化portainer/Linux下的docker可视化portainer/image-2024111234148.png)
![image-202411140960.png](00_sync/00linux/Linux下的docker可视化portainer/Linux下的docker可视化portainer/image-202411140960.png)