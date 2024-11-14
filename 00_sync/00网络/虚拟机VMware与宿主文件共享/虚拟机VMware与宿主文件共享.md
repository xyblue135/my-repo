![1bec572f84bf44a2b3c00e8bcb58084b.png](00_sync/00网络/虚拟机VMware与宿主文件共享/虚拟机VMware与宿主文件共享/1bec572f84bf44a2b3c00e8bcb58084b.png)
root@ubuntu:/home/caojj# vmware-hgfsclient 
mount -t vmhgfs .host:/F/3hp用于共享 /mnt/hgfs
如果没成功👇
sudo vmhgfs-fuse .host:/F3/hp用于共享 /mnt/hgfs
验证
```
mount -t vmhgfs .host:/F/3hp用于共享 /mnt/hgfs
sudo vmhgfs-fuse .host:/F3hp用于共享 /mnt/hgfs
cd /mnt/hgfs
ls
```
# 自启

sudo vim /etc/rc.local
在文件的最后添加如下内容:
```
#!/bin/bash
vmhgfs-fuse -o allow_other .host:/F /mnt/hgfs
exit 0
```
 增加脚本可执行权限并设置每次开机启动时自动执行
sudo chmod +x /etc/rc.local
systemctl start rc.local.service
