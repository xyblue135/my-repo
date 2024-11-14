# LINUX
## 重要
在无法安装任何东西的时候一定要注意下网卡的dns等配置，这是很重要的。
## 临时代理
```
export http_proxy="http://192.168.3.100:7890"
export https_proxy="http://192.168.3.100:7890"

echo $http_proxy
echo $https_proxy

curl ifconfig.me

```
## 简单代理
sudo nano /etc/environment
```
http_proxy="http://192.168.3.101:7890/"
https_proxy="http://192.168.3.101:7890/"
no_proxy="localhost,127.0.0.1,::1"
```
代理端口是可以同时使用的
![image-20249272243325.png](00_sync/00linux/%E9%85%8D%E7%BD%AE%E4%BB%A3%E7%90%86/%E9%85%8D%E7%BD%AE%E4%BB%A3%E7%90%86/image-20249272243325.png)

## 配置clash
## clash客户端
Clash Verge Linux 64位.deb（适用于 Debian/Ubuntu），[==点击下载==](https://github.com/clash-verge-rev/clash-verge-rev/releases/download/v1.7.7/clash-verge_1.7.7_amd64.deb)**  
Clash Verge Linux 64位.rpm（适用于 FedorapenSUS，[==点击下载==](https://github.com/clash-verge-rev/clash-verge-rev/releases/download/v1.7.7/clash-verge-1.7.7-1.x86_64.rpm)**
一般来说这一个命令就可以去看看客户端有没有了
```
sudo dpkg -i clash-verge_1.7.7_amd64.deb 
```
![image-20241025108338.png|450](00_sync/00linux/%E9%85%8D%E7%BD%AE%E4%BB%A3%E7%90%86/%E9%85%8D%E7%BD%AE%E7%AE%80%E5%8D%95%E4%BB%A3%E7%90%86_%E5%92%8Cclash/image-20241025108338.png)
如果无法正常安装 Ubuntu 24.04 需要额外安装 [==libwebkit2gtk-4.0-37==](https://github.com/clash-verge-rev/clash-verge-rev/releases/download/dependencies/libwebkit2gtk-4.0-37_2.43.3-1_amd64.deb) 和 [==libjavascriptcoregtk==](https://github.com/clash-verge-rev/clash-verge-rev/releases/download/dependencies/libjavascriptcoregtk-4.0-18_2.43.3-1_amd64.deb) 依赖，根据架构下载对应版本并安装。其他 Debian 系操作系统类似。
```不要进行
sudo apt install ./libwebkit2gtk-4.0-37_2.43.3-1_amd64.deb ./libjavascriptcoregtk-4.0-18_2.43.3-1_amd64.deb
```
安装gdebi【可以再本地安装依赖包了】
```
sudo apt install gdebi
```
![image-20241018189376.png|425](00_sync/00linux/%E9%85%8D%E7%BD%AE%E4%BB%A3%E7%90%86/%E9%85%8D%E7%BD%AE%E7%AE%80%E5%8D%95%E4%BB%A3%E7%90%86_%E5%92%8Cclash/image-20241018189376.png)
同样方法安装clash
![image-202410182033754.png|91](00_sync/00linux/%E9%85%8D%E7%BD%AE%E4%BB%A3%E7%90%86/%E9%85%8D%E7%BD%AE%E7%AE%80%E5%8D%95%E4%BB%A3%E7%90%86_%E5%92%8Cclash/image-202410182033754.png)
## Docker容器
https://hub.docker.com/r/haishanh/yacd
https://hub.docker.com/r/dreamacro/clash
配置文件请自己探索，注意：配置文件external-controller: '127.0.0.1:9090' 必须修改为0000不然进不来yacd 
小猫默认有三个端口http8090 socket8091 网页api接口9090
```
docker run -d \
  --name clash \
  --network host \
  -v /home/0000/docker/clash/config/config.yaml:/root/.config/clash/config.yaml \
  dreamacro/clash
```

```
version: '3.8'

services:
  clash:
    image: dreamacro/clash
    container_name: clash
    network_mode: "host"
    volumes:
      - /home/0000/docker/clash/config/config.yaml:/root/.config/clash/config.yaml
    restart: unless-stopped
```
这一步就已经可以使用了，只是没有web页面而已。
部署web
```
docker run -d -p 1234:80 --restart unless-stopped haishanh/yacd
```

```
version: '3.8'

services:
  yacd:
    image: haishanh/yacd
    ports:
      - "1234:80"
    restart: unless-stopped
```
不要填127
![image-202411153234284.png](00_sync/00linux/%E9%85%8D%E7%BD%AE%E4%BB%A3%E7%90%86/%E9%85%8D%E7%BD%AE%E7%AE%80%E5%8D%95%E4%BB%A3%E7%90%86_%E5%92%8Cclash/image-202411153234284.png)
![image-20241141846842.png|425](00_sync/00linux/%E9%85%8D%E7%BD%AE%E4%BB%A3%E7%90%86/%E9%85%8D%E7%BD%AE%E7%AE%80%E5%8D%95%E4%BB%A3%E7%90%86_%E5%92%8Cclash/image-20241141846842.png)

![image-20241141044913.png|500](00_sync/00linux/%E9%85%8D%E7%BD%AE%E4%BB%A3%E7%90%86/%E9%85%8D%E7%BD%AE%E7%AE%80%E5%8D%95%E4%BB%A3%E7%90%86_%E5%92%8Cclash/image-20241141044913.png)
## 自建订阅转换
https://github.com/stilleshan/subweb
https://github.com/stilleshan/subconverter
一个负责前端，夜歌负责后端
```
docker run  -d --name=subconverter --restart=always -p 25500:25500 stilleshan/subconverter

docker run -d --name subweb --restart always \
  -p 18080:80 \
  stilleshan/subweb
```
示例地址
http://192.168.3.212:18080/
![image-20241143354901.png|375](00_sync/00linux/%E9%85%8D%E7%BD%AE%E4%BB%A3%E7%90%86/%E9%85%8D%E7%BD%AE%E7%AE%80%E5%8D%95%E4%BB%A3%E7%90%86_%E5%92%8Cclash/image-20241143354901.png)
## 总结
配合临时变量用我觉得是比较舒服的
ping没办发检测 代理不转发icmp报文 curl我觉得也一般 wget比较适合
![image-20241143141941.png](00_sync/00linux/%E9%85%8D%E7%BD%AE%E4%BB%A3%E7%90%86/%E9%85%8D%E7%BD%AE%E7%AE%80%E5%8D%95%E4%BB%A3%E7%90%86_%E5%92%8Cclash/image-20241143141941.png)

# WIN

简单的按钮代理和软件代理，就不说了，主要是针对shell的代理，不然即使用了小猫等什么的软件仍旧走的不是代理
## powershell
```
$env:https_proxy = "127.0.0.1:7890"
$env:HTTPS_PROXY = "127.0.0.1:7890"
```
## cmd
```
set http_proxy=127.0.0.1:8090
set https_proxy=127.0.0.1:8090
```