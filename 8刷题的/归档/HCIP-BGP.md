
BGP和RIP是工作在应用层的协议 ==（也就是bgp是7层，如果说是会话层5层就是错的）==
TCP 179端口 
BGP不是周期更新的，是触发更新
# 属性
公认属性是所有路由器都要是别的，而可选并不一定是所有路由器都要识别
## 公认属性
### 公认必遵属性
这些属性必须存在于每一个UPDATE消息中，并且必须被处理。
==origin==：路由来源类型（origin的属性的数值为IGP、EGP 或 Incomplete,需要注意这里的IGP,EGP可不是跟EBGP和IBGP有关系的）
【IGP，表示路由产生于本AS内部，比如用network命令宣告进BGP】【EGP，通过EGP这个协议学习到的路由】【Incomplete，表示路由的来源无法确定，比如通过import命令引入到BGP的路由】
==as_path==：经过的自治系统（AS）列表
==next_hop==：下一跳的 IP 地址
### 公认可选(任意)属性
这些属性也是所有路由器必须识别的，但并不强制要求出现在每个UPDATE消息中。
==local_preference==：本地优先级【无论`Local Preference`值有多高，都会优先选择`Preferred-Value`【华为设备特有的属】值更大的路由A。】【默认优先级为100】
==atomic_aggregate==：标记聚合路由
## 可选属性
可选属性是指那些并非所有实现BGP的路由器都需要识别的属性。
### 可选可传递(过渡)属性
==aggregator==：将多个路由合并为一个更大的前缀。要跟标记区分开
==community==：路由分类
### 可选非传递属性
multi_exit_disc==（MED）==：多出口判别,在某些情况可以传递
==originator_id==:发起方ID
==cluster list== 【用来防止环路的，需要注意可选非传递和非可选过渡属性一个意思 在路由反射那里】 

以下关于BGP中Cluster List，属性的描述，错误的是哪一项？
当RR收到一条携带Cluster_ List属性的BGP路由，且该属性值中包含该簇的Cluster _ID时， RR认为该条路由存在环路，将忽略关于该条路由的更新
==该属性属于可选过渡类型==【可选非过度】
Cluster List由路由反射器产生， 它由一系列的Cluster ID组成
当一条路由被反射器反射后，该RR的Cluster _ID就会被添加至路由的Cluster_ List属性
# BGP操作和配置
## BGP邻居关系
VRP版本缺省情况下，当BGP的邻居入口路由策略(route-policy)改变后，会自动向该邻居发送【refresh】以请求邻居重新发送【Update】消息【注意这里如果说是notification就是错的】
- **BGP邻居刷新**：自动发送refresh请求邻居重新发送Update消息。
## open报文
Open报文用于建立连接，keepalive报文用于维持连接【所以这个就跟ospf那些不一样了】
BGP在opensent状态下等待open的报文
BGP的Open报文是用于建立对等体连接的，TCP的端口号不属于open报文中携带的参数信息
# keepalive报文/hold时间
BGP的hello报文是用来建立连接【bgp应该是没有hello报文 keepalive报文用来维护连接
BGP的hello仅仅是发现邻居关系【bgp应该是没有hello报文】，keepalive用于维护邻居关系，但是组播和ospf这些的hello是发现和维护邻居关系
BGP的邻居关系要Keepalive报文维持，BGP与IGP的互相引入不会导致BGP不发送Keepalive报文，因此BGP邻居关系不会断开
BGPKeepalive 报文发送时间间隔为60s
BGP的keepalive报文周期是60s 保持周期hold是180s，【但是说时间间隔180s是错的,因为这个时间间隔是keepalive才对】
BGP的Hold时间取值是最小的那个，但是hold的时间是keeplive的3倍率  所以hold时间一个是30s，一个是90s ，keepalive时间就是 10秒 30秒但是要选择最小的，就是10秒 【存疑】

## BGP路由更新+报文
BGP无需周期性通告路由信息，那样的话负载太高了
【错误】BGP路由器可以发送增量的BGP路由更新或者进行周期性更新（BGP只发增量 没有周期性更新）
Update消息是单播发送
【错误】"BGP基于TCP，所有报文都是单播的，所以说update是组播，就是错的"
AS-PATH必须存在于BGP的update中
notification报文用于报告错误信息【一定是错误信息】

# BGP聚合
聚合路由可以防止路由条目过多
对于==IPV6,BGP只能手动聚合==
BGP的选路规则中，手动聚合的优先级高于自动聚合 【手动聚合>自动聚合>network>import>对等体学到的】
BGP的选路规则中，通过aggregate命令生成的手动聚合路由的优先级高于summary automatic命令生成的自动聚合路由。
Aggregate命令的detail_suppressed参数用于抑制明细路由
路由聚合可以阻止低级RR在BGP上溢出
在==BGP中使用路由聚合会导致ASPath属性丢失，可能会产生环路的风险==（聚合后的AS_PATH会被删除，由本地AS代替，所以可能环路）

