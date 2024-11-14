# ospf五种报文格式
OSPF用IP报文直接封装协议报文，协议号为89。OSPF分为5种报文，Hello报文、DD报文、LSR报文、LSU报文和LSAck报文。
所有OSPF报文(五种)共享一个固定的报文头格式，头部长度为24字节。这个头部包含了报文类型和其他重要信息。
# 共享报的文头格式 
串行收，每行4字节，一共6行
![image-20247214033470.png|275](7_8ENSP实验配置/Z杂/关于OSPF的报文/OSPF报文/image-20247214033470.png)

| 字段             | 长度  | 含义                                                                                                                      |
| -------------- | --- | ----------------------------------------------------------------------------------------------------------------------- |
| **Version**    | 1字节 | 版本，OSPF的版本号。对于OSPFv2来说，其值为2。V6就是ospfv3 这里就是3                                                                            |
| **Type**       | 1字节 | 类型，OSPF报文的类型，有下面几种类型：**1：Hello报文；2：DD报文；3：LSR报文；4：LSU报文；5：LSAck报文。**                                                    |
| Packet length  | 2字节 | OSPF报文的总长度，包括报文头在内，单位为字节。                                                                                               |
| Router ID      | 4字节 | 发送该报文的路由器标识。                                                                                                            |
| Area ID        | 4字节 | 发送该报文的所属区域。                                                                                                             |
| Checksum       | 2字节 | 校验和，包含除了认证字段的整个报文的校验和。                                                                                                  |
| AuType         | 2字节 | 验证类型，值有如下几种表示， 0：不验证；1：简单认证；2：MD5认证。                                                                                    |
| Authentication | 8字节 | 鉴定字段，其数值根据验证类型而定。当验证类型为0时未作定义；类型为1时此字段为密码信息；类型为2时此字段包括Key ID、MD5验证数据长度和序列号的信息。MD5验证数据添加在OSPF报文后面，不包含在Authenticaiton字段中。 |
# 报文头抓包
![image-20247214532428.png|550](7_8ENSP实验配置/Z杂/关于OSPF的报文/OSPF报文/image-20247214532428.png)
# 1Hello报文格式
Hello报文是最常用的一种报文，其作用为建立和维护邻接关系，周期性的在使能了OSPF的接口上发送。报文内容包括一些定时器的数值、DR、BDR以及自己已知的邻居。
![hello%E6%8A%A5%E6%96%87.png|425](7_8ENSP实验配置/0端口隔离配置/1关于OSPF的报文/OSPF报文/hello%E6%8A%A5%E6%96%87.png)

| 字段                       | 长度   | 含义                                                                     |
| ------------------------ | ---- | ---------------------------------------------------------------------- |
| Network Mask             | 32比特 | 发送Hello报文的接口所在网络的掩码。                                                   |
| Hello Interval           | 16比特 | 发送Hello报文的时间间隔。                                                        |
| Options                  | 8比特  | 可选项：E：允许Flood AS-External-LSAs MC：转发IP组播报文 N/P：处理Type-7 LSAs DC：处理按需链路 |
| Router Priority          | 8比特  | DR优先级。默认为1。如果设置为0，则路由器不能参与DR或BDR的选举。                                   |
| RouterDeadInterval       | 32比特 | 失效时间。如果在此时间内未收到邻居发来的Hello报文，则认为邻居失效。                                   |
| Designated Router        | 32比特 | DR的接口地址。                                                               |
| Backup Designated Router | 32比特 | BDR的接口地址。                                                              |
| Neighbor                 | 32比特 | 邻居，以Router ID标识。                                                       |
# 1hello报文抓包

