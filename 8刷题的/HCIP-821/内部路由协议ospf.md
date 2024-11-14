![image-20247142347770.png|375](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/ospf/image-20247142347770.png)

-------------------------------------------------------------------------------------------------------------------------------------------------------
# 报文
第一个报文是建立邻居的
其余四个都是用来同步链路信息数据库lsdb的
关于计算路由表，每一个个体是独立的，自己计算。
![image-20247142410274.png|375](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/ospf/image-20247142410274.png)

-------------------------------------------------------------------------------------------------------------------------------------------------------
# 邻居→邻接
![image-20247145328714.png|450](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/ospf/image-20247145328714.png)

-------------------------------------------------------------------------------------------------------------------------------------------------------
# 建立过程
- **Down 状态**：初始状态，没有邻居信息。
- **Init 状态**：收到邻居的 Hello 报文，但没有看到自己的 Router ID。
- **2-Way 状态**：双方都收到了对方的 Hello 报文，并且看到了自己的 Router ID。然后就已经建立邻居关系了
- **Exstart 状态**：选举出主/从关系，准备开始数据库描述（DBD）交换。如果 MTU 不匹配，邻居关系会停留在这个状态。
- **Exchange 状态**：交换 DBD 报文。
- **Loading 状态**：请求更多的 LSA（Link State Advertisement）。
- **Full 状态**：邻居关系完全建立，可以交换完整的路由信息。、
已经建立邻接关系了

-------------------------------------------------------------------------------------------------------------------------------------------------------
# 关于选举
route priority 大的优先级高
router ID 大的优先级高

-------------------------------------------------------------------------------------------------------------------------------------------------------
# LSA类型
- **Router LSA（类型1）**：由每个路由器生成，描述其直接连接的链路和状态。
- **Network LSA（类型2）**：由DR（Designated Router）生成，`描述多访问网络中的所有路由器


- **Summary LSA（类型3和类型4）**：由ABR（Area Border Router）生成，描述一个区域中的网络在另一个区域中的可达性。
Type 3 LSA 用于在不同 OSPF 区域之间传播网络的总结信息。
Type 4 LSA 用于提供 ASBR（Autonomous System Boundary Router，自治系统边界路由器）的汇总信息。

- 外部
- **AS External LSA（类型5）**：由ASBR（Autonomous System Boundary Router）生成，描述AS外部的路由信息。
-------------------------------------------------------------------------------------------------------------------------------------------------------
# 维护关系
ospf 是用hello报文维护关系的

-------------------------------------------------------------------------------------------------------------------------------------------------------
# 算法
ospf 使用的是SPF最短路径算法

-------------------------------------------------------------------------------------------------------------------------------------------------------

# 骨干区域
area0 是骨干区域


-------------------------------------------------------------------------------------------------------------------------------------------------------
# DR和BDR背景（优化数据库同步）
为了解决左下角的路由增加了一个A网段，给其余4台路由器都发送消息后，其余四台再会给其余三台发信息。
![image-2024715374617.png|300](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/ospf/image-2024715374617.png)
所有有个DR和BDR,只要增加了信息， 都把信息先发给DR（同步数据库） BDR也需要发,这些DRother就不需要互相发送了。由DR给他发送
![image-20247153935119.png|350](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/ospf/image-20247153935119.png)
在划分了区域后，也就是下面，一个区域有一个DR接口，需要注意是接口！而不是路由器！需要注意，是基于网段的，而不是区域
![image-20247161018523.png|350](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/ospf/image-20247161018523.png)
其它的接口就是DRother了，如果优先级改为0，也会成为DRother

-------------------------------------------------------------------------------------------------------------------------------------------------------
# OSPF区域背景→BR-BR/ABR（area0）IR-IR/ASBR(非area0)
![image-2024716026969.png|350](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/ospf/image-2024716026969.png)
![image-20247163145917.png|325](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/ospf/image-20247163145917.png)
区域压力太大了，然后数据库ospf lsdb又是完全一致的，一个减少都减少，一个增加都增加，就会引入很多问题。
![image-20247154723453.png|350](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/ospf/image-20247154723453.png)
非骨干区域必须直接连接骨干区域，不然不算了都，也不通了
![image-20247155235410.png|350](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/ospf/image-20247155235410.png)
# OSPF的四种网络类型
一般情况下，两端的ospf的网络类型必须一致，才能建立链接
![image-2024715273789.png|375](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/ospf/image-2024715273789.png)
![image-20247153456761.png|350](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/ospf/image-20247153456761.png)
![image-2024715356635.png|325](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/ospf/image-2024715356635.png)


-------------------------------------------------------------------------------------------------------------------------------------------------------
# display ospf interface g0/0/0
```
[R4]display ospf interface g0/0/0

	 OSPF Process 1 with Router ID 10.0.4.4
		 Interfaces 


 Interface: 10.1.234.4 (GigabitEthernet0/0/0)
 Cost: 1       State: DROther    Type: Broadcast    MTU: 1500  
 Priority: 0
 Designated Router: 10.1.234.3
 Backup Designated Router: 10.1.234.2
 Timers: Hello 10 , Dead 40 , Poll  120 , Retransmit 5 , Transmit Delay 1 
```

-------------------------------------------------------------------------------------------------------------------------------------------------------
 
# Display ospf peer
```
<R2>display ospf peer

	 OSPF Process 1 with Router ID 10.0.2.2
		 Neighbors 

 Area 0.0.0.0 interface 10.1.234.2(GigabitEthernet0/0/0)'s neighbors
 Router ID: 10.0.1.1         Address: 10.1.234.1      
   State: Full  Mode:Nbr is  Slave  Priority: 1
   DR: 10.1.234.3  BDR: 10.1.234.2  MTU: 0    
   Dead timer due in 37  sec 
   Retrans timer interval: 5 
   Neighbor is up for 00:00:10     
   Authentication Sequence: [ 0 ] 

 Router ID: 10.0.3.3         Address: 10.1.234.3      
   State: Full  Mode:Nbr is  Master  Priority: 255
   DR: 10.1.234.3  BDR: 10.1.234.2  MTU: 0    
   Dead timer due in 28  sec 
   Retrans timer interval: 5 
   Neighbor is up for 00:00:42     
   Authentication Sequence: [ 0 ] 

 Router ID: 10.0.4.4         Address: 10.1.234.4      
   State: Full  Mode:Nbr is  Master  Priority: 0
   DR: 10.1.234.3  BDR: 10.1.234.2  MTU: 0    
   Dead timer due in 31  sec 
   Retrans timer interval: 5 
   Neighbor is up for 00:00:42     
   Authentication Sequence: [ 0 ] 
```
说明
```
<R2>display ospf peer




展示ospf进程1的信息 路由器的ID是10.0.2.2
	 OSPF Process 1 with Router ID 10.0.2.2      
		 Neighbors 




 #这个邻居关系属于OSPF区域0.0.0.0。建立在10.1.234.2上，接口类型是GigabitEthernet0/0/0。
 Area 0.0.0.0 interface 10.1.234.2(GigabitEthernet0/0/0)'s neighbors 


邻居路由器的OSPF Router ID是10.0.1.1。邻居路由器的IP地址是10.1.234.1。
 Router ID: 10.0.1.1         Address: 10.1.234.1 
OSPF邻居状态是Full，表示完全邻接。邻居在DR/BDR选举中是Slave（从属状态）。邻居的OSPF优先级是1。
   State: Full  Mode:Nbr is  Slave  Priority: 1
该网络的指定路由器（Designated Router，DR）是10.1.234.3。该网络的备份指定路由器（Backup Designated Router，BDR）是10.1.234.2。接口的最大传输单元（MTU），为0表示未配置。
   DR: 10.1.234.3  BDR: 10.1.234.2  MTU: 0    
邻居路由器的死计时器将在37秒后触发，如果在此时间内未收到心跳信号，邻居关系将被认为已断开。
   Dead timer due in 37  sec 
重传计时器的间隔时间是5秒。
   Retrans timer interval: 5 
邻居关系已经建立了10秒钟。
   Neighbor is up for 00:00:10   
认证序列号，当前值为0  
   Authentication Sequence: [ 0 ] 

 Router ID: 10.0.3.3         Address: 10.1.234.3      
   State: Full  Mode:Nbr is  Master  Priority: 255
   DR: 10.1.234.3  BDR: 10.1.234.2  MTU: 0    
   Dead timer due in 28  sec 
   Retrans timer interval: 5 
   Neighbor is up for 00:00:42     
   Authentication Sequence: [ 0 ] 

 Router ID: 10.0.4.4         Address: 10.1.234.4      
   State: Full  Mode:Nbr is  Master  Priority: 0
   DR: 10.1.234.3  BDR: 10.1.234.2  MTU: 0    
   Dead timer due in 31  sec 
   Retrans timer interval: 5 
   Neighbor is up for 00:00:42     
   Authentication Sequence: [ 0 ] 

