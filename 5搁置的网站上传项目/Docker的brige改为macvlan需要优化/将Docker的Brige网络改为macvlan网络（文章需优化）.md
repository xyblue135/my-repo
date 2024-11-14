![Pasted-image-20231125214622.png](5搁置的网站上传项目/Docker的brige改为macvlan需要优化/将Docker的Brige网络改为macvlan网络（文章需优化）/Pasted-image-20231125214622.png)
# 网桥
当你使用网桥连接虚拟机时，通常网桥本身并不会生成 IP 地址。网桥是一个虚拟交换机，它将连接到它的不同接口（包括虚拟机）放置在同一个子网下，而网桥本身没有自己的 IP 地址。如果你的物理网络是 192.168.1.0/24，连接到网桥的虚拟机将共享该子网，并且会获得该子网范围内的 IP 地址，如 192.168.1.x。
```
下图为openwrt中docker的默认网桥配置
```
![Pasted-image-20231125222747.png](5搁置的网站上传项目/Docker的brige改为macvlan需要优化/将Docker的Brige网络改为macvlan网络（文章需优化）/Pasted-image-20231125222747.png)
![Pasted-image-20231125222548.png](5搁置的网站上传项目/Docker的brige改为macvlan需要优化/将Docker的Brige网络改为macvlan网络（文章需优化）/Pasted-image-20231125222548.png)
查看桥接接口的命令：
```
ip link show eth1
```
![Pasted-image-20231125223409.png](5搁置的网站上传项目/Docker的brige改为macvlan需要优化/将Docker的Brige网络改为macvlan网络（文章需优化）/Pasted-image-20231125223409.png)
```
brctl show | grep br-lan
```
查看次网桥信息
![Pasted-image-20231125224045.png](5搁置的网站上传项目/Docker的brige改为macvlan需要优化/将Docker的Brige网络改为macvlan网络（文章需优化）/Pasted-image-20231125224045.png)
# macvlan
使用 Macvlan 时，虚拟机会使用主机（宿主机）的物理网卡（或者指定的父网卡）来创建一个独立的虚拟接口。这个虚拟接口可以有自己的 MAC 地址，并且可以配置自己的 IP 地址, - Macvlan 可以配置为在物理网络中使用不同的 IP 地址范围，取决于你的网络设置。因此，连接到 Macvlan 的虚拟机可以拥有不同于物理网络的 IP 地址。
总的来说，网桥并不会自己生成 IP 地址，它是将连接到它的设备放在同一个子网下。而 Macvlan 可以配置为使用不同于物理网络的 IP 地址范围，每个 Macvlan 接口都可以拥有自己独立的 IP 地址。
## 四种模式
### Bridge Mode
桥接模式允许 Macvlan 接口与宿主机上的其他接口以及同一物理网络上的其他设备通信。桥接模式下的 Macvlan 接口与宿主机共享同一个 MAC 地址
### Private Mode
私有模式下，Macvlan 接口可以与宿主机通信，但不能与其他同一物理网络上的设备通信。它与其他设备隔离，并且有自己独立的 MAC 地址
### VEPA
VEPA 模式下，虚拟接口将数据包发送到宿主机的虚拟交换机（vSwitch），由该交换机进行转发。这种模式需要支持 VEPA 的硬件或者虚拟交换机。
### Passthrough
透传模式允许 Macvlan 接口直接与物理网络通信，绕过宿主机。这使得虚拟机可以直接在物理网络上工作，但需要特殊硬件支持（如 SR-IOV）
PS:透传不同于P2P。，透传模式是一种虚拟化技术，允许虚拟机绕过宿主机直接访问物理网络，而 P2P 是一种通信模型，描述了节点之间直接通信的方式。透传模式通常在虚拟化环境下用于提供对物理网络的直接访问，而 P2P 则涉及到节点之间的直接交流与通信。
# 开始新建
我们先看下这张照片，左边是我的PC，右边是openwrt的，都是可以访问docker容器的(我的环境是光纤接光猫桥接模式然后接入软路由，软路由在接入桥接模式下的AP，PC是插入AP的网线接口中的,因为我软路由暂时只有两个千兆网口)
![Pasted-image-20231126025125.png](5搁置的网站上传项目/Docker的brige改为macvlan需要优化/将Docker的Brige网络改为macvlan网络（文章需优化）/Pasted-image-20231126025125.png)
![Pasted-image-20231126030153.png](5搁置的网站上传项目/Docker的brige改为macvlan需要优化/将Docker的Brige网络改为macvlan网络（文章需优化）/Pasted-image-20231126030153.png)
名字任意，然后网络我们可以设置为与自网络的网段一样的，这样我们的其它设备可以更方便的访问我们的docker容器（不需要再一次路由）
下面是重点：
```
名字任意
驱动改为macvlan
基础设备改为我们的brlan网桥
模式改为桥接（支持macvlan）
子网改为和上网地址一样的网段
网关一定不能和网桥的IP一样，一旦一样，后台就进不去了，这里切记！切记!
MACVLAN的容器和宿主网络是不通的！注意是宿主之间的网，不是和宿主的网络。（但是是可以配置完成通信的）
IP范围可以不写(你也可以把掩码改为/28)，且这里如果规划了范围不清晰容易和使用网络的设备造成IP冲突，我这边每次使用的时候手动指定一个IP给容器，然后在网络网段给这个IP加上不参与DHCP即可.
```
![Pasted-image-20231126030542.png](5搁置的网站上传项目/Docker的brige改为macvlan需要优化/将Docker的Brige网络改为macvlan网络（文章需优化）/Pasted-image-20231126030542.png)
创建完成后的新接口
![Pasted-image-20231126031603.png](5搁置的网站上传项目/Docker的brige改为macvlan需要优化/将Docker的Brige网络改为macvlan网络（文章需优化）/Pasted-image-20231126031603.png)
这边已死，网关只跟初始设置有关，这边改不了的怎么点都不行的。
![Pasted-image-20231126031715.png](5搁置的网站上传项目/Docker的brige改为macvlan需要优化/将Docker的Brige网络改为macvlan网络（文章需优化）/Pasted-image-20231126031715.png)
查看防火墙，可以看到docker_macvlan被划分到了lan的域中，也就是所有在macvlan中的容器可以直接通外网的。（注意，直接.）
![Pasted-image-20231126031850.png](5搁置的网站上传项目/Docker的brige改为macvlan需要优化/将Docker的Brige网络改为macvlan网络（文章需优化）/Pasted-image-20231126031850.png)
这边我们为Docker添加一下qbittorrent试一下
![Pasted-image-20231126032521.png](5搁置的网站上传项目/Docker的brige改为macvlan需要优化/将Docker的Brige网络改为macvlan网络（文章需优化）/Pasted-image-20231126032521.png)
可以看到，它默认是使用网桥来映射的端口来开放服务
![Pasted-image-20231126032624.png](5搁置的网站上传项目/Docker的brige改为macvlan需要优化/将Docker的Brige网络改为macvlan网络（文章需优化）/Pasted-image-20231126032624.png)
这边我们改为macvlan之后，发现没有暴露端口了，也就是说此时，相当于一个独立的主机了。
![Pasted-image-20231126032703.png](5搁置的网站上传项目/Docker的brige改为macvlan需要优化/将Docker的Brige网络改为macvlan网络（文章需优化）/Pasted-image-20231126032703.png)
我们给他个IP地址
![Pasted-image-20231126032818.png](5搁置的网站上传项目/Docker的brige改为macvlan需要优化/将Docker的Brige网络改为macvlan网络（文章需优化）/Pasted-image-20231126032818.png)
修改环境变量
前两行可以删掉，因为我们openwrt默认权限就是root。TimeZone可以改为Asia/Shanghai
![Pasted-image-20231126033129.png](5搁置的网站上传项目/Docker的brige改为macvlan需要优化/将Docker的Brige网络改为macvlan网络（文章需优化）/Pasted-image-20231126033129.png)
![Pasted-image-20231126033010.png](5搁置的网站上传项目/Docker的brige改为macvlan需要优化/将Docker的Brige网络改为macvlan网络（文章需优化）/Pasted-image-20231126033010.png)
绑定挂载点
![Pasted-image-20231126034241.png](5搁置的网站上传项目/Docker的brige改为macvlan需要优化/将Docker的Brige网络改为macvlan网络（文章需优化）/Pasted-image-20231126034241.png)