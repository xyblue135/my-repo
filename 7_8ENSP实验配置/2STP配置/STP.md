# 原理
 ![image-2024714464684.png](7_8ENSP实验配置/2STP配置/STP/image-2024714464684.png)
# 未开启FTP状态
默认清空下华为的交换机是开启MSTP切实enable状态的
但是我们先看一下没有开启的状态吧
```
stp disable
[Huawei]display stp brief
 Protocol Status       :Disabled             
 Protocol Standard     :IEEE 802.1s             
 Version               :3             
 CIST Bridge Priority  :32768             
 MAC address           :4c1f-cc8c-362e             
 Max age(s)            :20             
 Forward delay(s)      :15             
 Hello time(s)         :2             
 Max hops              :20 
[Huawei]
```
# 开启stp stp enable

```
stp enable
[Huawei]display stp brief 
 MSTID  Port                        Role  STP State     Protection
   0    GigabitEthernet0/0/1        DESI  FORWARDING      NONE
[Huawei]
```
# 将mstp改为stp模式 stp mode stp
将模拟器中默认的MSTP模式手动改为STP模式并查看STP信息和STP接口信息。
![image-20247131413721.png](7_8ENSP实验配置/2STP配置/STP/image-20247131413721.png)
```
[Lsw1]stp mode stp
Info: This operation may take a few seconds. Please wait for a moment...done.
[Lsw2]stp mode stp
Info: This operation may take a few seconds. Please wait for a moment...done.
```
等待一段时间学习状态变为转发状态
# 查看简要stp信息display stp brief
![image-20247134443775.png](7_8ENSP实验配置/2STP配置/STP/image-20247134443775.png)
# 查看接口stp信息display stp interface + 接口
`display stp interface + 接口` 
可以看到是stp模式
```
[Huawei]display stp interface GigabitEthernet 0/0/1
-------[CIST Global Info][Mode STP]-------
CIST Bridge         :32768.4c1f-cc8c-362e
Config Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 20
Active Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 20
CIST Root/ERPC      :32768.4c1f-cc8c-362e / 0
CIST RegRoot/IRPC   :32768.4c1f-cc8c-362e / 0
CIST RootPortId     :0.0
BPDU-Protection     :Disabled
TC or TCN received  :4
TC count per hello  :0
STP Converge Mode   :Normal 
Time since last TC  :0 days 0h:2m:33s
Number of TC        :3
Last TC occurred    :GigabitEthernet0/0/1
----[Port25(GigabitEthernet0/0/1)][FORWARDING]----
 Port Protocol       :Enabled
 Port Role           :Designated Port
 Port Priority       :128
 Port Cost(Dot1T )   :Config=auto / Active=20000
 Designated Bridge/Port   :32768.4c1f-cc8c-362e / 128.25
 Port Edged          :Config=default / Active=disabled
 Point-to-point      :Config=auto / Active=true
 Transit Limit       :147 packets/hello-time
 Protection Type     :None
 Port STP Mode       :STP 
 Port Protocol Type  :Config=auto / Active=dot1s
 BPDU Encapsulation  :Config=stp / Active=stp
 PortTimes           :Hello 2s MaxAge 20s FwDly 15s RemHop 20
 TC or TCN send      :18
 TC or TCN received  :2
 BPDU Sent           :90             
          TCN: 0, Config: 90, RST: 0, MST: 0
 BPDU Received       :3             
          TCN: 2, Config: 1, RST: 0, MST: 0


```
 这个是MSTP的，其实差不多
