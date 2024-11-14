
# 静态nat配置
![image-20247162346880.png|475](7_8ENSP实验配置/4NAT配置/NAT配置/image-20247162346880.png)
方法一：
```
配置好接口ip后
[接口]nat static global [global-address] inside [host-address]
[接口]nat static global 122.1.2.2 inside 192.168.1.2
[接口]nat static global 122.1.2.3 inside 192.168.1.3  
```
方法二：
```
配置好接口ip后
[huawei]nat static global [global-address] inside [host-address]
进入接口
[接口]nat static enable
```
## 静态案例
![image-20247161725274.png|500](7_8ENSP实验配置/4NAT配置/NAT配置/image-20247161725274.png)
![image-20247161811781.png](7_8ENSP实验配置/4NAT配置/NAT配置/image-20247161811781.png)
```
[AR1]
sy
int g0/0/0
ip address 192.168.1.254 24
int g0/0/1
ip address 122.1.2.14 24
qu
ip route-static 0.0.0.0 0 122.1.2.15
int g0/0/1
nat static global 122.1.2.1 inside 192.168.1.1
nat static global 122.1.2.2 inside 192.168.1.2
nat static global 122.1.2.3 inside 192.168.1.3
[AR2]
sy
int g0/0/0
ip address 122.1.2.15 24
qu
int g0/0/1
ip address 200.1.2.254 24
```
## 检查命令display nat static
```
<Huawei>display nat static 
  Static Nat Information:
  Interface  : GigabitEthernet0/0/1
    Global IP/Port     : 122.1.2.1/---- 
    Inside IP/Port     : 192.168.1.1/----
    Protocol : ----     
    VPN instance-name  : ----                            
    Acl number         : ----
    Netmask  : 255.255.255.255 
    Description : ----

    Global IP/Port     : 122.1.2.2/---- 
    Inside IP/Port     : 192.168.1.2/----
    Protocol : ----     
    VPN instance-name  : ----                            
    Acl number         : ----
    Netmask  : 255.255.255.255 
    Description : ----

    Global IP/Port     : 122.1.2.3/---- 
    Inside IP/Port     : 192.168.1.3/----
    Protocol : ----     
    VPN instance-name  : ----                            
    Acl number         : ----
    Netmask  : 255.255.255.255 
    Description : ----

  Total :    3
<Huawei>
```
# 动态nat配置
动态NAT：静态NAT严格地一对一进行地址映射，这就导致即使内网主机长时间离线或者不发送数据时，与之对应的公有地
址也处于使用状态。为了避免地址浪费，动态NAT提出了地址池的概念：所有可用的公有地址组成地址池。
当内部主机访问外部网络时临时分配一个地址池中未使用的地址，并将该地址标记为“In Use”。当该主机不再访问外部
网络时回收分配的地址，重新标记为 “Not Use ” 。

配置
```
#创建地址池
[huawei]nat address-group group-index[1-7] start-address end-address
[huawei]nat address-group 1 122.1.2.1 122.1.2.3
#配置地址转换的acl规则
[huawei]acl number
[huawei]acl 2000
[huawei-acl-basic-number]rule id permit source source-address source-wildcard
[huawei-acl-basic-2000]rule 5 permit source 192.168.1.0 0.0.0.255
#配置地址池nat outbound
#进入接口
[接口]nat outbound acl-number address-group group-index[no-pat]
[接口]nat outbound 2000 address-group 1 no-pat 
```
![image-2024716500698.png|375](7_8ENSP实验配置/4NAT配置/NAT配置/image-2024716500698.png)

