
# 清空配置命令
```
<Huawei>reset saved-configuration
```
<font color="#ff0000">This will delete the configuration in the flash memory.</font>
<font color="#ff0000">The device configurations will be erased to reconfigure.</font>
<font color="#ff0000">Are you sure? (y/n)</font>[n]
<font color="#6425d0">这个时候我们要选择y</font>
```
reboot
```
<font color="#ff0000">Info: The system is comparing the configuration, please wait.</font>
<font color="#ff0000">Warning: All the configuration will be saved to the next startup configuration. </font>
<font color="#ff0000">Continue ?</font> [y/n]:
<font color="#6425d0">这个时候我们要选择n，不保存配置</font>
<font color="#ff0000">System will reboot! Continue ?</font> [y/n]:
<font color="#6425d0">这个时候我们要选择y</font>
<font color="#6425d0">然后重启即可</font>
# 简单配置动态路由ospf
~~图示~~
![Pasted-image-20231128205346.png](2需要放入网站的笔记/Ensp的相关操作/Ensp的相关操作/Pasted-image-20231128205346.png)
图中配置仅展示两台路由器:

```
AR1220-AR1:
ospf 1      
area 123    
```
<font color="#9bbb59">ospf进程一共可取值1-65535</font>
<font color="#9bbb59">area取123的话区域为0.0.0.123</font>
```
AR1220-AR1:
ospf 1      
area 123    
```
两个路由器都建立好区域后，将连接的网段添加到区域即可。
```
[Huawei-ospf-1-area-0.0.0.123]network 10.1.1.0 0.0.0.255
[Huawei-ospf-1-area-0.0.0.123]network 192.168.1.0 0.0.0.255
```

```
[Huawei-ospf-1-area-0.0.0.123]network 10.1.1.0 0.0.0.255
[Huawei-ospf-1-area-0.0.0.123]network 192.168.2.0 0.0.0.255
```
输入以下可以查看ospf的邻居列表
```
display ospf peer b
```
删除:
```
router ospf 1 
no network 192.168.1.0 0.0.0.255 area 0
```
# 简单配置vlan
```
vlan 100
vlan 200
interface g0/0/1
port link-type access
port default vlan 100
display vlan
```

# 清除接口配置(接口和子接口)
1. 登陆ensp设备，进入用户视图模式；
2. 使用命令“system-view”进入系统视图模式；
3. 使用命令“interface GigabitEthernet 0/0/1”，进入GigabitEthernet 0/0/1的配置模式；
4. 使用命令“undo ip address 192.168.1.1 255.255.255.0”，删除IP地址及子网掩码配置；
5. 使用命令“quit”退出GigabitEthernet 0/0/1的配置模式，返回系统视图模式；
6. 如果需要保存配置，请使用命令“save”进行保存。









