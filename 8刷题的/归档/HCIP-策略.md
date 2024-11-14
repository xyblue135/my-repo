#  路由策略与过滤工具

## Route-policy
route-policy不仅能对路由过滤，还能修改路由属性，如cost，tag等
**Route-policy** 用于过滤路由信息，并且可以间接影响数据包的转发行为。
**Route-policy** 可用于多种路由协议，并且==由 `if-match` 和 `apply`== 子句组成。
**Route-policy** ==不能直接引用 `IP-prefix`==。【IP-prefix不能被route-policy的apply子句直接引用】
	一个Route-Policy下可以有多个节点,设备在调用Route-policy时按顺序开始匹配 
在使用Route-Policy的==if-match创建匹配规则时，不能匹配origin属性==【用来定义路径信息的来源，标记一条路由是怎么成为BGP路由的，不能用在if-match匹配中。】

一个Route-Policy下可以有多个节点，设备在调用Route-Policy时按顺序开始匹配。【正确 ==一个Route-Policy可以由多个节点（node）构成==。路由匹配Route-Policy时遵循以下两个规则：顺序匹配  系统按节点号从小到大的顺序依次检查各个表项  唯一匹配 ==route-policy节点号之间是“或”的关系==】

一个route-policy下可以有多个节点，不同的节点用node标识每个节点下可以有多个if-match和apple-子句，下面哪些描述时错误的？  （20分）【每个节点是与的关系，不同节点是或的关系】
==每个节点下的if-match子句之间是 “或”的关系==
每个节点下的if-match子句之间是"与"的关系
==不同节点之间是“与” 的关系==
不同节点之间是“或"的关系

[HUAW El]ip ip-prefix 1 permit 11.1.0.0 16
[HUA wEi] route-policy Set- cost permit node 10
[H UAwEl-route-policy]if-match ip-prefix 1
[HUAwEl-route-policy ]apply cost 300
[HUAWEl-route-policy ] quit
[HUA wEl] route-policy Set- cost permit node 20
[HUA wEl-route-policy ]apply cost 200
[H UAwEl-route-policy] quit
正确的是
路由11.1.0.0/16在通过node10后将继续匹配node20，最终cost被设置为200
==所有路由的cost都会被设置为200==
路由11.1.0.0/16能够通过node10,其cost被设置为300
有不通过node10的路由都会被拒绝
解析:路由11.1.0.0/16在通过node10后cost被设置为300并跳出，不会匹配node20；除了11.1.0.0/16路由以外的其他路由，cost被设置为200；

node10的路由讲继续匹配Node20，不会被拒绝。

## Filter-policy
Filter-polic只能用于过滤路由，不能对理由属性进行修改
在BGP中有两种部署Filter-Policy工具的方法，一种是在BGP下全局部署，另一种是在指向对等体 （组）时部署。
在链路状态路由协议中，如 OSPF 和 IS-IS，使用 `filter-policy` 在入方向过滤路由不会阻断链路状态信息的传递，因此路由表仍会生成，只是不转发。
【错误】Filter-Policy在OSPF中使用时，可以通过过滤LSA以实现路由控制 【错误 不能通过过滤LSA来实现路由控制】
【错误】对于链路状态路由协议，使用filter-policy import时，被过滤的链路状态信息，将不能被计算成路由，并且它的邻居也不能收到完整的链路状态信息【还是不能对属性进行修改】

## ip extcommunity-filter

# 基于数据包的
## Traffic Policy流策略 
流策略支持在接口上调用，并且可以应用于入和出方向
流策略的命令是 traffic-policy 【name】inbound/outbound【应用流策略的命令traffic-policy p1 inbound】
## ACL
基于接口1000-1999
基本acl 2000-2999
高级acl 3000-3999
二层acl 4000-4999
acl不能进行路由过滤，==acl是过滤数据包的【也就是说ACL不能用于路由过滤】==

- **拒绝包含65001的路由**：`deny 65001 ip`。
## PBR (Policy-Based Routing)
**PBR** 不能用于路由过滤，因为它是基于数据包的。
**PBR** 支持在接口上调用，但不仅限于三层接口，也可以在二层接口上调用。
==**PBR** 的每个节点在没有配置 `apply` 语句时，不执行任何操作。==
**PBR** 不可以修改 IP 报文的 IP Precedence【优先级】。

策略路由（policy-based -route）不支持根据下列哪 种策略来指定数据包转发的路径？
源地址
目的地址
==源MAC==
报文长度【[[防火墙安全策略不匹配报文长度]]】