```
![image-20247134139598.png|250](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/ospf/image-20247134139598.png)

-------------------------------------------------------------------------------------------------------------------------------------------------------
# display ospf error interface GigabitEthernet 0/0/0
```
<R1>display ospf error interface GigabitEthernet 0/0/0

         OSPF Process 1 with Router ID 10.0.1.1
                 OSPF error statistics 

 Interface: GigabitEthernet0/0/0 (10.1.234.1)
General packet errors:
 0     : Bad version                    0     : Bad checksum
 0     : Bad area id                    0     : Bad authentication type
 0     : Bad authentication key         0     : Unknown neighbor
 0     : Bad net segment                0     : Extern option mismatch
 0     : Router id confusion

HELLO packet errors:
 0     : Netmask mismatch               0     : Hello timer mismatch
 0     : Dead timer mismatch            0     : Invalid Source Address

DD packet errors:
 0     : MTU option mismatch

LS REQ packet errors:
 0     : Bad request

LS UPD packet errors:
 0     : LSA checksum bad

Receive Grace LSA errors:
 0     : Number of invalid LSAs         0     : Number of policy failed LSAs
 0     : Number of wrong period LSAs
```
解释
```
<R1>display ospf error interface GigabitEthernet 0/0/0
--------------这个接口有个ospf进程1的信息，路由器的ID是10.0.1.1

         OSPF Process 1 with Router ID 10.0.1.1
                OSPF error statistics 
----------------错误统计信息的接口是GigabitEthernet0/0/0，IP地址是10.1.234.1。
 Interface: GigabitEthernet0/0/0 (10.1.234.1)
----------通用数据包错误统计。 
General packet errors:

# 错误版本                                       错误校验和
 0     : Bad version                    0     : Bad checksum
 
# 错误区域ID                                     错误认证类型
 0     : Bad area id                    0     : Bad authentication type
 
# 错误认证密钥                                    错误邻居
 0     : Bad authentication key         0     : Unknown neighbor
 
# 错误网络段                                     外部选项不匹配的
 0     : Bad net segment                0     : Extern option mismatch
 
# 路由器ID混淆的
 0     : Router id confusion


###HELLO数据包错误统计
HELLO packet errors:

网络掩码不匹配                                  hello定时器不匹配
 0     : Netmask mismatch               0     : Hello timer mismatch

死亡定时器不匹配                                    无效源地址
 0     : Dead timer mismatch            0     : Invalid Source Address


数据描述数据包错误统计
DD packet errors:

MTU选项不匹配的数据
 0     : MTU option mismatch

链路状态请求数据包错误统计
LS REQ packet errors:

 错误请求数据包
 0     : Bad request

链路状态更新数据包错误统计
LS UPD packet errors:

链路状态校验和错误的数据包数量
 0     : LSA checksum bad


接收Grace LSA错误统计
Receive Grace LSA errors:

无效的LSA数据包                             策略失败的LSA数据包
 0     : Number of invalid LSAs         0     : Number of policy failed LSAs
 
 时间段错误的LSA数据包
 0     : Number of wrong period LSAs
```

-------------------------------------------------------------------------------------------------------------------------------------------------------
# dispaly ospf lsdb 看数据库
![image-20247142954239.png|425](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/ospf/image-20247142954239.png)
这些type的
 router
 network等就是lsa了
```
[R1]display ospf lsdb 

	 OSPF Process 1 with Router ID 10.0.1.1
		 Link State Database 

		         Area: 0.0.0.0
            连接的IP     发送产生lsa的
 Type      LinkState ID    AdvRouter          Age  Len   Sequence   Metric
 Router    10.0.3.3        10.0.3.3           996  48    8000001A       1
 Router    10.0.4.4        10.0.4.4           995  48    80000018       1
 Router    10.0.2.2        10.0.2.2           994  48    8000001C       1
 Router    10.0.1.1        10.0.1.1           996  36    80000012       1
 Network   10.1.234.3      10.0.3.3           995  40    80000010       0
 Sum-Net   10.0.35.0       10.0.3.3          1140  28    80000008      48
 Sum-Net   10.0.1.0        10.0.1.1          1130  28    80000008       0
 Sum-Asbr  10.0.5.5        10.0.3.3          1130  28    80000008      48
 
		         Area: 0.0.0.2
 Type      LinkState ID    AdvRouter          Age  Len   Sequence   Metric
 Router    10.0.1.1        10.0.1.1          1098  36    80000009       0
 Sum-Net   10.0.35.0       10.0.1.1           999  28    80000007      49
 Sum-Net   10.0.3.0        10.0.1.1           999  28    80000007       1
 Sum-Net   10.0.2.0        10.0.1.1           991  28    80000007       1
 Sum-Net   10.1.234.0      10.0.1.1          1130  28    80000008       1
 Sum-Net   10.0.4.0        10.0.1.1           999  28    80000007       1
 Sum-Asbr  10.0.5.5        10.0.1.1           999  28    80000007      49
 

		 AS External Database
 Type      LinkState ID    AdvRouter          Age  Len   Sequence   Metric
 External  10.0.5.0        10.0.5.5          1147  36    80000008       1
 External  10.0.35.0       10.0.5.5          1141  36    80000008       1
 External  10.0.35.3       10.0.5.5          1141  36    80000008       1
 
[R1]
```

-------------------------------------------------------------------------------------------------------------------------------------------------------
# display ospf routing 查看路由表
![image-2024714354234.png|425](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/ospf/image-2024714354234.png)

-------------------------------------------------------------------------------------------------------------------------------------------------------

# 命令 display ospf lsdb router
```
[R1]display ospf lsdb router

	 OSPF Process 1 with Router ID 10.0.1.1
		         Area: 0.0.0.0
		 Link State Database 


  Type      : Router
  Ls id     : 10.0.3.3
  Adv rtr   : 10.0.3.3  
  Ls age    : 274 
  Len       : 48 
  Options   :  ABR  E  
  seq#      : 8000000b 
  chksum    : 0x28f0
  Link count: 2
   * Link ID: 10.1.234.3   
     Data   : 10.1.234.3   
     Link Type: TransNet     
     Metric : 1
   * Link ID: 10.0.3.0     
     Data   : 255.255.255.0 
     Link Type: StubNet      
     Metric : 0 
     Priority : Low

  Type      : Router
  Ls id     : 10.0.4.4
  Adv rtr   : 10.0.4.4  
  Ls age    : 280 
  Len       : 48 
  Options   :  E  
  seq#      : 80000009 
  chksum    : 0x2aeb
  Link count: 2
   * Link ID: 10.1.234.3   
     Data   : 10.1.234.4   
     Link Type: TransNet     
     Metric : 1
   * Link ID: 10.0.4.0     
     Data   : 255.255.255.0 
     Link Type: StubNet      
     Metric : 0 
     Priority : Low

  Type      : Router
  Ls id     : 10.0.2.2
  Adv rtr   : 10.0.2.2  
  Ls age    : 275 
  Len       : 48 
  Options   :  E  
  seq#      : 8000000b 
  chksum    : 0x24fb
  Link count: 2
   * Link ID: 10.1.234.3   
     Data   : 10.1.234.2   
     Link Type: TransNet     
     Metric : 1
   * Link ID: 10.0.2.0     
     Data   : 255.255.255.0 
     Link Type: StubNet      
     Metric : 0 
     Priority : Low

  Type      : Router
  Ls id     : 10.0.1.1
  Adv rtr   : 10.0.1.1  
  Ls age    : 275 
  Len       : 36 
  Options   :  ABR  E  
  seq#      : 80000004 
  chksum    : 0xf056
  Link count: 1
   * Link ID: 10.1.234.3   
     Data   : 10.1.234.1   
     Link Type: TransNet     
     Metric : 1
		         Area: 0.0.0.2
		 Link State Database 


  Type      : Router
  Ls id     : 10.0.1.1
  Adv rtr   : 10.0.1.1  
  Ls age    : 287 
  Len       : 36 
  Options   :  ABR  E  
  seq#      : 80000002 
  chksum    : 0x1c12
  Link count: 1
   * Link ID: 10.0.1.0     
     Data   : 255.255.255.0 
     Link Type: StubNet      
     Metric : 0 
     Priority : Low
 

```

-------------------------------------------------------------------------------------------------------------------------------------------------------
# 命令 display ospf lsdb router self-originate 
这段显示的是OSPF（Open Shortest Path First）协议的LSDB（Link State Database）中关于自身生成的Router LSA（Link State Advertisement）信
```
[R1]display ospf lsdb router self-originate 

	 OSPF Process 1 with Router ID 10.0.1.1
		         Area: 0.0.0.0
		 Link State Database 


  Type      : Router
  Ls id     : 10.0.1.1
  Adv rtr   : 10.0.1.1  
  Ls age    : 1482 
  Len       : 36 
  Options   :  ABR  E  
  seq#      : 80000004 
  chksum    : 0xf056
  Link count: 1
   * Link ID: 10.1.234.3   
     Data   : 10.1.234.1   
     Link Type: TransNet     
     Metric : 1
		         Area: 0.0.0.2
		 Link State Database 


  Type      : Router
  Ls id     : 10.0.1.1
  Adv rtr   : 10.0.1.1  
  Ls age    : 1494 
  Len       : 36 
  Options   :  ABR  E  
  seq#      : 80000002 
  chksum    : 0x1c12
  Link count: 1
   * Link ID: 10.0.1.0     
     Data   : 255.255.255.0 
     Link Type: StubNet      
     Metric : 0 
     Priority : Low







