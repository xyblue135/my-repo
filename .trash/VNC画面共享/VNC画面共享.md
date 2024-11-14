VNC (Virtual Network Console)是**虚拟网络控制台的缩写**。 它是一款优秀的远程控制工具软件，由著名的AT&T 的欧洲研究实验室开发的。 VNC 是在基于UNIX 和Linux 操作系统的免费的开源软件，远程控制能力强大，高效实用，其性能可以和Windows 和MAC 中的任何远程控制软件媲美。
最重要的是跨平台~ 其它的我觉得一般
# 安装服务端
```
sudo apt update
sudo apt install tightvncserver
或者
sudo apt install tigervnc-standalone-server
sudo apt install realvnc-vnc-server
```
# 启动服务端
```
对于TightVNC：
vncserver :1
```

```
对于TigerVNC：
vncserver -depth 24 -geometry 1280x800 :1
```

```
对于RealVNC：  
vncserver -geometry 1280x800 :1
```

# 停止服务端
```
vncserver -kill :1
vncserver -kill :all

```
# 删除服务端
```
vncserver -kill :1
vncserver -kill :all
rm /tmp/.X1-lock
```
## 额外方法
```
ps aux | grep vncserver
```

# 查看配置
```
vncserver -list
vncserver
```
![image-202410271929126.png](00_sync/00linux/VNC%E7%94%BB%E9%9D%A2%E5%85%B1%E4%BA%AB/VNC%E7%94%BB%E9%9D%A2%E5%85%B1%E4%BA%AB/image-202410271929126.png)
# 查看是否拥有图像化
```
systemctl get-default
```
![image-202410272331406.png](00_sync/00linux/VNC%E7%94%BB%E9%9D%A2%E5%85%B1%E4%BA%AB/VNC%E7%94%BB%E9%9D%A2%E5%85%B1%E4%BA%AB/image-202410272331406.png)
# 卸载vnc
```
sudo apt remove 包名1
```