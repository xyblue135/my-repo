# 远程服务

通过此设置可以将路由器的端口暴露在公网服务器中进行远程操作或配置。

## 客户端frp配置

这边我服务端配置好了已经，详细请参考此博客内网穿透Minecraft篇章服务端的配置。

首先我们将我们的frp移动到我们的linux系统中，↓下载地址。

```

https://github.com/fatedier/frp/releases

```

这边可以看到我空间不足了，详细解决方案请参考此网页文章参考如何给路由器扩容。

![Pasted-image-20231122225832.png](00_sync/00网络/远程穿透DDNS开机自启Docker/Frp,DDNS,Docker部署,Overlay区域划分/Pasted-image-20231122225832.png)

文件传输好后，如果没解压记得解压命令

```

tar -xf frp_0.33.0_linux_amd64.tar.gz

```

给执行权限

```

chmod +x /opt/frp_0.33.0_linux_arm64/frpc

```

![Pasted-image-20231123020408.png](00_sync/00网络/远程穿透DDNS开机自启Docker/Frp,DDNS,Docker部署,Overlay区域划分/Pasted-image-20231123020408.png)

```

ls -l

```

查看权限,可以看到frpc变绿了，就可以执行了。

![Pasted-image-20231123020434.png](00_sync/00网络/远程穿透DDNS开机自启Docker/Frp,DDNS,Docker部署,Overlay区域划分/Pasted-image-20231123020434.png)

随后就可以打开我们配置好的frp服务了（如果不了解frp可以查看本博客内网穿透联机篇）

![Pasted-image-20231123020456.png](00_sync/00网络/远程穿透DDNS开机自启Docker/Frp,DDNS,Docker部署,Overlay区域划分/Pasted-image-20231123020456.png)

# 挂起状态

```

nohup frpc &

```

或者

```

tmux（图示）来挂起,sys加入进程也可以。

```

![41f92928773f0d9a4993102f008c1af.png](00_sync/00网络/远程穿透DDNS开机自启Docker/Frp,DDNS,Docker部署,Overlay区域划分/41f92928773f0d9a4993102f008c1af.png)

![Pasted-image-20231123164041.png](00_sync/00网络/远程穿透DDNS开机自启Docker/Frp,DDNS,Docker部署,Overlay区域划分/Pasted-image-20231123164041.png)

可以看到，可以通过IP来远程操控OpenWrt了，这里需要注意，密码一定要改为强密码！！！

![Pasted-image-20231123164124.png](00_sync/00网络/远程穿透DDNS开机自启Docker/Frp,DDNS,Docker部署,Overlay区域划分/Pasted-image-20231123164124.png)

# 开机自启动

首先例如frp的启动我们需要在对应目录下输入frpc才可以运行，或者nohup和tmux等来实现一直监听，但开机即会消失。

以下是一个示例，你可以创建一个名为 frp.service 的服务单元文件，然后将其放置在 systemd 服务目录下（通常是 /etc/systemd/system/），具体步骤如下：

  

## 创建服务单元文件

使用 root 或具有管理员权限的用户创建一个新文件，比如 frp.service。你可以使用 nano 或者其它文本编辑器来创建并编辑这个文件：

```

sudo nano /etc/systemd/system/frp.service

```

编辑服务单元文件： 在编辑器中添加以下内容，这是一个示例 frp 服务单元文件：

```

[Unit]

Description=Frp Client Service

After=network.target

  

[Service]

Type=simple

ExecStart=/path/to/your/frp/binary -c /path/to/your/frpc.ini

  

[Install]

WantedBy=multi-user.target

```

在 ExecStart= 行中，将 /path/to/your/frp/binary 替换为你 frp 客户端的二进制文件路径，将 /path/to/your/frpc.ini 替换为你的 frp 客户端配置文件路径。

根据你的实际情况修改服务描述和路径信息。

保存并关闭文件： 在 nano 编辑器中，按下 Ctrl + X，然后输入 Y 来确认保存更改，最后按下 Enter。

启用并启动服务： 一旦你编辑好了 frp.service 文件，你需要告诉 systemd 启用并启动这个服务：

```

sudo systemctl enable frp.service

sudo systemctl start frp.service

```