- **Type**: LSA的类型，这里是Router LSA（类型1），表示该LSA由该路由器生成。
- **Ls id**: LSA的ID，这里是该路由器的路由器ID（Router ID）10.0.1.1。
- **Adv rtr**: 发布LSA的路由器ID，与Ls id相同，表明这是自身生成的LSA。
- **Ls age**: LSA的年龄，以秒计。
- **Len**: LSA的长度，单位为字节。
- **Options**: LSA的选项字段，这里包括ABR（Area Border Router）和E（External Capable）标志。
- **seq#**: LSA的序列号，用于唯一标识LSA版本。
- **chksum**: LSA的校验和，用于数据完整性检查。
- **Link count**: 该LSA包含的链接数目。

#### Link信息

- **Link ID**: 连接的目标ID，这里是10.1.234.3，表示另一个网络或路由器的ID。
- **Data**: 关于链接的具体数据，例如IP地址或其他标识符。
- **Link Type**: 链接类型，这里是TransNet，可能表示传输网络。
- **Metric**: 到达链接目标的度量值，用于路径计算。



- 这部分是与前一部分相似的Router LSA，但是在另一个区域（Area 0.0.0.2）中生成。
- **Link ID**: 这里是10.0.1.0，表示另一个网络或路由器的ID。
- **Data**: 数据字段指示了链接的具体信息，如子网掩码255.255.255.0。
- **Link Type**: 链接类型是StubNet，表示一个虚拟链接到一个静态路由。
- **Metric**: 到达链接目标的度量值，这里是0，表示这是一个直接连接的网络或者是静态配置的。


