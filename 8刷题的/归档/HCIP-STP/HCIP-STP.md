# STP (802.1D)
stp==优先级默认为32768==，且STP的==优先级必须为4096的倍数==。
stp root primary 配置为==根桥，优先级固定为0==
stp root secondary 配置为==备份根桥，优先级固定为4096==


# 时间
**转发时间**15秒
**收敛时间** 30秒  是转发延迟时间（默认15秒）的两倍，即30秒。

# 添加的端口
Alternative端口为root根端口做备份
Backup 端口为DP指定端口做备份

在RSTP里面引入了边缘端口的概念，边缘端口不参与RSTP运算，可以由Disable直接转到Forwarding状态
RSTP中，某端口被选举为指定端口后，会先进入Discarding状态，再通过Proposal/Agreement机制快速进入Forwarding状态

# RSTP (802.1W)
RSTP定义了4个端口角色
删除了Learning和Listening和block状态，并增加了两种新的端口角色：Alternate Port和Backup Port。
RSTP相比于STP删除了3个端口状态，增加了两个端口角色，然 后一个端口如果3个hello没有收到上游设备发送的BPDU，则认为协商失败，【如果说是4个hello，那这个选项就是错的】
RSTP直接代替root根端口进入转发状态的是alternative端口
RSTP中边缘端口无需等待forwarding delay，可直接进入forwarding状态。如果边缘端口接收到了BPDU,则边缘端口会被直接关闭并进入error down状态【不会直接关闭并进入error down状态。相反，它会失去边缘端口的属性，转变为非边缘端口，开始参与生成树协议,需要注意这里BPDU开不开启跟保护都会有的，如果说开启BPDU保护，触发保护关键词，才能判断是关闭还是成为普通端口】
**端口角色** ==Alternative端口和Backup端口==在STP报文中flags字段内的==port role值均为01==。
## 根保护
跟保护是在指定端口上配置的
- **端口角色** Root Port和Backup Port不能配置根保护。
- **BPDU保护** 如果启用BPDU保护，边缘端口收到BPDU后会变为Down状态。
- 边缘端口可以快速进入转发状态，但如果收到BPDU，会失去边缘端口属性【因为没有开启BPDU保护】，成为普通端口

当一个运行MSTP协议的交换设备端口收到一个配置BPDU时，会与设备保存的全局配置消息进行对比【与该端口在相应MSTI中保存的配置BPDU进行对比】。若新收到的配置BPDU更优，则会同步更新交换设备保存的全局配置消息【】；反之，则丢弃该配置BPDU。==【错误 不是全局】==
## 拓扑
- **拓扑变化检测** 检测到非边缘端口迁移到Forwarding状态表示拓扑发生了变化。
- **BPDU类型** 存在一种BPDU类型，值为2，但依然存在拓扑变更通知BPDU（TCN BPDU）。
- RSTP中非边缘端口迁移到Forwarding状态是【唯一】的拓扑变化检测标准。

# MSTP (802.1S)
MSTP使用802.1S标准，而不是802.1D。

Instance ID范围为0-4094，而非0-32768
一个MST域内可以生成多棵生成树，每棵生成树都称为一个MSTI。其中MST I使用Instance ID标识，华为设备取值为0-32768.【错误 instance为0-4094 不是32768】
【错误】一个MST域内可以生成多棵生成树，每棵生成树都称为一个MSTl。其中MSTI使用Instance ID标识，华为设备取值为0-32768【错误，应该为0-4094】
在MSTP中，设备不能自动计算出根桥或备份根桥。

支持多个生成树实例（MST Instance），每个实例对应一棵生成树。
【错误】MSTP的CIST和MSTI都是根据优先级向量计算的，如果说是本桥到根桥就是错的，内部路径开销是【本桥【端口】到根桥的路径开销】
- **优先级向量** CIST和MSTI都是根据优先级向量计算的。
- RSTP中定义了4种端口角色，其中Alternative端口和Backup端口在STP报文中flags字段内的port role值一致都为01
- **TC保护** `stp tc-protection` 命令本身已经包含了enable功能，不需要额外添加enable。
## Discarding状态
	- **端口状态** Alternative和Backup端口最终只能处于Discarding状态。
在MSTP中，Alternative端口和Backup端口不能处于Learning状态。
- - **端口行为** 处于==Discarding状态下的端口不会接收数据帧==用于MAC地址学习。


# 简单的
接收到的配置BPDU更优时，不仅会更新全局配置信息，也会更新端口的信息。
sw2为instance20的根桥，display stp brief看到的MSTID 20的所有端口应该为DP
一个判断交换机环路的图片选择，please check the network accessed to flapping port
【错误】RSTP中处于Discarding状态下的端口，虽然会对接收到的数据帧做丢弃处理，但可以根据该端口收到的数据帧维护MAC地址表【不维护mac，都关闭了】。
【错误】VLAN映射表是IST域的属性，用来描述VLAN和MSTI之间的映射关系。其中每个VLAN可对应多个MSTI,且一个MSTI可对应多个VLAN。【一个IST(MSTP内部生成树)区域 一个vlan对应一个msti(生成树实例)  一个msti对应一个vlan】

# 图片题
上预备端口，直接进入转发状态
![image-2024912230179.png|400](8%E5%88%B7%E9%A2%98%E7%9A%84/%E5%BD%92%E6%A1%A3/HCIP-STP/HCIP-STP/image-2024912230179.png)
SWC上的预备端口成为新的根端口，并经过Learning状态后进入Forwarding状态
SWC重新选举根端口，并直接进入Forwarding状态
==SWC上的预备端口成为新的根端口，并直接进入Forwarding状态==
SWC重新选举根端口，并经过Learning后进入Forwarding状态


以下关于MSTP端口 状态的描述，错误的是哪一项？
根端口、指定端口和域边缘端口可处于Discarding状态
==Alternate端口和Backup端口可处于Learning状态==【只能处于discard】
Alternate端口和Backup端口只能处于Discarding状态
根端口、指定端口和域边缘端口最终会处于Forwarding状态

| STP  | 根端口(Root Port) 指定端口(Designated Port)   阻塞端口 (Blocking Port)                                                                                                            |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| RSTP | 根端口(Root Port) 指定端口(Designated Port)   <u>丢弃端口 (Discarding Port)</u>==替代端口 (Alternate Port)备份端口 (Backup Port)==                                                        |
| MSTP | 根端口(Root Port) 指定端口(Designated Port)                                              替代端口 (Alternate Port)备份端口 (Backup Port）<br> <br>==边缘端口(Edge Port)主端口 (Master Port)== |

| STP  | 收敛速度较慢，通常需要30到50秒。 | 只有根端口、指定端口和阻塞端口。             | 只有一个生成树实例。                         |
| ---- | ------------------ | ---------------------------- | ---------------------------------- |
| RSTP | 收敛速度较快，通常在几秒内完成。   | 增加了替代端口和备份端口，减少了阻塞端口的数量。     | 仍然只有一个生成树实例，但改进了收敛速度。              |
| MSTP | 与RSTP类似，具有快速收敛能力。  | 继承了RSTP的所有端口角色，并增加了边缘端口和主端口。 | 支持多个生成树实例，每个实例可以独立运行，提高了网络的灵活性和效率。 |
