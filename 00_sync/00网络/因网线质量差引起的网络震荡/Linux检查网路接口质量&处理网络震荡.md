在家庭nas中，突然发现看本地视频和传文件这么慢了，而且有时候ssh会断连就很离谱，后来查看接口的日志才发现爱你在反复重复连接
![image-202410274159555.png|325](00_sync/00%E7%BD%91%E7%BB%9C/%E5%9B%A0%E7%BD%91%E7%BA%BF%E8%B4%A8%E9%87%8F%E5%B7%AE%E5%BC%95%E8%B5%B7%E7%9A%84%E7%BD%91%E7%BB%9C%E9%9C%87%E8%8D%A1/%E5%9B%A0%E7%BD%91%E7%BA%BF%E8%B4%A8%E9%87%8F%E5%B7%AE%E5%BC%95%E8%B5%B7%E7%9A%84%E7%BD%91%E7%BB%9C%E9%9C%87%E8%8D%A1/image-202410274159555.png)
![image-202410274244893.png|325](00_sync/00%E7%BD%91%E7%BB%9C/%E5%9B%A0%E7%BD%91%E7%BA%BF%E8%B4%A8%E9%87%8F%E5%B7%AE%E5%BC%95%E8%B5%B7%E7%9A%84%E7%BD%91%E7%BB%9C%E9%9C%87%E8%8D%A1/%E5%9B%A0%E7%BD%91%E7%BA%BF%E8%B4%A8%E9%87%8F%E5%B7%AE%E5%BC%95%E8%B5%B7%E7%9A%84%E7%BD%91%E7%BB%9C%E9%9C%87%E8%8D%A1/image-202410274244893.png)
# 检测网口状态命令ethtool
支持的配置
```
xyblue@xyblue-HP-Pavilion-Gaming-Laptop-15-dk1xxx:~$ sudo ethtool eno1
Settings for eno1:
        Supported ports: [ TP    MII ]
        Supported link modes:   10baseT/Half 10baseT/Full
                                100baseT/Half 100baseT/Full
                                1000baseT/Full
        Supported pause frame use: Symmetric Receive-only
        Supports auto-negotiation: Yes
        Supported FEC modes: Not reported
        Advertised link modes:  10baseT/Half 10baseT/Full
                                100baseT/Half 100baseT/Full
                                1000baseT/Full
        Advertised pause frame use: Symmetric Receive-only
        Advertised auto-negotiation: Yes
        Advertised FEC modes: Not reported
        Link partner advertised link modes:  10baseT/Half 10baseT/Full
                                             100baseT/Half 100baseT/Full
                                             1000baseT/Full
        Link partner advertised pause frame use: Symmetric
        Link partner advertised auto-negotiation: Yes
        Link partner advertised FEC modes: Not reported
        Speed: 1000Mb/s
        Duplex: Full
        Auto-negotiation: on
        master-slave cfg: preferred slave
        master-slave status: slave
        Port: Twisted Pair
        PHYAD: 0
        Transceiver: external
        MDI-X: Unknown
        Supports Wake-on: pumbg
        Wake-on: d
        Link detected: yes
```
重点查看输出的 `Speed`、`Duplex` 和 `Auto-negotiation` 状态。如果发现协商失败，可以尝试手动设置网卡速率为千兆：
sudo ethtool -s eth0 speed 1000 duplex full autoneg on【不推荐直接使用，不稳定】

