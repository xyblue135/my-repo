# 引入
# C10K
c10K为同时处理10k个并发连接,单线程的服务器在高并发的情况下性能会非常非常差
市场份额,像同样的还有Apache和cloudflare等
![image-20231230592468.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-20231230592468.png)
# linux下的nginx部署
安装先更新 
`sudo apt update`
`sudo apt upgrade`
![image-20231229913601.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-20231229913601.png)
# 安装nginx
`sudo apt install nginx
![image-2024132952874.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-2024132952874.png)
然后跳转到一级标题,《nginx相关》进行攻略
而如果你提示了我类似的页面,你可以安装full的版本
![image-2024118144233.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-2024118144233.png)
# Docker下的nginx部署
sudo snap install docker         # version 20.10.24, or
sudo apt  install podman-docker  # version 3.4.4+ds1-1ubuntu1.22.04.2
sudo apt  install docker.io      # version 24.0.5-0ubuntu1~22.04.1

![bf973000062e6e5c82a8a7833cd3e7f5_720.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/bf973000062e6e5c82a8a7833cd3e7f5_720.png)
`sudo docker ps `检查是否运行
`sudo docker ps -a`检查所有容器
`sudo docker start ID`运行此容器(需要ID)
![be0ca69636a6addc26d4a88e78646ff4_720.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/be0ca69636a6addc26d4a88e78646ff4_720.png)
使用docker run创建容器(将容器内的nginx的默认端口80映射到主机的8080段考)
```
sudo docker run -d -p 8080:80 --name mynginx nginx
```
![image-202411143523.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-202411143523.png)
然后就可以在本机IP或者localhost访问到nginx的欢迎界面.
![image-2024111636568.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-2024111636568.png)
使用bash控制nginx
```
sudo docker exec -it mynginx bash
```
![image-2024111823250.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-2024111823250.png)
# nginx相关
然后我们输入大写的V
nginx -V   # 可以看安装目录,编译参数,配置文件以及各种信息
![image-202411193369.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-202411193369.png)
nginx配置文件
![image-2024112039885.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-2024112039885.png)
或者可以使用
nginx -t    # 来快速定位
![image-2024112134162.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-2024112134162.png)
## 修改资源（一）
如果是直接在linux下部署的nginx，直接在文件夹中修改即可，也比较方便。
## 修改资源（二）
而如果是在docker下部署的话，可能需要花些心思在挂载和命令上
### 方法
由于Docker是不对外开放的,我们可以在bash内操作,我们也找到了这个资源，但是我们是没有编辑器可以编辑的。我们考虑挂载。详细可以查看我其它教程《Docker数据卷挂载和本地挂载》
![image-2024112446590.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-2024112446590.png)
![image-202412586409.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-202412586409.png)![image-2024125952391.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-2024125952391.png)
这个是在非docker下可以直接查看的nginx.conf
![image-2024112843182.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-2024112843182.png)
然后我们查看hub.docker的参考说明，可以看到我们要想修改静态资源的话，这个位置在docker内部的/usr/share/nginx/html文件夹中，所以我们想办法挂载出去就可以了.
## 开始挂载
我们浏览hub.docker看到
![image-2024132922947.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-2024132922947.png)
![image-2024132949824.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-2024132949824.png)
然后我们就可以更改我们的docker run了
```
sudo docker run -d -p 8080:80 --name mynginx 73246731c4b0
```
更改为
```
sudo docker run -d -p 8080:80 --name mynginx \
	-v /root/nginx/html:/usr/share/nginx/html \
	-v /root/nginx/conf/nginx.conf:/etc/nginx/nginx.conf \
	73246731c4b0
