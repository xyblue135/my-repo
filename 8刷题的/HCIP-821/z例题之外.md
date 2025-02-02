# 扩展知识
![image-2024714459703.png|425](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/%E4%BE%8B%E9%A2%98%E4%B9%8B%E5%A4%96/image-2024714459703.png)
STA- FAP-FAC-HAC -HAP- 上层网 络
**STA-FAP-FAC-HAC-上层网络**
STA-FAP-FAC-上层网络
STA- FAP-FAC-HAC -HAP-HAC- 上 层网络
<u>解析:FAC直接通过隧道把报文转发给HAC，HAC直接将业务报文发送给上层网络。</u>
STA（Station）：指的是无线网络中的终端设备，如笔记本电脑、智能手机、平板电脑等。
FAP (Fixed Access Point)**固定接入点**：通常指那些安装在固定位置的接入点，主要用于提供无线网络覆盖。
HAP (Home Access Point)**家庭接入点**：专为家庭或小型办公室设计的接入点。
FAC（Functional Acceptance Criteria）和 HAC（Hardware Acceptance Criteria）是不同领域中用于质量和性能评估的标准和要求。
FAC (Functional Acceptance Criteria) 硬件
HAC (Hardware Acceptance Criteria) 功能

判断题1045/1247、STA在WLAN漫游后，若想继续访问家乡网络，则可将HAC或HAP设置为家乡代理。
**正确**
如果HAP和HAC在同一个子网时，可以将家乡代理设置为性能更强的HAC，减少HAP的负荷并提高转发效率。用户漫游到其他AP后，默认以HAP作为家乡代理。用户漫游时自动在FAP和家乡代理间建立一条隧道，用户的流量通过家乡代理中转，以保证用户漫游后仍能访问原网络。
# ip报文头部 协议号ESP和AH  AH!
说法正确的是
![image-20247141818523.png|375](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/%E4%BE%8B%E9%A2%98%E4%B9%8B%E5%A4%96/image-20247141818523.png)
该报文一定是只有AH时封装的IPseC VPN报文
**协议号是51，代表该ip header后的报文为AH头部**
协议号:50 ESP
协议号:51 AH
协议号51 代表该IPHeader 后的报文为ESP头部
该报文为IPseC VPN报文，并且该报文的数据部分被加密了
<u>AH（Authentication Header）和 ESP（Encapsulating Security Payload）是IPSec（Internet Protocol Security）协议中的两种主要协议，用于确保IP网络上的通信安全。它们通过不同的方式提供数据完整性、数据源验证和（在ESP的情况下）数据加密。IP协议号51和50分别用于标识AH和ESP流量。以下是对它们的详细解释：
协议号50是ESP，51是AH</u>


# 链路聚合
下列说法错误的是？
链路聚合是将一组物理接口捆绑在起作为一个逻辑接口来增加带宽及可靠性的方法，
链路聚合遵循lEEE802.3ad协议
将若十条物理链路捆绑在一起所形成的逻辑链路称之为链路聚合组（LAG）或者Trumk
**链路聚合只存在活动接口**
<u>解析:在链路捆绑技术中，可以存在一部分链路用于数据转发，一部分链路专门用于备份。所以选项“链路聚合只存在活动接口”的描述是错误的。</u>

单选题 392/1247、以下关于LACP模式的链路聚合的描述，正确的是哪一选项？
**LACP模式下链路两端的设备相互发送LACP报文。**
LACP模式下不能设置活动端口的数量
LACP模式下所有活动接口都参与数据的转发，分担负载流量。
LACP模式下最多只能有4个活动端口。
<u>LACP模式下最多可以有8个活动端口，并且可以设置M:N的活动与备份端口数量，LACP设备会互相发送LACP报文进行协商。  
手工模式下所有活动接口才会都参与数据的转发，分担负载流量。</u>

# 端口隔离
华为交换机提供配置端口隔离的功能，关于端口隔离描述错误的有

：
端口隔离模式可以配置为二层三层都隔离或者二层隔离三层互通
------------错误-------华为交换机支持64个隔离组，编号为0-63
若在接口A上配置它与接口B隔离，则从接口A发送的报文不能到达接口B但从接口B发送的报文可以到达接口A
接口单向隔离支持
GE、XGE和Eth-Trunk三种类型的接口混合隔离，但不支持接口与自身单向隔离、接口与管理网 口单尚向隔高、Eth-Trunk
与自身成员接口单向隔离

解析华为交换端口隔离编号为1-64


