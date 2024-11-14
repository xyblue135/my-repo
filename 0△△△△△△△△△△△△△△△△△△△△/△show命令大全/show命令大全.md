命令行	
show version  				查询设备版本信息及板卡在位情况
show cpu-usage  				查询cpu使用率
show mem-usage 			查询设备内存使用率
show power-info				查询设备电源输入情况
show fan-info				查询设备风扇运行情况
show temp-info 				查询设备板卡温度
show device					查询板卡状态及SN号等信息
show user-info 				查询用户情况
who							查询用户连接情况
show interface  brief main		查询所有接口状态及crc统计
show ip interface  brief			查询所有接口ip地址及接口状态
show interface  xgigabitethernet 0/1/1	查询设备单个接口信息，包含模块信息
show snmp-server  community 			查询设备团体名
show snmp-server   trap 				查询snmp上报服务器
show running-config  snmp			查询snmp配置脚本
show lldp neighbor  brief				查询链路发现协议的邻居
show dcn global 					        查询设备dcn全局信息
show ip ospf neighbor 					查询ospf邻居状态
show ip ospf interface  gigabitethernet 0/1/1.4094	查询ospf接口信息
show arp						查询arp表信息
show ip route 						查询路由表信息
show ip route  ospf 					查询路由表中ospf路由信息
show ip ospf  route 					查询ospf表
show ip route  vrf __dcn_vpn__				查询基于__dcn_vpn__的私网路由表
show running-config  router ospf 			查询ospf的配置信息
show dcn  route 					查询dcn路由表信息
show ldp  adjacency 					查询ldp邻居信息
show ldp  session  					查询ldp会话信息
show ldp  interface  					查询所有使能ldp接口信息
show running-config  router ldp 			查询ldp的全局配置
show mpls  lsp 						查询mpls的标签表信息
show mpls  l2vc brief 					查询所有pw业务信息
show mpls  l2vc  26816 					基于vcid查询单条pw业务信息
show ldp  l2vc  26816  detail 				查询ldp分发pw详细信息
show bfd session brief  				查询所有bfd信息
show running-config  interface gigabitethernet0/1/3.801	查询接口配置信息
show acl   2001						查询acl信息
show aaa configuration 					查询AAA的配置
show qos-schedule-policy all 				查询qos调度模板
show qos-policy 					查询qos限速模板
show clock  source 					查询以太时钟同步信息
show ptp   all   state  				查询PTP时间同步信息
show ntp-service status 				查询NTP时间同步信息
show running-config 					查询设备当前运行配置
show syslog  buffer 					查询syslog日志信息
show alarm current 					查询设备当前告警信息
