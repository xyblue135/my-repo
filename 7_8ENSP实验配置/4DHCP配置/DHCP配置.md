# 相关说明
![image-20247163110113.png|425](7_8ENSP实验配置/4DHCP配置/DHCP配置/image-20247163110113.png)
思考：为什么要二次，第二次确认，防止两个dhcp服务器
答案：广播，我在用了
# 配置
```
1.
[huawei]dhcp enable
2.
[接口]dhcp select interface
3.
指定dns
[接口]dhcp server dns-list ip-address
4.配置接口地址池中不参与分配ip的范围
[接口]dhcp server excluded-ip-address start-ip-address [end-ip-address]
5.配置租期
[接口]dhcp server lease []
--------------------------------------------------------------
6． 创建全局地址池
[Huawei]ip pool ip-pool-name
7. 配置全局地址池可动态分配的IP地址范围
[Huawei-ip-pool-2] network ip-address [ mask { mask | mask-length } ]
8. 配置DHCP客户端的网关地址
[Huawei-ip-pool-2] gateway-list ip-address
9. 配置DHCP客户端使用的DNS服务器的IP地址
[Huawei-ip-pool-2] dns-list ip-address
10.配置IP地址租期
[Huawei-ip-pool-2] lease { day day [ hour hour [ minute minute ] ] | unlimited }
11.使能接口的DHCP服务器功能
[Huawei-Gigabitthernet0/0/0] dhcp select global
```
# 案例1接口上
```
dhcp enable
interface g0/0/0
dhcp select interface
dhcp server lease day 3
```
![image-20247165347104.png|425](7_8ENSP实验配置/4DHCP配置/DHCP配置/image-20247165347104.png)
# 案例2全局
```
dhcp enable
ip pool pool2  #1-64
network 10.1.1.0 24
gateway-list 10.1.1.1
lease day 10
qu
int g0/0/0
dhcp select global
```
![image-20247165414158.png|425](7_8ENSP实验配置/4DHCP配置/DHCP配置/image-20247165414158.png)
# 案例3全局（推荐）
```
[Huawei]dhcp enable 
[Huawei]ip pool pool2
Info: It's successful to create an IP address pool.
[Huawei-ip-pool-pool2]network 192.168.1.0 mask 24
[Huawei-ip-pool-pool2]gateway-list 192.168.1.254
[Huawei-ip-pool-pool2]dns-list 192.168.1.254  可选啊
[Huawei-ip-pool-pool2]lease day 2

[Huawei-ip-pool-pool2]display this 
[V200R003C00]
#
ip pool pool2
 gateway-list 192.168.1.254 
 network 192.168.1.0 mask 255.255.255.0 
 lease day 2 hour 0 minute 0 
 dns-list 192.168.1.254 
#
return

[Huawei-ip-pool-pool2]int g0/0/0
[Huawei-GigabitEthernet0/0/0]dhcp select global 
```

![image-202471713693.png|300](7_8ENSP实验配置/4DHCP配置/DHCP配置/image-202471713693.png)
![image-20247171055371.png|250](7_8ENSP实验配置/4DHCP配置/DHCP配置/image-20247171055371.png)
# 精简版本
```
在路由器上
<Huawei>sy
[Huawei]dhcp enable 

[Huawei]ip pool dhcp1
[Huawei-ip-pool-dhcp1]network 192.168.1.0 mask 24	
[Huawei-ip-pool-dhcp1]gateway-list 192.168.1.254

[Huawei-ip-pool-dhcp1]qu
[Huawei]interface g0/0/0
[Huawei-GigabitEthernet0/0/0]ip address 192.168.1.254 24
[Huawei-GigabitEthernet0/0/0]dhcp select global 
```
# 减少dhcp的范围
全局的dhcp服务器删除dhcp的分配的范围
```
[huawei]ip pool pool2
[huawei-ip-poop-pool2]dhcp server excluded-ip-address 192.168.1.1 再加一个就是范围
```
基于接口的dhcp服务器删除dhcp分配的范围
```
int g0/0/0
[Huawei-GigabitEthernet0/0/0]dhcp server excluded-ip-address 192.168.1.1  再加一个就是范围
```


# ipv6的acl
ipv6的acl不用反掩码，因为就没有
基本acl6 【2000-2999】
高级acl6 【3000-3999】
```
acl ipv6 2000
rule 10 permit source 2001:00/64
```
案例:使用高级acl6允许源地址2001:;/64 目标为3000:1/的http流量，其他流量过滤，并在出接口调用
```
acl ipv6 3000
rule 10 permit tcp source 2001:64 destination 3000::1/128 destination-port eq 80
rule 20 deny ipv6 source any destination any
qu
int g0/0/0
traffic-filter inbound ipv6 acl 3000
```
# ACL的不足（不能精确匹配）
如果需要匹配192.168.1.0/24 192.168.1.0/25 192.168.1.0/26不能一条路由写出来，如果直接192.168.1.0 0.0.0.255匹配的是24开始以后的了，将不行。不能精确