# 路由器匹配判断
单选题
59/1247、下面是一台路由器的部分配置，关于该部分配置描述正确的是
[HUAWEl] ip ip-prefix pl permit 10.0.192.0/8 greater-equal 17 less-equal 18
10.0.192.0/8网段内，掩码长度为20的路由会匹配到该前缀列表，匹配规则为充许
---正确---10.0.192.0/8网段内，掩码长度为18的路由会匹配到该前缀列表，匹配规则为允许
10.0.192.0/8网段内，掩码长度为19的路由会匹配到该前缀列表，匹配规则为允许
10.0.192.0/8网段内，掩码长度为21的路由会匹配到该前缀列表，匹配规则为充许

配置名为P1的10.0.192.0/8网段内，掩码长度大于等于17小于等于18的路由匹配到该前缀列表，匹配规则为允许。


单选题
65/1247、使用如下所示的IP前缀列表进行路由匹配，则以下哪项路由可以被匹配到？
Ip ip-prefix List1 index 10 permit 192.168.1.0 24 greater-equal 24 less-equal 27
192.168.2.0/24
192.168.3.0/25
---正确---192.168.1.0/27
192.168.1.0/23

单选题
85/1247、 
前缀列表(ip ip-prefix)的命令格式为 ip ip-prefix ip-prefix-name[index index-number] {permit|deny}ipv4-address mask-length [greater-equal greater-equal-value][less-equal less-equal-value] ，如果仅指定了 greater-equal 未指定less-equal，则前缀范围为 （D)
[0.greater-equal-value]
无限制
[mask-length,greater-equal-value]
---正确---[greater-equal-value.32]

如果仅指定了greater-equal-value则代表掩码范围是大于等于指定的到32位

# 不适合部署策略路由
单选题
61/1247、以下哪个场景不适合部署接口策略路由？
企业网络多ISP出口的场景下，内网不同的网段通过不同的ISP出口访问互联网
---错误---修改本地始发的流量下一跳
在核心交换机上将内网和外网相互访问的流量牵引到旁挂的AC设备上
在核心交换机上将内网和外网相互访问的流量牵引到旁挂的安全检测设备上
# 策略路由特点
66/1247、关于路由策略的特点描述，正确的是

应用命令policy-based-route  # 这只是一个命令而已
---正确---基于目的地址按路由表转发  # 强说的话还是有点问题，不仅仅基于
需要手工逐跳配置，以保证报文按策略转发 # 大多数情况下并不需要逐跳手工配置。
基于转发平面为转发策略服务  # 路由策略是在控制平面（而不是转发平面）上实施的，用于决定哪些路由应该被接受、拒绝或修改。

相比较来说，但其实都有带你问题









# ASPF和Servermap
单选题 93/1247、 ASPF(Application Specific Packet Filter)是种基于应用层的包过滤，它会检查应用层协议信息并且监控连接的应用
层协议状态，并通过Server Map表实现了 特殊的安全机制。那么关于ASPF和Server map表的说法，**错误**的是
ASPF动态创建和删除过滤规则
ASPF通过Servermap表实现动态允许多通道协议数据通过
ASPF监视通信过程中的报文
**五元组里Server-map表项实现了和会话表类似的功能**  （五元组 源目ip端口+协议）
<u>解析：
Server-map是为特殊应用能够安全顺利通过防火墙而产生的一种动态、特殊的会话表项。所以选项“五元组里Servermap表项实现了和会话表类似的功能”的说法是错误的。  
报文到达防火墙，先查看是否会有会话表匹配。  
如果有会话表匹配，则匹配会话表转发；如果没有匹配会话表，看是否能够创建会话表。  
前提是必须是首包才能创建会话表。  
先匹配路由表，再匹配安全策略。
二次解析：
server Map 表则侧重于应用层会话的状态和细节管理。因此，“Server Map 表项实现了和会话表类似的功能”这句话不完全准确，因为它们虽然都有跟踪会话的功能，但具体的实现和应用场景有显著的差异。
</u>

单选题465/1247、以下关于ASPF和Server-map的描述，正确的是哪一项？
**会话表是通信双方连接状态的具体体现**
Server-map表是防火墙根据会话表生成的
报文命中Server-map表后，需要受安全策略的控制
防火墙收到报文会检查是否命中Server-map表

