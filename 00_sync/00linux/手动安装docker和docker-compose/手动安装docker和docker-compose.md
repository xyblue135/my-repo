当docker版本有问题或者源有问题的话，手动安装永远是最好的我觉得。
# 安装docker
https://download.docker.com/linux/static/stable/x86_64/
ce是社区版本
vim /opt/docker/docker.service
```
[Unit]
Description=Docker Application Container Engine
Documentation=https://docs.docker.com
After=network-online.target firewalld.service
Wants=network-online.target

[Service]
Type=notify
# the default is not to use systemd for cgroups because the delegate issues still
# exists and systemd currently does not support the cgroup feature set required
# for containers run by docker
ExecStart=/usr/bin/dockerd
ExecReload=/bin/kill -s HUP $MAINPID
# Having non-zero Limit*s causes performance problems due to accounting overhead
# in the kernel. We recommend using cgroups to do container-local accounting.
LimitNOFILE=infinity
LimitNPROC=infinity
LimitCORE=infinity
# Uncomment TasksMax if your systemd version supports it.
# Only systemd 226 and above support this version.
#TasksMax=infinity
TimeoutStartSec=0
# set delegate yes so that systemd does not reset the cgroups of docker containers
Delegate=yes
# kill only the docker process, not all processes in the cgroup
KillMode=process
# restart the docker process if it exits prematurely
Restart=on-failure
StartLimitBurst=3
StartLimitInterval=60s

[Install]
WantedBy=multi-user.target
```

vim /opt/docker/install.sh

```
#!/bin/sh
echo '解压tar包...'
tar -xvf $1
echo '将docker目录移到/usr/bin目录下...'
cp docker/* /usr/bin/
echo '将docker.service 移到/etc/systemd/system/ 目录...'
cp docker.service /etc/systemd/system/
echo '添加文件权限...'
chmod +x /etc/systemd/system/docker.service
echo '重新加载配置文件...'
systemctl daemon-reload
echo '启动docker...'
systemctl start docker
echo '设置开机自启...'
systemctl enable docker.service
echo 'docker安装成功...'
docker -v
```

vim /opt/docker/uninstall.sh
```
#!/bin/sh
echo '删除docker.service...'
rm -f /etc/systemd/system/docker.service
echo '删除docker文件...'
rm -rf /usr/bin/docker*
echo '重新加载配置文件'
systemctl daemon-reload
echo '卸载成功...'
```

# 如果有其他相关文件，也请一并删除
rm -rf /opt/docker/docker

目录下有这些文件
![image-202411123648458.png|400](00_sync/00linux/手动安装docker和docker-compose/手动安装docker和docker-compose/image-202411123648458.png)
sh install.sh docker-对应版本
![image-20241112383134.png|350](00_sync/00linux/手动安装docker和docker-compose/手动安装docker和docker-compose/image-20241112383134.png)
到这里就ok了，简单的很

删除的话
systemctl stop docker
systemctl disable docker.service
rm -f /etc/systemd/system/docker.service
systemctl daemon-reload
ls /usr/bin | grep docker
rm -f /usr/bin/docker
![image-202411142946293.png|300](00_sync/00linux/%E6%89%8B%E5%8A%A8%E5%AE%89%E8%A3%85docker%E5%92%8Cdocker-compose/%E6%89%8B%E5%8A%A8%E5%AE%89%E8%A3%85docker%E5%92%8Cdocker-compose/image-202411142946293.png)


apt remove docker \
					docker-client \
					docker-client-latest \
					docker-common \
					docker-latest \
					docker-latest-logrotate \
					docker-engine \
# 安装compose
https://github.com/docker/compose/releases

直接放到一个地方就可以了
![image-202411122536473.png|400](00_sync/00linux/手动安装docker和docker-compose/手动安装docker和docker-compose/image-202411122536473.png)
![image-202411123916293.png](00_sync/00linux/手动安装docker和docker-compose/手动安装docker和docker-compose/image-202411123916293.png)
# 问题
需要注意手动安装，那也是要依赖的,比如这些前置依赖，不然还是各种报错，所以还是得建议联网，然后卸载下，也能升级升级版本。
![image-20241114655737.png](00_sync/00linux/%E6%89%8B%E5%8A%A8%E5%AE%89%E8%A3%85docker%E5%92%8Cdocker-compose/%E6%89%8B%E5%8A%A8%E5%AE%89%E8%A3%85docker%E5%92%8Cdocker-compose/image-20241114655737.png)