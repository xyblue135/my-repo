# 网络 DNS 镜像源
# 科学办法解决网络
mkdir -p /etc/systemd/system/docker.service.d
nano /etc/systemd/system/docker.service.d/http-proxy.conf
```
[Service]
Environment="HTTP_PROXY=http://192.168.3.100:7890"
Environment="HTTPS_PROXY=http://192.168.3.100:7890"
```
如果代理方式带认证
```
Environment="HTTP_PROXY=http://username:password@192.168.3.100:7890"
Environment="HTTPS_PROXY=http://username:password@192.168.3.100:7890"
```
可选
```
Environment="NO_PROXY=localhost,127.0.0.1"
```
然后重启一下
```
sudo systemctl daemon-reload
sudo systemctl restart docker
```
查看环境
```
sudo systemctl show docker | grep "Environment"
```
# 镜像源和DNS
我就直接放一个官方源
nano /etc/docker/daemon.json 
```
{
  "registry-mirrors": ["https://registry.docker-cn.com"],
  "dns": ["8.8.8.8", "8.8.4.4"]
}
```

```
sudo systemctl daemon-reload
sudo systemctl restart docker
```
![image-20241114136194.png](00_sync/00%E7%BD%91%E7%BB%9C/Docker%E6%97%A0%E6%B3%95pull%E8%A7%A3%E5%86%B3/Docker%E6%97%A0%E6%B3%95pull%E8%A7%A3%E5%86%B3/image-20241114136194.png)
![image-2024111495883.png](00_sync/00%E7%BD%91%E7%BB%9C/Docker%E6%97%A0%E6%B3%95pull%E8%A7%A3%E5%86%B3/Docker%E6%97%A0%E6%B3%95pull%E8%A7%A3%E5%86%B3/image-2024111495883.png)