```

-------------------------------------------------------------------------------------------------------------------------------------------------------
# 例题
下列关于ospf报文错误的是
AR2200支特的验证模式按加密算法不同分为null、 simple、 MD5以及HMAC-MD5
AR2200支持两种认证方式：区域验证和接口验证
**-当区域验证方式和接口验证方式同时存在时，优先便用区域验证**
只有通过验证的OSPF报文才能接受，否则将不能正常建立邻居
<u>`错误原因，接口认证的优先级大于区域认证`</u>

-------------------------------------------------------------------------------------------------------------------------------------------------------

# 例题
说法错误的
![image-20247142317762.png|275](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/ospf/image-20247142317762.png)
本路由器的Router ID为10.0.12.1
**本路由器为DR**
本路由器已建立邻接关系
本路由器支持外部路由引入
<u>解析：一类LSA的在transnet网络中link id值为DR接口的IP地址，Data为宣告该LSA的接口IP地址，DR的IP地址和本设备IP地址不一致，所以DR不是本路由器。有点类似于stp那边的根桥判断了。</u>

-------------------------------------------------------------------------------------------------------------------------------------------------------
# 例题
![image-2024713368723.png|350](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/ospf/image-2024713368723.png)
答案：R1和R2可以建立邻居关系，但是不能完成路由计算。
解析:OSPF网络类型需要匹配，以确保路由器能够正确交换LSA（链路状态广告）。接口网络类型的不同，会影响路由计算，但不会影响邻居的建立。 p2p和以太网网络类型，hello/dead时间一样，可以建立邻接

-------------------------------------------------------------------------------------------------------------------------------------------------------

# 例题 display ospf lsdb network 【可以看lsa类型】
正确的是
**display ospf Isdb network**
display ospf isdb network
display ip ospf Isdb network
display ospf isdb router
display ip ospf Isdb router

![image-20247145754640.png|235](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/ospf/image-20247145754640.png)
- **Type**: LSA类型，这里是Network LSA（类型2）。＜（＾－＾）＞
- **Ls id**: 生成该LSA的网络的IP地址。
- **Adv rtr**: 生成该LSA的DR的路由器ID。
- **Ls age**: LSA的生存时间（秒）。
- **Len**: LSA的长度。
- **Options**: LSA的选项字段。
- **seq#**: LSA的序列号，用于检测更新。
- **chksum**: LSA的校验和，用于数据完整性验证。
- **Net mask**: 网络的子网掩码。
- **Priority**: DR的优先级。
- **Attached Router**: 列出了连接到该网络的所有路由器ID。
-------------------------------------------------------------------------------------------------------------------------------------------------------

# 例题 ospf描述 选举
ospf选举不正确的是
Router Priority大的选举优先级更高。
Router Priority一样大， RouterlD大者选举优先级更高
如果当前DR故障，当前BDR自动成为新的DR网络中重新选举BDR
**当OSPF网络中有新的具有最大Router Priority路由器加入时，则该新的路由会抢占原来的DR**
<u>默认没有开启抢占模式，Router Priority路由器加入时，不会抢占DR/BDR</u>

单选题368/1247、下面关于OSPF DR的描述，不正确的是：
如果当前DR故障，当前BDR自动成为新的DR，网络中重新选举BDR
DR Priority值大的，优先选举为DR
DR Priority一样时， RouterD大者优先选举为DR
**当OSPF时网络中有新的具有更大DR Priorityi路由器加入时、则该新的路由器会抢占原来的DR**
OSPF时网络中的DR默认没有开启抢占模式，不会抢占

-------------------------------------------------------------------------------------------------------------------------------------------------------

# 例题 DR BDR （Backup Designated Router，备份指定路由器）
单选题 55/1247、四台路由器R1、R2、R3和R4使能OSPF建立邻居关系，拓扑和相关参数如图所示，此时R2因某原因断开连接，那么
R1、R3和R4之间传输的Hello报文中，BDR字段的值是以下哪一项？
![image-20247145911430.png|325](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/ospf/image-20247145911430.png)

12.12.12.2
12.12.12.3
12.12.12.1
**0.0.0.0**
2.2.2.2
1.1.1.1
解析：
<u>DR/BDR的优先级不能为0,优先级为0之后将只能成为DRother资格。结合图片，所以选择“0.0.0.0”</u>

-------------------------------------------------------------------------------------------------------------------------------------------------------
# 例题 ospf 多进程
单选78/1247、关于OSPF多进程描述，错误的是
在同一台路由器上可以运行多个不同的OSPF进程，它们之间互不影响，彼此独立
路由器的一个接口只能属于一个OSPF进程
不同OSPF进程之间的路由交互相当于不同路由协议之间的路由交互
**不同OSPF路由器建立邻居，进程号必须相同**


-------------------------------------------------------------------------------------------------------------------------------------------------------
# 例题 Link state ID
单选题 89/1247、下面关于OSPF协议哪个描述是错误的？
Router-LSA描述的连接类型共有四种： P2P/TransNet/StubNetl虚链路
只允许在骨干区域和非骨干区域之间发布路由信息，不允许在非骨干区域之间直接发布路由信息
每台OSPF路由器只使用一条Router-LSA描述属于一个区域的本地活动连接状态
**-第三类LSA中描述的Link State ID为该ABR的router-iD**
<u>解析：第三类LSA中描述的Link State ID为目的地址。
二次解析：这句话不对。第三类 LSA（Type 3 LSA）描述的是 OSPF（Open Shortest Path First）协议中的网络汇总信息，而不是具体的 ABR（Area Border Router，区域边界路由器）的 Router ID。具体来说，第三类 LSA 的 Link State ID 代表的是要汇总的网络前缀。</u>

-------------------------------------------------------------------------------------------------------------------------------------------------------
# 例题mtu不匹配停留的环节
单选题92/1247当在广播网络中的两台路由器互联接口的MTU不匹配，且接口配置了ospf mtu-enable时，则关于两台路由器的邻居
关系状态变化描述正确的是
两台设备的邻居关系状态停留在2-way
**两台设备的邻居关系停留在Exstart**
两台设备的邻居关系可以进入FuLL
两台设备的邻居关系状态停留在lnit 状态

单选题 325/1247、在VRP系统中，当在广播网络中的两台路由器互联接口的MTU不匹配，且接口配置了 ospf mtu-enable时，则关于
两台路由器邻居关系状态变化描述，正确的是以下哪一项？
两台路由器的邻居关系可以进入Full状态
两台路由器的邻居关系状态停留在init 状态
**两台路由器的邻居关系停留在ExStart 状态**
两台路由器的邻居关系状态停留在2-way状态

<u>解析：两台设备的邻居关系停留在Exstart，因MTU不匹配，所以无法协商主从关系，无法确认DD报文序列号。
二次解析：down-init（hello）-2-way（收到heloo，看到自身router id）-exstart（选举主从，准备数据库交换）-exchange（交换DBD报文）-loading（请求更多lsa）-full（完全建立，可以交换完整的路由器信息）</u>

# 答案不是exstart而是exchange，不是mtu了
单选题492/1247、以下关于0SPF的描述，正确的是哪一项？
只有 LS Update和LS Request 报文携带完整的 LSA信息
Hello包的目的地址是224.0.0.5和224.0.0.6
在ospf mtu-enable命令后， OSPF会检查LSU中的MTU长度，如果和自己发出的报文中MTU长度不一致，则设备维持在Exchange状态
**DD报文中不一定携带链路状态摘要信息，此时该DD报文可以用于协商主从关系**
<u>在Exstart阶段，发送的第一个DD报文，其中不包含任何的LSA摘要信息，用于协商设备之间的主从关系，实现DD报文的可靠传输。</u>



-------------------------------------------------------------------------------------------------------------------------------------------------------
# ospf 在vrp系统的开销
单选题96/1247、在VRP系统中，以下关于OSPF开销（Cost)的描述错误的是哪一项？
Cost在接口的流量流入方向生效
**Loopback接口默认开销值是1**
修改OSPF的参考带宽会对OSPF中的所有本地接口开销构成影响
OSPF会根据该接口的带宽自动计算其开销值计算公式为接口开销一带宽参考值/接口带宽
<u>解析：本地，都loopback接口了，开销为0呢还??</u>
计算公式为接口开销一带宽参考值/接口带宽，确实是跟带宽有关


-------------------------------------------------------------------------------------------------------------------------------------------------------
# OSPF中ABR的描述
单选题97/1247、以下关于OSPF中ABR的描述，**错误**的是哪一项？
ABR将连接的 非骨干区域内的1类和2类LSA转换成3类LSA，发布到骨干区域中
**ABR不能够产生4类和5类LSA**
ABR上有多个LSDB，ABR为每一个区域维护一个LSDB
ABR将骨干区域内的1类、2类LSA和3类LSA转换成三类LSA，发布到连接的非骨干区域中
ABR可以产生4类LSA，所以选项“ABR不能够产生4类和5类LSA”的描述是错误的 看这个笔记最上面，ABR可以产生3类和4类lsa

-------------------------------------------------------------------------------------------------------------------------------------------------------

# OSPF 如果没有配置router id
单选题98/1247、关于OSPF的Router ID描述错误的是以下哪一项？
如果没有配置router-id命令且没有配置Loopback接口地址，则从其物理接口的IP地址中选择最大的作为Router ID
如果没有手工配置router-id命令且配置了 Loopback接口地址，则选择Loopback接口地址最大的作为Router ID
**Router ID改变之后，各个协议的Router ID就会改变不需要额外的操作**
如果使用router-id命令手工配置了 Router ID，那 么OSPF最优先使用该Router ID
<u>解析：Router ID改变之后需要重启或者重置OSPF进程后才会生效
优先级：routerid ：手工router id >loopback>物理接口ip</u>

-------------------------------------------------------------------------------------------------------------------------------------------------------
# ospf 选举主从关系
单选题99/1247、运行OSPF协议的路由器在交互DD报文时，会使用以下哪一个参数选举主从关系？
接口的IP地址
接口的DR优先级
Area ID
**Router ID**
<u>router-id大的为主，小的为从 换个信息不用考虑那么多,STP那边才是小的为主</u>

-------------------------------------------------------------------------------------------------------------------------------------------------------
# ospf的ABR的lsa问题
单选题129/1247、下面关于OSPF中的ABR，描述错误的是
**ABR不能够产生三类、四类、五类LSA**
将连接的非骨干区域内的一类、二类LSA转换成三类LSA,发布到骨干区域中
ABR将骨干区域内的一类、二类LSA、三类LSA转换成三类LSA,发布到连接的非骨干区域中
ABR上有多个LSDB,ABR为每一个区域维护一个LSDB
<u><u>解析:ABR能产生3，4L类LSA ，ASBR产生五类LSA</u>
二次解析:对于其他选项解惑,</u>
	- 骨干区域的 Type 3 LSA 发送到非骨干区域：
    - 骨干区域中的 ABR（Area Border Router，区域边界路由器）会收集连接的非骨干区域内的网络信息（Type 1 和 Type 2 LSA），然后将这些信息汇总成 Type 3 LSA 发送到骨干区域内。这样做的目的是让骨干区域内的所有路由器都能了解到连接的非骨干区域的网络拓扑，以便正确地计算最短路径。
- 非骨干区域的 Type 3 LSA 不发送到骨干区域：
    - 非骨干区域内的 ABR 会将其连接的骨干区域的网络信息汇总成 Type 3 LSA，但这些 Type 3 LSA 不会发送到骨干区域中。**这是因为骨干区域内的其他路由器通常只需要了解连接的非骨干区域的网络情况，而不需要了解非骨干区域内的详细网络拓扑**\
-------------------------------------------------------------------------------------------------------------------------------------------------------
# OSPF的协议封装 不属于UDP
单选题135/1247、以下关于OSPF协议报文说法错误的是？
OSPF协议使用五种报文完成路由信息的传递
OSPF所有报文头部都携带了Router-I D字段
**OSPF报文采用UDP报文封装，并且端口号是89**
OSPF所有报文的头部格式相同
<u>解析：OSPF属于第四层协议，直接封装在IP报头之后，不属于UDP也不属于TCP</u>
# ospf-metric-type-1/2 开销计算方式
单选题151/1247、 OSPF外部路由引I入时会使用Metric-Type-1或者Metric-Type-2类型，那么Metric-Type-1类型的路由开销计算方
法是以下哪一项
距离本设备最近的ABR到ASBR的开销与ASBR到该路由目的地址开销之和
**本设备到相应的ASBR的开销与ASBR到该路由目的地的开销之和**
本设备到相应的ASBR的开销
ASBR到 该路由目的地址的开销
<u>Type-1类型的路由开销计算方法为本设备相应的开销和目的地址开销之和，所以本题选择“本设备到相应的ASBR的开销与ASBR到该路由目的地址的开销之和”。</u>

-------------------------------------------------------------------------------------------------------------------------------------------------------
# ospf路由聚合
单选题
156/1247、关于OSPF路由聚合的描述错误的是
**OSPF中任意一台路由器都可以进行路由聚合的操作**
区域间路由聚合是指将相同前缀的路由信息聚合一起，只发布一条路由到其他区域
OSPF有两种路由聚合方式：ABR聚合和ASBR聚合
通过路由聚合可以减少路由信息，从而减少路由表的规模提高路由器的性能

单选题517/1247、以下关于0SPF路由聚合的描述，错误的是哪一项？
**OSPF中任意一台路由器都可以进行路由聚合的操作**
OSPF有两种路由聚合方式：ABR聚合和ASBR聚合
路由聚合是指将相同前缀的路由信息聚合一起，只发布一条路由到其他区域
通过路由聚合，可以减少路由信息，从而减少路由表的规模，提高路由器的性能

<u>解析：OSPF不支持自动聚合，只支持手动聚合。区域间路由聚合必须在ABR路由器上而外部路由聚合必须配置在ASBR路由器上。</u>



-------------------------------------------------------------------------------------------------------------------------------------------------------
# OSPF 广播排错
单选题
225/1247、以下关于0SPF的描述，错误的是哪一项？
网络类型为广播时，所接收的Hello报文中Dead Interval字段必须和接收端配置一致
网络类型为广播时，所接收的Hello报文中Hello Interval字段必须和接收端口的配置一致
**网络类型为广播时，所接收的Hello报文中MTU必须和接收端口的配置一致**（也就是可以建立邻居，但是建立不了邻接的状态）
网络类型为广播时，所接收的Hello报文中Network Mask字段必须和接收端口的网络掩码一致

<u>验证一个接收到的Hello报文是否合法包括：
如果接收端口的网络类型是广播型，点到多点或者NBMA，所接收的Hello报文中Network Mask字段必须和接收端口的网络掩码一
致，如果接收端口的网络类型为点到点类型或香是虚连接，则 不检查Network Mask字段
所接收的Hello报文中Hellolnterval字段必须和接收端口的配置一致；
所接收的Hello报文中 Router Dead lnterval字段必须和接收端口的配置 一致；
所接收的Hello报文中Options字段中E-bit （表示是否接收外部路由信息） 必须和相关区域的配置一致；
如集路由器发现所接收的合法Hello报文的邻居列表中有自己的Router ID，则认为已经和邻居建立了双尚连接，表示邻居关系已经建
立。可见，Hello报文没有网络类型的字段，因此不需检查网络类型是否匹配，只要双方都能收到对方Hello报文，关键字段匹配，就可建
邻居。 P2P、Broadcast 网络类型都会发送组播Hello报文，所以互联V LANIF OS PF网络类型不一致，**但可建立邻居关系。**</u>
# ospf建立邻居排错

![image-20247181912978.png|300](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/ospf/image-20247181912978.png)
![image-20247181831743.png|300](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/ospf/image-20247181831743.png)
<u>OSPF的hello时间需要保持一致。才能正常建立邻居。所以本题选择
[R2] interface GigabitEthernet 0/0/0
[R2-GigabitEthernet0/0/0] ospf timer hello 20</u>
# ospf虚连接
单选题242/1247、以下关于0SPF虚连接的描述，错误的是哪一项？
虚连接实际上是一个逻辑通道
虚连接增加了网络的复杂度
配置了虚连接所经过的区域必须拥有全部的路由选择信息
**虚链接必须配置在两台ASBR中**
<u>虚连接可以在任意两个ABR上建立，但是要求着两个ABR都有端口连接在一个相同的非骨干区域。</u>
# OSPF 报文
单选题248/1247、以下关于OSPF报文的描述，错误的是哪一项？
DD报文携带LSA头部信息描述链路状态摘要信息
Hello报文用于发现和维护邻居关系，在广播型网络和NBMA网络上Hello报文也用来选举DR和BDR
**DD报文包含全部的LSA信息，可以用于邻居间定期同步链路状态数据库信息**
两台路由器之间发送Hello报文的间隔必须一致，否则邻居无法建立
<u>在OSPF协议同步数据库的过程中，DD报文中包含的仅仅是数据库中的LSA的简要信息，LSU报文中包含的才是完整的LSA信息条目。所以正确答案是“DD报文包含全部的LSA信息，可以用于邻居间定期同步链路状态数据库信息”。</u>
# OSPF 特殊区域
单选题251/1247、以下关于0SPF特殊区域的描述，**错误**的是哪一项？
Stub Area和Totally Stub区域的不同在于该区域允许域间路由
**NSSA Area和Stub区域的不同在于该区域允许自治系统外部路由的引入，由ABR发布LSA7通告给本区域**
Totally Stub Area的作用是允许AB R发布的LSA3缺省路由， 不允许自治系统外部路由和区域间的路由
Totally Stub区域和NSSA区域的不同在于该区域不允许域间路由
<u>是由ASBR发布LSA7通告给本区域，不是ABR</u>

# ospf的stub区域和nssa区域
单选题431/1247、以下关于0SPF特殊区域的描述，**错误**的是哪一项？
Totally Stub区域的作用是允许ABR发布3类LSA缺省路由，不允许存在自治系统外部路由和区域间的路由
NSSA区域和Stub区域的不同在于NSSA区域充许自治系统外部路由的引入，由ASBR发布7类LSA通告给本区域
**Stub区域和NSSA区域的不同在于Stub区域不充许存在明细域间路由**
Stub区域和 Totally Stub区域的不同在于Stub区域允许存在明细域间路由
![[8刷题的/HCIP-821/--[1665302543302.png](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/%E5%86%85%E9%83%A8%E8%B7%AF%E7%94%B1%E5%8D%8F%E8%AE%AEospf/1665302543302.png)
# ospf的STUB区域和Totally STUB区域
单选题 410/1247、以下关于OSPF中Stub和Totally Stub区域的描述，正确的是哪一项？
**Totally Stub 区域和 Stub 区域相比，配置Totally Stub区域可以禁止明细Network Summary L SA进入该ABR连接的 Stub区域**
虚连接不能在lotally Stub 区域配置，但是可 以在Stub 区域上配置
Stub区域内的所有路由器都需要配置stub命令，但Totally Stub区域只需要在ABR配置即可
如果需要在骨干区域 上配置Stub和Totally Stub 区域，需要在Area O中使用stub -router 命令
<u>Totally stubby Area (完全末梢区域) 不但具有末梢区域的功能且一个完全末梢区域的ABR(边界路由)将不仅阻塞外部的LSA 而是阻塞所有的汇总LSA 除了通告默认路由的那一条类型3的LSA</u>
# OSPF的NSSA区域
单选题327/1247、以下对NSSA区域的描述**错误**的是哪一项？
NSSA区域的ABR会将7类LSA转化为5类LSA.并将该LSA注入到骨干区域，从而在整个OSPF域内泛洪
NSSA区域能够引入外部路由，同时又不会学习来自OSPF网络其它区域的外部路由
**NSSA区域内部不充许存在3类LSA.也不允许区域内存在4类和5类LSA**
NSSA区域的ABR会自动向该区域注入一条缺省路由，该路由采用7类LSA描述
<u>NSSA接受域间路由，也就是3类LSA</u>



# LSA的描述
单选题
289/1247、以下关于各种报文的LSA描述，**错误**的是哪一项？
**LSAck报文包含了完整的LSA信息**
LS Request报文R有 LS Type.LS ID和Advertising Router
DD只包含LSA的摘要信息，即包含LS Type、 LSID、Advertising Router和LS Sequence Number
LS Update报文包含了完整的LSA信息
<u>LSAck只包含LSA的摘要，LSU才包含完成的LSA信息</u>
# LSA的描述
单选题
313/1247、关于LSA描述正确的是
LS type.LS sequence number Advertising Router 的组合共同标识一条LSA
**LS type.Link State I D和Advertising Router 的组合共同标识一条LSA**
LS type.Link State I D和LS sequence number的组合共同标识一条LSA
LS sequence number.Link State ID和Advertising Router的组合共同标识一条LSA
<u>都出现过的，在OSPF协议中，唯一的表示一个 LSA的时候，是通过三个字段：LS type，Link State ID和Advertising Router，如果两个LSA的这三个字段相同，说明这两个 LSA 是相同的 LSA 。所以正确答案是：“LS type、Link State ID和Advertising Router的组合共同标识一条LSA”。</u>

单选题 433/1247、OSPF通过LSA来交换链路状态，以下关于LSA的描述，正确的是哪一项？
LS type、 LS sequence number Advertising Router 三个参数唯一标识一条LSA
LS sequence number、 Link State I D和Advertising Router 三个参数唯一标识一条LSA
**LS type，Link State ID和Advertising Router 三个参数唯一标识 一条L SA**
LS type、 Link State ID和LS sequence number 三个参数唯一标识一条LSA

# 回环
单选题 321/1247、已知路由器R1存在Loopback0且地址为1.1.1.1/32.在使能OSPF并引入直连路由时会把该环回口引入。那么以下哪
一项的配置能够实现在引入直连路由时，LoopbackO不会被引入并能够保证其他直连路由引入到oSPF内？
选c
![image-20247191923581.png](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/ospf/image-20247191923581.png)
<u>route-policy最后有一个隐含的拒绝所有的命令。并且在ACL中，想要精确匹配一个路由的话，通配符必须是0.0.0.0，不能是 255.255.255.255 。</u>
# ospf加密算法
单选题326/1247、OSPF协议对邻居路由器之间交换的所有数据包都具有认证能力，在VRP系统中，OSPF支持以下哪一种算法？
AES
DES
**MD5**
RSA
<u>OSPF认证支持simple/MD5/HMAC-MD5/HMAC-SHA256/Keychain/Null。</u>
# LSDB分析
![76e6d5797cddeb5e2bbba959465081f6.png|300](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/%E5%86%85%E9%83%A8%E8%B7%AF%E7%94%B1%E5%8D%8F%E8%AE%AEospf/76e6d5797cddeb5e2bbba959465081f6.png)
R2被部署在骨干区域里，且R2是一个ABR
Area1中存在区域边界路由聚合
**Area2中存在ASBR.EASBR Router ID为6.6.6.6**
图中涉及的整个环境中不存在Stub区域
<u>ASBR存在于区域1中，可以通过1类LSA,找到ASBR位置，不需要通告4类LSA。区域2因为与ASBR不在一个区域,不知道ASBR位置，所以需要4类LSA通告ASBR位置。
</u>
# LSDB同步描述
单选题337/1247、以下关于LSDB同步的描述，错误的是哪项？
**详细的LSA信息会在ExStart和 Loading两个状态之间交互**
DD报文在Exchange状态下会携带链路状态的摘要信息
LSR不携带详细的链路状态信息
Loading状态下，邻居之间会相互发送L SR报文、 LSU报文和LSAck报文
<u>ExStart和Loading两个状态主要用来传输DD报文（而不是LSA报文），描述本地LSDB（Link State Database）的摘要信息，用于两台设备进行数据库同步。
</u>
# 缺省路由属于哪一类lsa
单选题338/1247、使用default-route-advertise命令可将缺省路由通告进OSPF域内，该缺省路由属于以下哪一类LSA？
2类LSA
1类LSA
3类LSA
4类LSA
**5类LSA**.
<u>使用default-route-advertise命令后，ASBR将产生一个Link State ID为0.0.0.0，网络掩码为0.0.0.0的ASE LSA（Type 5），并且通告到整个OSPF区域中</u>
# LSR LSU  LSACK
单选题
344/1247、路由器R1和R2建立OSPF邻居，当R1收到R2发来的LSU报文时，会使用以下哪一种方法告知R2收到了该LSU？
R1会向R2回应DD报文，其中LSA头部的序列号和LSU的相同
**R1会回应LSAck报文给R2**
R1会传输ACK位置位为1的TCP包给R2
R1会向R2返回相同序列号的 LSU
# LSR 不包括字段
单选题360/1247、 LS Request报文不包括以下哪一字段？
通告路由器（Advertising Router)
链路状态ID（Link Srate ID）
**数据库描述序列号（Database Dascription Sequence lumber)**
链路状态类型（Link state type)
<u>Link State ID：（不同类型LSA 就有不同类型的Link ID）  
Advertising Router：通告路由器（就是通告这条路有的一个router id）  
LS Sequence Number：序列号 用来标明是否是一个更新的LSA 。  
所以本题不包括“数据库描述序列号（Database Dascription Sequence Number）”</u>

# 停留状态
![image-20247201944514.png|425](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/%E5%86%85%E9%83%A8%E8%B7%AF%E7%94%B1%E5%8D%8F%E8%AE%AEospf/image-20247201944514.png)
Down
Full
**2-way**
Loading
<u>当R1能收到R2发来的报文，且收到R2的Hello报文中，包含着R1的Router ID，意味着R1发的Hello报文，R2收到了，R2认可了这个R1这个邻居。所以R1的邻居状态（R2的状态）是2-way，双向通信状态。</u>

# 什么状态进行选举
单选题388/1247、当OSPF运行在广播型网络中时，需要选举DR和BDR。那么以下哪一种状态会进行DR和BDR的选举？
**2-way**
Full
Exchange
Init
<u>DR和BDR的地址以及优先级都携带在hello报文中，并且在MA网络中，只有选举出了DR和BDR才能进入邻接关系OSPF会在第一个hello后就进行DR与BDR的选举，在exstart之前选举完成</u>

# ASBR-Summarylsa错误的
单选题389/1247、以下关于OSPF的ASBR-Summary-LSA报文中各个字段的描述，**错误**的是哪一项？
Advertising Router字段表示产生该L SA的ABR
**所有区域的A SBR-Summary-LSA中的Advertising Router字段都相同**
Link State ID表示ASBR的Router ID
Metric表示该ABR到达AS BR的O SPF开销
<u>各个区域的ASBR-Summary-LSA中的Advertising Router字段都是本区域的ABR</u>

单选题447/1247、以下关于OSPF asbr-summary命令的描述，**错误**的是哪一项？
asbr-summary命令只在需要汇聚的ASBR上部署才能生效
使用asbr-summary命令汇总的路由会以5类LSA在区域内传递
使用asbr-summary命令汇总的路由能够被泛洪到其它区域
**abr-summary命令可以汇总被asbr-summary聚合后的LSA**
<u>abr-summary的汇总对象指的是3类LSA；asbr-summary的汇总对象指的是5类LSA，所以两者之间不能互相操作，不能互相汇总彼此的LSA。</u>

# Totally stub需要通过默认路由到达其他区域
单选领
400/1247、以下哪一种类型的OSPF区域，需要通过默认路由到达其他区域？
骨干区域
**Totally Stub区域**
虚连接区域
重发布区域
<u>Totally Stub区域不要3、4、5类LSA，只需要通过ABR下发的表示缺省路由的3类LSA，到达其他区域</u>

# 可以携带外部路由tag信息的lsa
单选题417/1247、可以携带外部路由的tag标签信息的是以下哪一类LSA？
4类LSA
**5类LSA**
3类LSA
2类LSA
<u>只有5、7类LSA中有tag字段</u>

# 路由器直连ospf-p2p
单选题418/1247、两台路由器直连，并设定网络类型为p2p建立OSPF邻居。那么两台路由器传输OSPF报文的目的IP地址是以下哪-项？
使用组播地址224.0.0.6
**使用组播地址224.0.0.5**
采用p2p模式建立邻居时，不使用IP地址建立
目的地址分别是对端端口的IP地址
<u>p2p的报文全是通过组播224.0.0.5发送,因为p2p中只有两个人,所以也不用选举DR,BDR，boardcast的hello包是通过组播224.0.0.5发送</u>

# OSPF是内部网关协议
单选题419/1247、以下关于OSPF协议的描述，**错误**的是哪一项？
**OSPF是一个基于链路状态的外部网关协议**
OSPF支持对等价路由进行负载分担
OSPF报文封装在IP报文内，可以采用单播或组播的形式发送
OSPF协议支持区域划分

# ospf报文合法
单选题 430/1247、以下关于OSPF报文合法性的描述中，错误的是哪一项？
**如果接收端口的网络类型是广播型、点到多点或者NB MA，所接收的Hello报文中Network  Mask字段和接口 端的可以不一致**
如果接收端口的网络类型为点对点类型或者虚链路，则不检查Network Mask字段
所接收的Hello报文中 RouterDeadlnterval字段必须和接收端口的配置一致
所接收的Hello报文中Options字段中的E-bit必须和相关区域的配置一致
<u>如果接收端口的网络类型是广播型，点到多点或者NBMA，所接收的Hello报文中Network Mask字段必须和接收端口的网络掩码一致。</u>

# 包含完整路由数据库的报文是
单选题432/1247、包含完整链路状态信息的OSPF报文是以下哪一项？
**LSU**
LSR
LSAck
Hello
<u>DD
只有LSU是链路状态更新，携带的是完整信息</u>

# ospf特性
单选题434/1247、以下关于OSPF特性的描述，正确的是以下哪一项？
OSPF采用Bellman-Ford算法，每个路由器都独立运行该算法
**OSPF使用触发更新和定期更新**
OSPF每隔5秒泛洪一个LSU
OSPF本身没有确认机制，所以OSPF依靠下层协议即TCP确认进行
<u>OSPF直接运行在IP之上，没有TCP协议。LSU并不会周期性更新，OSPF是触发更新的，也有定期刷新时间是30分钟。OSPF使用的算法是SPF</u>

单选题509/1247、**不属**于OSPF特性的是以下哪一项？
支持VLSM
支持邻居认证
**使用DUAL算法建立最短路径树**
定期更新
<u>OSPF使用SPF算法建立最短路径树</u>

# OSPF描述
单选题446/1247、以下关于0SPF的描述，错误的是哪一项？
**3类LSA中描述的 Link StatelD为该ABR的Router ID**
路由信息只充许在骨干区域和非骨干区域之间发布，不充许在非骨干区域之间直接发布路由信息
每台OSPF路由器只使用一条Router-LSA描述属于一个区域的本地活动连接状态
Router-LSA描述的连接类型共有四种，分别是P2P、 TransNet、 StubNet和虚链路
<u>3类LSA的link-state ID表示的是不同区域之间的路由的网段；掩码信息在LSA的详细信息中包含着。</u>

# link id
单选题463/1247、以下关于OSPF3类LSA中Link ID的描述，正确的是哪一项？
Link ID是所在网段上DR的端口IP地址
Link ID描述的该A BR的Router ID
**Link ID所描述的是路由的目的网络地址**
Link ID是生成这条 L SA的路由器的Router ID
<u>3 类LSA: summary LSA (汇总LSA)
1、功能：用于在区域之间传递路由信息
2 Link-id： 传递路由的网络号
3、ADV router： 默认为所在区域ABR 的router-id
4、特性：在穿越不同 区域时，由其他的ABR重新产生 （ADV router 是变化的）
5、传播范围： LSA-3在区域之间进行泛洪</u>

# 缺省路由下，ospf外部路由属于
单选题471/1247、缺省情况下，OSPF外部路由属于以下哪一种类型？
**Type2**
Type1
Type5
OSPF会计算最适合的外部路由类型，所以没有缺省情况
<u>缺省情况下，OSPF引I入外部路由的缺省度量值为1引入的外部路由类型为Type2设置缺省标记值为1。</u>

# vrp上开启ospf默认路由
单选题 483/1247、在VRP系统中，能使OSPF路由器生成一条默认路由的命令是以下哪一项？
default-route-initiate
default information-originate
ospf default-route
**default-route-advertise**
<u>在OSPF协议中，产生默认路由的命令是default-route-advertise。</u>

# OSPF_hello报文
单选题499/1247、以下选项中哪一项不是OSPFHello报文交互的目的？
检查邻居是否存活
**传递链路状态信息**
协商一些必要的参数
发现邻居路由器
<u>传递链路状态信息是DD和LSU报文的工作。</u>

# ospf认证描述
单选题508/1247、以下关于0SPF报文认证的描述，错误的是哪一项？
**OSPF报文认证会将OSPF报文一并加密以确保其安全性保密性**
路由器支持接口认证和区域认证两种OSPF报文认证方式，当两种认证方式都存在时，优先使用接口认证方式
OSPF接口认证方式下，相邻路由器直连接口下的认证模式和口令必须一致
OSPF使报文认证功能后，只有通过认证的OSPF报文才能被接收
<u>OSPF支持报文验证功能，只有通过验证的OSPF报文才能接收，否则将不能正常建立邻居。并不是将OSPF报文一并加密。</u>

# 选举router id
单选题512/1247、 以下关于OSPF Router ID的描述，正确的是哪一项？
充许多台设备使用同一个 Router ID，也便于识别该设备所在的区域位置
在没有手工配置OSPF Router I D的时候，设备最先使用Loopback O接口的IP地址作为Router ID
当使用物理接口的IP地址作为OSPF的Router ID时，该接口必须划进相应的OSPF域内
**若使用物理接口IP 地址作为OSPF的Router ID时，IP 地址最大的被选为该设备OSPF Router ID**
<u>如果多台设备使用相同的RID，可能会导致OSPF邻居无法建立；RID可以通过手动配置及自动选举的方式获取，自动选举先选Loopback口地址，如果存在多个，则选择Loopback地址大的作为RID，如果没有Loopback，则选择物理接口IP地址大的作为RID</u>

# 选举DR/BDR
单选题 516/1247、以下关于OSPF DR/BDR的描述，错误的是哪一项？
在邻居状态为lnit时，路由器之间并不会协商DR/BDR
即使直连的两台路由器dr-priority设定为255，他们 之间还是会有DR和 BDR选举出来
**在DR/BDR协商的过程中，参与协商的路由器都会认为自己是BDR**
如果双方DR/BDR选举失败，则双方邻居状态会持续保特在2-Way状态
<u>在网络刚开始，所有路由器都以为自己是DR，所以会把自己的路由信息发送在网络中，然后进行比较，优先级最高的为DR，次高为BDR，先选BDR，再选DR。
</u>
# 未建立卡在2-way
![image-2024720410678.png|400](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/%E5%86%85%E9%83%A8%E8%B7%AF%E7%94%B1%E5%8D%8F%E8%AE%AEospf/image-2024720410678.png)
双方Hello间隔不一致
使用了错误的Router ID
**双方dr-priority 都设置为了0**
主从关系没有建立
<u>图中的信息显示接口的DR优先级为0，故选C。D选项主从关系是邻接关系建立才会判断的，所以不对。A和B选项是影响邻居关系建立的，与图中信息不符。</u>
# full状态不是broadcast网络类型了了
![image-2024720557707.png|375](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/%E5%86%85%E9%83%A8%E8%B7%AF%E7%94%B1%E5%8D%8F%E8%AE%AEospf/image-2024720557707.png)
该邻 接关系使用的Hello包发送间隔是5秒
如果该路由器的邻居失效时间采用了缺省配置，并在图中显示的6秒内没有收到对方发来的Hello包，则该状态会变为Down
**该路由器使用的网络类型一定不是broadcast**
该图中没有DR和BDR的原因可能是 对端路由器dr-priorityi设置为0
<u>该邻居关系已经是Full了，并且没有选举DR和BDR，所以可以判定这个端口的网络类型一定不是Broadcast。
</u>
# 未开启mtu检查
单选面 545/1247、在OSPF协议中，下面说法哪个是错误的？
所接收的 Hello 报文中Hello Interval 字 段 必须和收端口的配置 一致
所接收的Hello 报文中Dead Interval字段必须和收端口的配置 一致
广播型网络中所接收的Hello报文中Network Mask字段必须和换收端口的网络拖码
**所接收的Hello报文中MTU必须和接收端口的配置一致**
<u>该题目考察的是在建立 OSPF 邻接关系时,hello 报文中的参数的比较原则。在报文中的 MTU 如果不一致的话,是没有关系的,因为华为设备上没有开启 MTU 参数的检查。况且在 OSPF 的 Hello 报文中,根本不存在 MTU,MTU 字段存在与 OSPF 的 DD 报文中。</u>

# 判断----------------------------------------------------
判断题 889/1247、OSPF支持多进程，在同一台路由器上可以运行多个不同的OSPF进程，它们之间互不影响，彼此独立。不同OSPF进
程之问的路由交互相当于不同路由协议之间的路由交互
**正确**
<u>不同的OSPF进程互相独立，彼此要学习路由需要和不同路由协议一样进行重发布</u>
判断题890/1247、OSPF中，在广播类型网络中的选举出来的DR和BDR既侦听224.0.0.5地址，也侦听224.0.0.6地址
**正确**
<u>224.0.0.5：所有OSPF路由器
224.0.0.6：DR和BDR</u>
判断题896/1247、如果RouterPriority被设置为0，那么在OSPF路由域中，该路由器允许被选举成DR或者BDR，只不过优先级最低
**错误**
<u>如果优先级是0，那么就是直接放弃对DR,BDR的选举。默认优先级为1</u>


# 判断图题目
![image-20247223532337.png|375](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/%E5%86%85%E9%83%A8%E8%B7%AF%E7%94%B1%E5%8D%8F%E8%AE%AEospf/image-20247223532337.png)
**错误**
<u>ABR是区域边界路由器，用来将一个或多个非骨干区域连接到骨干区域的路由器，可以是虚链路，题中未说明配置虚链路，因此RTD不是ABR。</u>
![image-20247221438398.png|325](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/%E5%86%85%E9%83%A8%E8%B7%AF%E7%94%B1%E5%8D%8F%E8%AE%AEospf/image-20247221438398.png)
**正确**
<u>因为R2和R3都是ABR设备</u>
![image-2024722163961.png|425](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/%E5%86%85%E9%83%A8%E8%B7%AF%E7%94%B1%E5%8D%8F%E8%AE%AEospf/image-2024722163961.png)
**正确**
<u>广播和非广播需要选举，首先比较优先级，优先级高的获胜，然后比较Router-ID，大的获胜。所以题目中的描述是正</u>
![image-20247221728919.png|275](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/%E5%86%85%E9%83%A8%E8%B7%AF%E7%94%B1%E5%8D%8F%E8%AE%AEospf/image-20247221728919.png)
**正确**
<u>p2mp和p2p可以通过修改时间一致性来建立邻居关系默认不能建立邻接关系的原因是hello时间不同，并不是因为不同的网络类型导致的，p2mp的hello和dead时间默认是30和120，p2p的hello和dead时间默认是10和40，两者如果需要建立邻居关系，将p2p的时间修改为和p2mp的时间一样的话是可以建立邻接的</u>
判断题914/1247、OSPF特点之一是只支持MD5验证。
**错误**
<u>OSPF还支持简单认证。</u>
判断题 916/1247、OSPF直接运行于TCP协议之上，使用TCP端口号179
**错误**
<u>OSPF是运行于IPV4之上的OSPF端口号是89。 BGP才是运行与TCP协议之上，使用的端口号是179。  </u>
判断题 920/1247、为了避免区域问的环路，0SPF规定不允许直接在两个非骨干区域之问发布路由信息，只允许在一个区域内部，或者
在骨干区域和 非骨干区域之间发布路由信息。因此，每个区域边界路由器（ABR）都必须连接到骨干区域
**正确**
<u>根据OSPF ABR规则，ABR是同时连接骨干区域和非骨干区域的路由器。
</u>

判断题927/1247、0SPF支持区域认证和接口认证两种方式，若同时配置这两种认证方式，则接口认证优于区域认证。
**正确**
<u>接口认证也称为链路认证。</u>

判断题931/1247、在广播或NBMA网络上，并非所有的邻居间都会建立邻接关系。
**正确**
<u>在OSPF的NBMA网络环境中会选择DR，所有的设备都会和DR建立邻接关系，但是DRother之间建立的是two-way状态的邻居关系。所以题目中的描述是正确的</u>。

判断题934/1247、 ospf dr-priority命令默认值为1，取值范围为0~255.
**正确**
<u>优先级默认为1，取值范围0-255</u>

判断题935/1247、在OSPF广播或者NBMA网络类型中，DR Priority大的设备不一定会成为DR
**正确**
<u>DR具有不可抢占性，后加入的设备，DR优先级高，也不会成为DR。除非重启网段内所有设备的OSPF进程，或者在建立了OSPF邻居的接口上shutdown，再undo shutdown。</u>

判断题982/1247Router id大的一定为主
**正确**
<u>在OSPF数据同步阶段，通过DD报文的信息来确定主从关系，仅仅比较两个设备的router-id，越大越好。所以题目中的描述是正确的。</u>

判断题949/1247AS边界路由器可以是内部路由器IR,或者是ABRR，必须属于骨干区域
**错误**
<u>边界路由器可以属于非骨干区域，但不是ABR是ASBR。</u>

判断题956/1247、OSPF路由协议中，asbr-summary命令可以跟not-advertise参数，该参数的意义是不通告聚合路由。
**正确**
<u>如果在命令中使用了关键字not-advertise，则属于这一网段的路由信息将不会被发布出去。</u>

判断题 957/1247、在OSPF路由域中，含有至少两个路由器的广播型网络和NBMA网络中，必须指定一台路由器为DR,另外一台为BDR
**错误**
<u>在OSPF的广播型网络和NBMA网络中，必须存在DR，但是BDR不是必须存在的，当其他路由器优先级改为0后将不参与DR/BDR选举，因此答案错误</u>

判断题958/1247、OSPF路由协议中，bandwidth-reference命令的单位是Mbps。
**正确**
<u>命令bandwidth-reference value，配置带宽参考值。  Value为计算链路开销时所依据的参考值，单位是Mbit/s。</u>

判断题959/1247、默认情况下，OSPF端口开销与端口的带宽有关计算公式为bandwidth-reference/bandwidth开销只OSPF自己计
算，不能手工更改。
**错误**
<u>OSPF使用Cost（开销）作为路由的度量值。每一个激活了OSPF的接口都会维护一个接口Cost值，缺省的接口Cost =100Mbits/接口带宽 。其中100 为OSPF指定的缺省参考值，该值是可手工配置的。</u>

判断题963/1247、当在华为路由器上运行OSPFv3时，**OSPFv3**进程会自动选择一个接口地址作为该进程的Router ID。
**错误**
<u>运行OSPFv2时，在没有手动配置进程Router ID时，进程会自动选择一个IP地址最大的作为进程的Router ID。但OSPFv3必须手动配置Router ID，否则OSPFv3无法正常运行。</u>

判断题984/1247、VRP平台上，当我们引I入OSPF路由到ISIS的时候如果不指定COST，开销值将默认设为16.
**错误**
<u>如果不指定COST，开销值将默认设为10（不管接口的带宽多大，开销默认值不变）。</u>

判断题989/1247、import-route limit命令不能够限制一个OSPF进程内可引I入的最大外部路由数量。
**错误**
<u>import-route limit命令作用是指定一个OSPF进程中可引入的最大外部路由数量。</u>

判断题992/1247、某一路由器的端口DR Priority被设置为0，那么该路由器接口充许被选举成DR或者BDR，只不过优先级最低
**错误**
DR Priority被设置为0代表的是放弃选举，不会成为DR或者BDR

判断题994/1247、在OSPF网络中，两台DRother设备并不会建立邻接关系，他们的状态会维持在2-way。
**正确**
<u>只允许DR、BDR与其他OSPF路由器建立邻接关系。DRother之间不会建立全毗邻的OSPF邻接关系，双方停滞在2-way状态。</u>

判断题1008/1247、DU标签分发方式下，如果采用Liberal保持方式，则设备都会保留所有LDPPeer发来的标签，无论该LDP Peer是否
为到达目的网段的下一跳
**正确**
<u>自由方式（Liberal）：对于从邻居LSR收到的标签映射，无论邻居LSR是不是自己的下一跳都保留。</u>

判断题1028/1247、OSPF的Router LSA中，如果其Link Type为1，则该LSA描述的是从本路由器到邻居路由器之间点到点的链路
时对应的LinkID描述的内容则为邻居路由器的接口IP地址
**错误**
<u>P2p类型的1LSA中，link ID是邻居的R-ID</u>

判断题1037/1247、在接口下修改接口的OSPF网络类型，需要对设备进行重启或者复位ospf，否则ospf不生效
**错误**
<u>这个是直接生效的，routerid那个不是</u>

判断题1046/1247、节点A和节点B之间有多条等价链路，但却没有实现等价负载分担，可能的原因是OSPF限制了最大负载分担链路的
数量。
**正确**
<u>ospf最高支持16条链路负载，但根据设备型号不同负载的数量也不同</u>

判断题1048/1247、在OSPF中，使用default-route-advertise命令会将该路由器变成ABR。
**错误**
<u>default-route-advertise命令会将该路由器变成ASBR，所以题目中的描述是错误的。</u>

判断题1057/1247、OSPF的Stub区域和Totally Stub区域解决了末端区域维护过大LSDB带来的问题，但对于某些特定场景，它们并不是最佳解决方案。
**正确**
<u>stub区域为特殊区域不接收外部路由，可以大大减少LSDB的大小</u>

判断题 1058/1247、两台路由器R1和R2直连，想要建立OSPF邻接关系，R1使用的MD5的端口认证，R2使用了MD5的区域认证，口令相同的情况下两台设备可以建立OSPF邻接关系。
**正确**
<u>直连设备间可以使用接口认证和区域认证建立邻居关系只要认证方式和密码相同</u>

判断题1059/1247、不选举DR/BDR的网络类型只有p2p类型。
**错误**
<u>只有多路访问网络才选举DR/BDR，或者可以说是多地址网络才选举DR/BDR，所以题目中的描述是错误的。</u>

判断题 1060/1247、当两个路由器之间通过DD报文交换数据库信息时，首先形成一个主从关系，DR Priority大的成为主路由器，确定其主从位为MS
**错误**
<u>确认主从和DR优先级没关系，而是Router id大的为主</u>

判断题1072/1247、OSPFv3采用与OSPFv2相同的路由通告方式：在OSPFv3区域视图通过network命令进行通告
**错误**
<u>OSPFv3是在端口下宣告的</u>

判断题1076/1247、管理员可使用import-route命令将不同进程号下的OSPF互相引入。
**正确**
<u>不同OSPF进行是互相独立的，需要学习路由的话可以通过import-route引入路由来实现</u>

判断题1077/1247、使用Silent-Interface的接口，不会接收和发送OSPF报文，但是直连路由可以通告到OSPF.
**正确**
<u>
接口可以配置为静态接口，不参与OSPF协议计算，但是还是可以通告进OSPF协议</u>

判断题1085/1247、在OSPF中，若网络类型为NBMA或广播型，且路由器两台或多台时，必须指定DR和BDR。
**错误**
<u>并不是必须要有BDR而是必须有DR才能工作</u>

判断题1095/1247、在MA网络中的两台DRother路由器R1和R2建立邻居关系，那么在R1中执行[R1]diaplay ospf peer命令，此时显示R2的邻居状态为Loading
**错误**
<u>MA环境下(在以太网环境、同一个广播域内),两个DRother路由器之间的状态即为邻居状态(two-way)</u>

判断题1096/1247、在MA网络中，DR、BDR选举完成之后，如果BDR出现了故障，那么DRother会重新选举出新的BDR,直到原BDR恢复正常。
**错误**
<u>因为BDR是不可以被抢占的，所以最后的那句“直到原BDR恢复正常”是错误的。</u>

判断题1104/1247、当OSPF处于ExStart状态时，路由器与邻居之间相互发送包含链路状态信息摘要的DD报文。
**错误**
<u>在下是一个状态exchange</u>

判断题1106/1247、在OSPF中部署Filter-Policy时， Filter-Policy会修改该OSPF的LSDB。
**错误**
<u>过滤策略会过滤路由信息，不会修改到链路状态数据库</u>

判断题1107/1247、在多个ASBR将同一条外部路由引l入到同一个OSPF域内时，使用metric-type为2的外部路由类型，可以避免次优路径。
**错误**
<u>为了防止OSPF外部路由的次优路径，一定要在计算一个OSPF外部路由的时候，考虑到OSPF网络内部的转发链路的实际情况，所以需要确保OSPF的外部路由的metric-type是1</u>

判断题1117/1247、Filter-Policy在OSPF中使用时，可以通过过滤LSA以实现路由控制。
**错误**
<u>Filter-policy不能直接过滤LSA</u>

判断题1130/1247、在VRP系统中，命令ospf cost和band width-reference同时配置的时候，接口上的cost值以band width-reference配置为准。
**错误**
<u>接口上和全局上一起配置，都是接口配置更优先</u>

![image-20247244543717.png|400](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/%E5%86%85%E9%83%A8%E8%B7%AF%E7%94%B1%E5%8D%8F%E8%AE%AEospf/image-20247244543717.png)
**import**

填空题 1158/1247、某工程师需要将路由器OSPF的Router ID修改为x.X.X.x,在不重启路由器和不删除该OSPF配置的前提下，用户视图中输入（）命令，使得该Router ID生效。，（答案需要携带该OSPF进程ID，并命令全小写，单词与单词之间使用一个空格隔开）
**reset ospf process 1**
<u>RouterID修改后需要重置进程后才会生效</u>

OSPFv3中传播范围为一个区域的LSA有()类。（仅填写阿拉伯教字）
**1 2 9**

![image-20247243313521.png](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/%E5%86%85%E9%83%A8%E8%B7%AF%E7%94%B1%E5%8D%8F%E8%AE%AEospf/image-20247243313521.png)\
**R3**
<u>R2为完全stub区域，只能产生0.0.0.0的Type3 LSA</u>

填空题1192/1247、使能了OSPF的路由器在Init状态下，发送Hello包的目的地址是 （） （请填写点分十进制IP地址)
**224.0.0.5**
<u>224.0.0.5是OSPF的组播地址，所有运行OSPF的路由器</u>

填空题 1197/1247、在OSPF中使用default-route-advertise命令用来将缺省路由通告到普通OSPF区域，当该区域里没有缺省路由的时候，使用 （）来强制通告。 （请填写小写英文）
**always**
<u>手工下放默认路由 default-route-advertise 下放默认路由,必须要保证本地有默认路由。 default-route-advertise always 无论本地是否有默认路由,都会下放一条默认路由。</u>

![image-20247243957835.png|425](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/%E5%86%85%E9%83%A8%E8%B7%AF%E7%94%B1%E5%8D%8F%E8%AE%AEospf/image-20247243957835.png)
**255 254 0 0 0** 
