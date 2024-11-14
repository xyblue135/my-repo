# 涉及命令
```
<Huawei>display ip routing-table 
<Huawei>display ip routing-table verbose   #详细路由表  重要
<Huawei>display fib
```
# 路由表
Destination/Mask  //路由前缀 是由目的IP地址和前缀长度/掩码 组成
Proto //以什么方式生成的路由
preference //优先级，路由器会根据优先级选择，将最优的路由加入到路由表中
Cost 度量值，开销 可以影响数据转发路径
Flags //标志位 路由已经下发到了FIB表 D为下发了，RD为已经下发了静态的 
```
<Huawei>display ip routing-table 
Route Flags: R - relay, D - download to fib
------------------------------------------------------------------------------
Routing Tables: Public
         Destinations : 10       Routes : 10       

Destination/Mask    Proto   Pre  Cost      Flags NextHop         Interface

      127.0.0.0/8   Direct  0    0           D   127.0.0.1       InLoopBack0
      127.0.0.1/32  Direct  0    0           D   127.0.0.1       InLoopBack0
127.255.255.255/32  Direct  0    0           D   127.0.0.1       InLoopBack0
    192.168.1.0/24  Direct  0    0           D   192.168.1.1     GigabitEthernet0/0/0
    192.168.1.1/32  Direct  0    0           D   127.0.0.1       GigabitEthernet0/0/0
  192.168.1.255/32  Direct  0    0           D   127.0.0.1       GigabitEthernet0/0/0
    192.168.2.0/24  OSPF    10   2           D   192.168.1.2     GigabitEthernet0/0/0
    192.168.3.0/24  OSPF    10   3           D   192.168.1.2     GigabitEthernet0/0/0
  192.168.100.0/24  Static  60   0          RD   192.168.1.2     GigabitEthernet0/0/0
255.255.255.255/32  Direct  0    0           D   127.0.0.1       InLoopBack0
------------------------------------------------------------------------------
<Huawei>
```
# 路由表详细信息
```
<Huawei>display IP routing-table verbose
Route Flags: R - relay, D - download to fib
------------------------------------------------------------------------------
Routing Tables: Public
         Destinations : 10       Routes : 10       


Destination: 127.0.0.0/8
     Protocol: Direct           Process ID: 0
   Preference: 0                      Cost: 0
      NextHop: 127.0.0.1         Neighbour: 0.0.0.0
        State: Active NoAdv            Age: 00h40m09s
          Tag: 0                  Priority: high
        Label: NULL                QoSInfo: 0x0
   IndirectID: 0x0              
 RelayNextHop: 0.0.0.0           Interface: InLoopBack0
     TunnelID: 0x0                   Flags:  D

Destination: 127.0.0.1/32
     Protocol: Direct           Process ID: 0
   Preference: 0                      Cost: 0
      NextHop: 127.0.0.1         Neighbour: 0.0.0.0
        State: Active NoAdv            Age: 00h40m09s
          Tag: 0                  Priority: high
        Label: NULL                QoSInfo: 0x0
   IndirectID: 0x0              
 RelayNextHop: 0.0.0.0           Interface: InLoopBack0
     TunnelID: 0x0                   Flags:  D


```
**等，上面的Tag(与mpls关联)和Label（策略路由）是比较重要的**
# FIB表
1. **G - Gateway Route**:表示这是一个网关路由条目。这种类型的路由通常用于指明到达远程网络的路径，其中下一跳是一个网关地址。
2. **H - Host Route**: 表示这是一个主机路由条目。主机路由用于精确指定单个 IP 地址的路由，通常子网掩码为 /32。
3. **U - Up Route**:表示这是一个有效的、活动的路由条目。这意味着这条路由是可达的，并且可以用于转发数据包。
4. **S - Static Route**:表示这是一个静态路由条目。静态路由是由网络管理员手动配置的，用于指定特定目的地的固定路径。
5. **D - Dynamic Route**:表示这是一个动态路由条目。动态路由是通过动态路由协议（如 OSPF、RIP 等）自动学习到的路由。
6. **B - Black Hole Route**:表示这是一个黑洞路由条目。黑洞路由是一种特殊的路由条目，用于指示无法到达的目的地。当数据包匹配黑洞路由时，它们会被丢弃。
7. **L - Vlink Route**:表示这是一个虚拟链路（Virtual Link, Vlink）路由条目。虚拟链路是 OSPF 中的一种特性，用于在两个非直接相连的 OSPF 区域间建立一条逻辑连接，以便于区域间的路由传播。
```
<Huawei>display fib
Route Flags: G - Gateway Route, H - Host Route,    U - Up Route
             S - Static Route,  D - Dynamic Route, B - Black Hole Route
             L - Vlink Route
--------------------------------------------------------------------------------
 FIB Table:
 Total number of Routes : 10 
 
Destination/Mask   Nexthop         Flag  TimeStamp     Interface      TunnelID
192.168.1.255/32   127.0.0.1       HU    t[9]          InLoop0        0x0
192.168.1.1/32     127.0.0.1       HU    t[9]          InLoop0        0x0
255.255.255.255/32 127.0.0.1       HU    t[2]          InLoop0        0x0
127.255.255.255/32 127.0.0.1       HU    t[2]          InLoop0        0x0
127.0.0.1/32       127.0.0.1       HU    t[2]          InLoop0        0x0
127.0.0.0/8        127.0.0.1       U     t[2]          InLoop0        0x0
192.168.1.0/24     192.168.1.1     U     t[9]          GE0/0/0        0x0
192.168.2.0/24     192.168.1.2     DGU   t[49]         GE0/0/0        0x0
192.168.3.0/24     192.168.1.2     DGU   t[54]         GE0/0/0        0x0
192.168.100.0/24   192.168.1.2     GSU   t[610]        GE0/0/0        0x0
<Huawei>
```
1. **G - Gateway Route**:反应到外部的路由，非直连的。  没G直连。有G非直连
2. **H - Host Route**: 掩码32，主机路由
3. **U - Up Route**:在转发的可以正常用的
4. **S - Static Route**:静态的
5. **D - Dynamic Route**:动态的
6. **B - Black Hole Route**:黑洞路由，垃圾回收站
7. **L - Vlink Route**:两个ospf非直连的建立的虚拟链路