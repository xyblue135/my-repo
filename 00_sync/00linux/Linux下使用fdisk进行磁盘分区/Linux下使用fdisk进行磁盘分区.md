# 查看信息
```
sudo fdisk -l
```
但是如果有loop设备的话不好观察,过滤loop行
```
sudo fdisk -l | grep -v loop
sudo blkid | grep -v loop
```
![image-2024751546540.png|475](00_sync/00linux/Linux下使用fdisk进行磁盘分区/Linux下使用fdisk进行磁盘分区/image-2024751546540.png)
# 1.进行分区
![image-202475380550.png](00_sync/00linux/Linux下使用fdisk进行磁盘分区/Linux下使用fdisk进行磁盘分区/image-202475380550.png)
```
# 只能是整个磁盘，不能以分区作为目标
sudo fdisk /dev/sdb
- 输入 `n` 并按 Enter 创建新分区。
- 选择 `p` 创建主分区，然后按 Enter。
- 输入分区号（默认是1），然后按 Enter。
- 指定分区的起始和结束位置（通常按 Enter 使用默认值）
- +20G
- p查看分区表
- 输入 `w` 来写入分区表并退出。
```
![image-2024753925946.png](00_sync/00linux/Linux下使用fdisk进行磁盘分区/Linux下使用fdisk进行磁盘分区/image-2024753925946.png)
# 2.格式化分区
```
sudo mkfs.ext4 /dev/sdb1
sudo mkfs.ext4 loop14
sudo mkfs.tab看可以看有哪些
```
![image-202475458931.png](00_sync/00linux/Linux下使用fdisk进行磁盘分区/Linux下使用fdisk进行磁盘分区/image-202475458931.png)
# 3.挂载分区
```
sudo mount /dev/sdb1 /mnt/upan
```
![image-2024754556838.png|475](00_sync/00linux/Linux下使用fdisk进行磁盘分区/Linux下使用fdisk进行磁盘分区/image-2024754556838.png)
# 开机自动挂载 （默认开机没挂载）
```
sudo vi /etc/fstab
/dev/sdb1 /mnt/upan ext4 defaults 0 0
```
一般用uid挂载比较保险，需要注意，一定要保证目前正在挂载使用blkid才可以看到挂载的uid，重要
![image-202475932777.png](00_sync/00linux/Linux下使用fdisk进行磁盘分区/Linux下使用fdisk进行磁盘分区/image-202475932777.png)

# 附件
m键以获得帮助
![image-202475188645.png|400](00_sync/00linux/Linux下使用fdisk进行磁盘分区/Linux下使用fdisk进行磁盘分区/image-202475188645.png)
![image-2024751850453.png](00_sync/00linux/Linux下使用fdisk进行磁盘分区/Linux下使用fdisk进行磁盘分区/image-2024751850453.png)
![image-2024751911204.png](00_sync/00linux/Linux下使用fdisk进行磁盘分区/Linux下使用fdisk进行磁盘分区/image-2024751911204.png)
# LOOP设备img【img当分区用】
```
其实这个我是用来本来分一个区的，又是一个硬盘的，要控制一个目录的大小用的。
```
loop 设备是 Linux 中的一种特殊类型的块设备，它可以将文件作为块设备来使用。这意味着你可以像对待普通磁盘一样对待文件
配合dd命令的img进行分区，即从已经分好区的硬盘里面抽个img来再分区
创建一个空白的磁盘映像文件,使用 fdisk 对磁盘映像文件进行分区 mkfs.ext4格式化磁盘
```
sudo dd if=/dev/zero of=123456.img bs=1M count=256
sudo fdisk 123456.img
sudo mkfs.ext4 123456.img
下面这个也可以
sudo mkfs.ext4 loop14
```
而且也需要和loop建立关联才可以，而且推荐是先分区，那就跟上面的流程异样了，然后在进行loop的关联
```
建立关联
sudo losetup /dev/loop0 virtual.img
删除关联
sudo losetup -d /dev/loop0
```
如果不知道要和哪个loop需要所挂载的目录建立关联
那就需要自己创建了
```
mount [options] [source] [directory]
mount [-o [操作选项]] [-t 文件系统类型] [-w|--rw|--ro] [文件系统源] [挂载点]
mount -o loop -t ext4 123456.img /mnt/123456一个目录  #警告，是覆盖行为
#以只读方式进行挂载
mount -o loop --ro v123456.img /mnt/一个目录 
mount -o loop,ro 123456.img /mnt/一个目录 
```
ps：当你使用 `mount` 命令来挂载一个文件时，系统会自动创建一个 loop 设备（例如 `/dev/loop14`）来关联该文件。因此，你看到 `/dev/loop14` 被挂载到了 `/mnt/upan_guazai`。


