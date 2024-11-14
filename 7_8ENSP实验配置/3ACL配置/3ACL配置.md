# 查看所有acl策略display acl all
display acl all
![image-20247134413593.png](7_8ENSP实验配置/3ACL配置/3ACL配置/image-20247134413593.png)
# 末尾都需要添加的
```选择其一
rule permit source any
rule deny source any
```
# 删除
```
undo rule 序号
```
# acl应用接口
```
int g0/0/0
traffic-filter inbound acl 2000
或者
traffic-filter outbound acl 2000

```
# 基于接口的acl【编号范围1000-1999】
# 基础acl display acl 2000  【编号在2000-2999】
允许192.168.1.1源地址访问，需要注意，基础的只能一个源地址或者一个目的地址
```
acl number 2000
rule 1 deny source 192.168.1.1 0
```
允许从 10.0.0.0/24 网络中的**所有主机**访问目标地址为 192.168.1.100 的主机：
```
acl number 2000
rule 5 permit source 10.0.0.0 0.0.0.255 destination 192.168.1.100 0
```
禁止从 172.16.1.0/24 网络中的**所有主机**访问目标地址为 10.1.1.1 的主机：
```
acl number 2000
rule 1 deny source 172.16.1.0 0.0.0.255 destination 10.1.1.1 0
```
△所有主机，反掩码，通配符，网段。
△不用通配符直接是0或者255.255.255.255就是本身，一般用0


# 高级acl display acl 3000 【编号在3000-4000】
允许 TCP 协议从任意源地址访问目标端口为 80 的服务器
```
acl number 3000
rule 1 permit tcp source any destination any destination-port eq 80
```
禁止icmp流量
```
acl number 3001
rule 1 deny icmp
```
# Layer 2 ACL display acl 4000二层acl【编号在 4000-4999】
允许特定 VLAN 的流量 允许vlan10的主机互相通信
```
acl number 4000 
rule 1 permit vlan 10
```
禁止 MAC 地址为 0011-2233-4455 的主机发送数据：
```
acl number 4000
rule 1 deny source-mac 0011-2233-4455 any
```
# 用户自定义ACL的编号范围是5000~5999，
# 用户ACL的编号范围是6000~6031。
# 附：复杂的示例 {一旦匹配到一条规则，后面的规则将不会再进行匹配}
在复杂ACL的示例中，编号可以高达5000，这种情况下可能是在示例中演示了多条ACL规则的组合使用，每条规则都有自己的序号和配置条件，用以控制复杂的网络流量策略。
允许从 192.168.1.0/24 到 10.0.0.0/24 的 ICMP 流量，并限制源端口范围为 1024-65535
```
acl number 5000
规则5：允许从 `192.168.1.0/24` 到 `10.0.0.0/24` 的所有 ICMP 流量。
rule 5 permit icmp source 192.168.1.0 0.0.0.255 destination 10.0.0.0 0.0.0.255 icmp-type any icmp-code any
规则10：允许从 `192.168.1.0/24` 到 `10.0.0.0/24` 的 TCP 流量，并限制源端口范围为 `1024-65535`。
rule 10 permit tcp source 192.168.1.0 0.0.0.255 destination 10.0.0.0 0.0.0.255 source-port range 1024 65535
```

# 案例一：基于时间过滤
```每天9-18点192.168.1.1不能经过路由器
time-range xyblue 9:00 to 18:00 working-day daily[很多可选]
acl 2000
rule 10 deny source 192.168.1.1 0 time-range xyblue
rule 10 permit source any
quit
int g0/0/0
traffic-filter inbound acl 2000
```
# 案例二：访问财务部
案例需求:
禁止销售部10.5.20.0/24和10.5.30.0/24在9:18点访问财务部。
禁止人力10.5.30.0/24远程登录财务部
经理可以随时登录
![image-2024813423979.png|275](7_8ENSP%E5%AE%9E%E9%AA%8C%E9%85%8D%E7%BD%AE/3ACL%E9%85%8D%E7%BD%AE/3ACL%E9%85%8D%E7%BD%AE/image-2024813423979.png)
```
time-range xyblue 9:00 to 18:00 working-day daily
acl 3000
rule permit ip source 10.5.8.8 destination any  #经理办公室
rule deny ip source 10.5.20.0 0.0.0.255 destination 10.5.100.5 0 time-range xyblue #销售部9-18不能访问
rule deny tcp source 10.5.30.0 0.0.0.255  destination 10.5.100.5 0 destination-port eq 23 #进制人力远程登录
rule deny source any #不匹配的全部不允许
quit
int g2/0/3
traffic-filter outbound acl 3000 #相对于路由器是出口流量
```
# 重点领域 反掩码
一般来说掩码是持续的也就是不能0后面是1再是0，但是反掩码是可以的。
# 案例三：匹配奇偶数和特定
案例：匹配192.168.1.0~192.168.1.255的所有奇数地址，且只能一条acl

我们看bit，先展开网段的
192.168.1.1     00000001
192.168.1.3     00000011
192.168.1.5     00000101
到
192.168.1.255  11111111
可以看到最后一位bit是不变的，那么正常俩说需要匹配的掩码就成了255.255.255.1（这边逻辑要搞清楚，需要匹配的即是不变的那些bit），反掩码就是0.0.0.254了

案例：匹配
10.1.1.0/24
10.1.3.0/24
10.1.5.0/24
10.1.7.0/24
10.1.17.0/24
10.1.19.0/24
10.1.21.0/24
10.1.23.0/24
可以看到从7-17那里就少了几个了，要是这样匹配的话，我们也是先展开，一个套路
00000001
00000011
00000101
00000111
00010001
00010011
00010101
00010111
可以看到第1235bit位置是不变的，那么需要匹配的掩码就是255.255.232.0 反掩码就是0.0.22.0来匹配（其实直接看变的，然后反掩码就可以了）