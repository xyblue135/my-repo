==89==端口 ==四层== ospf是一个网络层协议，基于IP数据报文  
关于区分不同lsa的link id到底是router id 还是目的网段，是靠这三种类型来区分的
- ==**点到点（Point-to-Point）链路**：`Link ID`是邻居路由器的Router ID。==
- ==**虚链路（Virtual Link）**：`Link ID`是目标路由器的Router ID。==
- **广播型网络（Broadcast）和NBMA网络**：`Link ID`是该网络的网络掩码对应的网络地址（即网段地址）。
只有多路访问网络才选举DR/BDR，或者可以说是多地址网络才选举DR/BDR，像是p2p,P2MP,虚链路就不选举

# DR BDR DROTHER
DR是可以抢占，但是默认没有开启  DR如果是广播是必须要有的
BDR是不可以被抢占的  BDR可有可没有
DR和BDR都监听224.0.0.5 224.0.0.6 DR/BDR的优先级默认为1 取值范围为0-255  DR/BDR的优先级不能为0，否则会成为DRother    DRother监听的是224.0.0.5

开始状态所有路由器都认为自己是DR
如果链路这些优先级都是0了，那么DR，BDR是0.0.0.0【反推】 DR和BDR是空的数值的时候，一定可以判断出来网络类型不是广播网络broadcast
【补充】DR/BDR是接口上的 也就是说路由器的router id 和接口的router id 没有任何关系



# 组播地址
224.0.0.5 所有ospf路由器
224.0.0.6 DR和BDR

### 开销
【错误】==VRP平台上==，当我们把==IS-IS路由引入到OSPF协议==中时，如果不指定==COST,那么开销值将默认设1==【如果说20是错的】【也就是说在ospf网络中，isis的开销是1】

# LSA更新机制
ospf 使用触发更新和定期更新
ospf的lsa每间隔30分钟进行定期更新
ospf的lsa最大有效时间为60分钟（3600秒） 【ISIS那边的跟新时间是1200秒】
# 邻居关系和邻接关系
并非所有的邻居关系都可以成为邻接关系
标识一条lsa的事ls type和 link state id 和 advertise router 这三个字段
# OSPF LSA类型
## 穿越区域会发生变化的lsa

下面关于LSA3、LSA4和LSA5，描述正确的是
==LSA5在穿越不同区域后，不会发生改变，而LSA3会发生变化==【LSA3和LSA4穿越区域会发生变化，仔细想一下一个从DR外部向里面走，一个ASBR外部向里面走，而像LSA5这种，它其实还是在ASBR外部的】
LSA3、 LSA4和LSA5在穿越不同区域后都不会发生改变
LSA3在穿越不同区域后，不会发生改变，而LSA4和LSA5会发生变化
LSA4在穿越不同区域后，不会发生改变，而SA3和LSA5会发生变化
## type1lsa
【错误】OSPF的Router LSA中，如果其Link Type为1，则该LSA描述的是从本路由器到邻居路由器之间点到点的链路，此时对应的LinkID描述的内容则为邻居路由器的接口IP地址 点到点的网络可不是邻居路由器接口ip，而是邻居的邻居的R-ID【因为是p2p网络了，不是广播的】
## type2 lsa
缺省情况下，ospf的外部路由属于type2 lsa 【此点需要注意，通常外部路由是Type 5 LSA，但是这个的意思是引入的外部路由的属性应该为，那就是5类变成2类了，其实也确实是，毕竟要在本区域消化】
## type3 lsa
ABR可以产生Type 3 LSA。
描述的目的网络地址 【而不是ABR的Router ID】
## type 4 lsa
==ABR可以产生type 4 lsa==，也就是描述怎么到达外部的路线的lsa 也就是到达asbr的路线
【错误】所有区域的ASBR-summary-LSA中的Advertising Router字段都相同 
【错误】关于OSPF的ASBR Summary-LSA  也就是type 4 lsa 的信息描述的是所有区域的ASBR-Summary-LSA中的Advertising Router3字段都相同
## type 5 lsa
==type5携带外部路由信息==
## type 7 lsa
==【错误】【7类lsa不能再area0传播】7类LSA不允许在骨干区域传输，但可以使用suppress-forwarding-address命令允许7类LSA在Area0内传输==,错误 就是不允许传输

