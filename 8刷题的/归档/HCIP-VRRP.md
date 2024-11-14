vrrp的master故障的时候是另一台先发送arp检测，然后backup才会切换过去【 Backup设备会等待Master-Down interval再切换为Master】

==VRRP==的协议号是==112==
目前vrrp协议只有两个版本，==一个v1，一个v2==
VRRP没有slaver角色，是==master和backup==
VRRP==V2:ipv4 支持认证==
VRRP==V3:ipv4+ipv6 不支持认证==
==默认模式为抢占(但如果不说具体，如法判断)==

master响应+转发虚拟ip的arp请求
backup丢弃+不转发虚拟ip的arp请求




【错误】即使该路由器已经是Master,也会被优先级高的Backup路由器抢占 【虽然vrrp默认抢占，但是这个不知道】

【错误】C、vrrp vrid 1 track bfd-session-name 1 reduced 100
【正确】D、vrrp vrid 1 track bfd-session session-name 1 reduced 100

配VRRP抢占时延的命令是
==vrrp vrid 1 preempt-mode timer delay 20==
vrrp vrid 1 timer delay20
vrrp vrid 1 preempt-timer 20
vrrp vrid 1 preempt-delay20

现有两台华为设备R1和R2组成一个VRRP备份组，R1为VRRPv2版本，R2为VRRPv3版本。以下
关于该备份组的描述，错误的是哪一项？  （20分）【默认情况V2V3不是互通的】
R2配置命令vrrp version-3 send-packet-mode v2v3-both后，可与R1交互VRRP报文
R2配置命令vrrp version-3 send-packet-mode v3-only后， 不可与R1交互VRRP报文
R2配置命令vrrp version-3 send-packet-mode v2-only后，可与R1交互VRRP报文
==缺省情况下.R1和R2可交互VRRP报文==

以下关于VRRP版本的描述，错误的是哪一项？
VRRPv2发送通告报文的时间间隔是以秒为单位
VRRPv3不支持认证功能
==VRRPv2适用于IPv4和IPv6两种网络==【VRRPv2仅适用于IPv4网络，VRRPv3适用于IPv4和IPv6两种网络。】
VRRPv2支持认证功能


VRRP虚拟路由器配置VRID是3，虚拟IP地址是100.1.1.10，那么虚拟MAC地址是以下哪一项？
00-00- 5E-00-01-64

==00-00-5E-00-01-03==
01-00-5E-00-01-64
01-00-5E-00-01-03

下列关于VRRP的描述错误的是
VRRP是一种冗余备份协议，为具有组播或广播能力的局城网如以太网设计保证当局城网内主机的下一跳路由器设备出现故障时，可以及时的有另一台路由器来代替，从而保持网络通信的连续性和可靠性
==在使用VRRP协议时，需要在路由器上配置虚拟路由器号和虚拟IP地址，直接使用主路由器的真实MAC,这样在这个网络中就加入了一个虚拟路由器==【不用真实mac】
网络上的主机与虚拟路由器通信，不需要了解这个网络上物理路由器的所有信息【易错】
一个虚拟路由器由一个主路由器和若干个备份路由器组成，主路由器实现真正的转发功能，当主路由器出现故障时，一个备份路由器将成为新的主路由器并接替他的工作

关于VRRP master设备的描述，错误的是
定期发送VRRP报文
以虚拟MAC地址响应对虚拟IP地址的ARP请求
转发目的MAC地址为虚拟MAC地址的IP报文
==即使该路由器已经是Master,也会被优先级高的Backup路由器抢占==【没有指明是抢占模式还是非抢占模式下，描述不严谨】

以下关于VRRP工作过程的描述，错误的是哪一项？
稳定后的Master设备会周期性发送通告报文
VRRP备份组中，首先会根据VRRP优先级选举Master设备
原Master设备发生故障后，新Master设备会立即发送ARP报文
==若Master设备发生故障，Backup设备会立即切换为Master设备==【不会立刻切换】


以下关于VRRP负载分担的描述，错误的是哪一项？
==同一台VRRP设备在加入多个备份组时的优先级需保特一致==
台VRRP设备可担任多个备份组的Master设备【vrrp可以一台多个备份组】
VRRP负载分担与VRRP主备备份的报文协商过程一致
为保证业务正常，每个VRRP备份组中有且只有一个Master设备

在VRRP中，当设备状态变为Master后，会立刻发送免费ARP来刷新下游设备的MAC表项，从而把用户的流量引到此台设备上来【正确】

【错误】VRRP中当两台优先级相同的设备同时竞争Master角色时，则iP地址较小的接口所在的设备应当被选为Master设备【ip地址大的被选为master】


~~补充:**Skew_Time** 是在 VRRP 中使用的一种**延迟机制**，用于避免多台备份路由器同时争夺成为 Master。当备份路由器收到优先级为 0 的报文时，实际的接管时间由 **Skew_Time** 决定，而不是立即切换。~~