![image-20247215624756.png|391](7_8ENSP实验配置/Z杂/关于OSPF的报文/OSPF报文/image-20247215624756.png)
# 2DD报文格式
两台路由器在邻接关系初始化时，用DD报文（Database Description  Packet）来描述自己的LSDB，进行数据库的同步。报文内容包括LSDB中每一条LSA的Header（LSA的Header可以唯一标识一条LSA）。
Header只占一条LSA的整个数据量的一小部分，这样可以减少路由器之间的协议报文流量，对端路由器根据LSA   Header就可以判断出是否已有这条LSA。在两台路由器交换DD报文的过程中，一台为Master，另一台为Slave。由Master规定起始序列号，每发送一个DD报文序列号加1，Slave方使用Master的序列号作为确认。

![image-202472121246.png|425](7_8ENSP实验配置/Z杂/关于OSPF的报文/OSPF报文/image-202472121246.png)

| 字段                 | 长度   | 含义                                                                        |
| ------------------ | ---- | ------------------------------------------------------------------------- |
| Interface MTU      | 16比特 | 在不分片的情况下，此接口最大可发出的IP报文长度。                                                 |
| Options            | 8比特  | 可选项：E：允许Flood AS-External-LSAs；MC：转发IP组播报文；N/P：处理Type-7 LSAs；DC：处理按需链路。   |
| I                  | 1比特  | 当发送连续多个DD报文时，如果这是第一个DD报文，则置为1，否则置为0。                                      |
| M (More)           | 1比特  | 当发送连续多个DD报文时，如果这是最后一个DD报文，则置为0。否则置为1，表示后面还有其他的DD报文。                       |
| M/S (Master/Slave) | 1比特  | 当两台OSPF路由器交换DD报文时，首先需要确定双方的主从关系，Router ID大的一方会成为Master。当值为1时表示发送方为Master。 |
| DD sequence number | 32比特 | DD报文序列号。主从双方利用序列号来保证DD报文传输的可靠性和完整性。                                       |
| LSA Headers        | 可变   | 该DD报文中所包含的LSA的头部信息。                                                       |
# 2DD报文抓包
![image-2024721486936.png|375](7_8ENSP实验配置/Z杂/关于OSPF的报文/OSPF报文/image-2024721486936.png)
# 3LSR报文格式
两台路由器互相交换过DD报文之后，知道对端的路由器有哪些LSA是本地的LSDB所缺少的和哪些LSA是已经失效的，这时需要发送LSR报文（Link State Request Packet）**向对方请求所需的LSA**。内容包括所需要的LSA的摘要。LSR报文格式如下图所示，其中LS type、Link State ID和Advertising Router可以唯一标识出一个LSA，当两个LSA一样时，需要根据LSA中的LS sequence number、LS checksum和LS age来判断出所需要LSA的新旧。
![image-2024721313872.png|425](7_8ENSP实验配置/Z杂/关于OSPF的报文/OSPF报文/image-2024721313872.png)

| 字段                 | 长度   | 含义                                          |
| ------------------ | ---- | ------------------------------------------- |
| LS type            | 32比特 | LSA的类型号。                                    |
| Link State ID      | 32比特 | 根据LSA中的LS Type和LSA description在路由域中描述一个LSA。 |
| Advertising Router | 32比特 | 产生此LSA的路由器的Router ID。                       |
# 3LSR报文抓包
![image-20247215031124.png|272](7_8ENSP实验配置/Z杂/关于OSPF的报文/OSPF报文/image-20247215031124.png)
```
- Router LSA（类型1 LSA）
    
    - Link State ID：1.1.1.1（R1的Router ID）
    - Advertising Router：1.1.1.1（发布该LSA的路由器R1）
- Network LSA（类型2 LSA）
    
    - Link State ID：192.168.1.1（DR的接口IP）
    - Advertising Router：2.2.2.2（发布该LSA的路由器R2）
- Summary LSA（类型3 LSA）
    
    - Link State ID：192.168.2.0（被总结的网络192.168.2.0/24的前缀）
    - Advertising Router：2.2.2.2（发布该LSA的路由器R2）
- AS External LSA（类型5 LSA）
    
    - Link State ID：10.0.0.0（被外部通告的网络10.0.0.0/8的前缀）
    - Advertising Router：3.3.3.3（发布该LSA的路由器R3）
```
# 4LSU报文格式
用来向对端Router发送其所需要的LSA或者泛洪自己更新的LSA，内容是多条LSA（全部内容）的集合。LSU报文（Link State Update  Packet）在支持组播和广播的链路上是以组播形式将LSA泛洪出去。为了实现Flooding的可靠性传输，需要LSAck报文对其进行确认。对没有收到确认报文的LSA进行重传，重传的LSA是直接发送到邻居的。
![image-20247213846905.png|400](7_8ENSP实验配置/Z杂/关于OSPF的报文/OSPF报文/image-20247213846905.png)