# ospf路由聚合
【正确】OSPF路由协议中，asbr-summary命令可以跟not-advertise参数，该参数的意义是不通告聚合路由。
【错误】asbr-summary命令可以汇总被asbr-summary聚合后的所有lsa   错误  3类和5类不能被汇总


# OSPF邻居关系建立
## 状态
1. **Down**：没有收到邻居的Hello报文。
2. **Attempt**：仅用于NBMA网络，表示路由器正在尝试与邻居建立联系。
3. **Init**：收到了邻居的Hello报文，但还没有看到自己的Router ID出现在邻居的Hello报文中。
4. **2-Way**：看到了自己的Router ID出现在邻居的Hello报文中，双向通信已经建立。
5. **ExStart**：开始交换DD报文以确定主从关系和初始序列号。
6. **Exchange**：实际交换包含链路状态信息摘要的DD报文。
7. **Loading**：请求并发送具体的LSA（Link State Advertisement）。
8. **Full**：邻居关系完全建立，双方的LSDB（Link State Database）同步。
### 2-WAY
2-way状态就已经开始DR和BDR的选举
如果hello时间不一致 无法建立邻居关系会卡在2-way
在MA网络中的两台DRother路由器R1和R2建立邻居关系，那么在R1中执行[R1]diaplay ospf peer 命令,应该卡到2-way 而不是loading

不能建立邻接关系的原因是以下哪一项？
两台路由器使用相同的Router ID【不能建立邻居关系】
==直连的两个端口ospf dr-priority设置为0==【卡在2-way状态，两台路由器无法进入邻接状态】
两台路由器直连的两个接口上设置了不同的网络类型【配置相同的Hello报文发送间隔和邻居失效时间，双方仍可以正常的建立起邻接关系】
两台路由器使用了不同的Process ID
### ExStart -loading

如果ospf的mtu不匹配，会卡在exstart无法协商主从关系，无法确认DD报文序列号

当OSPF处于Exchange状态时，路由器与邻居之间相互发送包含链路状态信息摘要的DD报文。【需要注意 exstart是开始交换DD报文以确定主从关系和初始序列号 不是交换链路状态信息】
exstart和loading两个状态主要用于传输DD报文,【如果说是lsa信息，就是错的】

DD报文是简要的信息，LSU才是全部信息
# ospf验证和认证
在vrp中，ospf支持md5算法
ospf特点之一是支持md5算法，也支持简单认证
除了MD5之外，还可以使用简单的明文密码验证。
两台路由器R1和R2直连，想要建立OS PF邻接关系，R1使用的MD5的端口认证，R2使用了MD5的区域认证，口令相同的情况下两台设备可以建立OS PF邻接关系。【正确 直连设备间可以使用接口认证和区域认证建立邻居关系只要认证方式和密码相同】
# ospf路由计算
ospf使用spf算法而不是DUAL算法
ospf计算最短路径树的第一阶段计算路由节点和transit网段，第二阶段计算stub网段
# ospf区域特性
## stub区域【减少路由规模】
**Stub区域**和**Totally Stub区域**必须通过默认路由到达其他区域。
Stub区域不存在4、5类LSA【内部路由器只关心如何到达 OSPF 网络的其余部分，而不关心外部自治系统的路由】
stub可以配置缺省路由的开销 【如果说stub区域不能配置缺省路由的开销就是错的】
stub区域的所有路由器都需要配置stub属性
OSPF的STUB区域的hello报文E-bit位可以为0，但是不会处理E-bit为1的数据包，【如果可以处理，那就是错的】
区域内路由器通过一条指向ABR的缺省路由发送报文。【存疑】
OSPF Stub区域的ABR不向Stub区域内泛洪4 5 类lsa，向Stub区域通告一条默认LSA，指导数据包如何到达AS外部的目的
## totally stub区域【更加减少路由规模】
<u>题目概括:stub和totally stub必须通过默认路由到达其他区域 且可以自动产生  没有3，4，5类lsa   可以禁止明细路由type3进入ABR连接的stub区域</u>


