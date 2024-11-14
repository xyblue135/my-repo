在安装双系统之前,我们需要先安装Win,再安装Linux,而不是先安装Linux,再安装Win
Windows安装过程可能会覆盖引导加载程序（通常是GRUB）的引导记录，导致Linux无法启动
# 下载iso
http://repo.huaweicloud.com/ubuntu-releases/22.04/
根据需要选择镜像
# 压缩空间
可以直接使用ventoy disk进入镜像
安装之前关闭独显直连,不然可能会出问题【简化驱动配置，减少潜在的兼容性问题】
压缩系统盘用来存放Linux系统，我这里拿出了20G给ubuntu
![image-202312301218523.png](00_sync/00外设/如何安装Win+Linux双系统/如何安装Win+Linux双系统/image-202312301218523.png)
# 关闭安全启动
我们进入bios关闭安全启动
![image-202312304334761.png|500](00_sync/00外设/如何安装Win+Linux双系统/如何安装Win+Linux双系统/image-202312304334761.png)
如果不关闭可能造成安全拦截，例如我直接插个u盘装个pe拷贝数据这显然是被拦截的
![image-20231230440648.png](00_sync/00外设/如何安装Win+Linux双系统/如何安装Win+Linux双系统/image-20231230440648.png)
# 安装镜像
使用ubuntu的ISO进行启动（做好linuxtogo的或者直接使用ventory存放镜像直接打开会更为方便）
![image-20241173454667.png](00_sync/00外设/如何安装Win+Linux双系统/如何安装Win+Linux双系统/image-20241173454667.png)
![image-20231230346812.png](00_sync/00外设/如何安装Win+Linux双系统/如何安装Win+Linux双系统/image-20231230346812.png)
手动进行分区
![d36bf1118ae3880d6b698a0b0f1bc70.jpg](00_sync/00外设/如何安装Win+Linux双系统/如何安装Win+Linux双系统/d36bf1118ae3880d6b698a0b0f1bc70.jpg)
为了简化分区
![image-202312301210225.png](00_sync/00外设/如何安装Win+Linux双系统/如何安装Win+Linux双系统/image-202312301210225.png)
可以将swap去掉,以后再进行配置,然后ubuntu的efi整合到windowsboot里面
紧接着在空闲分区创建根目录分区
![image-202312301642973.png](00_sync/00外设/如何安装Win+Linux双系统/如何安装Win+Linux双系统/image-202312301642973.png)
再将ubuntu的引导指向windows,注意空间别太小
![image-20241125510721.png](00_sync/00外设/如何安装Win+Linux双系统/如何安装Win+Linux双系统/image-20241125510721.png)
![image-202312301559541.png](00_sync/00外设/如何安装Win+Linux双系统/如何安装Win+Linux双系统/image-202312301559541.png)
等待安装即可
![image-20231230193807.png](00_sync/00外设/如何安装Win+Linux双系统/如何安装Win+Linux双系统/image-20231230193807.png)
# 成品
可以看到,双引导已经添加了
![835287f746cf5d92846d1c34840f1db.jpg](00_sync/00外设/如何安装Win+Linux双系统/如何安装Win+Linux双系统/835287f746cf5d92846d1c34840f1db.jpg)
OK,成功了
![7f0a9451e0b365375282ba926648647.jpg](00_sync/00外设/如何安装Win+Linux双系统/如何安装Win+Linux双系统/7f0a9451e0b365375282ba926648647.jpg)
![ba21bd7b7645b7b2c70e51bc0f8285e.jpg](00_sync/00外设/如何安装Win+Linux双系统/如何安装Win+Linux双系统/ba21bd7b7645b7b2c70e51bc0f8285e.jpg)

# 时间同步
众所周知,在windows里面时间是记录在BIOS电池里面的,所以即使关机断电,时间也会正常运转.但是我们一旦换成了ubuntu系统,ubuntu会将同步的时间-8小时写入到BIOS中,然后这个时候我们在打开windows,windows就从Bios读取到错误的时间.就需要在NTP服务器同步时间,很是麻烦.
![image-2024112153544.png](00_sync/00外设/如何安装Win+Linux双系统/如何安装Win+Linux双系统/image-2024112153544.png)
![image-2024112232506.png](00_sync/00外设/如何安装Win+Linux双系统/如何安装Win+Linux双系统/image-2024112232506.png)
等待同步
![image-2024112252741.png](00_sync/00外设/如何安装Win+Linux双系统/如何安装Win+Linux双系统/image-2024112252741.png)
将UTC改为localtime
![image-2024112238434.png](00_sync/00外设/如何安装Win+Linux双系统/如何安装Win+Linux双系统/image-2024112238434.png)
https://www.bilibili.com/video/BV1vM411J74S/?spm_id_from=333.337.search-card.all.click&vd_source=f8caedefe0d5d4c59944bf35b5374752
![image-202312301957791.png](00_sync/00外设/如何安装Win+Linux双系统/如何安装Win+Linux双系统/image-202312301957791.png)
# 网络驱动
部分型号的网卡可能未被linux适配,需要手动添加驱动
![image-20241173523381.png](00_sync/00外设/如何安装Win+Linux双系统/如何安装Win+Linux双系统/image-20241173523381.png)
英特尔网卡下载网站
https://www.intel.cn/content/www/cn/zh/search.html?ws=text#q=&sort=relevancy&f:@tabfilter=[Downloads]&f:@stm_10385_zh=[%E6%97%A0%E7%BA%BF]
硬盘扩容
https://www.bilibili.com/video/BV1Cc41127B9?p=21&vd_source=f8caedefe0d5d4c59944bf35b5374752
参考视频
https://www.bilibili.com/video/BV1554y1n7zv?p=9&vd_source=f8caedefe0d5d4c59944bf35b5374752 


# 注意事项
## sata接口设置

如果使用SATA的话需要进入BIOS将SATA管理选项改为AHCI模式(即SATA线连接的那个)(如果是用IDE接口连接的就需要改为IDE模式了)
![image-202312305252672.png](00_sync/00外设/如何安装Win+Linux双系统/如何安装Win+Linux双系统/image-202312305252672.png)

## 怎么移除ubuntu系统
将下面三行的linux分区都删除掉
![image-2024112463753.png](00_sync/00外设/如何安装Win+Linux双系统/如何安装Win+Linux双系统/image-2024112463753.png)
但是这样并不能完全移除,开机会进入grub,输入exit才可以进入windows
![image-20241124844861.png](00_sync/00外设/如何安装Win+Linux双系统/如何安装Win+Linux双系统/image-20241124844861.png)
需要将ubuntu的EFI删除
![image-2024112493987.png](00_sync/00外设/如何安装Win+Linux双系统/如何安装Win+Linux双系统/image-2024112493987.png)
![image-20241124927227.png](00_sync/00外设/如何安装Win+Linux双系统/如何安装Win+Linux双系统/image-20241124927227.png)

## 修改开机延迟时间
在进入ubuntu时,出现的方框可以更改
![image-202312311929857.png](00_sync/00外设/如何安装Win+Linux双系统/如何安装Win+Linux双系统/image-202312311929857.png)
首先进入系统后输入
```
sudo gedit /etc/defalut/grub
```
![image-20241122655272.png](00_sync/00外设/如何安装Win+Linux双系统/如何安装Win+Linux双系统/image-20241122655272.png)
进入后可以修改默认
![image-20241122739910.png](00_sync/00外设/如何安装Win+Linux双系统/如何安装Win+Linux双系统/image-20241122739910.png)
然后保存
```
sudo update-grub   # 更新设置并保存
```
重启即可