# 观察全局up down情况
```
sudo journalctl -k | grep -i "eno1"
sudo dmesg | grep -i "eno1"  【可选】
```
![image-202410273350844.png](00_sync/00%E7%BD%91%E7%BB%9C/%E5%9B%A0%E7%BD%91%E7%BA%BF%E8%B4%A8%E9%87%8F%E5%B7%AE%E5%BC%95%E8%B5%B7%E7%9A%84%E7%BD%91%E7%BB%9C%E9%9C%87%E8%8D%A1/Linux%E6%A3%80%E6%9F%A5%E7%BD%91%E8%B7%AF%E6%8E%A5%E5%8F%A3%E8%B4%A8%E9%87%8F&%E5%A4%84%E7%90%86%E7%BD%91%E7%BB%9C%E9%9C%87%E8%8D%A1/image-202410273350844.png)
# 更多信息
```
sudo journalctl -u NetworkManager | grep -i "eno1"
```
![image-202410273513327.png](00_sync/00%E7%BD%91%E7%BB%9C/%E5%9B%A0%E7%BD%91%E7%BA%BF%E8%B4%A8%E9%87%8F%E5%B7%AE%E5%BC%95%E8%B5%B7%E7%9A%84%E7%BD%91%E7%BB%9C%E9%9C%87%E8%8D%A1/Linux%E6%A3%80%E6%9F%A5%E7%BD%91%E8%B7%AF%E6%8E%A5%E5%8F%A3%E8%B4%A8%E9%87%8F&%E5%A4%84%E7%90%86%E7%BD%91%E7%BB%9C%E9%9C%87%E8%8D%A1/image-202410273513327.png)
```
 activated.
10月 27 17:50:38 xyblue-HP-Pavilion-Gaming-Laptop-15-dk1xxx NetworkManager[818]: <info>  [1730022638.7786] device (eno1): state change: activated -> deactivating (reason 'user-requested', sys-iface-state: 'managed')
10月 27 17:50:38 xyblue-HP-Pavilion-Gaming-Laptop-15-dk1xxx NetworkManager[818]: <info>  [1730022638.7792] audit: op="device-disconnect" interface="eno1" ifindex=2 pid=119789 uid=0 result="success"
10月 27 17:50:38 xyblue-HP-Pavilion-Gaming-Laptop-15-dk1xxx NetworkManager[818]: <info>  [1730022638.7922] device (eno1): state change: deactivating -> disconnected (reason 'user-requested', sys-iface-state: 'managed')
10月 27 17:50:39 xyblue-HP-Pavilion-Gaming-Laptop-15-dk1xxx NetworkManager[119882]: <info>  [1730022639.3424] device (eno1): carrier: link connected
10月 27 17:50:39 xyblue-HP-Pavilion-Gaming-Laptop-15-dk1xxx NetworkManager[119882]: <info>  [1730022639.3427] manager: (eno1): new Ethernet device (/org/freedesktop/NetworkManager/Devices/8)
10月 27 17:50:39 xyblue-HP-Pavilion-Gaming-Laptop-15-dk1xxx NetworkManager[119882]: <info>  [1730022639.3431] device (eno1): state change: unmanaged -> unavailable (reason 'managed', sys-iface-state: 'external')
10月 27 17:50:39 xyblue-HP-Pavilion-Gaming-Laptop-15-dk1xxx NetworkManager[119882]: <info>  [1730022639.3627] device (eno1): state change: unavailable -> disconnected (reason 'none', sys-iface-state: 'managed')
10月 27 17:50:39 xyblue-HP-Pavilion-Gaming-Laptop-15-dk1xxx NetworkManager[119882]: <info>  [1730022639.3788] policy: auto-activating connection 'netplan-eno1' (10838d80-caeb-349e-ba73-08ed16d4d666)
10月 27 17:50:39 xyblue-HP-Pavilion-Gaming-Laptop-15-dk1xxx NetworkManager[119882]: <info>  [1730022639.3808] device (eno1): Activation: starting connection 'netplan-eno1' (10838d80-caeb-349e-ba73-08ed16d4d666)
10月 27 17:50:39 xyblue-HP-Pavilion-Gaming-Laptop-15-dk1xxx NetworkManager[119882]: <info>  [1730022639.3850] device (eno1): state change: disconnected -> prepare (reason 'none', sys-iface-state: 'managed')
10月 27 17:50:39 xyblue-HP-Pavilion-Gaming-Laptop-15-dk1xxx NetworkManager[119882]: <info>  [1730022639.3855] device (eno1): state change: prepare -> config (reason 'none', sys-iface-state: 'managed')
10月 27 17:50:39 xyblue-HP-Pavilion-Gaming-Laptop-15-dk1xxx NetworkManager[119882]: <info>  [1730022639.3887] device (eno1): state change: config -> ip-config (reason 'none', sys-iface-state: 'managed')
10月 27 17:50:39 xyblue-HP-Pavilion-Gaming-Laptop-15-dk1xxx NetworkManager[119882]: <info>  [1730022639.3910] device (eno1): state change: ip-config -> ip-check (reason 'none', sys-iface-state: 'managed')
10月 27 17:50:39 xyblue-HP-Pavilion-Gaming-Laptop-15-dk1xxx NetworkManager[119882]: <info>  [1730022639.3917] policy: set 'netplan-eno1' (eno1) as default for IPv4 routing and DNS
10月 27 17:50:39 xyblue-HP-Pavilion-Gaming-Laptop-15-dk1xxx NetworkManager[119882]: <info>  [1730022639.3990] device (eno1): state change: ip-check -> secondaries (reason 'none', sys-iface-state: 'managed')
10月 27 17:50:39 xyblue-HP-Pavilion-Gaming-Laptop-15-dk1xxx NetworkManager[119882]: <info>  [1730022639.3991] device (eno1): state change: secondaries -> activated (reason 'none', sys-iface-state: 'managed')
10月 27 17:50:39 xyblue-HP-Pavilion-Gaming-Laptop-15-dk1xxx NetworkManager[119882]: <info>  [1730022639.4001] device (eno1): Activation: successful, device activated.
10月 27 17:50:41 xyblue-HP-Pavilion-Gaming-Laptop-15-dk1xxx NetworkManager[119882]: <info>  [1730022641.8128] dhcp6 (eno1): activation: beginning transaction (timeout in 45 seconds)
10月 27 17:50:41 xyblue-HP-Pavilion-Gaming-Laptop-15-dk1xxx NetworkManager[119882]: <info>  [1730022641.8141] policy: set 'netplan-eno1' (eno1) as default for IPv6 routing and DNS
10月 27 17:50:41 xyblue-HP-Pavilion-Gaming-Laptop-15-dk1xxx NetworkManager[119882]: <info>  [1730022641.8213] dhcp6 (eno1): state changed new lease
root@xyblue-HP-Pavilion-Gaming-Laptop-15-dk1xxx:~# 
```

更换网线后状态正常。