## 动态案例
```
[Huawei]nat address-group 1 122.1.2.1 122.1.2.3
[Huawei]acl 2000
[Huawei-acl-basic-2000]rule 10 permit source 192.168.1.0 0.0.0.255
[Huawei-acl-basic-2000]qu
[Huawei]interface g0/0/1	
[Huawei-GigabitEthernet0/0/1]nat outbound 2000 address-group 1 no-pat
```
## 动态nat不是固定的
所以也就是ping的时候中断,也就是不适用pat，地址不够用的情况下会这样。
资源耗尽【也就是那个ip正在被占用着，你又给分过去了，那是不通的】
![image-2024716343234.png|323](7_8ENSP实验配置/4NAT配置/NAT配置/image-2024716343234.png)
被访问主机抓包
![image-20247164851664.png|425](7_8ENSP实验配置/4NAT配置/NAT配置/image-20247164851664.png)
私网主机抓包
![image-20247165915558.png](7_8ENSP实验配置/4NAT配置/NAT配置/image-20247165915558.png)
# 动态NAPT端口转换功能
动态NAT选择地址池中的地址进行地址转换时,不会转换端口号，即No-PAT （No-Port Address Translation， 非端口地址转换），公有地址与私有地址还是1：1的映射关系，无法提高公有地址利用率。也叫PNAT
NAPT （Network Address and Port Translation， 网络地址端口转换） 从地址池中选择地址进行地址转换时不仅转换IP，还有端口,可以有效提高公有地址利用率.
参考动态路由的最后一条命令
```
一致[Huawei]nat address-group 1 122.1.2.1 122.1.2.3
一致[Huawei]acl 2000
一致[Huawei-acl-basic-2000]rule 10 permit source 192.168.1.0 0.0.0.255
一致[Huawei-acl-basic-2000]qu
一致[Huawei]interface g0/0/1	
去除掉no-pat就会为pat了
[Huawei-GigabitEthernet0/0/1]nat outbound 2000 address-group 1 no-pat
[Huawei-GigabitEthernet0/0/1]undo nat outbound 2000 address-group 1 no-pat
								↓ ↓ 
[Huawei-GigabitEthernet0/0/1]nat outbound 2000 address-group 1 
```
## 检查命令display nat outbound
![image-20247162033376.png](7_8ENSP实验配置/4NAT配置/NAT配置/image-20247162033376.png)
## 满足大量主机访问外网
可以看到现在开启pat后，不会终止了
![image-20247162347983.png|300](7_8ENSP实验配置/4NAT配置/NAT配置/image-20247162347983.png)

## EASYIP 【最节省ip地址】【特殊的NAPT】
![image-20247163454281.png|425](7_8ENSP实验配置/4NAT配置/NAT配置/image-20247163454281.png)
`没有NAPT合适企业`这个是把接口跟公网ip进行到一块的。
没有地址池，也就是说不是内外→公网
而是接口ip变的。
Easy IP适用于不具备固定公网IP地址的场景：如通过DHCP、PPPoE拨号获取地址的私有网络出口，可以直接使用获取到的
动态地址进行转换。
```配置好路由
[Huawei]nat address-group 1 122.1.2.1 122.1.2.3   #easyip不需要地址池
[Huawei]acl 2000
[Huawei-acl-basic-2000]rule 10 permit source 192.168.1.0 0.0.0.255
[Huawei-acl-basic-2000]qu
[Huawei]interface g0/0/1	
[Huawei-GigabitEthernet0/0/1]nat outbound 2000 address-group 1 no-pat # 不需要租 也不需要加后面的pat参数
[Huawei-GigabitEthernet0/0/1]nat outbound 2000  直接给接口匹配上策略
```
![image-20247163050477.png|500](7_8ENSP实验配置/4NAT配置/NAT配置/image-20247163050477.png)
![image-2024716314320.png|353](7_8ENSP实验配置/4NAT配置/NAT配置/image-2024716314320.png)
外部主机的抓包
![image-2024716358930.png](7_8ENSP实验配置/4NAT配置/NAT配置/image-2024716358930.png)
# 静态NAPT端口转换功能
NAT Server：指定[公有地址：端口]与[私有地址：端口的一对一映射关系，将内网服务器映射到公网，当私有网络中的服务器需要对公网提供服务时使用]
外网主机主动访问[公有地址：端口]实现对内网服务器的访问。

端口映射那味，192.168.3.100:25565→81.70.185.233:25565/25566
![image-20247163832190.png|400](7_8ENSP实验配置/4NAT配置/NAT配置/image-20247163832190.png)
配置NAT服务器192.168.1.100 80 → 122.1.2.1 80
```
nat server protocol tcp global 122.1.2.1 80 inside 192.168.1.100 8080
nat serve
nat server protocol tcp global 122.1.2.1 80 inside 192.168.1.100 80
nat server protocol tcp global 122.1.2.1 www inside 192.168.1.100 www    #display this 看到的是这样的，被翻译了 
```
使用客户端检测一下，成功ok
![image-20247165054190.png|325](7_8ENSP实验配置/4NAT配置/NAT配置/image-20247165054190.png)
# 区分进入和出去，想让节省ip，对出口端口做，想要外网进来，，也是出口端口。但是不要删除原来配置的。
