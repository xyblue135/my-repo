```
runlevel
```
上一次用户的级别
```
$ runlevel
N 3
```
更改用户级别
```
sudo telinit 3
```
![image-202410312823829.png|525](00_sync/00linux/Linux%E4%B8%8B%E7%9A%84%E8%A7%86%E5%9B%BE%E7%94%A8%E6%88%B7%E7%BA%A7%E5%88%AB/Linux%E4%B8%8B%E7%9A%84%E8%A7%86%E5%9B%BE%E7%94%A8%E6%88%B7%E7%BA%A7%E5%88%AB/image-202410312823829.png)
- **0**：关机状态。
- **1**：单用户模式，通常用于系统维护。
- **2**：多用户模式，没有NFS（网络文件系统）服务。
- **3**：多用户模式，带有网络支持，通常是没有图形界面的命令行模式。
- **4**：保留，通常未使用，可以自定义。
- **5**：图形化界面模式，带有显示管理器（如GDM、KDM、LightDM等）。
- **6**：重启系统。
## 决定是否待机
```
cat /etc/systemd/logind.conf
```
![image-202410313356370.png|425](00_sync/00linux/Linux%E4%B8%8B%E7%9A%84%E8%A7%86%E5%9B%BE%E7%94%A8%E6%88%B7%E7%BA%A7%E5%88%AB/Linux%E4%B8%8B%E7%9A%84%E8%A7%86%E5%9B%BE%E7%94%A8%E6%88%B7%E7%BA%A7%E5%88%AB/image-202410313356370.png)
```
root@xyblue-HP-Pavilion-Gaming-Laptop-15-dk1xxx:/etc/systemd# cat logind.conf 
[Login]
# NAutoVTs=6  # 自动创建的虚拟终端数量（默认：6）
# ReserveVT=6  # 为系统保留的虚拟终端（默认：6）
# KillUserProcesses=no  # 登出时是否杀死用户进程（默认：否）
# KillOnlyUsers=  # 指定在登出时应杀死的用户
# KillExcludeUsers=root  # 在登出时不应杀死的用户（默认：root）
# InhibitDelayMaxSec=5  # 禁用操作的最大延迟时间（默认：5秒）
# UserStopDelaySec=10  # 停止用户进程前的延迟时间（默认：10秒）
# HandlePowerKey=poweroff  # 按下电源键时采取的操作（默认：关机）
# HandleSuspendKey=suspend  # 按下挂起键时采取的操作（默认：挂起）
# HandleHibernateKey=hibernate  # 按下休眠键时采取的操作（默认：休眠）
# HandleLidSwitch=suspend  # 关闭盖子时采取的操作（默认：挂起）
# HandleLidSwitchExternalPower=suspend  # 关闭盖子时外接电源的操作（默认：挂起）
# HandleLidSwitchDocked=ignore  # 底座状态下关闭盖子的操作（默认：忽略）
# HandleRebootKey=reboot  # 按下重启键时采取的操作（默认：重启）
# PowerKeyIgnoreInhibited=no  # 处理电源键时是否忽略禁用状态（默认：否）
# SuspendKeyIgnoreInhibited=no  # 处理挂起键时是否忽略禁用状态（默认：否）
# HibernateKeyIgnoreInhibited=no  # 处理休眠键时是否忽略禁用状态（默认：否）
# LidSwitchIgnoreInhibited=yes  # 处理盖子开关时是否忽略禁用状态（默认：是）
# RebootKeyIgnoreInhibited=no  # 处理重启键时是否忽略禁用状态（默认：否）
# HoldoffTimeoutSec=30s  # 用户输入后采取行动的超时时间（默认：30秒）
# IdleAction=ignore  # 系统闲置时采取的操作（默认：忽略）
# IdleActionSec=30min  # 触发闲置操作的时间（默认：30分钟）
# RuntimeDirectorySize=10%  # 运行时目录的最大大小（默认：10%）
# RuntimeDirectoryInodesMax=400k  # 运行时目录的最大inode数量（默认：400,000）
# RemoveIPC=yes  # 关闭时是否删除IPC（进程间通信）对象（默认：是）
# InhibitorsMax=8192  # 允许的最大抑制器数量（默认：8192）
# SessionsMax=8192  # 允许的最大用户会话数量（默认：8192）
```


在 `logind.conf` 中，以下设置与控制息屏（屏幕关闭或休眠）相关：
1. **HandleLidSwitch**：关闭盖子时采取的操作。
    - 默认值：`suspend`（挂起）
2. **HandleLidSwitchExternalPower**：在外接电源情况下，关闭盖子时采取的操作。
    - 默认值：`suspend`（挂起）
3. **HandleLidSwitchDocked**：底座状态下，关闭盖子时采取的操作。
    - 默认值：`ignore`（忽略）
4. **IdleAction**：系统闲置时采取的操作。
    - 默认值：`ignore`（忽略）
5. **IdleActionSec**：触发闲置操作的时间。
    - 默认值：`30min`（30分钟）
所以我们要限制息屏需要改两个东西
```
# IdleAction=ignore  # 系统闲置时采取的操作（默认：忽略）
# IdleActionSec=30min  # 触发闲置操作的时间（默认：30分钟）

IdleAction=suspend  # 系统闲置时挂起
IdleActionSec=1min  # 30分钟后触发挂起
```
## 重启服务
```
sudo systemctl restart systemd-logind
systemctl status systemd-logind
```
# 无图形化息屏
找了好多办法都没法解决，只能针对屏幕亮度去解决了
```
ls /sys/class/backlight/
看当前亮度
cat /sys/class/backlight/intel_backlight/brightness

看最大亮度
cat /sys/class/backlight/intel_backlight/max_brightness

echo 0 > /sys/class/backlight/intel_backlight/brightness
echo 最大亮度 > /sys/class/backlight/intel_backlight/brightness

```
# 关闭笔记本盖子
```
cat /etc/systemd/logind.conf
```

```
# HandleLidSwitch=suspend  # 关闭盖子时采取的操作（默认：挂起）
改为
# HandleLidSwitch=ignore  # 关闭盖子时采取的操作（默认：挂起）
```

# 图形化的息屏
```
which xset
如果没有，可以安装
sudo apt install x11-xserver-utils
```
息屏 待机 屏幕背光
```
xset dpms 30 0 30
```

# 附件
## logind.conf参数
0. **`suspend`**：
待机 挂起

1. **`ignore`**：
    - 不执行任何操作，即忽略盖子关闭事件。
    - 适用于需要保持系统活跃的情况，例如远程连接或进行长时间的任务。
2. **`hibernate`**：
    - 将当前内存状态保存到磁盘，并关闭系统。
    - 适用于需要节省电力的情况，但恢复速度相对较慢。
3. **`hybrid-sleep`**：
    - 将当前内存状态保存到磁盘，并进入待机状态（同时保持内存供电）。
    - 结合了`suspend`和`hibernate`的优点，既能快速唤醒又能节省电力。
4. **`lock`**：
    - 锁定屏幕，但不执行任何电源操作。
    - 适用于需要暂时离开但不想关闭屏幕的情况。
5. **`nothing`**：
    - 相当于`ignore`，不执行任何操作。
6. **`poweroff`**：
    - 关闭系统电源。
    - 适用于不需要保持系统运行的情况。
7. **`reboot`**：
    - 重新启动系统。
    - 这种设置较少使用，因为通常不会因为关闭盖子而需要重启系统。