**Stub区域**和**Totally Stub区域**必须通过默认路由到达其他区域。
【错误】【完全stub区域不需要手工在区域内放下一条默认路由】OSPF完全Stub区域的ABR不向区域泛洪第三类、第四类和第五类LSA,因此完全Stub区域的ABR需要手工向区域内下放一条默认路由，指导数据包如何到达AS外部的目的地。
Totally Stub区域不存在3、4、5类LSA【不存在3类LSA，因为这种区域只关心如何到达其他区域的默认路由，而不关心具体的网络细节。】
不需要手工向区域内下放一条默认路由【也就是说可以自动产生默认路由】
可以禁止明细路由type 3 lsa（network summary lsa）进入abr连接的stub区域


## NSSA区域【外部引入】
相比于stub区域允许自治系统外部路由的引入，由ASBR引入【如果说是ABR引入就是错的】
NSSA区域不允许出现4类lsa 5类 lsa【NSSA 区域内的路由器已经知道如何处理外部路由】

NSAA区域中ABR会将7类lsa转换为5类lsa在发给其它区域
==【错误】在OSPF中ABR会将NSSA区域中所有的7类LSA转化为5类LSA== 错误 缺省情况是NSSA区域中RID最大的ABR执行7转5的动作  【不应该是所有的lsa,只有P-bit置位且FA不为0的7类LSA才会转】
【错误】NSSA区域的ABR不会向NSSA泛洪第四类和第五类LSA，会将第七类LSA泛洪给其他区域 错误 向外部发送的时候7类变成5类了 




## Totally NSSA区域【外部引入】
Totally NSSA区域不允许出现3类 4类 5类 lsa

# OSPF的命令和配置
default-route-advertise后，ASBR将产生一个link state id 为0.0.0.0  网络掩码为 0.0.0.0 的5类lsa

在OSPF中，使用default-route-advertise命令会将该路由器变成ABR。【错误 会变成ASBR】

能使OSPF路由器生成一条默认路由的命令是以下哪一项？
default-route-initiate
default information-originate
ospf default-route
==default-route-advertise==
# 虚连接

对于OSPF中虚连接的描述错误的是
可以采用虚连接解决骨干区域逻辑上不连续的问题，【虚连接克服分割问题】
虚连接可以在任意两个区域边界路由器上建立，但是要求这两台边界路由器有端口连接到一个共同的非骨干区域
==虚连接不一定属于骨干区域的，具体属于哪个区域要根据实际拓扑进行确定。==【虚连接一定属于区域0吗，如果是其它的就是错误的】
虚连接属于区域0

==虚链路是为了克服分割区域的问题，它允许在两个非连续区域之间常见逻辑上的直接连接==
# ospfv3
ospfv3相比于ospfv2，ospfv3不依赖于特定的网络层技术ipv4，而是直接运行在链路层之上
【错误】当在华为路由器上运行OSPFv3时，OSPFv3进程会自动选择一个接口地址作为该进程的RouterID  ospfv3必须手动指定router-id
==【错误】==OSPFv3采用与OSPFv2相同的路由通告方式：在OSPFv3区域视图通过<font color="#c0504d">netWork命</font>令进行通告    ==ospfv3是在端口下宣告的，如果说network就是错的==
# router-id
ospf router id 选择 如果没有配置ospf router id ，设备将选择具有最高ip地址的loopback接口作为router id
当两个路由器之间通过DD报文交换数据库信息的时候，首先形成一个主从关系，Routerid大的一定为主 这个是对的
改routerid后，要想建立影响还需要重启路由器或者ospf进程。
【错误】在接口下 ==修改接口的OSPF网络类型==，需要对设备进行==重启或者复位ospf，否则ospf不生效   【错误 不需要重启 这个跟router-id那个不一样==.只需等待OSPF协议自然地完成邻居关系重建和LSDB同步即可】
当两个路由器之间通过DD报文交换数据库信息时，首先形成一个主从关系，==DR Priority大的成为主路由器，错误== 确定其主从位为MS  和DR优先级没关系，主从是router-id
# 负载分担
ospf支持等价负载分担，即当存在多条成本相等的路径时，流量可以在这些路径之间均匀分配
节点A和节点B之间有多条等价链路，但却没有实现等价负载分担，可能的原因是OSPF限制了最大负载分担链路的数量。【ospf最高支持16条链路负载】
# 简单