单选题386/1247、 Server-Map根据以下哪一组参数生成？
源目MAC地址、源目IP地址和源目端口号
源目MAC地址、源目IP地址 和协议类型
**源目IP地址、 源目端口号和协议类型**
源目MAC地址、源目端口号和协议类型
<u>Server map是防火墙用来转发数据包的，因此需要知道目的IP、目的端口号、协议号即可。 此处只有C符合</u>
# 传统流量统计局限性
单选题
102/1247、以下关于传统流量统计局限性的描述，错误的是哪一项？

对于ACL规则以外的流量无法统计
---错误---需要消耗设备的接口，对于无法镜像的端口需要购买配套设备接入，成本高
基于IP报文计数，统计的信息简单，无法针对多种信息进行统计
通过SNMP协议进行流量统计，要不断的通过轮询向网管查询，浪费CPU和网络资源

解析：是对无法镜像的接口根本无能为力
![image-20247143641792.png|500](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/%E4%BE%8B%E9%A2%98%E4%B9%8B%E5%A4%96/image-20247143641792.png)
# 路由选择工具
用于过滤路由信息的是

---正确的---route-policy：用于过滤路由信息以及为通过过滤的路由信息设置路由属性  
As-path-filter：用于为对等体（组）设置基于AS路径列表的BGP路由过滤策略  
Policy-based-route：策略路由，可以根据管理员定义的策略条件来选择性的转发数据包  
Ip-prefix：指定地址前缀列表的名称

单选题
114/1247、下面是关于路由选择工具的描述其中表述错误的是

---错误---route-policy只能匹配路由和数据包，并不能用来修改路由属性或者数据包的转发行为
前缀列表(ip-prefix)匹配对象为路由信息的目的地址
访同控列表（ACL)用于匹IP路由信息或者数据包的地址
as-path-filter是用来匹配BGP路由信息中的AS-PATH属性的，所以它只能用于过滤BGP路由

解析：Route-policy：用于过滤路由信息以及为通过过滤的路由信息设置路由属性。
所以是可以修改的



单选题120/1247、下面关于各个协议下发缺省路由的配置命令，描述错误的是
在ISIS协议中， default-route-advertise命令用来将缺省路由信息通告给邻居
**ip route-static default preferencer命令用来在当前路由器生成一条缺省路由**
在OSPF协议中，default-route-advertised命令用来将缺省路由信息通告到普通OSPF区域
在BGP协议中， default-route imported命令用使能将省路由引I入到BGP路由表中的功能
解析：ip route-static default-preference，不是用来产生默认路由，而是用来修改默认路由的优先级的。、



# display current-configuration|clude vlan
单选题
123/1247、 display current-configurationlinclude vlan命令的含义是？

查看各VLAN下绑定的物理接口信息
---正确---查看所有包含"VLAN"关键字的配置
查看当前创建了哪些VLAN
查看VLANIF接口的IP地址







# URPF
单选题244/1247、 以下关于URPF （Unicast Reverse Path Forwarding） 的描述，正确的是哪一项？
**如果部署严格模式的URPF，也能够可以同时部署允许匹配缺省路由模式**
如果部署松散模式的URPF，默认情况下不需要匹配明细路由
如果部署松散模式的URPF，如果需要检查默认路由，则需要检查接口是否让匹配
如果部署严格模式的URPF，只要报文能够匹配<u></u>明细路由，即可认定该IP地址合法，并充许转发该报文
<u>解析:松散模式的URPF，默认情况下需要匹配明细路由，如果需要检查默认路由，则不需要检查接口是否匹配，所以BC错误。  
部署严格模式的URPF需要验证路由表中是否存在IPv4数据包的源IPv4地址，并且源IPv4地址可以通过输入接口，故D错误。
URPF（Unicast Reverse Path Forwarding）是一种网络技术，用于防止源地址欺骗和拒绝服务（DoS）攻击。URPF的工作原理是在路由器上检查传入的数据包的源IP地址，验证是否可以从该接口接收到从这个源地址发来的数据包。它通过反向查找路由表，确认数据包的源地址是否有效。
</u>
# ip报文分类
单选题259/1247、在网络层，以下不可以用来对IP报文进行分类的有
报文长度
**VLANID**
源IP地址和目的IP地址
ToS字段
<u>VLAN ID 属于二层技术参数 ，对IP报文进行分类需要使用报文 长度、源IP地址和目的IP地址、TOS字段等三层参数。所以正确答案是“VLAN ID”。</u>
# 远程端口镜像功能 
单选题260/1247、在华为路由器上配置远程端口镜像功能，实现将远程端口镜像出去的报文，可以通过三层IP网络传送到家监控设备，
其命令是
Mirror-server destination-ip 10.1.0.1 source-ip 192.168.1.1
monitorr-server destination-ip 10.1.0.1 source-ip 192.168.1.1
**Observe-server destinattion-ip 10.10.1 source-ip 192.168.1.1**
erver destination-ip 10.1.0.1 source-ip 192.168.1.1
<u>通过observe-server 实现远程端口镜像出去的报文可以通过三层IP网络传送到监控设备。</u>