第一行命令 sudo systemctl enable frp.service 将启用这个服务，使其在系统启动时自动启动。第二行命令 sudo systemctl start frp.service 将立即启动 frp 服务。

  

验证服务状态： 使用以下命令来验证服务是否已经成功启动：

```

sudo systemctl status frp.service

```

如果服务正在运行，你应该会看到有关服务状态的相关信息。

  

这样，frp 客户端就应该被配置为在系统启动时自动运行。如果需要修改服务或配置，请记得在修改后重新加载 systemd 并重启服务，使用命令 sudo systemctl daemon-reload 和 sudo systemctl restart frp.service。

# 扩容Docker分区以及overlay分区

  

![Pasted-image-20231123005748.png](00_sync/00网络/远程穿透DDNS开机自启Docker/Frp,DDNS,Docker部署,Overlay区域划分/Pasted-image-20231123005748.png)

```

lsblk

```

指令可以查看我们的分区情况我们可以看到sda为我们的硬盘存储，sda1为boot，可以理解为引导，sda2为固件本身的大小，且还有一部分剩余空间用于读写。而loop0作为循环设备，同时也是用户的可写空间被挂载到了overlay。反映到图示为这样

![Pasted-image-20231123010304.png](00_sync/00网络/远程穿透DDNS开机自启Docker/Frp,DDNS,Docker部署,Overlay区域划分/Pasted-image-20231123010304.png)

注意：Upper Layer为read/write，Lower Layer为read only

所以真真正正能使用的只有FreeSpace这一点空间,上一层作为逻辑层阻止了我们对于kernel和Firmware的读写，这样就允许我们有重置的救命稻草。就一后悔药。

需要注意，![Pasted-image-20231123011406.png](00_sync/00网络/远程穿透DDNS开机自启Docker/Frp,DDNS,Docker部署,Overlay区域划分/Pasted-image-20231123011406.png)刷的包时squash格式才可以，要是ext4将无法重置系统。

然后我们扩容的话，就应该让Firmware不指向原来的sda2分区中的剩余部分，而是新的sda3的分区中来达到扩容的目的。

![Pasted-image-20231123011723.png](00_sync/00网络/远程穿透DDNS开机自启Docker/Frp,DDNS,Docker部署,Overlay区域划分/Pasted-image-20231123011723.png)

# 方法一（只方便分区一次）

我们用ssh连接openwrt并输入（如果无，请自行安装disk组件）

```

cfdisk

```

现在我们进入了这个窗口中

![Pasted-image-20231123012027.png](00_sync/00网络/远程穿透DDNS开机自启Docker/Frp,DDNS,Docker部署,Overlay区域划分/Pasted-image-20231123012027.png)

然后选择Free space 回车

![Pasted-image-20231123012215.png](00_sync/00网络/远程穿透DDNS开机自启Docker/Frp,DDNS,Docker部署,Overlay区域划分/Pasted-image-20231123012215.png)

回车并将总大小Back掉然后新建6个G的分区（自行选择）

![Pasted-image-20231123013734.png](00_sync/00网络/远程穿透DDNS开机自启Docker/Frp,DDNS,Docker部署,Overlay区域划分/Pasted-image-20231123013734.png)

选择Write并输入yes

![Pasted-image-20231123012504.png](00_sync/00网络/远程穿透DDNS开机自启Docker/Frp,DDNS,Docker部署,Overlay区域划分/Pasted-image-20231123012504.png)

选择Quit![Pasted-image-20231123012529.png](00_sync/00网络/远程穿透DDNS开机自启Docker/Frp,DDNS,Docker部署,Overlay区域划分/Pasted-image-20231123012529.png)

同步磁盘![Pasted-image-20231123012628.png](00_sync/00网络/远程穿透DDNS开机自启Docker/Frp,DDNS,Docker部署,Overlay区域划分/Pasted-image-20231123012628.png)

格式化我们的分区，名字对应正确，我这边是sda3。（上两张图片遗留的sda4，不要考虑）

```

mkfs.ext4 /dev/sda3

```

![Pasted-image-20231130012533.png](00_sync/00网络/远程穿透DDNS开机自启Docker/Frp,DDNS,Docker部署,Overlay区域划分/Pasted-image-20231130012533.png)