|字段|长度|含义|
|---|---|---|
|Number of LSAs|32比特|LSA的数量。|
# 4LSU报文抓包
![image-20247213938401.png|400](7_8ENSP实验配置/Z杂/关于OSPF的报文/OSPF报文/image-20247213938401.png)
# 5LSACK报文格式
用来对接收到的LSU报文进行确认。内容是需要确认的LSA的Header（一个LSAck报文可对多个LSA进行确认）。LSAck（Link State  
Acknowledgment Packet）报文根据不同的链路以单播或组播的形式发送。
![image-2024721409226.png|375](7_8ENSP实验配置/Z杂/关于OSPF的报文/OSPF报文/image-2024721409226.png)

|字段|长度|含义|
|---|---|---|
|LSAs Headers|可变|通过LSA的头部信息确认收到该LSA。|
# 5LSACK报文抓包
![image-20247214254340.png|350](7_8ENSP实验配置/Z杂/关于OSPF的报文/OSPF报文/image-20247214254340.png)
# ospf的五种LSA
# Router lsa
所有ospf路由器都会有，反映本地链路和邻居路由器，**只在本区域内全部泛洪**（邻居的链路类型，开销，ip地址，路由器router id）
![image-20247222219202.png|350](7_8ENSP实验配置/Z杂/关于OSPF的报文/OSPF报文/image-20247222219202.png)
![[7_8ENSP实验配置/Z杂/关于OSPF的报文/----/Pasted image 20240721185102.png|325]]
![image-20247215414171.png|325](7_8ENSP实验配置/Z杂/关于OSPF的报文/OSPF报文/image-20247215414171.png)
# Network lsa
由DR生成（一个网段一个DR），反映多路访问网络上ospf路由器的连接，**只在本区域全部泛洪**（路由器的连接，DR地址）
![image-20247222231751.png|400](7_8ENSP实验配置/Z杂/关于OSPF的报文/OSPF报文/image-20247222231751.png)
![[7_8ENSP实验配置/Z杂/关于OSPF的报文/----/Pasted image 20240721185505.png|250]]
![image-202472154524.png|350](7_8ENSP实验配置/Z杂/关于OSPF的报文/OSPF报文/image-202472154524.png)
# network-summary-lsa
Network-summary-LSA（Type3）：描述区域内所有网段的路由，并通告给其他相关区域。
ASBR-summary-LSA（Type4）：描述到ASBR的路由，通告给除ASBR所在区域的其他相关区域。
Type3和Type4的LSA有相同的格式，它们都是由ABR产生。
![image-20247222146500.png|350](7_8ENSP实验配置/Z杂/关于OSPF的报文/OSPF报文/image-20247222146500.png)
# ASBR-summary-lsa
ASBR-Summary-LSA（Type4）：描述到ASBR的路由，通告给除ASBR所在区域的其他相关区域。
	Type3和Type4的LSA有相同的格式，它们都是由ABR产生。
![image-20247224143732.png|400](7_8ENSP实验配置/Z杂/关于OSPF的报文/OSPF报文/image-20247224143732.png)
# AS-external-lsa
