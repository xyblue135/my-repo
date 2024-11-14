# 改静态
## netplan【个人推荐】
Ubuntu 18.04 及以后版本使用 `Netplan` 来配置网络。Netplan 是一个用 YAML 格式管理网络配置的工具。配置文件通常位于 `/etc/netplan/` 目录下。
假设你要给接口 `enp3s0` 配置静态 IP 地址或动态 IP（DHCP）。
cd /etc/netplan
sudo nano /etc/netplan/01-netcfg.yaml
![image-20241025248620.png](00_sync/00linux/%E8%AE%BE%E7%BD%AE%E7%BD%91%E5%8D%A1%E4%B8%BA%E9%9D%99%E6%80%81ip%E5%92%8C%E6%9F%A5%E7%9C%8Bmac/%E8%AE%BE%E7%BD%AE%E7%BD%91%E5%8D%A1%E4%B8%BA%E9%9D%99%E6%80%81ip%E5%92%8C%E6%9F%A5%E7%9C%8Bmac/image-20241025248620.png)
```
network:
  version: 2
  renderer: networkd
  ethernets:
    eno1:
      dhcp4: true
```

```
network:
  version: 2
  renderer: NetworkManager
  ethernets:
    eno1:
      dhcp4: no
      addresses:
        - 192.168.3.101/24
      routes:
        - to: default
          via: 192.168.3.1
      nameservers:
        addresses:
          - 8.8.8.8
          - 8.8.4.4
```
模版dhcp ，改注释为静态
```
network:
  version: 2
  renderer: NetworkManager
  ethernets:
    eno1:
      # 注释掉静态 IP 地址配置
      # addresses:
      #   - 192.168.3.101/24
      # 注释掉静态路由配置
      # routes:
      #   - to: default
      #     via: 192.168.3.1
      # 注释掉 DNS 服务器配置
      # nameservers:
      #   addresses:
      #     - 8.8.8.8
      #     - 8.8.4.4
      # 启用 DHCPv4
      dhcp4: yes
      # 保持 DHCPv6 启用
      dhcp6: yes
```
sudo netplan apply
## systemd-networkd
```
sudo systemctl status systemd-networkd
```

```
sudo nano /etc/systemd/network/10-wired.network
```

```
[Match]
Name=enp3s0

[Network]
DHCP=yes

```

```
[Match]
Name=enp3s0

[Network]
Address=192.168.1.100/24
Gateway=192.168.1.1
DNS=8.8.8.8
DNS=8.8.4.4

```

```
sudo systemctl enable systemd-networkd
sudo systemctl start systemd-networkd
```


## Network

```
sudo nano /etc/network/interfaces
sudo nano /etc/sysconfig/network-scripts/ifcfg-eth0
```

```
TYPE=”Ethernet”  
PROXY_METHOD=”none”  
BROWSER_ONLY=”no”  
BOOTPROTO=”dhcp”  
DEFROUTE=”yes”  
IPV4_FAILURE_FATAL=”no”  
IPV6INIT=”yes”  
IPV6_AUTOCONF=”yes”  
IPV6_DEFROUTE=”yes”  
IPV6_FAILURE_FATAL=”no”  
IPV6_ADDR_GEN_MODE=”stable-privacy”  
NAME=”ens33”  
UUID=”xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx”
```
将 `BOOTPROTO` 的值从 `dhcp` 修改为 `static`，表示使用静态 IP 地址。在 `BOOTPROTO` 行下方添加以下配置项，以设置静态 IP 地址、子网掩码、网关地址和 DNS 服务器的值：
重启网络服务使配置生效。在终端中执行以下命令：  
systemctl restart network

## 权限太开放解决
```
sudo chmod 600 /etc/netplan/01-network-manager-all.yaml
sudo netplan apply
```
![image-202410165639190.png|325](00_sync/00linux/%E8%AE%BE%E7%BD%AE%E7%BD%91%E5%8D%A1%E4%B8%BA%E9%9D%99%E6%80%81ip%E5%92%8C%E6%9F%A5%E7%9C%8Bmac/%E8%AE%BE%E7%BD%AE%E7%BD%91%E5%8D%A1%E4%B8%BA%E9%9D%99%E6%80%81ip%E5%92%8C%E6%9F%A5%E7%9C%8Bmac/image-202410165639190.png)

