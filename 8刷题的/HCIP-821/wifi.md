# 802.1x和RADIUS
单选题274/1247、关于802.1x和RADIUS两种技术的关系，下列选项描述正确的是：
802.1X和RADIUS是同种技术的不同名称
802.1X是一个技术体系，它包含了RADIUS技术
RADIUS是一个技术体系，它包含了802.1X技术
**802.1X和RADIUS是不同的技术，但经常配合在一起使用共同完成对终端用户的准入控制**
<u>802.1X和RADIUS是不同的技术，通常radius 作为服务器端进行验证，802.1X 作为准入控制。</u>
<u>802.1X该协议主要用于局域网（LAN）和无线局域网（WLAN）中，为用户提供安全的网络接入控制，尤其是在企业、学校、公共热点等需要对用户进行身份验证的环境中。
RADIUS（Remote Authentication Dial In User Service）是一种认证、授权和计费（AAA）协议，它提供了一种标准方法来集中处理用户认证、授权和计费的过程</u>


# Agile Controller
单选题277/1247、在Agile Controller的无线准入控制场景中推荐使用下列哪种方式控制企业内部员工和访客接入网络？
根据不同的用户名控制接入
根据无线终端MAC地址是否注册控制接入
**为内部员工和访客设置不同的SSID控制接入**
根据无线终端的类型控制接入
<u>一般都是通过设置访客SSID和内部SSID来控制接入 Agile Controller作为一个先进的网络控制平台，能够很好地支持这种基于SSID的网络策略实施，它不仅能够控制接入，还可以实现精细化的流量管理和安全策略，从而提升网络的安全性和效率。</u>

# AR路由器上应用策略的命令
单选题
282/1247、在AR路由器接口上应用流策略的命令是
**Traffic-policy p1 inbound**
Traffic classifer p1 inbound
Traffic behavior p1 inbound
services-policy p1 Inbound
![image-2024718440254.png|350](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/wifi/image-2024718440254.png)
# 漫游组
单选题323/1247、以下关于漫游组服务器的描述，错误的是哪一项？
**AC在设置为漫游组服务器后，将默认加入漫游组并可以管理其他AC**
一个AC可以同时担任多个漫游组的漫游组服务器
漫游组服务器需维护漫游组的成员表
漫游组服务器是通过CAPWAP隧道管理各个AC的
<u>漫游组服务器管理其他AC的同时不能被其他的漫游组服务器管理。也就是说如果一个AC是作为漫游组服务器角色负责向其他AC同步漫游配置的，则它无法再作为被管理者接受其他AC向其同步漫游配置（即配置了漫游组就不能再配置漫游组服务器）</u>

# AP启动异常
单选题238/1247、在WLAN组网中，某工程师发现AP启动异常，则失败原因不包括以下哪一项？
**供电方不支特PoE功能**~~~~
供电方输出电源功率不足
**AP上线失败**
供电方发生故障


# dhcp配置，dhcp池已有掩码
单选题
136/1247、某台PC的MAC地址是5489-98FB-65D8，管理员希望这台PC从DHCP服务器获得指定IP地址192.168.1.11/24所以
管理员配置的命令应该是？
dhcp static-bind ip-address 192.168.1.11 24 mac-address 5489-98FB-65D8
---正确---dhcp server static-bind ip-address 192.168.1.11 mac-address 5489-98FB-65D8
dhcp server static-bind ip-address 192.168.1.11 255.255255.0 mac-address 5489-98FB-65D8
dhcp static-bind ip-address 192.168.1.11 mac-address 5489-98FB-65D8

