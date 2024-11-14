# 设置时区为上海【timedatectl】
命令本身与 NTP（Network Time Protocol）没有直接关系,是设置系统的时区，正确的时区对于确保 NTP 同步的时间准确是非常重要的
```
sudo timedatectl set-timezone Asia/Shanghai
date
```

# NTP
```
sudo apt update
sudo apt install ntp
```

```
/etc/ntp.conf
```

```
server 0.pool.ntp.org
server 1.pool.ntp.org
server 2.pool.ntp.org
server 3.pool.ntp.org
```

```
sudo systemctl status ntp
sudo systemctl start ntp
sudo systemctl enable ntp
```
![image-2024111151654.png|400](00_sync/00linux/Linux下的NTP同步设置/Linux下的NTP同步设置/image-2024111151654.png)
## 手动同步时间
```
sudo ntpd -qg
```

## 验证时间同步
```
ntpq -p
timedatectl status
```
## 内网设备NTP
/etc/ntp.conf
```
restrict 192.168.1.0 mask 255.255.255.0 nomodify notrap
```

```
sudo systemctl restart ntp
sudo systemctl restart ntpd
```

#### 客户端
/etc/ntp.conf
```
server 192.168.1.1
```

```
sudo systemctl restart ntp
sudo systemctl restart ntpd
```

# 防火墙
```
NTP 使用 UDP 端口 123。
sudo ufw allow out 123/udp
sudo firewall-cmd --add-service=ntp --permanent
sudo firewall-cmd --reload
```
