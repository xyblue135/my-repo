# 危险
△危险的dd命令{处理二进制数据的强大工具}
`dd` 命令用于转换和复制文件，不过它的复制不同于 `cp`。之前提到过关于 Linux 的很重要的一点，**一切即文件**，在 Linux 上，硬件的设备驱动（如硬盘）和特殊设备文件（如 `/dev/zero` 和 `/dev/random`）都像普通文件一样，只是在各自的驱动程序中实现了对应的功能，`dd` 也可以读取文件或写入这些文件。这样，`dd` 也可以用在备份硬件的引导扇区、获取一定数量的随机数据或者空数据等任务中。`dd` 程序也可以在复制时处理数据，例如转换字节序、或在 ASCII 与 EBCDIC 编码间互换。
# dev目录
/dev/null 为类似于回收站的东西，黑洞
/dev/zero 为类似于白洞的东西，向外吐字符
/dev/random 随机数文件
/dev/stdin   标准输入，要是引用这个就可以直接写东西了
bs为块大小 count为块数量
if是input file of是output file
bs=10 缺省单位为字节Byte 可以为K M G
# 示例
```
#1.从zero或者random里面去拿数据去填充到/home/zero_test文件,可以为txt或者什么都可以
dd if=/dev/zero of=/home/zero_test bs=10M count=1
dd if=/dev/random of=/home/zero_test bs=1M count=1
```
![image-2024745132471.png](3可以放入网站的笔记/Linux下使用dd命令进行挂载/Linux下使用dd命令进行挂载/image-2024745132471.png)
```
#2.从stdin标准输入中创建文件 需要注意这里的块大小这些，你输入了1234567890123  这里面限制大小是10*1Byte，将只会有123456789 十个Byte
dd               of=test bs=10 count=1
dd if=/dev/stdin of=test bs=10 count=1
```

```
#3.从stdin标准输出输出到标准输出，套娃行为，什么都不会有哈哈
dd if=/dev/stdin of=/dev/stdout bs=10 count=1
```

```
# 将标准输出转换为大写的
dd if=/dev/stdin of=test bs=10 count=1 conv=ucase
```

```
#dd命令不能转换为小写的，只能通过tr命令去传递了
echo "DAXIE_TEST" | tr '[:upper:]' '[:lower:]' | dd of=test bs=10 count=1
```
# dd命令来分区并挂载
该命令将创建一个 256 MB 的虚拟磁盘映像文件 `virtual.img`，其中填充了零字节。这个文件可以用作虚拟机的磁盘映像、
```
#创建镜像文件
dd if=/dev/zero of=123456.img bs=1M count=256
du -h 123456.img
```
![image-2024745246547.png](3可以放入网站的笔记/Linux下使用dd命令进行挂载/Linux下使用dd命令进行挂载/image-2024745246547.png)
给文件系统
```
sudo mkfs tab查看可以用的文件系统
sudo mkfs.ext4 123456.img
```
![image-2024745258529.png|425](3可以放入网站的笔记/Linux下使用dd命令进行挂载/Linux下使用dd命令进行挂载/image-2024745258529.png)
将这个123456.image 挂载到一个目录下，△会直接覆盖掉目录，一定要谨慎操作！
```
#查看已挂载
sudo mount 
```
![image-2024745412305.png](3可以放入网站的笔记/Linux下使用dd命令进行挂载/Linux下使用dd命令进行挂载/image-2024745412305.png)
把刚才的image挂载上去
```
mount [options] [source] [directory]
mount [-o [操作选项]] [-t 文件系统类型] [-w|--rw|--ro] [文件系统源] [挂载点]
mount -o loop -t ext4 123456.img /mnt/123456一个目录  #警告，是覆盖行为
#以只读方式进行挂载
mount -o loop --ro v123456.img /mnt/一个目录 
mount -o loop,ro 123456.img /mnt/一个目录 
```
![image-2024745639503.png|425](3可以放入网站的笔记/Linux下使用dd命令进行挂载/Linux下使用dd命令进行挂载/image-2024745639503.png)
![image-202474594188.png](3可以放入网站的笔记/Linux下使用dd命令进行挂载/Linux下使用dd命令进行挂载/image-202474594188.png)
df -ht可以看文件类型
![image-202475110431.png|450](3可以放入网站的笔记/Linux下使用dd命令进行挂载/Linux下使用dd命令进行挂载/image-202475110431.png)
# 卸载挂载点、
查看挂载点关联
```
sudo losetup -a
```
![image-202475119140.png|425](3可以放入网站的笔记/Linux下使用dd命令进行挂载/Linux下使用dd命令进行挂载/image-202475119140.png)
```
sudo umount /mnt/一个目录  如果提示busy 检查pid sudo lsof /mnt/123456/ 尝试kill
sudo umount -l /mnt/一个目录  强制取消挂载
sudo losetup -d /dev/loop序号  #分离
```
![image-202475243781.png|450](3可以放入网站的笔记/Linux下使用dd命令进行挂载/Linux下使用dd命令进行挂载/image-202475243781.png)
取消挂载后，df-h是看不到了，但是lsblk还是会有一个loop序号 挂载点为空的标识符 还是挺烦的
![image-202475910968.png](3可以放入网站的笔记/Linux下使用dd命令进行挂载/Linux下使用dd命令进行挂载/image-202475910968.png)
重启一下就可以了，或者就别管了
![image-20247592690.png|425](3可以放入网站的笔记/Linux下使用dd命令进行挂载/Linux下使用dd命令进行挂载/image-20247592690.png)