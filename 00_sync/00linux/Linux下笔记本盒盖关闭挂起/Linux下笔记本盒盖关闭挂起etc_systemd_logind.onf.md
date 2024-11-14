`cat /etc/systemd/logind.conf`
```
root@xybluelinux:~# cat /etc/systemd/logind.conf
#  This file is part of systemd.
#
#  systemd is free software; you can redistribute it and/or modify it under the
#  terms of the GNU Lesser General Public License as published by the Free
#  Software Foundation; either version 2.1 of the License, or (at your option)
#  any later version.
#
# Entries in this file show the compile time defaults. Local configuration
# should be created by either modifying this file (or a copy of it placed in
# /etc/ if the original file is shipped in /usr/), or by creating "drop-ins" in
# the /etc/systemd/logind.conf.d/ directory. The latter is generally
# recommended. Defaults can be restored by simply deleting the main
# configuration file and all drop-ins located in /etc/.
#
# Use 'systemd-analyze cat-config systemd/logind.conf' to display the full config.
#
# See logind.conf(5) for details.

[Login]
#NAutoVTs=6
#ReserveVT=6
#KillUserProcesses=no
#KillOnlyUsers=
#KillExcludeUsers=root
#InhibitDelayMaxSec=5
#UserStopDelaySec=10
#HandlePowerKey=poweroff
#HandlePowerKeyLongPress=ignore
#HandleRebootKey=reboot
#HandleRebootKeyLongPress=poweroff
#HandleSuspendKey=suspend
#HandleSuspendKeyLongPress=hibernate
#HandleHibernateKey=hibernate
#HandleHibernateKeyLongPress=ignore
#HandleLidSwitch=suspend
#HandleLidSwitchExternalPower=suspend
#HandleLidSwitchDocked=ignore
#PowerKeyIgnoreInhibited=no
#SuspendKeyIgnoreInhibited=no
#HibernateKeyIgnoreInhibited=no
#LidSwitchIgnoreInhibited=yes
#RebootKeyIgnoreInhibited=no
#HoldoffTimeoutSec=30s
#IdleAction=ignore
#IdleActionSec=30min
#RuntimeDirectorySize=10%
#RuntimeDirectoryInodesMax=
#RemoveIPC=yes
#InhibitorsMax=8192
#SessionsMax=8192
#StopIdleSessionSec=infinity
root@xybluelinux:~# 
```