单选题342/1247、以下关于路由策略特点的描述，错误的是哪一项？
能通过控制路由器的路由表规模，来节约系统资源
能通过修改路由属性，对网络数据流量可以合理规划，以提高网络性能
**能够修改路由属性，但是不能改变网络流量经过的路径**
能通过控制路由的接收、发布和引入，以提高网络的安全性
<u>修改路由属性，可以从控制层面控制接收者收到的路由信息，从而影响路由的选路</u>

# PBR
单选题
351/1247、 以下关于PBR（Policy-Based-Routing)的描述正确的是哪一项？
PBR每个节点内只能包含一个条件语句（if-match）
PBR节点之间的关系为 “与”
**PBR每个节点在没有配置执行语句（apply)时不执行任何动作**
PBR的条件语句（if-match)可以匹配ACL和前缀列表
<u>每个节点内可包含多个条件语句。节点之间的关系为“或”。
节点内的多个条件语句之间的关系为“与”。本地策略路由支持基于ACL或报文长度的匹配规则。
策略路由(PBR)的操作对象是数据包，所以if-match后面是可以跟ACL，但是不可以跟ip-prefix；
每个节点/条目中，可以有apply语句，就是修改数据包；如果没有，则不做任何动作，直接转发。</u>

单选题444/1247、以下关于PBR不同分类的描述，正确的是哪一项？
接口PBR调用在接口下，对接口的出方向报文生效
PBR可以分为接口PBR、本地PBR以及路由PBR
**接口 PBR可以修改IP报文的IP-Precedence**
本地PBR对始发的报文无效，只对转发的报文起作用
<u>接口PBR，只对转发的报文起作用，对本地始发的报文无效。接口PBR调用在接口下，对接口的入方向报文生效，对出接口方向已经放出，无法执行策略PBR为策略路由，可以是基于标准和扩展访问控制列表，也可以基于报文的长度；而转发策略则是控制报文按照指定的策略路由表进行转发，也可以修改报文的IP优先字段。本地PBR可以对本地报文有效</u>


# 不适合接口策略路由
单选题352/1247、以下哪一场景不适合部署接口策略路由？
企业网络多ISP出口的场景下，内网不同的网段通过不同的ISP出口访问互联网
**两个不同的OSPF域实施多点双向重分发**
在核心交换机上将内网和外网相互访问的流量牵引到旁挂的AC设备上
在核心交换机上将内网和外网相互访问的流量牵引到旁挂的安全检测设备上
~~基于接口的策略路由可以修改流经设备的数据转发，而选项“两个不同的OSPF域实施多点双向重分发，或修改本地始发的流量下一跳”是指从本设备发起的数据，该情况适合本地策略路由而非基于接口的策略路由。~~

# 正则表达式
单选题 363/1247、某台BGP设备配置了ip as-path-filter 1 permit ^12.*35$命令，那么以下哪一项的AS_ Path可以被正确匹配？
AS _ Path(123 35 28)
AS Path(35 123 28)
AS Path(35 28 12)
**AS _ Path(12 28 35)**
<u>^12表示以12开头，35$表示以35结尾。</u>

单选题 381/1247、一般情况下，一个接口只需配置一个主IP地址，但在有些特殊情况下需要配置从IP地址。那么每个三层接口最多可配
置地址数量是以下选项中哪一项？
28
29
30
**31**
<u>无线接入控制器的每个三层接口可以配置多个IP地址，其中一个为主IP地址，其余为从IP地址，每个三层接口最多可配置“31”个从IP地址。</u>

# 关于cost
单选题 393/1247、以下关于路由协议开销值（cost） 的描述，错误的是哪一选项？
通过调整路由的Cost值，可以解诀某些场景中的次优路径问题。
不同路由协议的路由开销的计算方法一般是不同的，所以不同路由协议的Cost值之间没有可比性。
**不同路由协议在互相引入时，必须要手动指定Cost值，否则无法正常引入。**
通常IS-IS和OSPF的开销E基于带宽，取值范围很大，可L以适用于较大规模的网络。
<u>不同路由协议互相引入时，会使用各自协议不同的默认cost描述外部路由</u>

