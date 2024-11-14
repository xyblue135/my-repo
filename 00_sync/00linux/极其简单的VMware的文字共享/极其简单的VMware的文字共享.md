如果想将Windows中的文件复制到VMware的[Linux虚拟机](https://so.csdn.net/so/search?q=Linux%E8%99%9A%E6%8B%9F%E6%9C%BA&spm=1001.2101.3001.7020)中，或者将Windows中复制的命令粘贴到VMware中，该怎么办呢？
需要安装 VMware Tools。
安装VMware Tools最简单的方式莫过于三行代码。
在终端中依次输入：
```
sudo apt update  #获得系统上所有包的最新信息
sudo apt upgrade  #下载和升级到最新版本
sudo apt install open-vm-tools-desktop -y 
sudo reboot
```
重启之后就可以实现Windows和VMware的相互复制了，也支持拖拽呢！

但是我习惯使用FTP服务器了，而且文件屏幕拖拽不好用，不如共享文件夹。要个剪切板共享就可以了哈。
![xyblue2024_02_18_16_34_24.png](00_sync/00linux/极其简单的VMware的文字共享/极其简单的VMware的文字共享/xyblue2024_02_18_16_34_24.png)