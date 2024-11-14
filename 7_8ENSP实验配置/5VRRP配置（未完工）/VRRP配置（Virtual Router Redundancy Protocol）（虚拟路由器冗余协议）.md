```
[lsw1-Eth-Trunk12]display interface Eth-Trunk 12
Eth-Trunk12 current state : UP
Line protocol current state : UP
Description:
Switch Port, PVID :    1, Hash arithmetic : According to SA-XOR-DA,Maximal BW: 2
G, Current BW: 2G, The Maximum Frame Length is 9216
IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is 4c1f-ccd8-1c86
Current system time: 2024-07-19 13:29:47-08:00
    Input bandwidth utilization  :    0%
    Output bandwidth utilization :    0%
-----------------------------------------------------
PortName                      Status      Weight
-----------------------------------------------------
GigabitEthernet0/0/23         UP          1
GigabitEthernet0/0/24         UP          1
-----------------------------------------------------
The Number of Ports in Trunk : 2
The Number of UP Ports in Trunk : 2

[lsw2-Eth-Trunk12]display interface Eth-Trunk 12
Eth-Trunk12 current state : UP
Line protocol current state : UP
Description:
Switch Port, PVID :    1, Hash arithmetic : According to SA-XOR-DA,Maximal BW: 2
G, Current BW: 2G, The Maximum Frame Length is 9216
IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is 4c1f-cc93-2025
Current system time: 2024-07-19 13:29:14-08:00
    Input bandwidth utilization  :    0%
    Output bandwidth utilization :    0%
-----------------------------------------------------
PortName                      Status      Weight
-----------------------------------------------------
GigabitEthernet0/0/23         UP          1
GigabitEthernet0/0/24         UP          1
-----------------------------------------------------
The Number of Ports in Trunk : 2
The Number of UP Ports in Trunk : 2

[lsw2-Eth-Trunk12]
```
# 配置vrrp抢占延时
```
vrrp vrid 1 preempt-mode timer delay 20
```