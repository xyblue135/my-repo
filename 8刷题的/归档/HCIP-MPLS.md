# 隐式空标签，
隐式空标签是MPLS网络中用于指示出口路由器弹出标签栈顶部标签的一种机制。它的作用是告诉出口路由器，当看到该标签时，应将数据包恢复为普通的IP报文，并根据IP报文头信息进行下一步转发。也就是出口的时候就不带标签了
```
FEC          IN/OUT LABEL   IN/OUT IF  VRF NAME
22.2.2.2/32   NULL/3   -/GE0/0/2
```
MPLS运行在以太网时，采用的帧封装格式

Mpls中，相同的路由，出标签也一定相同。

MPLS既不支持数据加密也不支持身份认证



- **MPLS LSP**：通过BFD检测静态或动态LSP的连通性。
- **MPLS标签分发**：Liberal保持方式会保留所有标签。

MPLS支持多层标签和转发平面面向连接的特性，在很多方面得到广泛的应用，那么部署MPLS的原因不包括
==各厂商标准普遍认可==【并不认可】
流量工程能力
在基于软件的路由器上简化路由查找
有能力使用VPN技术

运行MPLS设备的标签转发表中，对于相同的路由（下一跳也相同），出标签
一定不同
==-定相同==
可能相同

MPLS技术以标签交换代替IP转发，当MPLS运行在以太网中时，它使用哪种封装模式？
包模式
==帧模式==
传输模式
信道模式
通道模式

DU标签分发方式下，如果采用Liberal保持方式，则设备都会保留所有LDPPeer发来的标签，无论该LDP Peer是否为到达目的网段的下一跳【正确】3


通过BFD与MPL SLS P进行联动，可动态创建BFD来检测静态或动态LSP的连通性。【错误  动态BFD只支持动态LSP】

# 衍生
### 标签发布
- **==下游自主==（Downstream Unsolicited, DU）**：在这种模式下，LSR（Label Switching Router）不需要等待上游节点的请求就会主动向上游节点发送标签绑定信息。这种方式适用于那些需要快速建立LSP（Label Switched Path）的情况，因为它减少了标签请求的时间延迟。
### 标签分配方式
- ==**独立方式==（Independent Mode）**：一个LSR为每一个FEC（Forwarding Equivalence Class，转发等价类）分配一个标签，并且这个标签是独立于其他任何FEC的。这意味着即使两个FEC最终指向相同的下一跳，它们也会被分配不同的标签。
- **有序方式（Ordered Mode）**：与独立方式相对，在有序方式下，一个LSR只有在其所有下游邻居都为特定的FEC分配了标签后，才会为自己分配该FEC的标签并向其上游邻居通告。这种方式确保了当一个LSP建立时，整个路径上的每个LSR都已经准备好处理该FEC的数据流。
### 标签保持方式
- **保守方式（Conservative Mode）**：LSR只保留来自直接下一跳邻居的标签映射。如果存在多条到达同一目的地的不同路径，则只会保存其中一条路径的信息。
- ==**自由方式==（Liberal Mode）**：LSR会保存从所有邻居收到的所有标签映射，不论这些邻居是否是最优路径的一部分。这样做的好处是在主路径发生故障时能够更快地切换到备用路径，但代价是消耗更多的内存资源。