当我们mgmt口做其他用途时，或者根本就没有mgmt口的时候![image-2024617337243.png](00_sync/00网络/二层交换机通过vlan配置管理口IP/二层交换机通过vlan配置管理口IP/image-2024617337243.png)

先创建vlan 创建vlan的最大号码
vlan batch 4094 
vlan 4094也可以 不过要qu
创建完成后
```
interface vlanif 4094  可能用不了
]interface Vlan-interface 4094   △△△△△华三 进入虚拟接口
```
ip address 192.168.3.50 24  当管理地址了
该进入接口了
```
interface  G1/0/1
port link-type access


port default vlan 4094  将端口加入4094 可能用不了
port access vlan 4094   △△△△△△△△h3c交换机的
```
![image-2024617145316.png](00_sync/00网络/二层交换机通过vlan配置管理口IP/二层交换机通过vlan配置管理口IP/image-2024617145316.png)

![image-20246171459208.png](00_sync/00网络/二层交换机通过vlan配置管理口IP/二层交换机通过vlan配置管理口IP/image-20246171459208.png)
这样的话就可以，vlan是虚拟接口，就算是20个接口都是vlan4094 那也是一个。
# 不幸
如果还是非常不幸4094根本用不了，
interface vlanif1
ip address  ip 24
随便插个口都是可以通的，你懂我意思吧