挂载分区

```

mount /dev/sda3 /mnt/sda

```

ls /mnt/sda3 查看有lost+found就是挂载成功了

![Pasted-image-20231123014211.png](00_sync/00网络/远程穿透DDNS开机自启Docker/Frp,DDNS,Docker部署,Overlay区域划分/Pasted-image-20231123014211.png)

将在overlay的文件复制到sda3

```

 cp -r /overlay/* /mnt/sda3

```

![Pasted-image-20231123014447.png](00_sync/00网络/远程穿透DDNS开机自启Docker/Frp,DDNS,Docker部署,Overlay区域划分/Pasted-image-20231123014447.png)

检查是否拷贝

```

ls /mnt/sda3

```

![Pasted-image-20231123014559.png](00_sync/00网络/远程穿透DDNS开机自启Docker/Frp,DDNS,Docker部署,Overlay区域划分/Pasted-image-20231123014559.png)

![Pasted-image-20231129235554.png](00_sync/00网络/远程穿透DDNS开机自启Docker/Frp,DDNS,Docker部署,Overlay区域划分/Pasted-image-20231129235554.png)

![Pasted-image-20231123014710.png](00_sync/00网络/远程穿透DDNS开机自启Docker/Frp,DDNS,Docker部署,Overlay区域划分/Pasted-image-20231123014710.png)

好了大功告成，重启即可（改逻辑指向）

```

reboot

```

验证：

![Pasted-image-20231123140541.png](00_sync/00网络/远程穿透DDNS开机自启Docker/Frp,DDNS,Docker部署,Overlay区域划分/Pasted-image-20231123140541.png)

![Pasted-image-20231123152659.png](00_sync/00网络/远程穿透DDNS开机自启Docker/Frp,DDNS,Docker部署,Overlay区域划分/Pasted-image-20231123152659.png)

![Pasted-image-20231123152715.png](00_sync/00网络/远程穿透DDNS开机自启Docker/Frp,DDNS,Docker部署,Overlay区域划分/Pasted-image-20231123152715.png)

这样docker也就变相增加容量了

### 方法一注意事项

如果想在sda3的基础上在进行扩容，往往是不可行的（sda3扩容简单，但我想说的是overlay的扩容,），你需要备份这个分区的所有重要数据。overlay的扩容需要卸载掉原来的sda3分区才可以，也就是说数据会丢失，不建议（对于学习来说可以尝试一番）

重点:需要搞清楚linux的文件划分机制，overlay分区会挂载到opt中，而不会挂载到mnt中，所以Docker挂载到mnt是比较好的情况。

### 清除docker的数据

通常来说，如果空间不足，一般是docker引起的，或者你所存放的文件。

docker清理命令

```

docker system prune -a

```

谨慎执行，此命令有以下效果.

1. 删除未运行的容器（Stopped containers）。

2. 删除所有未被使用的网络（Unused networks）。

3. 删除所有未被使用的镜像（Dangling images）。

4. 删除所有未被使用的存储卷（Unused volumes）。

## 方法二，使用istore扩容。

要是实在搞定不了，就换个简单方便的固件好啦，istore本身给2GB的overlay区域，是完全足够的，但若要使用docker，则必须要给docker容器分出去，即给硬盘的剩余空间挂载到mnt区域（`nt`分区通常用于挂载（mount）其他文件系统。它是Linux和类Unix操作系统中的一个标准目录，用于临时挂载其他设备或文件系统。）

![Snipaste_2023-11-30_02-41-32-1.png](00_sync/00网络/远程穿透DDNS开机自启Docker/Frp,DDNS,Docker部署,Overlay区域划分/Snipaste_2023-11-30_02-41-32-1.png)

![Snipaste_2023-11-30_02-41-41.png](00_sync/00网络/远程穿透DDNS开机自启Docker/Frp,DDNS,Docker部署,Overlay区域划分/Snipaste_2023-11-30_02-41-41.png)

![Pasted-image-20231130030750.png](00_sync/00网络/远程穿透DDNS开机自启Docker/Frp,DDNS,Docker部署,Overlay区域划分/Pasted-image-20231130030750.png)