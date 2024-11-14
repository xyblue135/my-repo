如果我们需要再Win上运行Docker的话，我们可以使用desktop的Docker，但安装此Docker也需要WSL2来支持运行，但WSL2又是依赖于Hyper-v，但Hyper-v适合Virtual Box抵触的，所以我们运行在Virtual Box的虚拟机会打开失败，如支持Ensp的依赖虚拟机，导致Ensp无法正常使用。且我的电脑的Hyper-v服务其实是没有开启的。
![Pasted-image-20231207033455.png](00_sync/00网络/VirtualBox和Hyper-V和WSL和Docker的不兼容/VirtualBox和Hyper-V和WSL和Docker的不兼容/Pasted-image-20231207033455.png)
![Pasted-image-20231207033450.png](00_sync/00网络/VirtualBox和Hyper-V和WSL和Docker的不兼容/VirtualBox和Hyper-V和WSL和Docker的不兼容/Pasted-image-20231207033450.png)
![Pasted-image-20231207033555.png](00_sync/00网络/VirtualBox和Hyper-V和WSL和Docker的不兼容/VirtualBox和Hyper-V和WSL和Docker的不兼容/Pasted-image-20231207033555.png)
以至于网上很多教程让去关闭Hpyer-V而错误！
这样的话可以Docker和Ensp只能留一个，是真的非常难受，没其它办法了吗?
翻了翻VirtualBox的更新日志，看到6.0.0的Virtual Box就添加了对Hyper-V的支持，但是这个特性是隐藏的，并不默认开启，可能是因为测试效果并不是很理想？
https://www.virtualbox.org/wiki/Downloads
![Pasted-image-20231207033731.png](00_sync/00网络/VirtualBox和Hyper-V和WSL和Docker的不兼容/VirtualBox和Hyper-V和WSL和Docker的不兼容/Pasted-image-20231207033731.png)
而我们出现这个问题大概率是因为我们使用的VirtualBox是别人的一个网盘分享文件，然后是5.X版本的,并没有这个功能。
![Pasted-image-20231207033939.png](00_sync/00网络/VirtualBox和Hyper-V和WSL和Docker的不兼容/VirtualBox和Hyper-V和WSL和Docker的不兼容/Pasted-image-20231207033939.png)
哦对了，eNSP他真的很讲究，
需要的virtualbox版本为5.2.X系列  
这个版本很讲究，太高太低都不行

所以舍不得孩子套不着狼的办法是把ensp卸载了，或者在vm上开一个虚拟机，需要注意：
在同一时间点上，通常不能同时启用 VMware Workstation 和 Hyper-V，因为它们使用了不同的虚拟化技术，存在冲突。
也就是说Docker和VMware不能一块开启!


# 后续40错误
![image-202312144811460.png](00_sync/00网络/VirtualBox和Hyper-V和WSL和Docker的不兼容/VirtualBox和Hyper-V和WSL和Docker的不兼容/image-202312144811460.png)
这些错误需要彻底关闭此项
![image-202312144850725.png](00_sync/00网络/VirtualBox和Hyper-V和WSL和Docker的不兼容/VirtualBox和Hyper-V和WSL和Docker的不兼容/image-202312144850725.png)
用管理员powershell窗口,然厚重启电脑
```
bcdedit /set hypervisorlaunchtype off
```
![image-202312144936422.png](00_sync/00网络/VirtualBox和Hyper-V和WSL和Docker的不兼容/VirtualBox和Hyper-V和WSL和Docker的不兼容/image-202312144936422.png)
![image-202312145712196.png|500](00_sync/00网络/VirtualBox和Hyper-V和WSL和Docker的不兼容/VirtualBox和Hyper-V和WSL和Docker的不兼容/image-202312145712196.png)
就可以正常使用了