# protal认证
单选题 408/1247、网络接入控制是一种"端到端” 的安全技术，可负责控制用户的接入方式。其中用户需要在Web页面输入用户名和密码完成认证的是以下哪一个认证技术？
**Portal认证**
微信认证
802.1x认证
MAC认证
<u>Portal认证是弹出web页面进行认证，微信认证是通过微信程序进行认证，802.1x认证是通过认证客户端进行认证，MAC认证只需要管理设备上配置，用户的无需配置</u>

单选题462/1247、 Portal认证中有许多定时器，其中可用来防止DoS攻击的是以下哪一种定时器？
**用户静默定时器**
内置Portal服务器 心 跳 探测定时器
Portal服务器探测定时器
用户下线重传定时器
<u>用来防止用户认证失败时频繁认证，形成了一种DoS攻击，浪费系统资源。</u>
# SRV6
单选题416/1247、在华为IP广域承载网络解决方案中，以下哪一种技术主要是保障SLA和承诺时延的？
**SRv6**
FlexE切片
使用大容量全业务NetEngine8000系列设备
A持的智能运维

![1669014171088.png|245](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/z%E4%BE%8B%E9%A2%98%E4%B9%8B%E5%A4%96/1669014171088.png)

# APR是二层的
单选题426/1247、以下攻击方法中，不属于网络层攻击的是哪一种？
**ARP欺骗攻击**
IP欺编攻击
ICMP攻击
Smurf攻击

单选题493/1247、以下关于MAC地址欺骗攻击的描述，错误的是哪一项？
**MAC地址欺骗攻击会造成交换机学习到错误的MAC地址与IP地址的映射关系**
MAC地址欺骗攻击会导致交换机要发送到正确目的地的数据被发送给了攻击者
MAC 地址欺骗攻击主要利用了交换机MAC地址学习机制
攻击者可以通过伪造源MAC地址的数据帧发送给交换机来实施MAC地址欺骗攻击
<u>MAC地址欺骗和IP地址的映射没有关系</u>
# ssh
单选题 450/1247、 SSH协议基本框架不包括以下哪一项？
SSH连接协议
SSH用户认证协议
**SSH用户审计协议**
SSH传输层协议

# if-match apply（route-policy）
单选题474/1247、以下哪一种工具可用于多种路由协议，并且是由if-match和apply子句组成的？
community-filter
as-path-filter
**route-policy**
ip-prefix
<u>Route-Policy的每个节点由一组if-match子句和apply子句组成。</u>

# 路由过滤
单选题487/1247、以下哪一种工具**不能**用于路由过滤？
route-policy
community-filter
ip-prefix
**acl**

# 优选路径MED ，越小越优先
![image-20247205241853.png|450](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/z%E4%BE%8B%E9%A2%98%E4%B9%8B%E5%A4%96/image-20247205241853.png)
无法判断，MED不能作为AS之间BGP选路的条件
优选R3传递的路由，因为MED值越大越优先
负载分担，因为从EBGP收到的路由MED值会恢复缺省值
**优选R2传递的路由，因为MED值越小越优先**
<u>MED值是BGP选路规则的其中之一，越小越优。</u>

# lldp是二层的
单选领531/1247、以下哪一种协议不支持网络配置管理？
**LLDP**
NETCONF
SSH
SNMP
<u>链路层发现协议(LLDP)是一个二层协议,它允许网络设备在本地子网中通告自己的设备标识和性能。 此协议无法进行配置管理</u>

单选题 535/1247、以下哪一项不属于网络安全部署目标？
**确保数据合法性**
确保数据可用性
确保数据保密性
确保数据完整性

# 通配符掩码
单选额536/1247、以下关于通配符掩码的描述，正确的是哪一项？
通配符掩码可直接由二进制子网掩码取反得出
通配符掩码中，0.0.0.0代表所有IP地址
通配符掩码必须由从左到右连续的“1” 和“0“组成，连续的” 1”不可以被"0” 隔开
**通配符掩码中，掩码为设为“0”表示IP地址中相对应的位必须情确匹配**
<u>通配符掩码和普通的掩码地址是相反的，0为必须匹配，1为无须匹配</u>


