举例:ubuntu
vsftpd 是“very secure FTP daemon”的缩写，安全性是它的一个最大的特点。vsftpd 是一个 UNIX 类操作系统上运行的服务器的名字，它可以运行在诸如 Linux、BSD、Solaris、 HP-UNIX等系统上面，是一个完全免费的、开放源代码的ftp服务器软件，支持很多其他的 FTP 服务器所不支持的特征。比如：非常高的安全性需求、带宽限制、良好的可伸缩性、可创建虚拟用户、支持IPv6、速率高等。
```
sudo apt-get install vsftpd
```
![image-202312144124542.png](00_sync/00linux/Linux上配置Ftp_Server/Linux上配置Ftp_Server/image-202312144124542.png)
等待软件自动安装，安装完成以后使用如下 VI 命令打开/etc/[vsftpd](https://so.csdn.net/so/search?q=vsftpd&spm=1001.2101.3001.7020).conf，命令如下：
```
sudo vi /etc/vsftpd.conf
```
![image-20231215195924.png](00_sync/00linux/Linux上配置Ftp_Server/Linux上配置Ftp_Server/image-20231215195924.png)
![image-202312152011143.png](00_sync/00linux/Linux上配置Ftp_Server/Linux上配置Ftp_Server/image-202312152011143.png)
使用以下命令重启ftp服务.
```
sudo /etc/init.d/vsftpd restart
```