"在没有手工配置OSPFRouterID的时候，设备最先使用LoopbackO接口的IP地址作为RouterID，这句话是错的，选用的是ip最高的loopback，所以不一定是loopback0"
LSA5在穿越区域后，不会发生改变，但是LSA3，LSA4穿越区域后，会发生改变，（AID会改变成当前)
ospf的hello报文用于发现和维护邻居关系
ospf上如果网络配置(p2p，broadcast)不一样，可以建立邻接关系，但是不能路由计算
OSPF中如果接收端口的网络类型是广播型，点对多点或者NBMA，NETworkmask字段必须和接收端的掩码一致【如果不一致就是错的 因为点对点可以是任意数值0.0.0.0的】
Ospf中，area0的数据库lsdb是相同的，但是所有路由器的lsdb不是相同的，ABR同时也接着其他的非骨干区域
【错误】在MA网络中，DR、BDR选举完成之后，如果BDR出现了故障，那么DRother会重新选举出新的BDR，直到原BDR恢复正常。不被抢占
# 不简单
AS-pathfilter不能应用于ospf
两个不同的ospf区域实施多点双向重发不适合部署接口策略路由，适合本地策略路由
ospf路由分级管理，type3缺省路由优先级高于type5和type7路由
不能建立邻接关系的本质是hello时间不一致，所以网络类型不一致，如p2mp的hello和dead时间默认是30和120，p2p的hello和dead时间默认是10和40，两者如果需要建立邻居关系，将p2p的时间修改为和p2mp的时间一样的话是可以建立邻居的
==使用Silent-Interface的接口，不会接收和发送OSPF报文，但是直连路由可以通告到OSPF  正确  这个是静态接口==


避免次优路径也是metric-type1
【错误】在多个ASBR将同一条外部路由引入到同一个OSPF域内时，使用metric-type为2的外部路由类型，可以避免次优路径。 ==【应该是用metric-type1,可以避免次优，但需要注意默认是metric-2】==
开销的这个是type-1计算
【错误 Type-2不计算AS内部开销 ，Type-1才会计算开销】==OSPF第二类外部路由开销为AS内部开销（路由器到ASBR的开销）与AS外部开销之和==



【错误】在VRP系统中，命令ospf cost和band width-reference 同时配置的时候，接口上的cost值以bandwidth-reference配置为准。 应该优先接口(ospf cost)而不是全局(band width-reference)


以下关于OSPF报文认证的描述，错误的是哪一项？
==OSPF报文认证会将OSPF报文一并加密以确保其安全性保密性==【并不是一并加密，那样数量太多了】
路由器支持接口认证和区域认证两种OSPF报文认证方式，当两种认证方式都存在时，优先使用接口认证方式
OSPF接口认证方式下，相邻路由器直连接口下的认证模式和口令必须一致
OSPF使报文认证功能后，只有通过认证的OSPF报文才能被接收