# 判断题----------------------------------------------------
![image-2024722136897.png|325](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/z%E4%BE%8B%E9%A2%98%E4%B9%8B%E5%A4%96/image-2024722136897.png)
**错误**
<u>SW1发送出去的vlan10，带着标签；被SW2接收，SW2将该数据发送到 VLAN 10的端口中去；SW2发送出去的vlan10,不带标签，因为SW2的Gi0/0/1的PVID是10,所以剥掉标签，然后发送给SW1；SW1收到SW2发送过来的不带VLAN标签的数据，就会使用自己的Gi0/0/1的PVID添加一个标签；SW1发出来的是VLAN10的数据，SW2会认为是VLAN20的数据。所以，SW1和SW2之间的VLAN 10的数据，是没办法进行正常传输的。出现了VLAN间的数据跳跃转发。</u>

判断题 918/1247、当虚拟路由器回应ARP请求时，使用主路由器的真实MAC地址
**错误**
<u>由于在一个VRRP组中，多个路由器需要作为一台虚拟路由器对外提供服务。因此，虚拟路由器回应ARP请求时，使用虚拟路由器的虚拟MAC地址。</u>

判断题919/1247、可以通过发送主备服务报文和重传等机制防止主备AC间的HSB备份通道中断且无法感知的情况
**错误**
<u>通过发送主备服务报文和重传等机制来防止TCP较长时间中断而协议栈没有检测到该连接中断的情况发生，所以题目中的描述是错误的。</u>

判断题 921/1247、策略路由和路由策略都可以影响数据包的转发过程，但它们对数据包的影响方式是不同的。策略路由是基于策略的转发，基于转发平面。路由策略基于控制平面，为路由协议和路由表服务
**正确**
<u>策略路由，指的是某种特殊的路由；针对的是数据转发层面；路由策略，指的是一个策略，通过影响最终的路由选路，影响数据转发；针对的对象是路由。</u>

判断题923/1247、IGP路由要想成为BGP路由，只能通过network命令。
**错误**
<u>IGP是内部网关协议，在AS内部实现路由信息的交换，BGP是边界网关协议，在AS之间实现路由信息的交换。IGP想要成为BGP路由除了network命令还有静态路由和缺省路由等。</u>

判断题936/1247、框式交换机在收到业务报文后，先经过上行接口板处理，然后再经过下行接口板处理，最后从接口发出
**错误**
<u>少了一步，业务报文从接口进入上行接口板处理之后,通过框式交换机内部总线交由交换网板,交换网板交由下行接口板处理之后从接口发出去，所以题目中的描述是错误的。</u>

判断题 937/1247、 iMaster NCE-Campus支持通过NETCONF实现对华为网络设备进行管理，并且支持通过SNMP对第三方设备进行管理
**正确**
<u>iMaster NCE-Campus是针对企业网络推出的SDN控制，可以支持NETCONF的方式控制最新设备，也支持老的网关协议比如SNMP。</u>

判断题973/1247、随板AC指的是华为敏捷交换机内置AC能力，实现有线无线业务的融合管理，有线业务和无线业务流量统一由敏捷交
换机集中管理
**正确**

判断题974/1247、在VRRP中，当设备状态变为Master后，会立刻发送免费ARP来刷新下游设备的MAC表项，从而把用户的流量引到此台设备上来
**正确**
<u>Master设备由一台设备切换为另外一台设备，新的Master设备会立即发送携带虚拟路由器的虚拟MAC地址和虚拟IP地址信息的免费ARP报文，刷新与它连接的主机或设备中的MAC表项，从而把用户流量引到新的Master设备上来，整个过程对用户完全透明</u>

判断题983/1247、BGP AS PATH属性是一种可选过渡属性。
**错误**
<u>AS_Path属性公认必遵属性。</u>

判断题1988/1247、如果一台框式交换机只支持使用主控板上的集群卡建立集群连接，则表示该框式交换机使用的是CSS2堆叠技术。
**错误**
<u>支持CSS2构架的框式交换机采用转控分离的架构，单框内接口板之间流量、跨框流量无需经过主控板，集群系统内单台框式能够正常工作的主控板不影响该框的流量转发。所以题目中的描述是错误的</u>

判断题993/1247、ASPF技术使得防火墙能够支持如FTP等多通道协议，同时还可以对复杂的应用制定相应的安全策略。
**正确**
<u>ASPF功能可以自动检测某些报文的应用层信息并根据应用层信息放开相应的访问规则（生成Server-map表）。ASPF支持多通道协议（如FTP、H.323、SIP等）。</u>

判断题996/1247、MQC与PBR一样，只能在设备的三层接口下调用。
**错误**
MQC还可以在设备的二层接口下调用。