```
sudo docker run -d -p 8080:80 --name mynginx \
	-v /root/nginx/html:/usr/share/nginx/html \
	-v /root/nginx/conf:/etc/nginx/nginx.conf \
	nginx:latest  # 替换为正确的容器镜像名称

成功
![image-202413351112.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-202413351112.png)
# 监控进程(非docker)
```
ps -ef|grep nginx
```
第一行为master process,其它的为worker进程,master只有一个,worker可改(修改配置文件).
![image-2024133221364.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-2024133221364.png)
![image-202312302813460.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-202312302813460.png)
# 监控进程(docker)
而如果我的docker也开启了nginx的话，会有两个master呐在宿主机上的ps
![image-202413376343.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-202413376343.png)
# 配合node和npm
这边以nodejs的环境来演示,我们先安装npm包管理工具。`可以看到版本是比较低的,所以不要这样安装!`
```
sudo apt install npm
sudo apt install node
```
![image-2024133531394.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-2024133531394.png)
![image-20241333755.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-20241333755.png)
卸载
```
sudo apt remove npm
sudo apt remove nodejs
```
## 安装npm和nodejs和hexo
这里拿静态网站hexo来举例，但是可以看到hexo需要Nodev14 或更高版本,而我们的node是v12,所以不行.
![image-20241125622744.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-20241125622744.png)
![image-2024151154228.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-2024151154228.png)
因为有了前面的铺垫.
我们来直接到官网，我们看一下目前的LTS为20.10.0版本
![image-2024144654740.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-2024144654740.png)
选择合适的一款
![image-2024144938238.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-2024144938238.png)
![image-2024145220651.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-2024145220651.png)
```
tar -xvf node-v20.10.0-linux-x64.tar.xz
```
```
wget https://nodejs.org/dist/v14.17.0/node-v14.17.0-linux-x64.tar.xz
wegt https://nodejs.org/dist/v20.10.0/node-v20.10.0-linux-x64.tar.xz   #也可以使用wegt下载
```
默认存放为/home
![image-2024112515866.png|450](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-2024112515866.png)
将其解压
```
tar -xvf node-v13.11.0-linux-x64.tar.xz   #选择自己对应的版本
```
![image-2024141946996.png|425](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-2024141946996.png)
进入bin查看是否安装成功
```
./node
./node -v
```
![image-2024112740587.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-2024112740587.png)
添加软链
```
sudo ln -s /home/xyblue/node-v20.10.0-linux-x64/bin/npm /usr/bin/npm
sudo ln -s /home/xyblue/node-v20.10.0-linux-x64/bin/node /usr/bin/node
```
最好使用最新版本的nodejs
![image-20241122946912.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-20241122946912.png)
删除软链请使用
```
sudo rm /usr/bin/npm
sudo rm /usr/bin/node
```
## 安装hexo(一)
![image-2024152438621.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-2024152438621.png)
```
npm install hexo-cli -g
hexo init blog
cd ~
cd blog
npm install 
hexo s
```
尽可能用最新版本的nodejs,它会附带较为新的npm下载器,可以防止我们使用npm下载其它失败
![image-20241123132164.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-20241123132164.png)
## 升级npm
我们安装成功可能会提示选择升级
![image-20241123530263.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-20241123530263.png)
而我们升级完成后,软链是不会被覆盖的放心
![image-2024112375738.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-2024112375738.png)
可以看到即使在nodejs这边的文件夹下,npm也被更新了
![image-20241123816866.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-20241123816866.png)
## 安装git
```
sudo apt-get install git-core    #debian系
sudo yum install git-core
```
## 安装hexo(二)
```
npm install hexo-cli -g
```
安装好后,这边会多出文件
![image-2024112462472.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-2024112462472.png)
添加软链
```
sudo ln -s /home/xyblue/node-v20.10.0-linux-x64/bin/node /usr/bin/hexo
```
![image-20241124446706.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-20241124446706.png)
npm检查不到
![image-2024112451238.png](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-2024112451238.png)
但是是可以正常使用的

# nvm（多版本）
Node.js 的 Node Version Manager（nvm）。nvm 允许您在同一台计算机上管理多个 Node.js 版本，并且会随着 Node.js 的更新而提供最新的 npm 版本。


# 使用nginx管理SSL证书使安全访问

首先我们在服务器上下载对应文件
![image-20241184346376.png|150](00_sync/00linux/linux上的nginx以及扩展配置/2024_1_12linux上的nginx以及扩展配置/image-20241184346376.png)
我们需要


# 彻底卸载nginx
如果有两个master,就是没卸载干净
https://cloud.tencent.com/developer/article/1752589
卸载 删除 nginx
1.删除nginx，–purge包括配置文件
```javascript
sudo apt-get --purge remove nginx
```
复制
2.自动移除全部不使用的软件包
```javascript
sudo apt-get autoremove
```
复制
3.罗列出与nginx相关的软件
```javascript
dpkg --get-selections|grep nginx
```
复制
执行结果:
```javascript
stephen@stephen-OptiPlex-390:~$ dpkg --get-selections|grep nginx

nginx                       install
nginx-common                install
nginx-core                  install
```
复制
4.删除3.查询出与nginx有关的软件
```javascript
sudo apt-get --purge remove nginx
sudo apt-get --purge remove nginx-common
sudo apt-get --purge remove nginx-core
```
复制
这样就可以完全卸载掉nginx包括配置文件
###### 5.查看nginx正在运行的进程，如果有就kill掉
```javascript
ps -ef |grep nginx
```
复制
看下nginx还有没有启动,一般执行完1后，nginx还是启动着的，如下：
```javascript
stephen@stephen-OptiPlex-390:~$ ps -ef |grep nginx
root      7875  2317  0 15:02 ?        00:00:00 nginx: master process /usr/sbin/nginx
www-data  7876  7875  0 15:02 ?        00:00:00 nginx: worker process
www-data  7877  7875  0 15:02 ?        00:00:00 nginx: worker process
www-data  7878  7875  0 15:02 ?        00:00:00 nginx: worker process
www-data  7879  7875  0 15:02 ?        00:00:00 nginx: worker process
stephen   8321  3510  0 15:20 pts/0    00:00:00 grep --color=auto nginx
```
复制
###### 6.kill nginx进程

```javascript
sudo kill  -9  7875 7876 7877 7879
```
复制
###### 7.全局查找与nginx相关的文件

```javascript
sudo  find  /  -name  nginx*
```
复制
###### 8.依依删除4列出的所有文件

```javascript
sudo rm -rf file
```
复制
这样就彻底删除nginx了.
查看端口lsof -i:80

# 总结
不用docker安装nginx使用的话，配置命令教程较多，也比较好操作，但是卸载残留及其臃肿,以及即使使用nvm管理不同版本也并不是很方便。
用docker安装nginx使用的话，命令需要去官方查看使用教程，熟悉了之后还是比较好操作的，就是操作难度会比不用要大些。且更方便管理了，也不需要在意npm，nodejs和nvm这些。


# 扩展
# 10 个场景，基本会玩 Nginx 了
https://www.bilibili.com/video/BV1Ks4y117Ba/?spm_id_from=333.337.search-card.all.click&vd_source=f8caedefe0d5d4c59944bf35b5374752

