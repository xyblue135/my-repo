
```bash
watch grep \'cpu MHz\' /proc/cpuinfo
```
![image-2024264910411.png](5搁置的网站上传项目/linux常用指令(收藏夹)/linux常用指令/image-2024264910411.png)
# cpu频率设置
sudo apt-get install cpufrequtils
cpufreq-info
sudo cpufreq-set -g performance  #改为性能模式
sudo cpufreq-set -f 3.5GHz
如果重启恢复了的话
sudo apt-get install sysfsutils
cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
sudo gedit  /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
填写需要更改的状态。
# 查看系统内核
uname -a
![image-2024265119200.png](5搁置的网站上传项目/linux常用指令(收藏夹)/linux常用指令/image-2024265119200.png)
# 看操作系统
lsb_release -a
![image-2024265149754.png](5搁置的网站上传项目/linux常用指令(收藏夹)/linux常用指令/image-2024265149754.png)
# 看CPU
cat /proc/cpuinfo
![image-2024265244620.png](5搁置的网站上传项目/linux常用指令(收藏夹)/linux常用指令/image-2024265244620.png)
# 看计算机名
hostname
![image-202426532921.png](5搁置的网站上传项目/linux常用指令(收藏夹)/linux常用指令/image-202426532921.png)
# 查看PCI设备
![image-2024265353183.png](5搁置的网站上传项目/linux常用指令(收藏夹)/linux常用指令/image-2024265353183.png)
# 查看usb设备
lsusb -tv
![image-2024265543942.png](5搁置的网站上传项目/linux常用指令(收藏夹)/linux常用指令/image-2024265543942.png)
在这这里看到我的AX201竟然usb2.0??????????
# 加载的内核模块
lsmod
![image-2024262911656.png](5搁置的网站上传项目/linux常用指令(收藏夹)/linux常用指令/image-2024262911656.png)
# 系统变量
env
![image-2024262943814.png](5搁置的网站上传项目/linux常用指令(收藏夹)/linux常用指令/image-2024262943814.png)