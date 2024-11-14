docker容器数据完整迁移到另一个设备
以jellyfin为例
流程:stop暂停镜像→commit更新出来一个新的容器→将容器打包为tar→复制到对应服务器→docker load挂载镜像→使用原始的docker compose→ok.
![image-202410233445639.png](00_sync/00linux/Docker容器数据完整迁移到另一个设备/Docker容器数据完整迁移到另一个设备/image-202410233445639.png)
docker stop 容器
迁移对应的docker pull的持久化存储的数据。
↓
docker commit 原容器ID 新镜像名字
docker save -o 123.tar 新镜像名字

scp到对应服务器


docker load -i 123.tar
docker tag 老名 原始镜像名字  →这样就不用去修改docker-compose了 
使用原始的docker compose
docker-compose up -d


![image-202410231418615.png](00_sync/00linux/Docker容器数据完整迁移到另一个设备/Docker容器数据完整迁移到另一个设备/image-202410231418615.png)

# 注意事项
持久化部署需要迁移数据 不是持久化部署不需要，但是相对应的，image会增加
可以看到我在容器里面放入文件再打包变大了很多
![image-202410231925777.png](00_sync/00linux/Docker容器数据完整迁移到另一个设备/Docker容器数据完整迁移到另一个设备/image-202410231925777.png)