# 选路
BGP Speaker默认只会把BGP路由表中的最佳路由通告给邻居。
最优路径的选择基于多种因素，如AS path长度 ，local pref数值等
BGP带preference的越大越优先(有两个)，其它的都是越小越优先，AS path和MED，AS Path更加优先，先考虑as path而不是MED
【错误】在BGP选路规则中， Local Pref值高的路由优先。 【当Preferred-Value值相同时，才优选Local_pref值高的路由】
【错误】BGP选路规则中，Local Pref值高的路由优先（仅当Preferred-Value相同时成立）


# BGP和IGP的交互
IBGP不一定需要物理上直连
【错误】IBGP不一定需要物理上直连，如果是，那就是错的
【错误】从IBGP对等体获得的路由，只能发送给IBGP对等体，这句话是错误的
BGP和IGP互相引入不会影响keepalive报文的发送
【错误】BGP和IGP互相引入可能导致BGP邻居关系断开，这个是错误的
---跟下面的区分开来【上面是BGP和IGP引入，下面是同一设备不同BGP进程互相引入】----
【错误】同一设备 不同的BGP进程之间可以相互路由引入。==【同一设备BGP不可以互相引入】==
# 路由反射
全连接的BGP网络中不仅对等体的配置变得复杂，而且网络资源和设备CPU资源的消耗都将增大。可以采用以下哪一项技术来简化IBGP网络连接？
路由衰减
==路由反射器==【简化IBGP连接】
路由聚合【区分！这个是防止RR在BGP上溢出】
GTSM

【正确】路由反射器可以减少IBGP的网络连接
【正确】在BGP中，路由反射器RR会将学习的路由反射出去，从而使得IBGP路由在AS内传播无需建立IBGP全互联
【正确】在BGP中，当一条路由被反射器反射后，该RR的Cluster_ID就会被添加至路由的Cluster List属性中，用于判断是否存在环路。
# 简单的
==默认情况下，BGP路由不会开启自动聚合功能== 配置summary automatic命令后，BGP会对import路由进行自动汇总。
BGP不是链路状态信息，而是路径矢量协议
如果路由器system视图下和BGP视图下都配置了router-id，则使用BGP视图下的router id
一台路由器只能配置一个AS号，所以只能配置一个BGP进程
缺省情况下，BGP使用报文出接口作为TCP连接的本地接口
==BGP Speaker只将发生变化的路由通告给邻居==【**BGP Speaker** 是一个术语，用来指代运行BGP协议的路由器或设备。】
【错误】在BGP中公认属性是所有BGP路由器都必须识别并且包含在Update消息里的属性（应区分公认必遵循和可选属性）
IGP>EGP>Incomplet
BGP和EBGP的邻居关系，默认TTL为1
EBGP的默认TTL是1跳 如果说是2，那就是错的
no-export参数表明该路由条目不能被通告到本地AS之外
NO_Advertise 不通告给任何BGP对等体
AS-PATH这种公认必遵属性必须存在于BGP的update中
【错误】MED是不必须存在于BGP的update报文中的，如果有，那就是错的。
MED是可选非过渡属性。不是必须遵守的
【错误】BGP的cluster list是非可选过渡属性，如果说是可选过渡属性，那是错的
没开负载分担，只有被BGP优选的路由会发送BGP邻居关系
BGP发现下一跳路由不可达时，会加入到BGP路由表，但是不会被优选，也不会加入IP路由表
BGP里面 发现自己的AS号在AS Path里会直接丢弃，避免环路
BGP的display如果有>大于号，就代表这条路有是最优路由
Import-route引入BGP的时候，像是rip必须指定进程号!
BGP4+的next hop network address字段可以同时携带链路本地地址，和全球单播地址
在BGP配置中使用认证，应该如何配置？==一对BGP对等体之间必须使用相同的MD5 passworD==

UPDATE消息所包含的内容，描述错误的是
==UPDATE包含本端AS自制系统号==【update不包含本端AS自制系统号】【AS path是必须存在的】
UPDATE包含路径属性
UPDATE包含撤销路由前缀信息
UPDATE包含可达路由前缀信息

