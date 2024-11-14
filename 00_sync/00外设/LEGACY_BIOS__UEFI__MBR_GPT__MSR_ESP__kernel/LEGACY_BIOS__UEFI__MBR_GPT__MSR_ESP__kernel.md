# F11
## LEGACY_BIOS
LEGACY BIOS:（BASIC INPUT OUPUT SYSTEM传统基本输入输出系统）自检、基本硬件驱动，启动引导操作系统
早些年,按下开机键,最先进入的为BIOS界面,即下图所示.
![image-202312173146150.png](00_sync/00外设/LEGACY_BIOS__UEFI__MBR_GPT__MSR_ESP__kernel/LEGACY_BIOS__UEFI__MBR_GPT__MSR_ESP__kernel/image-202312173146150.png)
而对应的文件格式为下图.
![image-2023121729229.png](00_sync/00外设/LEGACY_BIOS__UEFI__MBR_GPT__MSR_ESP__kernel/LEGACY_BIOS__UEFI__MBR_GPT__MSR_ESP__kernel/image-2023121729229.png)
当计算机启动时，BIOS 将按照预设的引导设备顺序逐一检查，直到找到一个可引导的设备或分区。然后，BIOS 将加载该设备或分区上的引导加载程序（例如，MBR 或引导扇区），并执行其中的引导代码，从而引导启动操作系统。
## UEFI
UEFI（Unified Extensive Fireware Interface统一的可扩展固件接口）:向下兼容BIOS，并且能可视化操作更加友好，界面丰富；跳过Bios自 检，启动更快
![image-20231217448252.png](00_sync/00外设/LEGACY_BIOS__UEFI__MBR_GPT__MSR_ESP__kernel/LEGACY_BIOS__UEFI__MBR_GPT__MSR_ESP__kernel/image-20231217448252.png)
![image-202312172914133.png|475](00_sync/00外设/LEGACY_BIOS__UEFI__MBR_GPT__MSR_ESP__kernel/LEGACY_BIOS__UEFI__MBR_GPT__MSR_ESP__kernel/image-202312172914133.png)
## 区别
![image-202312173719282.png|425](00_sync/00外设/LEGACY_BIOS__UEFI__MBR_GPT__MSR_ESP__kernel/LEGACY_BIOS__UEFI__MBR_GPT__MSR_ESP__kernel/image-202312173719282.png)
# 分区表
分区表（Partition Table）是硬盘上用于记录和管理分区信息的数据结构。它包含了硬盘上所有分区的位置、大小、类型等信息，使操作系统能够识别和访问这些分区。
常见的分区表类型有以下几种：
## **MBR msdos（Master Boot Record）分区表**：
- MBR 是传统的分区表格式，适用于大多数早期和一些较老的计算机系统。它使用 32 位的地址空间，最多支持 4 个主分区或 3 个主分区和一个扩展分区。
- MBR 分区表的限制包括每个分区最大支持 2TB 大小、只能有 4 个主分区（其中一个可以是扩展分区），以及对于较大容量硬盘的不足支持等问题。
## **GPT GUID（GUID Partition Table）分区表**：
- GPT 是现代计算机系统使用的分区表格式，通常与 UEFI（统一可扩展固件接口）一起使用。它采用全局唯一标识符（GUID）来标识分区，支持更大容量的硬盘和更多分区。
- GPT 分区表最大支持 128 个分区（不包括保留分区），每个分区大小可以达到数EB（exabytes），并且提供了更多的数据冗余和恢复功能。

绑定
对于分区表来说,他们常常与启动方式绑定在一起,如Legacy(BIOS)和MBR,以及UEFI和GPT.但因为UEFI是可以向下兼容的,所以UEFI(EFI)的启动方式可以和MBR分区表一起使用.但BIOS不可以和GPT一起使用.

# 分区名/文件系统
## BIOS引导分区
  
传统 BIOS 引导通常使用 MBR（Master Boot Record）分区表格式。在这种情况下，BIOS 引导分区（通常是活动分区）上的引导加载程序和相关文件可能使用 FAT32 文件系统，但并非必须。
在传统 BIOS 引导情况下，引导加载程序通常存储在硬盘的 MBR 区域或者引导扇区上。这个区域通常较小（仅占几个扇区），因此可能使用 FAT32 格式来容纳引导加载程序和相关的引导文件，因为 FAT32 文件系统对于小容量的分区来说是比较适合的选择。
![image-202312175933389.png](00_sync/00外设/LEGACY_BIOS__UEFI__MBR_GPT__MSR_ESP__kernel/LEGACY_BIOS__UEFI__MBR_GPT__MSR_ESP__kernel/image-202312175933389.png)
## UEFI引导分区:
### **MSR（Microsoft Reserved Partition）**：

- MSR 是为 Microsoft Windows 操作系统保留的分区，通常是 GPT（GUID Partition Table）分区表结构中的一部分。
- 在 GPT 分区表中，MSR 是一个较小的隐藏分区，用于存储 Windows 操作系统或其他 Microsoft 产品的特定数据。这个分区通常不会被显示为可见分区，也不会包含用户数据，而是被系统用于一些特定的操作或存储需求。
![image-202312174816584.png](00_sync/00外设/LEGACY_BIOS__UEFI__MBR_GPT__MSR_ESP__kernel/LEGACY_BIOS__UEFI__MBR_GPT__MSR_ESP__kernel/image-202312174816584.png)
### ESP(分区名)FAT32(文件系统)
ESP（EFI System Partition）并不是一个文件系统的名称，而是一个特殊的分区，用于存储与计算机启动相关的文件。
在使用 UEFI（统一可扩展固件接口）的计算机系统中，ESP 是一个必需的分区，它包含用于启动操作系统的引导加载程序（如 GRUB、Windows Boot Manager 等）和其他与引导相关的文件。
ESP 分区通常被格式化为 FAT32 文件系统，因为 FAT32 在不同操作系统之间具有良好的兼容性，可以轻松地在各种系统上读取和写入。这个分区在 UEFI 启动过程中起着重要的作用，操作系统的引导加载程序和其他启动文件存储在这里，使得计算机能够正确地引导和启动操作系统。

## linux
Linux 发行版通常可以适应两种引导方式，并且可以在传统 BIOS 或 UEFI 下运行。现代的 Linux 发行版通常支持 UEFI 引导，并且能够充分利用 UEFI 提供的功能。
![image-202312175537611.png](00_sync/00外设/LEGACY_BIOS__UEFI__MBR_GPT__MSR_ESP__kernel/LEGACY_BIOS__UEFI__MBR_GPT__MSR_ESP__kernel/image-202312175537611.png)
![image-202312175446113.png](00_sync/00外设/LEGACY_BIOS__UEFI__MBR_GPT__MSR_ESP__kernel/LEGACY_BIOS__UEFI__MBR_GPT__MSR_ESP__kernel/image-202312175446113.png)