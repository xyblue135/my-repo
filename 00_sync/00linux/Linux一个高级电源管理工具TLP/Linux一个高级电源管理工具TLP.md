多年来，Linux 在电池优化方面取得了很大进步，但我们仍然需要做一些必要的事情来改善 Linux 中笔记本电脑的电池寿命。

# TLP
由于它的默认配置已针对电池寿命进行了优化，因此你可能只需要安装，然后就忘记它吧。 
TLP 是一个具有自动后台任务的纯命令行工具。它不包含GUI。
TLP 适用于各种品牌的笔记本电脑。设置电池充电阈值仅适用于 IBM/Lenovo ThinkPad。
```
sudo apt install tlp
# 查看所有信息
systemctl start tlp.service
sudo tlp-stat
```

```
查看特定信息
```

```
xyblue@xyblue-HP-Pavilion-Gaming-Laptop-15-dk1xxx:~sudo tlp-stat
--- TLP 1.3.1 --------------------------------------------

+++ Configured Settings:
defaults.conf L0004: TLP_ENABLE="1"
defaults.conf L0005: TLP_PERSISTENT_DEFAULT="0"
defaults.conf L0006: DISK_IDLE_SECS_ON_AC="0"
defaults.conf L0007: DISK_IDLE_SECS_ON_BAT="2"
defaults.conf L0008: MAX_LOST_WORK_SECS_ON_AC="15"
defaults.conf L0009: MAX_LOST_WORK_SECS_ON_BAT="60"
defaults.conf L0010: CPU_ENERGY_PERF_POLICY_ON_AC="balance_performance"
defaults.conf L0011: CPU_ENERGY_PERF_POLICY_ON_BAT="balance_power"
defaults.conf L0012: SCHED_POWERSAVE_ON_AC="0"
defaults.conf L0013: SCHED_POWERSAVE_ON_BAT="1"
defaults.conf L0014: NMI_WATCHDOG="0"
defaults.conf L0015: DISK_DEVICES="nvme0n1 sda"
defaults.conf L0016: DISK_APM_LEVEL_ON_AC="254 254"
defaults.conf L0017: DISK_APM_LEVEL_ON_BAT="128 128"
defaults.conf L0018: DISK_IOSCHED="keep keep"
defaults.conf L0019: SATA_LINKPWR_ON_AC="med_power_with_dipm max_performance"
defaults.conf L0020: SATA_LINKPWR_ON_BAT="med_power_with_dipm min_power"
defaults.conf L0021: AHCI_RUNTIME_PM_TIMEOUT="15"
defaults.conf L0022: PCIE_ASPM_ON_AC="default"
defaults.conf L0023: PCIE_ASPM_ON_BAT="default"
defaults.conf L0024: RADEON_POWER_PROFILE_ON_AC="default"
defaults.conf L0025: RADEON_POWER_PROFILE_ON_BAT="default"
defaults.conf L0026: RADEON_DPM_PERF_LEVEL_ON_AC="auto"
defaults.conf L0027: RADEON_DPM_PERF_LEVEL_ON_BAT="auto"
defaults.conf L0028: WIFI_PWR_ON_AC="off"
defaults.conf L0029: WIFI_PWR_ON_BAT="on"
defaults.conf L0030: WOL_DISABLE="Y"
defaults.conf L0031: SOUND_POWER_SAVE_ON_AC="0"
defaults.conf L0032: SOUND_POWER_SAVE_ON_BAT="1"
defaults.conf L0033: SOUND_POWER_SAVE_CONTROLLER="Y"
defaults.conf L0034: BAY_POWEROFF_ON_AC="0"
defaults.conf L0035: BAY_POWEROFF_ON_BAT="0"
defaults.conf L0036: BAY_DEVICE="sr0"
defaults.conf L0037: RUNTIME_PM_ON_AC="on"
defaults.conf L0038: RUNTIME_PM_ON_BAT="auto"
defaults.conf L0039: RUNTIME_PM_DRIVER_BLACKLIST="amdgpu mei_me nouveau nvidia pcieport radeon"
defaults.conf L0040: USB_AUTOSUSPEND="1"
defaults.conf L0041: USB_BLACKLIST_BTUSB="0"
defaults.conf L0042: USB_BLACKLIST_PHONE="0"
defaults.conf L0043: USB_BLACKLIST_PRINTER="1"
defaults.conf L0044: USB_BLACKLIST_WWAN="0"
defaults.conf L0045: USB_AUTOSUSPEND_DISABLE_ON_SHUTDOWN="0"
defaults.conf L0046: RESTORE_DEVICE_STATE_ON_STARTUP="0"
defaults.conf L0047: RESTORE_THRESHOLDS_ON_BAT="0"
defaults.conf L0048: NATACPI_ENABLE="1"
defaults.conf L0049: TPACPI_ENABLE="1"
defaults.conf L0050: TPSMAPI_ENABLE="1"

+++ System Info
System         = HP Type1ProductConfigId HP Pavilion Gaming Laptop 15-dk1xxx
BIOS           = F.46
Release        = Ubuntu 22.04.3 LTS
Kernel         = 6.2.0-26-generic #26~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Thu Jul 13 16:27:29 UTC 2 x86_64
/proc/cmdline  = BOOT_IMAGE=/boot/vmlinuz-6.2.0-26-generic root=UUID=071a80ac-e9be-4789-9bfa-3dd4c9277730 ro quiet splash vt.handoff=7
Init system    = systemd v249 (249.11-0ubuntu3.9)
Boot mode      = UEFI

+++ TLP Status
State          = enabled
RDW state      = enabled
Last run       = unknown
Mode           = unknown
Power source   = AC

+++ Processor
CPU model      = Intel(R) Core(TM) i5-10300H CPU @ 2.50GHz

/sys/devices/system/cpu/cpu0/cpufreq/scaling_driver    = intel_pstate
/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor  = powersave
/sys/devices/system/cpu/cpu0/cpufreq/scaling_available_governors = performance powersave
/sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq  =   800000 [kHz]
/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq  =  4500000 [kHz]
/sys/devices/system/cpu/cpu0/cpufreq/energy_performance_preference = balance_performance [HWP.EPP]
/sys/devices/system/cpu/cpu0/cpufreq/energy_performance_available_preferences = default performance balance_performance balance_power power 

/sys/devices/system/cpu/cpu1/cpufreq/scaling_driver    = intel_pstate
/sys/devices/system/cpu/cpu1/cpufreq/scaling_governor  = powersave
/sys/devices/system/cpu/cpu1/cpufreq/scaling_available_governors = performance powersave
/sys/devices/system/cpu/cpu1/cpufreq/scaling_min_freq  =   800000 [kHz]
/sys/devices/system/cpu/cpu1/cpufreq/scaling_max_freq  =  4500000 [kHz]
/sys/devices/system/cpu/cpu1/cpufreq/energy_performance_preference = balance_performance [HWP.EPP]
/sys/devices/system/cpu/cpu1/cpufreq/energy_performance_available_preferences = default performance balance_performance balance_power power 

/sys/devices/system/cpu/cpu2/cpufreq/scaling_driver    = intel_pstate
/sys/devices/system/cpu/cpu2/cpufreq/scaling_governor  = powersave
/sys/devices/system/cpu/cpu2/cpufreq/scaling_available_governors = performance powersave
/sys/devices/system/cpu/cpu2/cpufreq/scaling_min_freq  =   800000 [kHz]
/sys/devices/system/cpu/cpu2/cpufreq/scaling_max_freq  =  4500000 [kHz]
/sys/devices/system/cpu/cpu2/cpufreq/energy_performance_preference = balance_performance [HWP.EPP]
/sys/devices/system/cpu/cpu2/cpufreq/energy_performance_available_preferences = default performance balance_performance balance_power power 

/sys/devices/system/cpu/cpu3/cpufreq/scaling_driver    = intel_pstate
/sys/devices/system/cpu/cpu3/cpufreq/scaling_governor  = powersave
/sys/devices/system/cpu/cpu3/cpufreq/scaling_available_governors = performance powersave
/sys/devices/system/cpu/cpu3/cpufreq/scaling_min_freq  =   800000 [kHz]
/sys/devices/system/cpu/cpu3/cpufreq/scaling_max_freq  =  4500000 [kHz]
/sys/devices/system/cpu/cpu3/cpufreq/energy_performance_preference = balance_performance [HWP.EPP]
/sys/devices/system/cpu/cpu3/cpufreq/energy_performance_available_preferences = default performance balance_performance balance_power power 

/sys/devices/system/cpu/cpu4/cpufreq/scaling_driver    = intel_pstate
/sys/devices/system/cpu/cpu4/cpufreq/scaling_governor  = powersave
/sys/devices/system/cpu/cpu4/cpufreq/scaling_available_governors = performance powersave
/sys/devices/system/cpu/cpu4/cpufreq/scaling_min_freq  =   800000 [kHz]
/sys/devices/system/cpu/cpu4/cpufreq/scaling_max_freq  =  4500000 [kHz]
/sys/devices/system/cpu/cpu4/cpufreq/energy_performance_preference = balance_performance [HWP.EPP]
/sys/devices/system/cpu/cpu4/cpufreq/energy_performance_available_preferences = default performance balance_performance balance_power power 

/sys/devices/system/cpu/cpu5/cpufreq/scaling_driver    = intel_pstate
/sys/devices/system/cpu/cpu5/cpufreq/scaling_governor  = powersave
/sys/devices/system/cpu/cpu5/cpufreq/scaling_available_governors = performance powersave
/sys/devices/system/cpu/cpu5/cpufreq/scaling_min_freq  =   800000 [kHz]
/sys/devices/system/cpu/cpu5/cpufreq/scaling_max_freq  =  4500000 [kHz]
/sys/devices/system/cpu/cpu5/cpufreq/energy_performance_preference = balance_performance [HWP.EPP]
/sys/devices/system/cpu/cpu5/cpufreq/energy_performance_available_preferences = default performance balance_performance balance_power power 

/sys/devices/system/cpu/cpu6/cpufreq/scaling_driver    = intel_pstate
/sys/devices/system/cpu/cpu6/cpufreq/scaling_governor  = powersave
/sys/devices/system/cpu/cpu6/cpufreq/scaling_available_governors = performance powersave
/sys/devices/system/cpu/cpu6/cpufreq/scaling_min_freq  =   800000 [kHz]
/sys/devices/system/cpu/cpu6/cpufreq/scaling_max_freq  =  4500000 [kHz]
/sys/devices/system/cpu/cpu6/cpufreq/energy_performance_preference = balance_performance [HWP.EPP]
/sys/devices/system/cpu/cpu6/cpufreq/energy_performance_available_preferences = default performance balance_performance balance_power power 

/sys/devices/system/cpu/cpu7/cpufreq/scaling_driver    = intel_pstate
/sys/devices/system/cpu/cpu7/cpufreq/scaling_governor  = powersave
/sys/devices/system/cpu/cpu7/cpufreq/scaling_available_governors = performance powersave
/sys/devices/system/cpu/cpu7/cpufreq/scaling_min_freq  =   800000 [kHz]
/sys/devices/system/cpu/cpu7/cpufreq/scaling_max_freq  =  4500000 [kHz]
/sys/devices/system/cpu/cpu7/cpufreq/energy_performance_preference = balance_performance [HWP.EPP]
/sys/devices/system/cpu/cpu7/cpufreq/energy_performance_available_preferences = default performance balance_performance balance_power power 

/sys/devices/system/cpu/intel_pstate/min_perf_pct      =  17 [%]
/sys/devices/system/cpu/intel_pstate/max_perf_pct      = 100 [%]
/sys/devices/system/cpu/intel_pstate/no_turbo          =   0
/sys/devices/system/cpu/intel_pstate/turbo_pct         =  53 [%]
/sys/devices/system/cpu/intel_pstate/num_pstates       =  38

/sys/module/workqueue/parameters/power_efficient       = Y
/proc/sys/kernel/nmi_watchdog                          = 1

+++ Temperatures
CPU temp               =    45 [°C]
Fan speed (fan1)       =     0 [/min]
Fan speed (fan2)       =     0 [/min]

+++ File System
/proc/sys/vm/laptop_mode               =     0
/proc/sys/vm/dirty_writeback_centisecs =   500
/proc/sys/vm/dirty_expire_centisecs    =  3000
/proc/sys/vm/dirty_ratio               =    20
/proc/sys/vm/dirty_background_ratio    =    10

+++ Storage Devices
Devices = nvme0n1 sda

/dev/nvme0n1:
  Type      = NVMe
  Model     = Fanxiang S500PRO 256GB                  
  Firmware  = SN10093 
  Scheduler = [none] mq-deadline (multi queue)

  Runtime PM: control = auto, autosuspend_delay_ms = (not available)

/dev/sda: not present.

+++ AHCI Link Power Management (ALPM)
/sys/class/scsi_host/host0/link_power_management_policy  = max_performance

+++ AHCI Host Controller Runtime Power Management
/sys/bus/pci/devices/0000:00:17.0/ata1/power/control = on

+++ Docks and Device Bays
/sys/devices/platform/dock.0: dock_station  = undocked

+++ Intel Graphics
/sys/module/i915/parameters/enable_dc        = -1 (use per-chip default)
/sys/module/i915/parameters/enable_fbc       = -1 (use per-chip default)
/sys/module/i915/parameters/enable_psr       = -1 (use per-chip default)
/sys/module/i915/parameters/modeset          = -1 (use per-chip default)

/sys/class/drm/card1/gt_min_freq_mhz         =   350 [MHz]
/sys/class/drm/card1/gt_max_freq_mhz         =  1050 [MHz]
/sys/class/drm/card1/gt_boost_freq_mhz       =  1050 [MHz]

+++ Wireless
bluetooth = on
wifi      = off (software)
wwan      = none (no device)

hci0(btusb)                   : bluetooth, not connected
wlo1(iwlwifi)                 : wifi, not connected, power management = on

+++ Audio
/sys/module/snd_hda_intel/parameters/power_save            = 1
/sys/module/snd_hda_intel/parameters/power_save_controller = Y

+++ PCIe Active State Power Management
/sys/module/pcie_aspm/parameters/policy = [default] performance powersave powersupersave (using BIOS preferences)

+++ Runtime Power Management
Device blacklist = (not configured)
Driver blacklist = amdgpu mei_me nouveau nvidia pcieport radeon

/sys/bus/pci/devices/0000:00:00.0/power/control = on   (0x060000, Host bridge, skl_uncore)
/sys/bus/pci/devices/0000:00:01.0/power/control = auto (0x060400, PCI bridge, pcieport)
/sys/bus/pci/devices/0000:00:02.0/power/control = auto (0x030000, VGA compatible controller, i915)
/sys/bus/pci/devices/0000:00:04.0/power/control = auto (0x118000, Signal processing controller, proc_thermal)
/sys/bus/pci/devices/0000:00:08.0/power/control = auto (0x088000, System peripheral, no driver)
/sys/bus/pci/devices/0000:00:12.0/power/control = on   (0x118000, Signal processing controller, intel_pch_thermal)
/sys/bus/pci/devices/0000:00:14.0/power/control = on   (0x0c0330, USB controller, xhci_hcd)
/sys/bus/pci/devices/0000:00:14.2/power/control = on   (0x050000, RAM memory, no driver)
/sys/bus/pci/devices/0000:00:14.3/power/control = on   (0x028000, Network controller, iwlwifi)
/sys/bus/pci/devices/0000:00:15.0/power/control = auto (0x0c8000, Serial bus controller, intel-lpss)
/sys/bus/pci/devices/0000:00:15.1/power/control = auto (0x0c8000, Serial bus controller, intel-lpss)
/sys/bus/pci/devices/0000:00:16.0/power/control = auto (0x078000, Communication controller, mei_me)
/sys/bus/pci/devices/0000:00:17.0/power/control = on   (0x010400, RAID bus controller, ahci)
/sys/bus/pci/devices/0000:00:1d.0/power/control = auto (0x060400, PCI bridge, pcieport)
/sys/bus/pci/devices/0000:00:1d.5/power/control = auto (0x060400, PCI bridge, pcieport)
/sys/bus/pci/devices/0000:00:1d.6/power/control = auto (0x060400, PCI bridge, pcieport)
/sys/bus/pci/devices/0000:00:1f.0/power/control = on   (0x060100, ISA bridge, no driver)
/sys/bus/pci/devices/0000:00:1f.3/power/control = auto (0x040300, Audio device, snd_hda_intel)
/sys/bus/pci/devices/0000:00:1f.4/power/control = auto (0x0c0500, SMBus, i801_smbus)
/sys/bus/pci/devices/0000:00:1f.5/power/control = on   (0x0c8000, Serial bus controller, intel-spi)
/sys/bus/pci/devices/0000:01:00.0/power/control = auto (0x030000, VGA compatible controller, nouveau)
/sys/bus/pci/devices/0000:01:00.1/power/control = auto (0x040300, Audio device, snd_hda_intel)
/sys/bus/pci/devices/0000:06:00.0/power/control = on   (0x010802, Non-Volatile memory controller, nvme)
/sys/bus/pci/devices/0000:07:00.0/power/control = on   (0x020000, Ethernet controller, r8169)
/sys/bus/pci/devices/0000:08:00.0/power/control = on   (0xff0000, Unassigned class [ff00], alcor_pci)

+++ USB
Autosuspend         = enabled
Device whitelist    = (not configured)
Device blacklist    = (not configured)
Bluetooth blacklist = disabled
Phone blacklist     = disabled
WWAN blacklist      = disabled

Bus 002 Device 001 ID 1d6b:0003 control = auto, autosuspend_delay_ms =    0 -- Linux Foundation 3.0 root hub (hub)
Bus 001 Device 003 ID 04ca:707f control = auto, autosuspend_delay_ms = 2000 -- Lite-On Technology Corp. HP Wide Vision HD Camera (uvcvideo)
Bus 001 Device 002 ID 1ea7:0064 control = on,   autosuspend_delay_ms = 2000 -- SHARKOON Technologies GmbH 2.4GHz Wireless rechargeable vertical mouse [More&Better] (usbhid)
Bus 001 Device 004 ID 8087:0026 control = auto, autosuspend_delay_ms = 2000 -- Intel Corp. AX201 Bluetooth (btusb)
Bus 001 Device 001 ID 1d6b:0002 control = auto, autosuspend_delay_ms =    0 -- Linux Foundation 2.0 root hub (hub)

+++ Battery Features: Charge Thresholds and Recalibrate
natacpi    = inactive (laptop not supported)
tpacpi-bat = inactive (laptop not supported)
tp-smapi   = inactive (laptop not supported)

+++ Battery Status: BAT1
/sys/class/power_supply/BAT1/manufacturer                   = Hewlett-Packard 
/sys/class/power_supply/BAT1/model_name                     = PABAS0241231
/sys/class/power_supply/BAT1/cycle_count                    = (not supported)
/sys/class/power_supply/BAT1/energy_full_design             =  52500 [mWh]
/sys/class/power_supply/BAT1/energy_full                    =  39410 [mWh]
/sys/class/power_supply/BAT1/energy_now                     =  40370 [mWh]
/sys/class/power_supply/BAT1/power_now                      = (not available) 
/sys/class/power_supply/BAT1/status                         = Not charging

Charge                                                      =  102.4 [%]
Capacity                                                    =   75.1 [%]

+++ Recommendations
* Install smartmontools for disk drive health info
```
# TLP功能
- 内核笔记本电脑模式和脏缓冲区超时
- 处理器频率调整，包括 “turbo boost”/“turbo core”
- 限制最大/最小的 P 状态以控制 CPU 的功耗
- HWP 能源性能提示
- 用于多核/超线程的功率感知进程调度程序
- 处理器性能与节能策略（`x86_energy_perf_policy`）
- 硬盘高级电源管理级别（APM）和降速超时（按磁盘）
- AHCI 链路电源管理（ALPM）与设备黑名单
- PCIe 活动状态电源管理（PCIe ASPM）
- PCI(e) 总线设备的运行时电源管理
- Radeon 图形电源管理（KMS 和 DPM）
- Wifi 省电模式
- 关闭驱动器托架中的光盘驱动器
- 音频省电模式
- I/O 调度程序（按磁盘）
- USB 自动暂停，支持设备黑名单/白名单（输入设备自动排除）
- 在系统启动和关闭时启用或禁用集成的 wifi、蓝牙或 wwan 设备
- 在系统启动时恢复无线电设备状态（从之前的关机时的状态）
- 无线电设备向导：在网络连接/断开和停靠/取消停靠时切换无线电
- 禁用 LAN 唤醒
- 挂起/休眠后恢复集成的 WWAN 和蓝牙状态
- 英特尔处理器的动态电源降低 —— 需要内核和 PHC-Patch 支持
- 电池充电阈值 —— 仅限 ThinkPad
- 重新校准电池 —— 仅限 ThinkPad
# 具体TLP显示
## 电池
sudo tlp-stat -b
sudo tlp-stat --battery
## 磁盘
sudo tlp-stat -d
sudo tlp-stat --disk
## PCI
sudo tlp-stat -e
sudo tlp-stat --pcie
## 图形卡
sudo tlp-stat -g
sudo tlp-stat --graphics
## 处理器
sudo tlp-stat -p
sudo tlp-stat --processor
## 系统数据
sudo tlp-stat -s
sudo tlp-stat --system
## 显示温度和风扇速度信息
但是感觉不如sensors好用
sudo tlp-stat -t
sudo tlp-stat --temp
## 显示 USB 设备数据信息
sudo tlp-stat -u
sudo tlp-stat --usb
# 显示告警
sudo tlp-stat -w
sudo tlp-stat --warn