解析：在DHCP服务器中配置了全局地址池的掩码或接口中配置了IP地址，所以在绑定时不需要配置掩码信息。
# dhcp流程
单选题1159/1247、DHCP协议运行过程中，客户端从申请到获得IP地址时的流程是：
①主机发送DHCP Request请求IP地址
② Server发送DHCP Offer报文响应
③主机发送DHCP Discover报文寻找DHCP Server
④ Server收到请求后回应ACK响应请求
**③-②-①-④**
①-②-③-④
①-④-③-②
③-④-①-②
# dhcp续约第二次
单选题
257/1247、在DHCP运行过程中，如果客户端IP地址在相约过去87.5%还没有完成续约的话，客户将发送什么报文进行再次续约
DHCP discover广播报文
DHCP release单播报文
**DHCP request广播报文**
DHCP request单播报文
<u>1. 当IP地址租期剩余50%时，客户端会尝试通过单播发送DHCP Request消息给DHCP服务器，以更新租约（T1状态）。
2. 如果在租期剩余75%时，客户端仍未收到DHCP服务器的确认，它会再次尝试更新租约，这次通过广播发送DHCP Request消息（T2状态），因为此时可能客户端不知道DHCP服务器的确切位置。</u>
# DHCP报文
单选题258/1247、在DHCP运行过程中，会交互多种报文类型，那么下列那些报文不是从客户端发往服务器的？
**DHCP NAK**
DHCP REQUEST
DHCP DISCOVER
DHCP RELEASE
<u>DHCP NAK：服务器对客户端的请求报文的确认响应报文。  
DHCP REQUEST：客户端初始化后，发送广播的DHCP REQUEST报文来回应服务器的DHCP OFFER报文。  
DHCP RELEASE：客户端可通过发送此报文主动释放服务器分配给它的IP地址。  
DHCP DISCOVER：DHCP客户端首次登录网络时进行DHCP交互过程发送的第一个报文。
</u>
# dhcpv6
单选题250/1247、以下关于DHCPv6地址分配过程的描述，**正确**的是哪一项？
**DHCPv6服务器发送携带了地址和配置信息的Reply消息来回应从DHCPv6客户端收到的Request报文**
如果需要续租从DHCPv6服务器获取到的地址，会在T1时刻发送Rebind报文请求租约更新
DHCPv6客户端使用Soliciti报文来确定DHCPv6服务器的位置，报文的目的IPv6 地址为FF02::1:3
如果DHCPv6服务器收到了客户端发来的Rebind报文，且服务器确认客户端可以继续使用该地址，则向客户端发送confirm报文以告知客户端
<u>DHCPv6客户端想要续租IPv6 地址，首选发送的是Renew报文
表示DHCPV6服务器的组摇IP 地址是FF05:13
DHCP的Confirm 报文，是由客户端发送的，不是服务器发送的
DHCPv6服务器使用Reply报文包含IPv6 地址和配置信息， 然后返回给客户端。</u>
# DHCP租期 一天
单选题71/1247、DHCP地址池租期默认是多久？
1个月
1小时
1周
**1天** 


# 新增AP选择AC
![image-20247202359826.png](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/wifi/image-20247202359826.png)
随机接入
**AC1**
都不会接入
AC2
<u>AP根据AC优先级选择AC，优先级取值范围0~7，取值越小优先级越高，因此新AP会选择AC1进行接入</u>

# option43字段 
单选题511/1247、在WLAN网络中，当AC和AP之间是IPV4三层组网时，用户需要配置Option43字段，其主要实现的是以下哪一功能？
设置DNS服务器地址选项
**设置厂商自定义选项**
设置网关地址选项
设置子网掩码选项
<u>1：设置子网掩码选项。
3：设置网关地址选项。
6：设置DNS服务器地址选项。
43：设置厂商自定义选项。
AC与AP不在同一个网段时，需要通过配置option 43字段为AP指定AC的IP地址，否则AP无法发现AC
</u>

# ap检测到超时需要花费时间
单选图 534/1247、在WLAN网络中配置双链路热备时，工程师配置CAPWAP心跳检测的问隔时问为20秒，并使用默认次数进行检测，
此时使能双链路备份功能，则AP检测到主链路超时从而进行主备切换需要花费多长时间？
20秒
90秒
**60秒**
75秒
<u>缺省情况下，CAPWAP心跳检测的间隔时间为25秒，心跳检测报文次数为6。如果开启了双链路备份功能，则缺省情况下，CAPWAP心跳检测的间隔时间为25秒，心跳检测报文次数为3。本题中时间为20秒且配置CAPWAP，故时间为60秒。</u>

