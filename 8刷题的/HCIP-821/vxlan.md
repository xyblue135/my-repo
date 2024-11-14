判断题1015/1247、VXLAN报文的VNI字段长度为24bit。
**正确**
<u>VXLAN中的24比特VNI字段，提供多达16M租户的标识能力</u>

判断题1016/1247、 VXLAN用户可通过VXLAN接口访问lnternet
**正确**
<u>VxLAN用户是可以通过VxLAN接口访问互联网的。</u>

判断题1017/1247、VXLAN基于UDP封装，将以太网数据帧封装在IP报文中的UDP之上，所以被称为MACin UDP的封装。
**争取**
<u>VXLAN（Visual eXtensible Local Area Network虚拟扩展本地局域网）通过采用MAC in UDP封装来延伸二层网络，将以太报文封装在IP报文之上，实现二三层互通</u>

# vxlan说法
单选题 265/1247以下关于VXLAN的说法哪项是错误的？
在园区网络中引I入VXLAN技术，可以实现二层及三层通信
VXLAN通过采用IMACin UDP封装来延伸二层网络，将以太报文封装在IP报文之上
**部署VXLAN时，除了VXLAN隧道两端的设备需支持VXLAN，中间的转发设备也必须支持，否则VXLAN报文无法被正常转发**
VXLAN报文在Underlay网络中由路由指导转发，且Underlay转发时不关注内层数据的终端MAC地址

<u>原因在于VXLAN的设计就是为了让中间设备无需理解VXLAN封装。VXLAN报文在Underlay网络中仅根据外层的IP和UDP头部进行路由和转发。中间设备，如路由器，只需要具备基本的IP路由能力，它们并不需要支持或理解VXLAN的细节，因为它们只处理外层的IP头部，而忽略内层的VXLAN封装和MAC地址信息。因此，只要VXLAN隧道的两端设备支持VXLAN，中间的网络设备能够基于标准的IP路由转发VXLAN封装的数据包，整个VXLAN网络就可以正常工作。这是VXLAN能够跨越不同物理网络和提供商网络的一个关键优势，因为它不需要整个网络基础设施的全面升级或更改。</u>

<u>VXLAN（Visual eXtensible Local Area Network虚拟扩展本地局域网）通过采用MAC in UDP封装来延伸二层网络，将以太报文封装在IP报文之上，实现二三层互通；通过路由在网络中传输，无需关注虚拟机的MAC地址。且路由网络无网络结构限制，具备大规模扩展能力。 VxLAN 本质上是一种隧道封装技术。它使用 TCP/IP 协议栈的惯用手法——封装/解封装技术，将 L2 的以太网帧（Ethernet frames）封装成 L4 的 UDP 数据报（datagrams），然后在 L3 的网络中传输，效果就像 L2 的以太网帧在一个广播域中传输一样，实际上是跨越了 L3 网络，但却感知不到 L3 网络的存在。</u>