# smb【server message block】
块传输的  感觉适合局域网 看视频挺快的  这里以xyblue_smb用户的纯/home/xyblue_smb目录演示
```
sudo apt update 
sudo apt install samba
where samba
useradd -m xyblue_smb
```

```
sudo nano /etc/samba/smb.conf

文件加入,下面[这就是个名字]
[xyblue_smb]
	comment = Samba on ubuntu
	path = /home/xyblue_smb
	read only = no
	browsable = yes
	
下面这个是所有人匿名访问 一般不建议添加
[xyblue_smb_dairui2]
   comment = Samba on ubuntu
   path = /home/xyblue_everyone  【注意这里我直接新建了个文件夹且给到了777的权限，不然也是访问不了的】
   read only = no
   browsable = yes
   guest ok = yes
   create mask = 0777
   directory mask = 0777
   force user = nobody
```
![image-20241017244558.png|375](00_sync/00%E7%BD%91%E7%BB%9C/smb_ftp_nfs_WebDav%E5%85%B1%E4%BA%AB/smb_ftp_nfs_WebDav%E5%85%B1%E4%BA%AB/image-20241017244558.png)
![image-202410171244349.png](00_sync/00%E7%BD%91%E7%BB%9C/smb_ftp_nfs_WebDav%E5%85%B1%E4%BA%AB/smb_ftp_nfs_WebDav%E5%85%B1%E4%BA%AB/image-202410171244349.png)
最重要的一步，因为smb账号和设备账号密码是不一致的 
下面我创建的就是创建,
也就是说如果单纯passwd xyblue_smb修改是不会影响smb的密码的。需要smbpasswd才可以
```
创建用户并修改密码
sudo smbpasswd -a xyblue_smb 123456
修改密码
smbpasswd -a xyblue_smb
```
重启
```
sudo service smbd restart
sudo testparm /etc/samba/smb.conf
sudo systemctl status smbd
```
# FTP【file transfer protocol】
感觉缺点挺大的，有缺陷
```
sudo apt update 
sudo apt install vsftpd
useradd -m xyblue_ftp
```
搞好用户后哟啊编辑文件权限
```
sudo nano /etc/vsftpd.conf
临时去除注释行的查看
grep -v '^#' /etc/vsftpd.conf | grep -v '^$'
删除注释
sudo sed -i '/^\s*#/d; /^\s*$/d' /etc/vsftpd.conf
sudo grep -v '^\s*#' /etc/vsftpd.conf | sudo grep -v '^\s*$' > /etc/vsftpd.conf.tmp && sudo mv /etc/vsftpd.conf.tmp /etc/vsftpd.conf
```
![image-20241017501441.png|450](00_sync/00%E7%BD%91%E7%BB%9C/smb_ftp_nfs_WebDav%E5%85%B1%E4%BA%AB/smb_ftp_nfs_WebDav%E5%85%B1%E4%BA%AB/image-20241017501441.png)
1. **listen=NO** - 这个设置表示 vsftpd 不会监听 IPv4 地址。如果你希望 vsftpd 监听 IPv4 地址，你需要将这个值改为 `YES`。
2. **listen_ipv6=YES** - 这个设置表示 vsftpd 会监听 IPv6 地址。如果你不希望 vsftpd 监听 IPv6 地址，你需要将这个值改为 `NO`。
3. **anonymous_enable=NO** - 这个设置已经正确地禁止了匿名登录。如果你想要允许匿名用户登录，你可以将其改为 `YES`。
4. **local_enable=YES** - 这个设置允许本地用户通过 FTP 登录。如果你想禁止本地用户登录，可以将其改为 `NO`。
5. **dirmessage_enable=YES** - 当用户进入某个目录时显示消息。如果你不想显示任何消息，可以将其改为 `NO`。
6. **use_localtime=YES** - 使用本地时间记录日志。通常不需要更改这个设置，除非你有特殊的时间要求。
7. **xferlog_enable=YES** - 启用了传输日志记录。如果你想禁用日志记录，可以将其改为 `NO`。
8. **connect_from_port_20=YES** - 允许从端口 20 进行数据连接。这是标准的 FTP 数据端口，一般不需要改变。
9. **secure_chroot_dir=/var/run/vsftpd/empty** - 设置了一个安全的 chroot 目录。如果你启用了 `chroot_local_user=YES` 或者其他相关的 chroot 选项，确保这个目录存在并且是空的。
10. **pam_service_name=vsftpd** - 指定了 PAM（Pluggable Authentication Modules）服务名称。通常是 `vsftpd`，不需要更改。
11. **rsa_cert_file 和 rsa_private_key_file** - 这些指定了 SSL 证书和私钥文件的位置。如果你不打算使用 SSL/TLS 来加密 FTP 传输，这些设置可以保持不变。
12. **ssl_enable=NO** - 禁用了 SSL 加密。如果你想启用 SSL/TLS 加密，需要将其改为 `YES` 并且确保前面提到的证书和私钥文件是有效的。
修改后
v4v6只能开启一个
```
listen=YES
listen_ipv6=NO
anonymous_enable=NO
local_enable=YES
dirmessage_enable=YES
use_localtime=YES
xferlog_enable=YES
connect_from_port_20=YES
secure_chroot_dir=/home/xyblue_ftp     
pam_service_name=vsftpd
rsa_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem
rsa_private_key_file=/etc/ssl/private/ssl-cert-snakeoil.key
ssl_enable=NO
```
重启
```
sudo systemctl restart vsftpd
sudo systemctl status vsftpd
查看报错和日志
sudo vsftpd /etc/vsftpd.conf
sudo journalctl -u vsftpd
```
![image-202410172728866.png|425](00_sync/00%E7%BD%91%E7%BB%9C/smb_ftp_nfs_WebDav%E5%85%B1%E4%BA%AB/smb_ftp_nfs_WebDav%E5%85%B1%E4%BA%AB/image-202410172728866.png)
```修改登录者的密码，不然也是无法登录的
sudo passwd xyblue_ftp
```
![image-202410171453268.png|400](00_sync/00%E7%BD%91%E7%BB%9C/smb_ftp_nfs_WebDav%E5%85%B1%E4%BA%AB/smb_ftp_nfs_WebDav%E5%85%B1%E4%BA%AB/image-202410171453268.png)
## 修改端口
编辑 `/etc/vsftpd.conf` 文件，并添加或修改以下行
### 主动模式
```
listen_port=你想要的新端口号
listen_port=2121
ufw allow
```
### 被动模式
```
pasv_min_port=最小端口号 
pasv_max_port=最大端口号
pasv_min_port=50000 
pasv_max_port=50100
ufw allow
```
### 用户只能访问家目录
```
chroot_local_user=YES 
allow_writeable_chroot=YES
````
## 卸载FTP
sudo systemctl stop vsftpd
sudo apt remove --purge vsftpd
sudo rm -rf /etc/vsftpd.conf
sudo rm -rf /etc/vsftpd/
sudo rm -rf /var/log/vsftpd.log
# 文件读取区别
## 安全区别
运营商禁用了samba的端口139和445，所以公网一般用不了smb了。
ftp配上ssh安全性极其高，但是传输速率会下降
## 用户区别
smb貌似同时只能一个用户
![image-2024101713976.png|371](00_sync/00%E7%BD%91%E7%BB%9C/smb_ftp_nfs_WebDav%E5%85%B1%E4%BA%AB/smb_ftp_nfs_WebDav%E5%85%B1%E4%BA%AB/image-2024101713976.png)

## 其他区别
下面是smb的
![image-202410173550800.png|450](00_sync/00%E7%BD%91%E7%BB%9C/smb_ftp_nfs_WebDav%E5%85%B1%E4%BA%AB/smb_ftp_nfs_WebDav%E5%85%B1%E4%BA%AB/image-202410173550800.png)
下面是ftp的
![image-202410173354699.png|450](00_sync/00%E7%BD%91%E7%BB%9C/smb_ftp_nfs_WebDav%E5%85%B1%E4%BA%AB/smb_ftp_nfs_WebDav%E5%85%B1%E4%BA%AB/image-202410173354699.png)
都能传输到千兆网兆比特
![image-202410174146949.png|285](00_sync/00%E7%BD%91%E7%BB%9C/smb_ftp_nfs_WebDav%E5%85%B1%E4%BA%AB/smb_ftp_nfs_WebDav%E5%85%B1%E4%BA%AB/image-202410174146949.png)
千兆网也把我机械硬盘吃满了
![image-202410172711865.png|475](00_sync/00%E7%BD%91%E7%BB%9C/smb_ftp_nfs_WebDav%E5%85%B1%E4%BA%AB/smb_ftp_nfs_WebDav%E5%85%B1%E4%BA%AB/image-202410172711865.png)
# WebDav
这个就是可以在云盘上直接看了，基于http的，部分家庭影院用的这个，和搭建云盘，写这篇笔记的时候用的jellyfin，真的很好用，虽然在docker里面搭建起来也没那么容易和搜刮电影
![image-20241025330567.png](00_sync/00%E7%BD%91%E7%BB%9C/smb_ftp_nfs_WebDav%E5%85%B1%E4%BA%AB/smb_ftp_nfs_WebDav%E5%85%B1%E4%BA%AB/image-20241025330567.png)
![image-202410254757807.png](00_sync/00%E7%BD%91%E7%BB%9C/smb_ftp_nfs_WebDav%E5%85%B1%E4%BA%AB/smb_ftp_nfs_WebDav%E5%85%B1%E4%BA%AB/image-202410254757807.png)
![d659cd4396fafe6be3bcd4b105e57c1.jpg|475](00_sync/00%E7%BD%91%E7%BB%9C/smb_ftp_nfs_WebDav%E5%85%B1%E4%BA%AB/smb_ftp_nfs_WebDav%E5%85%B1%E4%BA%AB/d659cd4396fafe6be3bcd4b105e57c1.jpg)