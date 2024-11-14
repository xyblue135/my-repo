# 简而言之
 4块1TB的硬盘可以为1块4TB的硬盘，或者自由划分。
 但是如果数据量存的多了，撤掉一块硬盘，基本上就是会数据丢失了
## PV【物理卷】【最底层单元硬盘】
PV（Physical Volume - 物理卷）
一个物理卷对应一个磁盘分区或整个磁盘。
即一个sda1或者sda2就是一个物理卷pv
### PE【基本单位】
一个物理卷分了一堆PE出来,基本单位为PE （physical extend）默认单位为4MB,不管多少快硬盘，都分割为一个个PE

## VG 【卷组】【硬盘集合体】
VG（Volume Group - 卷组）
把物理卷分出来的一些个小pe柔和在一起的叫卷组

## 分割---------------------------
## LV【逻辑卷】【从集合体拿出来的】
 LV（Logical Volume - 逻辑卷）
 从硬盘VG拿出来的，实现实时扩容什么的

# 创建LVM
假设有两个硬盘 /dev/sdb 和 /dev/sdc。
创建物理卷
```
sudo pvcreate /dev/sdb
sudo pvcreate /dev/sdc
```
# LVM扩容
```
看lvm容量
vgs
增加5G
lvextend -L +5G /dev/fedora_192/root
如果是ext4
resize2fs /dev/fedora_192/root
如果是xfs
xfs_growfs /dev/fedora_192/root
判断文件系统
df -T
lsblk -f
```
![image-202411122316555.png|400](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux_LVM/Linux_LVM/image-202411122316555.png)
# 附件
![image-20247428874.png|275](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux_LVM/Linux_LVM/image-20247428874.png)
更详细的还是得配合fdisk和dd命令进行