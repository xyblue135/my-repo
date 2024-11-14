
创建文件夹,给权限
```
docker run -d \
    --name palworld-server123 \
    -p 8211:8211/udp \
    -p 27015:27015/udp \
    -v /mnt/palworld:/palworld/ \
    -e PLAYERS=8 \
    -e MULTITHREADING=true \
    -e RCON_ENABLED=true \
    -e RCON_PORT=25575 \
    -e ADMIN_PASSWORD="123456789" \
    -e COMMUNITY=false \
    --restart unless-stopped \
    thijsvanloef/palworld-server-docker:latest
```
等待cmd  steam cmd  等待 如果是内网，做好内网穿透frp的服务
完成后替换存档,给权限(需要考虑ID和以前是怎么样的)`
![image-2024214453144.png](5搁置的网站上传项目/Docker部署帕鲁服务器/帕鲁/image-2024214453144.png)

![image-2024215029479.png](5搁置的网站上传项目/Docker部署帕鲁服务器/帕鲁/image-2024215029479.png)
sudo dd if=/dev/zero of=/mnt/swap123456/swapfile bs=1M count=15360
![image-2024215043536.png](5搁置的网站上传项目/Docker部署帕鲁服务器/帕鲁/image-2024215043536.png)

![image-2024215149362.png](5搁置的网站上传项目/Docker部署帕鲁服务器/帕鲁/image-2024215149362.png)

![image-2024215252620.png](5搁置的网站上传项目/Docker部署帕鲁服务器/帕鲁/image-2024215252620.png)
![image-202422814455.png](5搁置的网站上传项目/Docker部署帕鲁服务器/帕鲁/image-202422814455.png)
![image-20242292729.png](5搁置的网站上传项目/Docker部署帕鲁服务器/帕鲁/image-20242292729.png)
![image-202422726687.png](5搁置的网站上传项目/Docker部署帕鲁服务器/帕鲁/image-202422726687.png)