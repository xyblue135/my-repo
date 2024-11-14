- BGP是基于TCP179端口的路由协议，只要能够建立TCP就能够建立BGP；
- BGP只传递路由信息，不计算路由，不会暴露AS内部的网络拓扑；
- BGP的路由更新是触发更新，不是周期性更新；
- BGP是一种距离矢量路由协议，在设计上就避免了环路的发生；

OSPF、ISIS路由协议在网络中已经广泛使用，但是随着网络规模的扩大，路由条目也随增加，IGP协议已经无法管理大规模网络了。因此出现了AS的概念。
如果使用IGP路由协议（OSPF、ISIS）对接时，那么这个时候企业网络和运营商的网络是运行在一张网络中，这个是不安全的，你可以认为运营商为什么信任你的企业网络？
![4899f946162855eb75df5eb5f1e22ad6.png|325](7_8ENSP实验配置/6BGP原理/6BGP原理/4899f946162855eb75df5eb5f1e22ad6.png)
![675d41ed592568a6e0845f476a832890.png|275](7_8ENSP实验配置/6BGP原理/6BGP原理/675d41ed592568a6e0845f476a832890.png)
这个时候可能有人还会站出来说，静态协议不就可以解决吗？其实是可以解决，不过有个问题就是使用静态协议时网络变动时都需要人手动去增删路由，那么有没有一种动态的方式呢？答案就是BGP路由协议了。
# BGP对等体
![6655c7054661637e83cd875144ace01b.png](7_8ENSP实验配置/6BGP原理/6BGP原理/6655c7054661637e83cd875144ace01b.png)
# 建立连接
![8d95f18998a8f58828b0a3e3c624f8b4.png|450](7_8ENSP实验配置/6BGP原理/6BGP原理/8d95f18998a8f58828b0a3e3c624f8b4.png)
# 报文
![a3a6cf1169d6ffd2ddbb66bace1a6ff5.png|475](7_8ENSP实验配置/6BGP原理/6BGP原理/a3a6cf1169d6ffd2ddbb66bace1a6ff5.png)
## open报文
open报文是TCP连接建立后发送的第一个报文，用于协商参数；
- version：bgp版本，通常为4；
- My AS：本地AS号；
- Hold time：保持时间。在建立对等体关系时两端要协商hold time，如果在这段时间内未收到对端发来的keepalive报文和update报文，则认为BGP连接中断；
- BGP identifier: BGP标识符，以IP地址形式标识，用来识别路由器。
![image-2024819321777.png](7_8ENSP实验配置/6BGP原理/6BGP原理/image-2024819321777.png)
## update报文
Update报文用于在对等体之间传递路由信息，可以用来发布和撤销路由。
一个Update报文可以通告具有相同路径属性的多条路由，这些路由保存在NLRI（网络层可达信息）中。
- Withdrawn Routes Length：标明Withdrawn Routes部分的长度。其值为零时，表示没有撤销的路由。
- Total path attribute length：路径属性字段的长度，以Byte为单位。如果为0则说明没有Path Attributes 字段。
![image-2024819338222.png|425](7_8ENSP实验配置/6BGP原理/6BGP原理/image-2024819338222.png)
## Notification报文 
当BGP检测到错误状态时，就会向对等体发送Notification报文，告知对端错误，之后BGP连接会立即中断。
- Error Code、Error Code：差错码、差错子码，描述错误类型；
- Data:错误内容；
![image-20248193357295.png](7_8ENSP实验配置/6BGP原理/6BGP原理/image-20248193357295.png)
## Keepalive报文
双方相互发送keepalive报文，收到对方的keepalive报文后对等体建立成功，同时后续定期发送keepalive报文用于保持连接。
![image-20248193517458.png](7_8ENSP实验配置/6BGP原理/6BGP原理/image-20248193517458.png)
## Route-refresh报文
Route-refresh报文用于要求对等体重新发送指定地址族的路由信息，一般是本地修改了相关的路由策略，让对方重新发送update报文。
在Open报文协商时会协商是否支持Route-refresh，如果对等体支持Route-refresh能力，则可以通过refresh bgp命令手工对BGP连接进行软复位，BGP软复位可以在不中断BGP连接的情况下重新刷新BGP路由表，并应用新的策略。
![image-20248193532389.png](7_8ENSP实验配置/6BGP原理/6BGP原理/image-20248193532389.png)
# 六种状态
BGP的状态有idle、connect、active、opensent、openconfirm、established六种状态。
![image-20248193623276.png|375](7_8ENSP实验配置/6BGP原理/6BGP原理/image-20248193623276.png)
![c08ab0f0af41b58f135203867d43b494.png|475](7_8ENSP实验配置/6BGP原理/6BGP原理/c08ab0f0af41b58f135203867d43b494.png)
（1）Idle状态是BGP初始状态。
在Idle状态下，BGP拒绝对等体发送的连接请求。只有在收到本设备的Start事件后，BGP才开始尝试和其它BGP对等体进行TCP连接，并转至Connect状态。
Start事件是由一个操作者配置一个BGP过程，或者重置一个已经存在的过程或者路由器软件重置BGP过程引起的。
任何状态中收到Notification报文或TCP拆链通知等Error事件后，BGP都会转至Idle状态。
（2）Connect状态
在Connect状态
- 如果TCP连接成功，那么BGP向对等体发送Open报文，并转至OpenSent状态。
- 如果TCP连接失败，那么BGP转至Active状态。
- 如果连接重传定时器超时，BGP仍没有收到BGP对等体的响应，那么BGP继续尝试和其它BGP对等体进行TCP连接，停留在Connect状态。
（3）Active状态
在Active状态下，BGP总是在试图建立TCP连接。
- 如果TCP连接成功，那么BGP向对等体发送Open报文，关闭连接重传定时器，并转至OpenSent状态。
- 如果TCP连接失败，那么BGP停留在Active状态。
- 如果连接重传定时器超时，BGP仍没有收到BGP对等体的响应，那么BGP转至Connect状态。
（4）Opensent状态、openconfirm状态
TCP三次握手建立成功后，发送open报文建立对等体关系，此时的状态为
opensent状态，当收到对端回应的open报文，并且参数检查无误，在发送keepalive报文后进入openconfirm状态。
（5）established状态
进入openconfirm状态后，收到对端的keepalive报文后进入established状态。
# BGP对等体表
```
dis bgp peer
```
![5f012b299b2db14517f480d1bf425b00.png](7_8ENSP%E5%AE%9E%E9%AA%8C%E9%85%8D%E7%BD%AE/6BGP%E5%8E%9F%E7%90%86/6BGP%E5%8E%9F%E7%90%86/5f012b299b2db14517f480d1bf425b00.png)
（1）peer：对等体地址
（2）V：版本号
（3）AS：对等体AS号
（4）UP/DOWN：对等体存在up或者down的时间
（5）state：对等体状态
（6）prefRce：从该对等体收到的路由前缀数目
# BGP路由表
```
display bgp routing-table
```
![9feafe125664848a7c54fb104971289a.png](7_8ENSP%E5%AE%9E%E9%AA%8C%E9%85%8D%E7%BD%AE/6BGP%E5%8E%9F%E7%90%86/6BGP%E5%8E%9F%E7%90%86/9feafe125664848a7c54fb104971289a.png)
如果到达同一个目的地存在多条路由，则将路由都进行罗列，但每个目的地只会优选一条路由。
![d1bee0ed328fe1f03fb3c2326b9ce081.png](7_8ENSP%E5%AE%9E%E9%AA%8C%E9%85%8D%E7%BD%AE/6BGP%E5%8E%9F%E7%90%86/6BGP%E5%8E%9F%E7%90%86/d1bee0ed328fe1f03fb3c2326b9ce081.png)
通过display bgp routing-table ipv4-address { mask | mask-length } 可以显示指定IP地址/掩码长度的路由信息，在其中有关于该BGP路由的详细信息，如：路由始发者、下一跳地址、路由的路径属性等。
# BGP路由生成
BGP路由是通过BGP命令通告而成的，而通告BGP路由的方法有两种：network和Import。
（1）network方式：
使用network命令可以将当前设备路由表中的路由（非BGP）发布到BGP路由表中并通告给邻居，和OSPF中使用network命令的方式大同小异，只不过在BGP宣告时，只需要宣告网段+掩码数即可，如：network 12.12.0.0 16。
（2）Import方式：
使用Import命令可以将该路由器学到的路由信息重分发到BGP路由表中，是BGP宣告路由的一种方式，可以引入BGP的路由包括：直连路由、静态路由及动态路由协议学到的路由。其命令格式与在RIP中重分发OSPF差不多。
# BGP通告原则
BGP设备会将最优路由加入BGP路由表，形成BGP路由。
BGP设备与对等体建立邻居关系后，采用以下交互原则：
- 从IBGP对等体获得的BGP路由，BGP设备只传递给它的EBGP对等体。
- 从EBGP对等体获得的BGP路由，BGP设备传递给它所有EBGP和IBGP对等体（对等体是IBGP只能传递一跳，对等体是EBGP则不限制）
- 当存在多条到达同一目的地址的有效路由时，BGP设备只将最优路由发布给对等体
- 路由更新时，BGP设备只发送更新的BGP路由
- 所有对等体发送的路由，BGP设备都会接收
- 所有EBGP对等体在传递过程中下一跳改变
- 所有IBGP对等体在传递过程中下一跳不变（需要特别注意）
- 默认EBGP传递时 TTL值为1（需要特别注意）
- 默认IBGP传递时 **TTL值为255**

参考文章:https://cloud.tencent.com/developer/article/1922673