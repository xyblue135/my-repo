查看占用
docker system df
![Pasted-image-20231209043940.png](1自用笔记无上传/Docker命令/Docker命令/Pasted-image-20231209043940.png)
- `TYPE`: 显示 Docker 占用的不同资源类型，如镜像、容器和本地卷等。
- `TOTAL`: 显示每种类型的总数。
- `ACTIVE`: 显示当前正在使用的数量。
- `SIZE`: 显示 Docker 占用的磁盘空间大小。
- `RECLAIMABLE`: 显示可以回收的磁盘空间大小。



进入容器的操作,some-mysql为容器名词,bash为bash shell终端.
```
root@iStoreOS:~# docker exec -it some-mysql bash
```
![Pasted-image-20231210202227.png](1自用笔记无上传/Docker命令/Docker命令/Pasted-image-20231210202227.png)