## 查看mac
```
## 查看mac
cat /sys/class/net/eth0/address
```
![image-202410161131519.png|450](00_sync/00linux/%E8%AE%BE%E7%BD%AE%E7%BD%91%E5%8D%A1%E4%B8%BA%E9%9D%99%E6%80%81ip%E5%92%8C%E6%9F%A5%E7%9C%8Bmac/%E8%AE%BE%E7%BD%AE%E7%BD%91%E5%8D%A1%E4%B8%BA%E9%9D%99%E6%80%81ip%E5%92%8C%E6%9F%A5%E7%9C%8Bmac/image-202410161131519.png)
![image-202410161141772.png|475](00_sync/00linux/%E8%AE%BE%E7%BD%AE%E7%BD%91%E5%8D%A1%E4%B8%BA%E9%9D%99%E6%80%81ip%E5%92%8C%E6%9F%A5%E7%9C%8Bmac/%E8%AE%BE%E7%BD%AE%E7%BD%91%E5%8D%A1%E4%B8%BA%E9%9D%99%E6%80%81ip%E5%92%8C%E6%9F%A5%E7%9C%8Bmac/image-202410161141772.png)
# 扩展
## 五种常见的修改网卡操作
### 1. **Netplan**

Netplan 是现代 Ubuntu 和其他一些基于 Systemd 的发行版中默认的网络配置工具。它使用 YAML 格式的配置文件来定义网络设置，并且可以与多种后端（如 NetworkManager 和 Systemd-networkd）协同工作。

- **配置文件路径**: `/etc/netplan/`
- **优先级**: 高
- **适用场景**: 现代 Ubuntu 发行版，以及其他使用 Netplan 的系统。

### 2. **NetworkManager**

NetworkManager 是一个用户友好的网络管理工具，适用于桌面环境和服务器。它提供了一个图形界面和命令行工具（如 `nmcli` 和 `nmtui`）来配置网络。

- **配置文件路径**: `/etc/NetworkManager/` 和 `/etc/NetworkManager/system-connections/`
- **优先级**: 高
- **适用场景**: 桌面环境和服务器，特别是那些需要图形界面或用户友好命令行工具的环境。

### 3. **Systemd-networkd**

Systemd-networkd 是 Systemd 的一部分，用于管理网络接口。它适用于无头服务器和嵌入式系统，通常与 Netplan 一起使用。

- **配置文件路径**: `/etc/systemd/network/`
- **优先级**: 中
- **适用场景**: 无头服务器、嵌入式系统和其他不需要复杂网络管理的环境。

### 4. **/etc/network/interfaces**

传统的 Debian 和 Ubuntu 系统使用 `/etc/network/interfaces` 文件来配置网络接口。虽然在现代系统中逐渐被 Netplan 和 NetworkManager 替代，但在一些老系统中仍然可用。

- **配置文件路径**: `/etc/network/interfaces`
- **优先级**: 低
- **适用场景**: 传统 Debian 和 Ubuntu 系统。

### 5. **/etc/sysconfig/network-scripts/ifcfg-eth0**

Red Hat 系列发行版（如 RHEL、CentOS 和 Fedora）使用 `/etc/sysconfig/network-scripts/` 目录下的配置文件来管理网络接口。

- **配置文件路径**: `/etc/sysconfig/network-scripts/`
- **优先级**: 低
- **适用场景**: Red Hat 系列发行版。

### 优先级和冲突处理

在同一个系统中，多个网络配置工具可能会发生冲突。一般来说，优先级较高的工具会覆盖优先级较低的工具的配置。以下是大致的优先级顺序：

1. **Netplan** (高优先级)
2. **NetworkManager** (高优先级)
3. **Systemd-networkd** (中等优先级)
4. **/etc/network/interfaces** (低优先级)
5. **/etc/sysconfig/network-scripts/`ifcfg-eth0`** (低优先级)

### 示例配置