Router-LSA能够描述不同 的链 路类型，不属于Router LSA链 路类型的是以下哪一项？
Link Type可以用来描述到未梢网络的连接，即StubNet
Link Type可以用来描述到中转网络的连接，即TranNet
Link Type可以用来描述到另一台路由器的点到点连接，即p2p
==Link Type可以用来描述虚连接，即VlinkE、 Link Type可以用来描述到另外路由器组的点到多点连接，即p2mp==(OSPF的link type没有P2MP的类型


下面关于OSPF缺省 路由描述错误的是
OSPF缺省路由可以由区域边界路由器 （ABR） 发布 Type3 缺省 Summary LSA，用来指导区域内路由器进行区域之间报文的转发
OSPF缺省路由可以由自治系统边界路由器 （ASBR） 发布 Type5 外部缺省 ASE LSA，或者Type7外部缺省NSSA LSA，用来指导自治系统 （AS）内路由器进行自治系统外报文的转发
当路由器无精确匹配的路由时，就可以通过缺省路由进行报文转发
==由于OSPF路由的分级管理， Type5/7 缺省路由的优先级高于Type3 路由==【Type3缺省路由的优先级高于Type5和Type7路由。】


关于OSPF的描述，错误的是哪一项？
网络类型为广播时， 所接收的Hello报文中Dead Interval字段必须和接收端配置一致
网络类型为广播时，所接收的Hello报文中Hello Interval字段必 须和接收端口的配置 一致
==网络类型为广播时，所接收的Hello报文中MTU必须和接收端口的配置一致==【mtu没必要】
网络类型为广播时，所接收的Hello报文中Network Mask字段必须和接收端口的网络掩码一致

以下关于OSPF虚连接的描述，错误的是哪一项？
虚连接实际上是一个逻辑通道
虚连接增加了网络的复杂度
配置了虚连接所经过的区域必须拥有全部的路由选择信息
==虚链接必须配置在两台ASBR中==【虚连接可以在任意两个ABR上建立，但是要求着两个ABR都有端口连接在一个相同的非骨干区域。】


以下关于LSDB同步的描述，错误的是哪项？
==详细的LSA信息会在ExStart和Loading两个状态之间交互==【应该是exchange】
DD报文在Exchange状态下会携带链路状态的摘要信息
LSR不携带详细的链路状态信息
Loading状态下，邻居之间会相互发送LSR报文、 LSU报文和LSAck报文

使用default-route-advertise命令可将缺省路由通告进oSPF域内，该缺省路由属于以下哪一类LSA？
2类LSA
1类LSA
3类LSA
4类LSA
==5类LSA==【使用default-route-advertise命令后，ASBR将产生一个Link State ID为0.0.0.0，网络掩码为0.0.0.0的ASE LSA（Type 5），并且通告到整个OSPF区域中】

以下关于OSPF特殊区域的描述，错误的是哪一项？
Stub Area和Totally Stub区域的不同在于该区域充许域间路由
==NSSA Area和Stub区域的不同在于该区域允许自治系统外部路由的引入，由ABR发布LSA7通告给本区域==【是由ASBR发布LSA7通告给本区域，不是ABR】
Totally Stub Area的 作用是允许ABR发布的 LSA3缺省路由，不充许自治系统外部路由和区域间的路由
Totally Stub区域和NSSA区域的不同在于该区域不充许域间路由


LS Request报文不包括以下哪一字段？
通告路由器（Advertising Router)
链路状态ID（Link Srate ID）
==数据库描述序列号(Database Dascription Sequence lumber)==【来标明是否是一个更新的LSA 。】
链路状态类型(Link state type)

下面关于OSPF DR的描述，不正确的是：
如果当前DR故障，当前BDR自动成为新的DR,网络中重新选举BDR
DR Priority值大的，优先选举为DR
DR Priority一样时， RouterD大者优先选举为DR
==当OSPF时网络中有新的具有更大DR Priorityi路由器加入时、则该新的路由器会抢占原来的DR==【不严谨】


两台路由器直连，并设定网络类型为p2p建立OSPF邻居。那么两台路由器传输OSPF报文的目的IP地址是以下哪一项？
使用组播地址224.0.0.6
==使用组播地址224.0.0.5==
采用p2p模式建立邻居时，不使用IP地址建立
目的地址分别是对端端口的IP地址


以下关于osPF asbr-summary命令的描述，错误的是哪一项？.
asbr-summary命令只在需要汇聚的ASBR上部署才能生效
使用asbr-summary命令汇总的路由会以5类LSA在区域内传递
使用asbr-summary命令汇总的路由能够被泛洪到其它区域
==abr-summary命令可以汇总被asbr-summary聚合后的LSA==【注意这里说的是abr和asbr ！！！！abr-summary的汇总对象指的是3类LSA；asbr-summary的汇总对象指的是5类LSA，所以两者之间不能互相操作，不能互相汇总彼此的LSA。】