以下关于PBR不同分类的描述，正确的是哪一项？
接口PBR调用在接口下，对接口的出方向报文生效【接口下的pbr对出方向已经无效了】
PBR可以分为接口PBR、本地PBR以及路由PBR
==接口PBR可L以修改IP报文的IP-Precedence==
本地PBR对始发的报文无效，只对转发的报文起作用【本地PBR可以堆开始的报文有效】
# 其他策略
## 前缀列表
前缀列表不能用于数据包的过滤！
`reset ip ip-prefix` 命令用于清除 IPv4 地址前缀列表的统计数据。
前缀列表mask-length<=greater-equal-value<=less-equal-value<=32
前缀列表可以在部署BGP中直接通过peer命令使用，无需通过Filter-Policy或Route-Policy。
## MQC(Modular QoS CLI)
**MQC** 是模块化 QoS 的命令行，是配置 QoS 处理数据的一种方式。
==MQC==流命令 ==不能 使用if-match匹配前缀列表==
【错误】MQC与PBR一样，只能在设备的三层接口下调用 错误 MQC可以在二层【MQC可以在二层接口使用】
MQC流分类中各规则之间的关系分为：and或or缺省情况下的关系为==【or】==

MQC中流分类命令不能使用if-match匹配以下哪一参数？
源MAC地址
==前缀列表==
Inbound-interface
DSCP值






## import引入路由
使用简单的import-route就可以引入部分满足条件的路由信息，并且对所引入的路由信息的某些属性进行设置，不一定需要router-policy
### import-ospf
import-route limit 可以限制一个ospf进程内可引入的最大外部路由数量【如果说不可以限制就是错的】
==管理员可使用import-route命令将不同进程号下的oSPF互相引入【正确】==
### import-bgp
通过import-route命令把路由引入BGP，下面哪种描述是正确的？
import-route命令只将IGP路由、静态路由引入BGP【Import-route还可以引入直连路由；】
情况下，引入路由的Origin值为IGP【缺省情况下，引入路由的Origin值为incomplete】
==当引入路由协议为ISIS时，必须指定进程号==
不能使用路由策略过滤从其他路由协议引入的路由【import-route可以与route-policy配合过滤其他路由协议引入BGP的路由；】

以下关于路由引入的描述，错误的是哪一项？
把路由引I入到ISIS中默认等级为Leve-2
把某类型的路由引I入到BGP时可以直接指定其MED值，不需要使用Route-Policy
把路由引I入到OSPF中默认为Metric-Type-2
==同一设备中不同的BGP进程之间可以相互路由引入==【不可以】
### 相互引入
当讲ISIS路由引入OSPF中，如果不指定开销，默认就是1【不是20！】



# 其他
如果部署严格的 URPF（Unicast Reverse Path Forwarding），也可以同时部署匹配缺省路由模式。
AS-Path 过滤器（如 `ip as-path-filter`）可以拒绝包含特定 AS 号的路由。
`traffic-filter` 是将 ACL 绑定至接口下，以实现流量过滤功能。【扩展非题目】
策略路由policy-bashed-route不支持源mac来指定数据包转发路径
Policy-based-route不能用于路由过滤，因为有based是，是本地的 【策略路由，可以根据管理员定义的策略条件来选择性的转发数据包】
传统的丢包策略采用尾部丢弃（tail-drp）的方法，这种丢弃方法会导致TCP全局同步现象
cost 描述外部路由   不同路由协议互相引入时，会使用不同协议来描述，如果说必须需要手动指定，那是错误的
"ip as-path-filter 1 deny_65001 _ip as-path-filter 1 permit.* 拒绝包含65001的路由经过   是65001前面的下划线符号_  "
实现流量过滤功能，可以使用traffic-filter,也可以使用MQC，相比于traffic-filter,MQC可以在更多的视图内调用

[ Huawei] display ip as-path-filter
As path filter number: 1
permit ^12345_（0-9)*$
==该配置匹配的是从任意AS始发穿过AS12345到达该路由器==
该配置匹配的是从任意AS始发到达该路由器，该路由器属于AS 12345
该配置匹配的是从AS 12345始发穿过任意AS到达该路由器
该配置匹配的是从任意AS始发穿过AS 12345，再到达另一任意AS，最后到达该路由器


关于路由策略的特点描述，正确的是
应用命令policy-based-route【这个都带based了，是针对数据包的，是策略路由】
==基于目的地址按路由表转发==
需要手工逐跳配置，以保证报文按策略转发【可以不手工】
基于转发平面为转发策略服务【管理层面】

MQC与PBR一样，只能在设备的三层接口下调用。【错误 mqc还可以二层】



