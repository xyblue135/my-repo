
# 必须
```
ospf 进程 router的id
ospf 1 router-id 1.1.1.1
area 0.0.0.0 
area 0
network 192.168.100.0 255.255.255.0
network 192.168.101.0 255.255.255.0
network 192.168.102.0 255.255.255.0
```
ospf 进程id router id
默认进程为1，可以设置为1-65535
router id 不设置的话，也会给个默认的
area 给0区域是只想要0区域，给其它就是0.0.0.1 0.0.0.2了
network给路由了，网段和反掩码
# 修改开销
开销=100M/接口带宽
但实际情况下，百兆和千兆的接口带宽是1和0.1      0.1的开销也会被显示为1
```
[接口]ospf cost 数值（0-65535）
```
设置`参考带宽`，缺省为100M（开销cost=参考带宽/接口带宽）
```
[ospf-1]bandwidth-reference value(1-2147483648缺省100M)
```
# 设置接口选举DR优先级 缺省为1
```
[接口]ospf dr-priority priority(0-255)
```
# 配置案例1
使得R1和R3的loopback接口的1.1.1.1和3.3.3.3可以互相ping通
![image-20247165643519.png|500](7_8ENSP实验配置/1ospf配置/ospf配置/image-20247165643519.png)

```
[R1]
sy
interface loopback 10
ip address 1.1.1.1 32
qu
interface g0/0/0
ip address 10.1.12.1 30
qu
ospf 1 router-id 1.1.1.1
area 0
network 10.1.12.0 0.0.0.3
network 1.1.1.1 0.0.0.0
qu
[R2]
sy
interface g0/0/0
ip address 10.1.12.2 30
qu
interface g0/0/1
ip address 10.1.23.1 30
qu
ospf 1 router-id 2.2.2.2
area 0
network 10.1.12.0 0.0.0.3
qu
area 1
network 10.1.23.0 0.0.0.3
qu
[R3]
sy
interface loopback 10
ip address 3.3.3.3 32
qu
interface g0/0/0
ip address 10.1.23.2 30
qu
ospf 1 router-id 3.3.3.3
area 1
network 10.1.23.0 0.0.0.3
network 3.3.3.3 0.0.0.0
qu

```

# 关于Router ID
也就是用命令 ospf 1的时候，也就是没有手工设置routerid的话，应该是从loopback里面选择一个最大的ip，但是模拟器上不是，需要真机
# 重启进程
```
reset ospf 1 process
```
# 手动指定邻居
```
ospf 1
peer 10.1.12.2
```
# 相关命令
```
display ospf interface g0/0/0
display ospf peer 
display ospf peer brief
display ospf error
display ospf error interface g0/0/0
display ospf lsdb
display ospf lsbd brief
display ospf lsdb self-originate
display ospf 1 lsdb self-originate
display ospf 1 lsdb network self-originate
display ospf 1 lsdb router self-originate
```

# 查看接口状态
```
<Huawei>display ospf interface 

	 OSPF Process 1 with Router ID 4.4.4.4
		 Interfaces 

 Area: 0.0.0.1          (MPLS TE not enabled)
 IP Address      Type         State    Cost    Pri   DR              BDR 
 192.168.3.2     Broadcast    DR       1       1     192.168.3.2     192.168.3.1
 
 Area: 0.0.0.2          (MPLS TE not enabled)
 IP Address      Type         State    Cost    Pri   DR              BDR 
 192.168.4.1     Broadcast    BDR      1       1     192.168.4.2     192.168.4.1
 
<Huawei>
```
# 查看ospf路由表
```
display ospf routing
```