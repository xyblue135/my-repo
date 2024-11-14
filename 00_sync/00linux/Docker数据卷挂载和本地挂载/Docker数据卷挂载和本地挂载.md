# 引入
拿docker下的nginx距离，我们如果要修改内部的index文件，是很不方便的，需要sudo docker exec -it mynginx bash来修改，且vim还不能用。
# 数据卷
这个时候就我们就要引入一个桥梁,我们要做一个`双向映射`
我们就可以修改宿主机文件系统/var/lib/docker/volume的文件来间接修改容器内的文件了
![image-2024131311460.png](00_sync/00linux/Docker数据卷挂载和本地挂载/2024_1_1Docker数据卷挂载和本地挂载/image-2024131311460.png)
常用命令:
docker volume creat   #创建数据卷
docker volume ls     #查看所有数据卷
docker volume rm      #删除制定数据卷
docker volume inspect  #查看整个数据卷的详细
docker volume prune  #清楚数据卷
 所以我们先删除原有的nginx容器,跟上述一样.
![image-2024131334227.png](00_sync/00linux/Docker数据卷挂载和本地挂载/2024_1_1Docker数据卷挂载和本地挂载/image-2024131334227.png)
然后就可以创建带有数据卷的容器了
原始命令:
```
sudo docker run -d -p 8080:80 --name mynginx ID
```
带数据卷的
```
sudo docker run -d -p 8080:80 --name mynginx -v html:/usr/share/nginx/html ID
```
然后创建成功
![image-2024131350591.png](00_sync/00linux/Docker数据卷挂载和本地挂载/2024_1_1Docker数据卷挂载和本地挂载/image-2024131350591.png)
也可以查看到挂载卷的信息
![image-202413145630.png](00_sync/00linux/Docker数据卷挂载和本地挂载/2024_1_1Docker数据卷挂载和本地挂载/image-202413145630.png)
我们进入那个目录,首先以一个具有管理员权限的交互式 shell进行访问
`sudo -i`
![image-2024131416840.png](00_sync/00linux/Docker数据卷挂载和本地挂载/2024_1_1Docker数据卷挂载和本地挂载/image-2024131416840.png)
我们使用vim修改index
![image-2024131436185.png](00_sync/00linux/Docker数据卷挂载和本地挂载/2024_1_1Docker数据卷挂载和本地挂载/image-2024131436185.png)
![image-2024131534428.png](00_sync/00linux/Docker数据卷挂载和本地挂载/2024_1_1Docker数据卷挂载和本地挂载/image-2024131534428.png)
# 数据卷挂载
先试用docker run命令
```
docker run -d \
	--name mysql2 \
	-p 3307:3306 \
	-e TZ=Asia/shanghai \
	-e MYSQL_ROOT_PASSWORD=123 \
	mysql
```
加载完成后可以看到映射到了宿主机的3307顿考上,然后volume name为c08899
![image-202413164703.png](00_sync/00linux/Docker数据卷挂载和本地挂载/2024_1_1Docker数据卷挂载和本地挂载/image-202413164703.png)
也是可以正常连接的
![image-2024131616857.png](00_sync/00linux/Docker数据卷挂载和本地挂载/2024_1_1Docker数据卷挂载和本地挂载/image-2024131616857.png)
查看详细信息,这就达到了持久化存储
![image-2024131628287.png](00_sync/00linux/Docker数据卷挂载和本地挂载/2024_1_1Docker数据卷挂载和本地挂载/image-2024131628287.png)
# 本地挂载(非数据卷)
可以看到,用上述挂载卷来挂载的话,目录依旧不太好找.所以我们可以使用本地目录来进行挂载
如:
```
docker run --name mymysql -v mymysql:/etc/mysql/conf.d -e MYSQL_ROOT_PASSWORD=123456 -d mysql:tag
docker run --name mymysql -v /home/mysql:/etc/mysql/conf.d -e MYSQL_ROOT_PASSWORD=123456 -d mysql:tag
```
需要注意
-v mymysql:/etc/mysql/conf.d
-v /home/mysql:/etc/mysql/conf.d
挂载到本地目录的后者必须为/或者./开头,不然会被识别为挂载卷
我们需要完成三个挂载.
## 挂载三目录
![image-2024131642236.png](00_sync/00linux/Docker数据卷挂载和本地挂载/2024_1_1Docker数据卷挂载和本地挂载/image-2024131642236.png)
## 第一个为mysql目录
![image-202413165389.png](00_sync/00linux/Docker数据卷挂载和本地挂载/2024_1_1Docker数据卷挂载和本地挂载/image-202413165389.png)
## 第二个为初始化脚本
![image-2024131711197.png](00_sync/00linux/Docker数据卷挂载和本地挂载/2024_1_1Docker数据卷挂载和本地挂载/image-2024131711197.png)


## 第三个为配置文件
![image-2024131717122.png](00_sync/00linux/Docker数据卷挂载和本地挂载/2024_1_1Docker数据卷挂载和本地挂载/image-2024131717122.png)
## 完成compose
```
docker run -d \
	--name mysql2 \
	-p 3307:3306 \
	-e TZ=Asia/shanghai \
	-e MYSQL_ROOT_PASSWORD=123 \
	-v /root/mysql/data:/var/lib/mysql \
	-v /root/mysql/init:/docker-entrypoint-initdb.d \
	-v /root/mysql/conf:/etc/mysql/conf.d \
	mysql
```

下面就是我们新增的本地挂载了
```
	-v /root/mysql/data:/var/lib/mysql \
	-v /root/mysql/init:/docker-entrypoint-initdb.d \
	-v /root/mysql/conf:/etc/mysql/conf.d \
```
## 创建对应目录
也可以不创建,run容器的时候会自动创建
```
sudo -i
cd /root/mysql
mkdir data
mkdir config
mkdir init
```
![image-202413185776.png](00_sync/00linux/Docker数据卷挂载和本地挂载/2024_1_1Docker数据卷挂载和本地挂载/image-202413185776.png)

## 成功启动
![image-2024131825778.png](00_sync/00linux/Docker数据卷挂载和本地挂载/2024_1_1Docker数据卷挂载和本地挂载/image-2024131825778.png)
![image-2024131833578.png](00_sync/00linux/Docker数据卷挂载和本地挂载/2024_1_1Docker数据卷挂载和本地挂载/image-2024131833578.png)
## 注意
这个本地挂载是在volume list看不到路径
![image-2024134915223.png](00_sync/00linux/Docker数据卷挂载和本地挂载/2024_1_1Docker数据卷挂载和本地挂载/image-2024134915223.png)