对与在linux系统中插入u盘直接拔出导致分区表被识别为RAW且无法各种操作.
![image-202410242814975.png](00_sync/ZZ%E7%9E%8E%E5%86%99/U%E7%9B%98RAW%E5%A4%84%E7%90%86/U%E7%9B%98RAW%E5%A4%84%E7%90%86/image-202410242814975.png)
使用disk修复
```
sudo umount /dev/sdb
sudo fdisk /dev/sdb
d  # 删除所有分区
w  # 写入更改并退出
sudo parted /dev/sdb mklabel msdos
sudo parted /dev/sdb mkpart primary fat32 0% 100%
sudo mkfs.vfat -n "MyUSB" /dev/sdb1
```
![image-202410243826339.png](00_sync/ZZ%E7%9E%8E%E5%86%99/U%E7%9B%98RAW%E5%A4%84%E7%90%86/U%E7%9B%98RAW%E5%A4%84%E7%90%86/image-202410243826339.png)