```
[Huawei]display stp interface GigabitEthernet 0/0/1
-------[CIST Global Info][Mode MSTP]-------
CIST Bridge         :32768.4c1f-cc8c-362e
Config Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 20
Active Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 20
CIST Root/ERPC      :32768.4c1f-cc8c-362e / 0
CIST RegRoot/IRPC   :32768.4c1f-cc8c-362e / 0
CIST RootPortId     :0.0
BPDU-Protection     :Disabled
TC or TCN received  :2
TC count per hello  :0
STP Converge Mode   :Normal 
Time since last TC  :0 days 0h:0m:39s
Number of TC        :2
Last TC occurred    :GigabitEthernet0/0/1
----[Port1(GigabitEthernet0/0/1)][FORWARDING]----
 Port Protocol       :Enabled
 Port Role           :Designated Port
 Port Priority       :128
 Port Cost(Dot1T )   :Config=auto / Active=20000
 Designated Bridge/Port   :32768.4c1f-cc8c-362e / 128.1
 Port Edged          :Config=default / Active=disabled
 Point-to-point      :Config=auto / Active=true
 Transit Limit       :147 packets/hello-time
 Protection Type     :None
 Port STP Mode       :MSTP 
 Port Protocol Type  :Config=auto / Active=dot1s
 BPDU Encapsulation  :Config=stp / Active=stp
 PortTimes           :Hello 2s MaxAge 20s FwDly 15s RemHop 20
 TC or TCN send      :1
 TC or TCN received  :2
 BPDU Sent           :25             
          TCN: 0, Config: 0, RST: 0, MST: 25
 BPDU Received       :2             
          TCN: 0, Config: 0, RST: 0, MST: 2
```
解释参数
```
[Huawei]display stp interface GigabitEthernet 0/0/1




CIST Global Info（CIST 全局信息）

-------[CIST Global Info][Mode STP]------- 

这是交换机的桥接 ID 和 MAC 地址。
CIST Bridge         :32768.4c1f-cc8c-362e

配置时间，分别是 Hello 时间（默认2秒）、MaxAge 时间（最大生存时间，默认20秒）、FwDly（转发延迟时间，默认15秒）、MaxHop（最大跳数，默认20）。
Config Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 20

当前活动配置的时间。
Active Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 20

网络中的根桥和根路径开销（ERPC）值。
CIST Root/ERPC      :32768.4c1f-cc8c-362e / 0

当前网络中注册的根桥和路径开销（IRPC）值。
CIST RegRoot/IRPC   :32768.4c1f-cc8c-362e / 0

根端口 ID（0.0表示没有根端口）。
CIST RootPortId     :0.0

BPDU 保护是否启用（此处为禁用）。
BPDU-Protection     :Disabled

收到的拓扑变化（TC）或拓扑变化通知（TCN）的次数（此处为4）。
TC or TCN received  :4

每个 Hello 时间间隔内的 TC 计数（此处为0）。
TC count per hello  :0

STP 收敛模式（此处为正常）。
STP Converge Mode   :Normal

自上次拓扑变化以来的时间（此处为0天0小时2分33秒）。
Time since last TC  :0 days 0h:2m:33s

拓扑变化的次数（此处为3）
Number of TC        :3

最近一次拓扑变化发生的接口（此处为 GigabitEthernet0/0/1）。
Last TC occurred    :GigabitEthernet0/0/1




（端口信息）
----[Port25(GigabitEthernet0/0/1)][FORWARDING]----


端口协议是否启用（此处为启用）。
 Port Protocol       :Enabled

端口角色（此处为指定端口）。
 Port Role           :Designated Port

端口优先级（默认128）。
 Port Priority       :128

端口成本，配置为自动，实际为20000。
 Port Cost(Dot1T )   :Config=auto / Active=20000

指定桥和端口 ID（此处为32768.4c1f-cc8c-362e / 128.25）。
 Designated Bridge/Port   :32768.4c1f-cc8c-362e / 128.25

端口是否配置为边缘端口（默认值为 disabled）。
 Port Edged          :Config=default / Active=disabled

点对点状态，配置为自动，实际为 true。
 Point-to-point      :Config=auto / Active=true

传输限制，每个 Hello 时间内的最大数据包数量（此处为147）。
 Transit Limit       :147 packets/hello-time

保护类型（此处为无）
 Protection Type     :None

端口 STP 模式（此处为STP）
 Port STP Mode       :STP 

口协议类型，配置为自动，实际为 dot1s。
 Port Protocol Type  :Config=auto / Active=dot1s

BPDU 封装类型，配置为 STP，实际为 STP。
 BPDU Encapsulation  :Config=stp / Active=stp

端口时间参数，包括 Hello 时间（2秒）、MaxAge 时间（20秒）、FwDly 时间（15秒）、RemHop（剩余跳数，20）。
 PortTimes           :Hello 2s MaxAge 20s FwDly 15s RemHop 20

发送的拓扑变化（TC）或拓扑变化通知（TCN）的次数（此处为18）。
 TC or TCN send      :18

收到的拓扑变化（TC）或拓扑变化通知（TCN）的次数（此处为2）。
 TC or TCN received  :2



发送的 BPDU 数量（此处为90），包括 TCN、配置和 RST、MST BPDU。 **TCN**: 拓扑变化通知 **Config**: 配置 BPDU **RST**: 快速生成树（RST）BPDU **MST**: 多生成树（MST）BPDU


 BPDU Sent           :90             
          TCN: 0, Config: 90, RST: 0, MST: 0





**BPDU Received**: 接收到的 BPDU 数量（此处为3），包括 TCN、配置和 RST、MST BPDU。 **TCN**: 拓扑变化通知 **Config**: 配置 BPDU **RST**: 快速生成树（RST）BPDU **MST**: 多生成树（MST）BPDU


 BPDU Received       :3             
          TCN: 2, Config: 1, RST: 0, MST: 0
```
文件对比，主要在time和发送的拓扑变化（TC）或拓扑变化通知（TCN）这边了 以及不同交换机被选举的
这个是一个交换机的不同模式的
![[7_8ENSP实验配置/2STP配置/三stp.htm]]
这个是相邻交换机的
![[7_8ENSP实验配置/2STP配置/相邻路由器对比.htm]]
# 交换机选举根交换机 display stp
display stp 且这个里面的不能简单判断是不是根交换机，`根交换机上的所有端口都会是指定端口`，因为它们负责在各自的网段中转发数据。
display stp brief 信息有点少
display stp interface G 0/0/1
如果不符合，那就不是根交换机
上面那个是交换机本身，下面的那个是根桥，不一样，所以下图这个就是非根桥交换机
![image-20247133044757.png](7_8ENSP实验配置/2STP配置/STP/image-20247133044757.png)
这个是根路由器
![image-2024713322278.png](7_8ENSP实验配置/2STP配置/STP/image-2024713322278.png)


# 设置边缘端口（不参与生成树的运算）
一般就是用于连接pc啥的，断了就断了，没办法，除非带内带外去吧
```
port-group group-member GigabitEthernet 0/0/20 to GigabitEthernet 0/0/24
stp edged-port enable
```