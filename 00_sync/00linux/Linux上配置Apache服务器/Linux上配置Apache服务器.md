# Apache
```
sudo systemctl stop apache2
sudo apt-get remove --purge apache2 apache2-utils
sudo rm -rf /etc/apache2
sudo rm -rf /var/www/html
sudo apt-get autoremove
```
sudo apt install apache2

apache2 -version

Server version: Apache/2.4.29 (Ubuntu)
Server built:   2023-03-08T17:34:33

```
systemctl status apache2

● apache2.service - The Apache HTTP Server
   Loaded: loaded (/lib/systemd/system/apache2.service; enabled; vendor preset: enabled)
  Drop-In: /lib/systemd/system/apache2.service.d
           └─apache2-systemd.conf
   Active: active (running) since Thu 2023-08-31 14:58:40 CST; 46min ago
  Process: 31473 ExecStop=/usr/sbin/apachectl stop (code=exited, status=0/SUCCESS)
  Process: 31478 ExecStart=/usr/sbin/apachectl start (code=exited, status=0/SUCCESS)
 Main PID: 31482 (apache2)
    Tasks: 55 (limit: 4915)
   CGroup: /system.slice/apache2.service
           ├─31482 /usr/sbin/apache2 -k start
           ├─31483 /usr/sbin/apache2 -k start
           └─31484 /usr/sbin/apache2 -k start

Aug 31 14:58:40 netease-Precision-3630-Tower systemd[1]: Starting The Apache HTTP Server...
Aug 31 14:58:40 netease-Precision-3630-Tower apachectl[31478]: [Thu Aug 31 14:58:40.080095 2023] [so:warn] [pid 31481:tid 140536320043968] AH01574: module rewrite_module is alr
Aug 31 14:58:40 netease-Precision-3630-Tower apachectl[31478]: AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 127.0.1.1. Set the
Aug 31 14:58:40 netease-Precision-3630-Tower systemd[1]: Started The Apache HTTP Server
```


- 默认服务器文档根目录在/var/www/html
- 浏览器访问ip地址，即可访问到index.html, 即/var/www/html/index.html,如下：
#### 自定义文件目录配置

```
[netease@netease-Precision-3630-Tower /var/www/html]$ ls -l
total 12
lrwxrwxrwx 1 root root    41 Aug 31 15:10 files -> /home/netease/working/Apache_File_System/
-rw-r--r-- 1 root root 10918 Aug 31 11:53 index.html
```
# 下载文件
创建软链接
sudo ln -s /home/ubuntu/0000apache_web/ /var/www/html/files

```
ubuntu@VM-8-3-ubuntu:/var/www/html$ ll
total 20
drwxr-xr-x 2 root root  4096 Jun 11 13:38 ./
drwxr-xr-x 4 root root  4096 Jun 11 12:11 ../
lrwxrwxrwx 1 root root    28 Jun 11 13:38 files -> /home/ubuntu/0000apache_web//
-rw-r--r-- 1 root root 10918 Jun 11 12:11 index.html
```
![image-20246114155552.png](00_sync/00linux/Linux上配置Apache服务器/Linux上配置Apache服务器/image-20246114155552.png)