判断题 997/1247、随板AC指的是华为敏捷交换机内置AC能力，实现有线无线业务的融合管理，有线业务和无线业务流量统一由敏捷交换机集中管理
**正确**
<u>有线无线深度融合是指在敏捷交换机上融合WLAN AC功能后，有线和无线用户可以在敏捷交换机统一进行管理、认证和策略控制，流量集中易于管控，管理极致简化，实现了全新的接入体验，所以题目中的描述是正确的。</u>

判断题1000/1247、流策略支持在接口上调用，但是只支持在接口的出方向调用流策略。
**错误**
<u>流策略在一个接口上，可以在出方向调用，也可以在入方向调用。</u>

判断题1003/1247、绑定到VRF实例的物理接口不能再划分出子接口。
**错误**
<u>即使物理接口被绑定到了VRF，依然可以进行子接口的划分；反过来，每一个被划分出来的子接口，也可以绑定到VRF中。</u>

判断题1004/1247、VLAN映射表是IST域的属性，用来描述VLAN和MSTI之间的映射关系。其中每个VLAN可对应多个MSTI,且一个MSTI可对应多个VLAN。
**错误**
<u>一个域中，一个VLAN对应一个实例，一个实例对应一个MSTI。</u>

判断题1005/1247、华为CloudCampus解决方案支持业务随行功能，该功能可通过图形化策略配置，实现用户随时随地接入。
**正确**
<u>iMaster NCE-Campus控制器不仅是园区的认证中心，同时也是业务策略的管理中心。管理员可以在控制器上统一管理全网策略执行设备上的业务策略。管理员只需要配置一次，就可以将这些业务策略自动下发到全网的执行设备上</u>

判断题 1007/1247、当业务机配置为VLANPool时，若用户在一定时间内连续获取IP地址失败且配置了dhcp update vlan assignment threshold命令，则会触发V LANPool为用户分配新的VLAN，使用户在新VLAN中重新获取IP地址。
**正确**
<u>dhcp update vlan assignment threshold命令用来配置用户一定时间内从VLAN对应的地址池中获取地址失败的次数阈值，达到阈值后VLAN Pool将锁定该VLAN一段时间不分配给用户。缺省情况下，3分钟内用户从VLAN对应的地址池中获取地址失败达到3次，VLAN将被锁定，设备重新从VLAN pool中选择未被锁定的VLAN授权给用户。</u>

判断题1009/1247、NFV和SDN是高度互补、相互依赖的关系，所以必须结合使用。
**错误**

判断题1010/1247、SDN架构中业务协同层的作用是基于用户意图完成业务部署，OpenStack属于业务协同层。
**正确**
<u>SDN网络结构分为协同应用层、控制器层、设备层。协同应用层包括：主要完成用户意图的上层应用，包括OSS（负责整网的业务协同）、OpenStack（一般用于数据中心，负责网络、计算、存储的业务协同）；控制层：即SDN控制器；设备层：用于接收控制器的指令，并执行设备的转发</u>

判断题1011/1247、SDN控制器可以根据网络状态智能调整流量路径，以达到提升整网吞吐的目的。
**正确**
<u>通常传统网络的路径选择依据是通过路由协议计算出的“最优"路径，但结果可能会导致"最优"路径上流量拥塞，其它菲"最优°路径空闲。当采用SDN网络架构时，SDN控制器可以根据网络流量状态智能调整流量路径，提升网络利用率</u>

