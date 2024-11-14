# 创建swap空间
## 创建文件
```创建4G的swap分区
sudo fallocate -l 4G /home/swapfile.swap
或者
sudo dd if=/dev/zero of=/home/swapfile.swap bs=1M count=4096
```
## 格式化文件
```
sudo mkswap /home/swapfile.swap
```
## 临时启用
```
sudo swapon /home/swapfile.swap
```
## 永久启用
```
sudo nano /etc/fstab
```

```添加
/home/swapfile.swap none swap sw 0 0
```
## 验证
```
free -m
```
# 删除swap空间
## 删除基础配置
```
swapon --show
free -m
# 取消带哦
sudo swapoff /dev/sda2  # 替换为实际的 swap 分区设备名
sudo swapoff /path/to/swapfile # 替换为实际的 img
sudo nano /etc/fstab # 删除掉
```
使用分区工具fdisk或者parted删除分区，但我习惯建立img
## 删除分区表或文件
```
sudo fdisk /dev/sda  # 替换为实际的硬盘设备名
# 在 fdisk 提示符下，输入：
# p （查看分区表）
# d （删除分区，输入分区号）
# w （写入更改并退出）
```

```
sudo parted /dev/sda  # 替换为实际的硬盘设备名

# 在 parted 提示符下，输入：
# print （查看分区表）
# rm 2 （删除分区2）
# quit （退出）
```
## 格式化分区【可选 不建议】
```
sudo mkfs.ext4 /dev/sdaAAAA2
```

如果是文件的话，直接rm就行

![image-202410261457676.png](00_sync/00linux/%E5%88%9B%E5%BB%BA%E5%88%A0%E9%99%A4swap%E4%BA%A4%E6%8D%A2/%E5%88%9B%E5%BB%BA%E5%88%A0%E9%99%A4swap%E4%BA%A4%E6%8D%A2/image-202410261457676.png)