# 不简单的
通过重发布命令注入BGP的路由，其Origin属性为【Incomplete】
两台路由器通过多跳物理链路建立一对逻辑BGP对等体时，==必须使用【peer connect-interface】命令==【非直连接口必须使用】
【错误】 BGP在建立邻居的过程中，如果在Active状态下TCP连接失败，则BGP会回到Idle状态重新尝试TCP连接（应为进入Active状态，反复尝试连接）
"BGP的自动汇总，结果只能是路由条目所属于的主类路由，10.1.1.1/24 和10.2.1.1/24 路由聚合为1条条目应该是16，BGP只能是主类路由"
MP-BGP用于实现BGP-4的的扩展以允许BGP带多种网络层协议。这种扩展有很好的后向兼容性，即一个支持MP-BGP的路由器可以和一个仅支持BGP-4的路由器交互
【错误】"支持MP-BGP协议的路由器，通常都是支持普通的IPv4 BGP协议的路由器，说MP-BGP不能和仅支持BGP-4的路由器交互 【能交互的】
"BGP中的==aggreate命令的detail_suppressed==参数的意思==仅通告聚合路由给其他BGP邻居==
Display bgp netwrok 看的是network通告的路由，也就是本地的，不能看外部import-route的 display bgp routing-table
【错误】在BGP中公认属性是所有BGP路由器都必须识别并且包含在Update消息里的属性 【公认属性分为 必需的公认属性 和可选的公认属性 update只需要公认必遵循就可以了】
在BGP使用Filter-Policy时，可以通过filter-policy export命令将对外发布的路由进行过滤，只有通过过滤的路由才能加入到BGP本地路由表中，并被BGP发布。
【正确】MBGP的主要作用是帮助跨域组播流进行RPF校验。
BGP建立对等体连接时，本端和对端都会发起TCP三次握手，所以会建立两个TCP连接，但是实际BGP只会保留其中一个TCP连接，从Open报文中，获取对端BGPIdentifier 之后BGP对等体会比较本端的Router ID和对端的Router ID大小，如果本端Router ID小于对端Router ID.则会关闭，本地建立的TCP连接，使用由对端主动发起创建的TCP连接进行后续的BGP报文交互。

VRP缺省情况下，当BGP的邻居出口路由策略(route-policy)改变后，需要手工操作才会向该邻居重新发送Update消息。【正确 update就是路由信息变了就发送的】

【正确】前缀列表可以在部署BGP中直接通过peer命令使用，无需通过Filter-Policy或Route-Policy。

【错误】在BGP中通过Network方式注入的路由不一定必须是存在于IP路由表中的路由条目，同时这种方式注入路由比较精确 【network的时候路由必须是存在IP路由表中的条目】

# 填空
MED主要用于在AS之间影响BGP的选路，MED属性值越小则BGP路由越优。缺省情况下，华为设备BGP的MED值是【0】。
【AS】指的是在同一个组织管理下，使用统一选路策略的设备集合。（请填写英文缩写，全大写）
在BGP中【origin】、AS Path和Next Hop属于公认必遵属性。（请填写英文，并首字母大写）
使能了0SPF的路由器在lnit 状态下，发送hello包的目的地址是【224.0.0.5】（请填写点分十进制IP地址）



在BGP中建立EBGP邻居关系时，报文的默认TTL值是多少？
==1==【EBGP邻居默认是1跳，所以不是直连的话要配置允许多条】
5
2
10


以下关于BGP通告原则的描述，错误的是哪一项？
==从IBGP对等体获取的路由。只能发送给IBGP对等体==【怎么可能】
当一台路由器从自己的BGP对等体学习到一条BGP路由时，它将不能使用该条路由或把这条路由通告给自己的EBGP对等
体，除非它又从IGP协议学习到这条路由
只发布最优路由从EBGP对等体获取的路由，会发布给所有的对等体

BGP的Open报文是用于建立对等体连接的，以下哪一项不属于Open报文中携带的参数信息？
发送者的Router ID
AS号
BGP版本号
==TCP端口号==【不需要】


BGP邻居关系无法建立，可能的原因不包括以下哪一项？
Open报文在协商的过程中产生错误，导致邻居关系无法建立
==在建立非直连EBGP邻居关系时，由于默认EBGP更新报文的TTL是2.并没有手工进行更改，导致邻居无法建立==【]默认是1】
禁用了TCP端口179，从而导致邻居无法建立
BGP邻居不可达，导致邻居无法建立

当TCP连接正常，BGP邻居配置的AS号和邻居路由器配置的BGP版本不一致时，该邻居通常会在建立TCP连接并交互一定信息后发Notitication报文进行断连，那么该Notification报文中的Error Code会标识出哪 一项消息是在协商时出现错误的？
==Open==【当底层TCP连接建⽴，后续发送BGP的Open报⽂，然后协商建⽴BGP邻居的参数。】
Route-refresh
Update
Keepalive


在BGP中，MED作为一种度量值，用于向外部对等体指出进入本As的首选路径。缺省情况下，路由器会比较来自不同AS的BGP路由的MED值，MED属性值越小的BGP路由越优。【错误  缺省不会携带MED属性】

# 衍生多选
BGP peer 一定需要ip地址和as号才行
