这件事发生在，我有两台笔记本本设备当服务器，当我把192.168.1.101的ip给了另外一台设备后，我的客户端总是ping不到我的服务器，且我的被替换的设备用的是转接网卡连接的。
![57776f3885ee9925c681dfde9fe5b03.png|375](00_sync/00网络/Linux网络排错之断流【修改grub】/网络排错之断流/57776f3885ee9925c681dfde9fe5b03.png)

# 排错思路
首先我看了win和linux的arp表，对应的mac也都是正确的。这就不是arp的问题。且很奇怪的一个点是我的服务器如果一致保持ping我的客户端，那么网络就可以一直通信，客户端→路由器→服务端，于是我移除客户端的限制，用路由器做客户端来进一步排错。发现如果我的路由器和服务端一段时间没有网络信息交流也会断掉。不应该，罕见，于是我拿出来我的无线网卡
右边的有线网卡超时后，进行左边ping无线网卡，发现竟然通了。 那也能排除掉usb口供电什么的没有问题
![image-20241112311207.png](00_sync/00网络/Linux网络排错之断流【修改grub】/网络排错之断流/image-20241112311207.png)
于是我看了有线接口的日志，发现一直在改系统一直在接口的名字，看了下这是为了防止多网络接口冲突，但是这个好像对我的系统并不有用，且让我造成了困扰。。
dmesg | grep -i eth
dmesg | grep -i wlan
![image-20241112524917.png](00_sync/00网络/Linux网络排错之断流【修改grub】/网络排错之断流/image-20241112524917.png)
更新一下grub不让它替换看看
sudo nano /etc/default/grub
GRUB_CMDLINE_LINUX="rd.lvm.lv=fedora_192/root rhgb quiet net.ifnames=0 biosdevname=0"
![image-202411121645208.png|425](00_sync/00网络/Linux网络排错之断流【修改grub】/网络排错之断流/image-202411121645208.png)
Ubuntu/Debian
sudo update-grub
Fedora/RHEL/CentOS 系统
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
重启系统sudo reboot
注意:这个最好绝对不要离开设备操作，很有可能失联，这个重启！！！
切换为其它网络管理
sudo dnf install systemd-udev systemd-networkd
sudo systemctl enable systemd-networkd.service --now
/etc/systemd/network
sudo systemctl restart
这里有个配置文件
sudo systemctl restart systemd-networkd
发现还是不行
去BIOS里面把USB 上电延迟（Device Power-Up Delay）改为40秒
将 USB 上电延迟（Device Power-Up Delay） 设置为 40 秒会导致 BIOS 在启动时等待 USB 设备上电并完全准备好，这样会显著延长开机时间，尤其是在启动过程中会等待所有 USB 设备的响应。
![73c010ff3c42a09997b547936a3e488.jpg|475](00_sync/00网络/Linux网络排错之断流【修改grub】/Linux网络排错之断流【修改grub】/73c010ff3c42a09997b547936a3e488.jpg)

还是不行
再次修改grub
```
GRUB_DISTRIBUTOR="$(sed 's, release .*$,,g' /etc/system-release)"
GRUB_DEFAULT=saved
GRUB_DISABLE_SUBMENU=true
GRUB_TERMINAL_OUTPUT="console"
GRUB_CMDLINE_LINUX="rd.lvm.lv=fedora_192/root rhgb quiet net.ifnames=0 biosdevname=0 usbcore.autosuspend=-1"
GRUB_DISABLE_RECOVERY="true"
GRUB_ENABLE_BLSCFG=true
```
这次可以了
# 疑问
但是我用PE和以前安装的win的版本也会卡死【没更新驱动】，PE要是说没有合适的驱动稳定usb休眠的话，可以理解，但是win那边说不过去，毕竟win不是走的usb总线，虽然问题解决了，但是还是有点说不过去。

![d2efb75569b0ae2c3b6091f1f83592d.jpg|450](00_sync/00网络/Linux网络排错之断流【修改grub】/Linux网络排错之断流【修改grub】/d2efb75569b0ae2c3b6091f1f83592d.jpg)



