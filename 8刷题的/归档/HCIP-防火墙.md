# 防火墙
==SPU模块==是防火墙独有模块
==**SFU**：实现高速==无拥堵数据通道。
缺省防火墙==优先级为空0==。
**新建安全区域**：没有默认优先级。
**USG系列防火墙**：配置接口后仍属于Local区域。
# 包过滤防火墙
# 状态检测防火墙说明

## 默认关闭状态检测
TCP→创建会话，转发报文
UDP→创建会话，转发报文
ICMP【ping回显请求和ping回显应答】→创建会话，转发报文   ICMP【其它ICMP报文】 ==不创建会话，但是依旧转发报文==
## 开启状态检测
TCP【SYN报文】→创建会话，转发报文   TCP【SYN+ACK ACK报文】 → ==不创建会话，丢弃报文==
UDP→创建会话，转发报文
ICMP【ping回显请求和】→创建会话，转发报文   ICMP【ping回显应答ICMP】→==不创建会话，且丢弃报文==【其它ICMP报文】 ==不创建会话，但是依旧转发报文==

【防火墙图片题】在状态检测防火墙中，**开启**状态检测机制时，三次握手的第二个报文(SYN+ACK)到达防火墙的时候如果防火墙上**还没有对应的会话表**，则下面说法正确的是
如果防火墙安全策略允许报文通过，则创建会话表
==缺省状态下关闭状态检测防火墙功能后，需要配置了允许策略即可通过==
报文一定通过防火墙，并建立会话表
如果防火墙安全策略允许报文通过则报文可以通过防火墙

# 题目们

**状态检测防火墙**：==只需要匹配首包==，后续报文在状态表匹配，==可以检测UDP==，只需要匹配去或回中的一个，提高性能
==状态检测防火墙只对没有命中会话的首包进行安全策略检查==




# 简单的
以下关于不同类型防火墙的描述，正确的是哪些项？
状态检测防火墙安全策略检查源目IP地址符合策略即可建立状态化表项【仅仅通过检查数据包的源目IP地址是不一定就可以匹配策略】
==状态检测防火墙只对没有命中会话的首包进行安全策略检查==
==应用代理防火墙代理内部网络和外部网络用户之间的业务==
==缺省情况下，包过滤防火墙对于通过防火墙的每个数据包，都要进行ACL匹配检查==