```
1. **NAutoVTs**:
    
    - 默认值：6
    - 说明：自动创建的虚拟终端的数量。虚拟终端是文本模式下的登录界面，通常从 tty1 到 tty6。
2. **ReserveVT**:
    
    - 默认值：6
    - 说明：保留的虚拟终端编号。这个虚拟终端不会被自动分配给用户登录，而是留给系统管理员使用。
3. **KillUserProcesses**:
    
    - 默认值：no
    - 说明：当用户注销时，是否终止该用户的所有进程。如果设置为 `yes`，则用户注销时会终止其所有进程。
4. **KillOnlyUsers**:
    
    - 默认值：空
    - 说明：指定哪些用户的进程在注销时会被终止。可以是一个逗号分隔的用户名列表。
5. **KillExcludeUsers**:
    
    - 默认值：root
    - 说明：指定哪些用户的进程在注销时不会被终止。可以是一个逗号分隔的用户名列表。
6. **InhibitDelayMaxSec**:
    
    - 默认值：5
    - 说明：最大延迟时间（秒），在执行关机、重启等操作前等待的时间，以防止意外操作。
7. **UserStopDelaySec**:
    
    - 默认值：10
    - 说明：用户注销后，系统等待多少秒后再终止该用户的进程。
8. **HandlePowerKey**:
    
    - 默认值：poweroff
    - 说明：按下电源键时的行为。可以是 `poweroff`（关机）、`reboot`（重启）、`suspend`（休眠）、`hibernate`（休眠）或 `ignore`（忽略）。
9. **HandlePowerKeyLongPress**:
    
    - 默认值：ignore
    - 说明：长时间按下电源键时的行为。可以是 `poweroff`、`reboot`、`suspend`、`hibernate` 或 `ignore`。
10. **HandleRebootKey**:
    
    - 默认值：reboot
    - 说明：按下重启键时的行为。可以是 `reboot`、`poweroff`、`suspend`、`hibernate` 或 `ignore`。
11. **HandleRebootKeyLongPress**:
    
    - 默认值：poweroff
    - 说明：长时间按下重启键时的行为。可以是 `reboot`、`poweroff`、`suspend`、`hibernate` 或 `ignore`。
12. **HandleSuspendKey**:
    
    - 默认值：suspend
    - 说明：按下休眠键时的行为。可以是 `suspend`、`hibernate`、`poweroff`、`reboot` 或 `ignore`。
13. **HandleSuspendKeyLongPress**:
    
    - 默认值：hibernate
    - 说明：长时间按下休眠键时的行为。可以是 `suspend`、`hibernate`、`poweroff`、`reboot` 或 `ignore`。
14. **HandleHibernateKey**:
    
    - 默认值：hibernate
    - 说明：按下休眠键时的行为。可以是 `hibernate`、`suspend`、`poweroff`、`reboot` 或 `ignore`。
15. **HandleHibernateKeyLongPress**:
    
    - 默认值：ignore
    - 说明：长时间按下休眠键时的行为。可以是 `hibernate`、`suspend`、`poweroff`、`reboot` 或 `ignore`。
16. **HandleLidSwitch**:
    
    - 默认值：suspend
    - 说明：合上笔记本盖子时的行为。可以是 `suspend`、`hibernate`、`poweroff`、`reboot` 或 `ignore`。
17. **HandleLidSwitchExternalPower**:
    
    - 默认值：suspend
    - 说明：在外部电源供电时合上笔记本盖子的行为。可以是 `suspend`、`hibernate`、`poweroff`、`reboot` 或 `ignore`。
18. **HandleLidSwitchDocked**:
    
    - 默认值：ignore
    - 说明：在对接状态下合上笔记本盖子的行为。可以是 `suspend`、`hibernate`、`poweroff`、`reboot` 或 `ignore`。
19. **PowerKeyIgnoreInhibited**:
    
    - 默认值：no
    - 说明：是否忽略由其他进程抑制的电源键事件。如果设置为 `yes`，则即使有其他进程抑制，电源键事件也会被处理。
20. **SuspendKeyIgnoreInhibited**:
    
    - 默认值：no
    - 说明：是否忽略由其他进程抑制的休眠键事件。如果设置为 `yes`，则即使有其他进程抑制，休眠键事件也会被处理。
21. **HibernateKeyIgnoreInhibited**:
    
    - 默认值：no
    - 说明：是否忽略由其他进程抑制的休眠键事件。如果设置为 `yes`，则即使有其他进程抑制，休眠键事件也会被处理。
22. **LidSwitchIgnoreInhibited**:
    
    - 默认值：yes
    - 说明：是否忽略由其他进程抑制的笔记本盖子事件。如果设置为 `yes`，则即使有其他进程抑制，笔记本盖子事件也会被处理。
23. **RebootKeyIgnoreInhibited**:
    
    - 默认值：no
    - 说明：是否忽略由其他进程抑制的重启键事件。如果设置为 `yes`，则即使有其他进程抑制，重启键事件也会被处理。
24. **HoldoffTimeoutSec**:
    
    - 默认值：30s
    - 说明：在执行关机、重启等操作前等待的时间（秒），以防止意外操作。
25. **IdleAction**:
    
    - 默认值：ignore
    - 说明：系统空闲时的行为。可以是 `ignore`（忽略）、`suspend`（休眠）、`hibernate`（休眠）、`poweroff`（关机）或 `reboot`（重启）。
26. **IdleActionSec**:
    
    - 默认值：30min
    - 说明：系统空闲多久后触发 `IdleAction` 行为。
27. **RuntimeDirectorySize**:
    
    - 默认值：10%
    - 说明：运行时目录的最大大小，占根文件系统的百分比。
28. **RuntimeDirectoryInodesMax**:
    
    - 默认值：空
    - 说明：运行时目录中允许的最大 inode 数量。
29. **RemoveIPC**:
    
    - 默认值：yes
    - 说明：用户注销时是否删除其 IPC（进程间通信）对象。
30. **InhibitorsMax**:
    
    - 默认值：8192
    - 说明：允许的最大抑制器数量。
31. **SessionsMax**:
    
    - 默认值：8192
    - 说明：允许的最大会话数量。
32. **StopIdleSessionSec**:
    
    - 默认值：infinity
    - 说明：系统空闲会话在多长时间后被停止。
```

我们要用这个
```
HandleLidSwitch:
默认值：suspend
说明：合上笔记本盖子时的行为。可以是 suspend、hibernate、poweroff、reboot 或 ignore。
HandleLidSwitchExternalPower:
改为
```

更新配置
```
sudo systemctl restart systemd-logind
systemctl status systemd-logind
```

#  问题
![image-2024118542760.png](00_sync/00linux/Linux%E4%B8%8B%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%9B%92%E7%9B%96%E5%85%B3%E9%97%AD%E6%8C%82%E8%B5%B7/Linux%E4%B8%8B%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%9B%92%E7%9B%96%E5%85%B3%E9%97%AD%E6%8C%82%E8%B5%B7etc_systemd_logind.onf/image-2024118542760.png)
貌似笔记本合盖子不让关机