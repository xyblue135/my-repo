# Diff-serv 定义EF类的业务类型
276/1247、在Diff-Serv网络中，定义EF类的业务类型的主要目的是
**为要求低时延低丢失、低抖动和确保带宽的业务优先提供业务保证**
为报文转发提供通道
为特定流量确保带宽
有能力使用VPN技术
<u>EF队列的作用是满足低时延业务，拥有绝对优先级，仅当EF队列中的报文调度完毕后，才会调度其他队列中的报文。
Diff-Serv是一种在IP网络中提供服务质量（Quality of Service，QoS）的方法。它通过在IP数据包的头部设置DSCP（Differentiated Services Code Point）字段来标记数据包的类别，从而让网络设备能够识别并按照预先定义的策略对数据包进行处理。
EF类是Diff-Serv定义的一种PHB（Per-Hop Behaviors，逐跳行为）类别，它特别适合于实时应用，如语音和视频流，这些应用对延迟和抖动敏感。当网络设备识别到带有EF标记的数据包时，它会尽力提供低延迟、低丢包率和低抖动的传输，以确保此类流量的服务质量。</u>

# 端口队列调度
单选题278/1247、在端口队列调度中，哪种队列没有公平、且不同的流之间不能相互隔离？
CQ + WFQ
PQ + WFQ
**FIFO**
WRR
<u>FIFO先入先出队列，谁先来谁先走，没有公平性可言，不同的流量不能区分隔离。</u>
<u>FIFO（First-In-First-Out）WFQ（Weighted Fair Queuing）、PQ（Priority Queuing）、WRR（Weighted Round Robin）</u>
# 模型队列调度
单选题283/1247、Best-Effort Server模型是通过什么队列技术来实现的？
**FIFO**
WFQ
PQ
LQ
尽力服务（BE Service）Best-Effort服务模型是网络的缺省服务模型，通过FIFO队列来实现。它适用于绝大多数网络应用，如FTP、E-Mail等
# MQC中流命令
单选题286/1247、MQC中流分类命令不能使用if-match匹配以下哪一参数？
源MAC地址
**前缀列表**
Inbound -interface
DSCP值
<u>MQC（Modular QoS Command Line Interface，模块化QoS命令行接口）用于配置QoS（Quality of Service，服务质量）策略的一种工具。在MQC中，流分类（traffic classifier）用于识别网络流量的特征，以便将其映射到特定的行为集（behavior set），进而实现流量的优先级处理、整形、限速等功能。</u>![image-2024718843174.png|225](8%E5%88%B7%E9%A2%98%E7%9A%84/HCIP-821/QOS/image-2024718843174.png)