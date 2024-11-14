# nmcli
```
nmcli device wifi list
nmcli device wifi connect <SSID> password <password>
```
![image-20247104833481.png](00_sync/00linux/Linux下使用命令连接wifi的三种方式/Linux下使用命令连接wifi的三种方式/image-20247104833481.png)
# wpa_supplicant
```
sudo apt-get install wpasupplicant
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```
-
```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=US

network={
    ssid="PCDN"
    psk="20020918"
}
```
-
```
sudo wpa_supplicant -B -i <interface> -c /etc/wpa_supplicant/wpa_supplicant.conf
```
-
```
sudo dhclient <interface>
```

## 推荐【临时生效】
wpa_passphrase "PDCN" "20020918" | sudo tee /etc/wpa_supplicant/pdcn.conf
sudo wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant/pdcn.conf
sudo dhclient wlan0

# iwconfig

```
sudo iwlist <interface> scan
sudo iwconfig <interface> essid <SSID>
sudo iwconfig <interface> key s:<password>
sudo dhclient <interface>
```
![image-20247104949130.png|300](00_sync/00linux/Linux下使用命令连接wifi的三种方式/Linux下使用命令连接wifi的三种方式/image-20247104949130.png)
![image-20247105032761.png](00_sync/00linux/Linux下使用命令连接wifi的三种方式/Linux下使用命令连接wifi的三种方式/image-20247105032761.png)
# nmtui 图形化
```
nmtui
```
![image-20247105045143.png](00_sync/00linux/Linux下使用命令连接wifi的三种方式/Linux下使用命令连接wifi的三种方式/image-20247105045143.png)