# 判断题----------------------------------------------------
判断题 902/1247、在WLAN组中配置双链路热备时 AP会与主AC和备份AC分别建立CAPWAP链路。
**正确**
<u>描述是对的，双链路热备场景，AP都会与主AC和备份AC分别建立CAPWAP链路</u>
判断题904/1247、在WLAN组网中配置双链路热备时，配置AC优先级的数值越大，则AC的实际优先级就越高
**错误**
<u>选择AC的主备关系的时候，优先级的数值越小越优先</u>

判断题947/1247、以下关于双链路热备配置，在配置AC的优先级时，优先级的数值越大该AC的实际优先级就越高
**错误**
<u>优先级的数值越大，该AC的实际优先级就越低</u>

判断题962/1247、双链路热备时，AP会与主AC、备份AC建立CAPWAP链路。
**正确**
<u>AP与双链路备份组网中的主AC建立CAPWAP主链路，主AC上配置了另一个AC的IP地址，该AC为备AC。AP持续向备AC发送Discover request 报文，直到备AC回复Discover response报文，AP与备AC成功建立CAPWAP链路作为备链路。</u>

判断题 980/1247、DHCP中继负责转发DHCP服务器和DHCP客户端之间的DHCP报文，协助DHCP服务器向DHCP客户端动态分配网络参数。
**正确**
<u>DHCP中继，解决客户端和dhcpserver不在同一网段的问题</u>

判由
81/1247在wlan大型组网中，vlan pool采用hash方式分配vlan的话，每个vlan用户数的数目会被均匀划分？
**错误**
<u>不会被均分</u>

判断题 1053/1247、在WLAN网络中有两台AC和多台AP时，配置主备方式的组网是将一半AP规划AC1为主AC、AC2为备AC,另一半AP规划AC2为主AC、AC1为备AC，从而提高AC资源利用率。
**正确**
<u>应该使用双链路热备份、VRRP热备份、双链路冷备份和N+1备份保证可靠性。</u>

1105/1247、在WLAN网络中，使能HSB备份组，若AP已经在主AC上上线之后，再在备AC上离线添加AP信息后，备AC上的AP状态会显示为fault。 此时需要在备AC的HSB备份组视图 下先执行undohsb enable命令去使能HSB主备备份功能 ，再执行hsb enable命令使HSB主备备份功能 ， 此时，主AC上的信息会备份到备AC，实现主备信息备份一致，AC上的AP状态会显示为standby
**正确**
<u>AP状态不能自动备份，需要在备AC上事先离线添加AP，否则AP永远不会变成STANDBY状态。AP在主备AC上线之前，需要先在主备AC上都完成离线添加。若AP已经在主AC上上线之后，再在备AC上离线添加AP信息，备AC上的AP状态会显示为fault。此时需要在备AC的HSB备份组视图先执行undo hsb enable命令去使能HSB主备备份功能，再执行hsb enable命令使能HSB主备备份功能，重新将主AC上的信息备份过来，实现主备信息备份一致，此时备AC上的AP状态会显示为standby，所以题目中的描述是正确的。</u>

判断题1113/1247、在WLAN网络中使能HSB备份组时，若AP在主AC上线之后，再在备AC上离线添加AP信息，则备AC上的AP状态
会显示为fault
**正确**
<u>需要上线前两个都完成备份组的配置</u>

填空题1173/1247、现需将源接口IP地址为10.1.200.100的AC1和源接口IP地址为10.1.200.200的AC2加入到HuaWei漫游组，其配置如图下。则空格处应配置命令（）（英文，全小写）
```
[AC1-wlan-view]mobility-group  name Huawei
[AC1-mc-mg-mobility]___ip-address 10.1.200.100
[AC1-mc-mg-mobility]___ip-address 10.1.200.200

[AC2-wlan-view]mobility-group  name Huawei
[AC2-mc-mg-mobility]___ip-address 10.1.200.100
[AC2-mc-mg-mobility]___ip-address 10.1.200.200
```
**member**

填空题1194/1247、如果在两个AP之间实现漫游，必须要满足相同的安全策略转发模式以及相同的（）（若涉及到英文单词，清使用大写)
**SSID**
<u>vSSID才不需要重新输入密码，例如学校所有的wifi都是一样的名字</u>