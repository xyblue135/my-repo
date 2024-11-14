### **部署zabbix组件**

zabbix支持mysql/postgresql两种数据库，本示例使用支持mysql的zabbix版本。
1. 安装数据库
下载镜像，zabbix 6.x版本要求使用mysql 8.0。
```javascript
$ docker pull mysql:8.0
```
创建存储卷，用于持久化mysql数据。
```javascript
$ docker volume create -d local  mysql_data #存放mysql数据
$ docker volume create -d local  mysql_logs #存放mysql日志
$ docker volume create -d local  mysql_conf #存放mysql配置文件 
```
注释：存储卷默认存储位置路径为：/var/lib/docker/volume/${volume_name}。
启动容器
```javascript
$ docker run --name mysql-server -t \
   -v mysql_data:/var/lib/mysql \
      -v mysql_logs:/var/log/mysql \
      -v mysql_conf:/etc/mysql \
      -e MYSQL_DATABASE="zabbix" \
      -e MYSQL_USER="zabbix" \
      -e MYSQL_PASSWORD="zabbix_pwd" \
      -e MYSQL_ROOT_PASSWORD="123456" \
      --restart=unless-stopped \
      -d mysql:8.0 \
      --character-set-server=utf8 --collation-server=utf8_bin \
      --default-authentication-plugin=mysql_native_password
```
2. 安装zabbix-java-gateway
下载镜像
```javascript
$ docker pull zabbix/zabbix-java-gateway:alpine-6.2-latest
```
启动容器
```javascript
$ docker run --name zabbix-java-gateway -t \
   --restart=unless-stopped \
      -d zabbix/zabbix-java-gateway:alpine-6.2-latest
```
3. 安装zabbix-server
下载镜像
```javascript
$ docker pull zabbix/zabbix-server-mysql:6.2-alpine-latest
```
创建存储卷，用于存储zabbix配置文件。
```javascript
$ docker volume create -d local  zabbix_server
```
启动server容器，开放10051/TCP端口，用于接收监控数据。添加--link参数，实现mysql和java-gateway容器间的互相通信。
```javascript
$ docker run --name zabbix-server-mysql -t \
    -v zabbix_server:/etc/zabbix \
      -e DB_SERVER_HOST="mysql-server" \
      -e MYSQL_DATABASE="zabbix" \
      -e MYSQL_USER="zabbix" \
      -e MYSQL_PASSWORD="zabbix_pwd" \
      -e MYSQL_ROOT_PASSWORD="123456" \
      -e ZBX_JAVAGATEWAY="zabbix-java-gateway" \
      --link mysql-server:mysql \
      --link zabbix-java-gateway:zabbix-java-gateway \
      --restart=unless-stopped \
      -p 10051:10051 \
      -d zabbix/zabbix-server-mysql:alpine-6.2-latest
```
注释：此方式适合所有容器部署在同一台主机上，如果是分开部署，则在前面的步骤需要开放相关端口，并通过局域网进行连接。
4. 安装Zabbix Web 界面
```javascript
$ docker pull zabbix/zabbix-web-nginx-mysql:alpine-6.2-latest
```
启动web容器
```
sudo docker run --name zabbix-web-nginx-mysql -t \
  -e PHP_TZ="Asia/Shanghai" \
  -e ZBX_SERVER_HOST="zabbix-server-mysql" \
  -e DB_SERVER_HOST="mysql-server" \
  -e MYSQL_DATABASE="zabbix" \
  -e MYSQL_USER="zabbix" \
  -e MYSQL_PASSWORD="zabbix_pwd" \
  -e MYSQL_ROOT_PASSWORD="123456" \
  --link mysql-server:mysql \
  --link zabbix-server-mysql:zabbix-server \
  -p 80:8080 \
  --restart unless-stopped \
  -d zabbix/zabbix-web-nginx-mysql:alpine-6.2-latest
```
5. 登录zabbix
部署完成后，打开浏览器访问主机地址，即可访问zabbix。
登录账号：Admin
密码：zabbix
![image-20242215752684.png](3可以放入网站的笔记/Linux上使用Docker配置zabbix/Linux上使用Docker配置zabbix/image-20242215752684.png)