判断题1019/1247、传统的丢包策略采用尾部丢弃（Tail-Drop）的方法，这种丢弃方法会导致TCP全局同步现象
**正确**
<u>尾丢弃策略(Tail Drop）也就是我们所说的传统丢包策略，即网络发生拥塞时报文进入队列，当队列已满则后面的流量直接丢弃，无法进行缓存。尾丢弃策略无法提供差分服务。丢弃策略会引发TCP全局同步现象。所谓TCP全局同步现象，是指当多个队列同时丢弃多个TCP连接报文时，将造成多个TCP连接同时进入拥塞避免和慢启动状态，以降低并调整流量;而后这几个TCP连接又会在某个时刻同时出现流量高峰。如此反复，使网络流量忽大忽小，影响链路利用率。</u>

判断题1020/1247、流镜像端口能多**实现将镜像端口**上特定业务流的报文，传送到监控设备进行分析和监控的功能
**正确**
<u>流镜像是指在设备上配置一定的规则，将符合规则的特定业务流复制到观察端口进行分析和监控。</u>

判断题1021/1247、在Diff-Serv域的核心路由器通常只需要进行简单流分类
**正确**
<u>Diff-Serv一般基于报文中的EXP、802.1p、IPP等字段值进行简单的流分类，以及对相应的流进行流量控制。所以题目中的描述是正确的。</u>

判断题1025/1247、丢包仅发生在报文的发送端
**错误**
<u>丢包可能出现在传输路径的任意节点，任意节点出现链路拥塞或者因为策略的影响都有可能出现丢包</u>

判断题1026/1247、一种路由协议在引入其他路由协议时，为了只引1入一部分满足条件的路由信息，并且对所引1入的路由信息的某些属
性进行设置，那么只能使用route-policy工具。
**错误**
<u>使用普通的import-route 命令就可以实现</u>


判断题1070/1247、以太网中部署端口隔离技术可以实现二层互通三层隔离，使组网更加灵活
**错误**
<u>端口隔离有二层隔离和二层三层都隔离。
，没有单独隔离三层的</u>

判断题1083/1247、在NetStream流输出方式中，原始流输出的优点在于NSC可以得到每条流的详细统计信息
**正确**
<u>NetStream的流输出方式可以获得每条流的详细信息</u>

判断题1097/1247、攻击溯源能够依据攻击报文的信息找出攻击源用户或者攻击源接口，从而可以通过告警和日志等方式提醒管理员，或者直接丢弃该报文
**正确**

判断题1100/1247、OSPF中，在广播类型网举出来的DR和BDR，既侦听224.0.0.5地址，也侦听224.0.0.6地址。
**正确**
<u>DR和BDR能够侦听224.0.0.5和224.0.0.6，DR other只能侦听224.0.0.5</u>

一个Route-Policy 下可以有多个节点，设备在调用Route-Policy 时按顺序开始匹配
**正确**
<u>一个Route-Policy可以由多个节点（node）构成。路由匹配Route-Policy时遵循以下两个规则：  
(1）顺序匹配：在匹配过程中，系统按节点号从小到大的顺序依次检查各个表项，因此在指定节点号时，要注意符合期望的匹配顺序。  
(2）唯一匹配：Route-Policy各节点号之间是“或”的关系，只要通过一个节点的匹配，就认为通过该过滤器，不再进行其它节点的匹配。</u>

判断题1114/1247、可使用路由引入的方式
**错误**
<u>路由引入是实现不同协议直接通信的方法之一，也可以通过下发默认路由方式实现不同路由协议之间的通信</u>

判断题 1115/1247、针对链路状态路由协议，采用多区域、层次化网络设计可以加快路由收敛，减轻单区域内设备的负荷，同时使得网络的扩展性更好。
**正确**
<u>ospf、isis链路状态区域通过划分区域可实现隔离LAS泛洪量减轻单区域设备符合、防止环路加快收敛。</u>

填空题 1146/1247、 ip ip-prefx List1 index10 permit10.1.0.0 24 greater-equal （） less-equal 32表示匹配网络地址的前24bit与10.1.0.0相同，网络俺码长度大于或等于26且小于或等于32的路由。（便用阿拉伯数字）
**26**
<u>greater-equal为大于等于</u>

填空题 1172/1247、工程师在日常排障过程中，可能需要查看设备的一些告警信息。通过执行terminal （） 命令打开终端显示信息中心发送的调试/日志/告警信息功能。 （请使用英文小写字母将命令补全，且命令不能缩写）
**monitor**

![image-2024724324508.png](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/z%E4%BE%8B%E9%A2%98%E4%B9%8B%E5%A4%96/image-2024724324508.png)
**34.34.34.34**

填空题1193/1247、DHCP报文中的Option82称为中继代理信息选项，管理员可以从其中获得客户端的很多信息。Option82中最多可以包()个Sub-Option
**255**
<u>DHCP报文中的一个选项，该选项在dhcp报文中为可变长的字段, option选项中包含了部分租约信息、报文类型等。option选项中最多可以包括255个option，最少为1个option。
</u>

填空题1195/1247、执行 （） saved-configuration命令，清空设备下次启动使用的配置文件的内容，并取消指定系统下次启动时使用
的配置文件，从而使设备配置恢复到缺省值。（请填写完整命令，不能缩写，且全部使用英文字母小写）
**reset**
<u>reset saved-configuration命令用来清空设备下次启动使用的配置文件内的内容，并取消指定系统下次启动时使用的配置文件。</u>