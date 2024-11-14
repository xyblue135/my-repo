如果使用内网穿透，暴露在公网的端口势必是不太安全的，也没什么加密的条件。如果设置密码也不是很安全，相比来说使用密钥对登录以及采取内网登录这种方法能大大提高网络安全性，且常规的方法ipsec和ssr被那啥的差不多了。
wireguard默认不是全局流量，所以不会挂个vpn导致网速变慢（也节省了服务端的消耗）
但是像openvpn和zero tier这样的默认走的全局流量，且有封端口的风险。连着连着断连
# 方法一 Wireguard
## 服务端搭建
安装wireguard，ubuntu示例
```
sudo -i
apt install wireguard resolvconf -y
sudo apt-get -y install easy-rsa
echo "net.ipv4.ip_forward = 1" >> /etc/sysctl.conf
sysctl -p
```
调整目录权限
```
cd /etc/wireguard/
chmod 0777 /etc/wireguard
#调整目录默认权限
umask 077
```
生成服务器秘钥
```
#生成私钥
wg genkey > server.key
#通过私钥生成公钥
wg pubkey < server.key > server.key.pub
```
生成客户端秘钥
```
mkdir client
#生成私钥
wg genkey > client/client1.key
wg genkey > client/client2.key
wg genkey > client/client3.key
wg genkey > client/client4.key
wg genkey > client/client5.key
wg genkey > client/client6.key
wg genkey > client/client7.key
wg genkey > client/client8.key
wg genkey > client/client9.key
wg genkey > client/client10.key
#通过私钥生成公钥
wg pubkey < client/client1.key > client/client1.key.pub
wg pubkey < client/client2.key > client/client2.key.pub
wg pubkey < client/client3.key > client/client3.key.pub
wg pubkey < client/client4.key > client/client4.key.pub
wg pubkey < client/client5.key > client/client5.key.pub
wg pubkey < client/client6.key > client/client6.key.pub
wg pubkey < client/client7.key > client/client7.key.pub
wg pubkey < client/client8.key > client/client8.key.pub
wg pubkey < client/client9.key > client/client9.key.pub
wg pubkey < client/client10.key > client/client10.key.pub
```
创建配置文件
```
sudo vi wg0.conf
```
直接在窗口输入 注意etho0为网络的公网出口
```
echo "
[Interface]
PrivateKey = $(cat server.key) # 填写本机的privatekey 内容
Address = 192.168.100.254 #本机虚拟局域网IP
PostUp   = iptables -A FORWARD -i wg0 -j ACCEPT; iptables -A FORWARD -o wg0 -j ACCEPT; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
PostDown = iptables -D FORWARD -i wg0 -j ACCEPT; iptables -D FORWARD -o wg0 -j ACCEPT; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE
#注意eth0需要为本机网卡名称
ListenPort = 50814 # 监听端口
DNS = 8.8.8.8
MTU = 1420
[Peer]
PublicKey =  $(cat client/client1.key.pub)  
AllowedIPs = 192.168.100.1/24 #客户端所使用的IP" > wg0.conf
```
文本中追加增加节点
```
echo "[Peer]" >> wg0.conf
echo "PublicKey = $(cat client/client2.key.pub)" >> wg0.conf
echo "AllowedIPs = 192.168.100.2/32" >> wg0.conf

echo "[Peer]" >> wg0.conf
echo "PublicKey = $(cat client/client3.key.pub)" >> wg0.conf
echo "AllowedIPs = 192.168.100.3/32" >> wg0.conf

echo "[Peer]" >> wg0.conf
echo "PublicKey = $(cat client/client4.key.pub)" >> wg0.conf
echo "AllowedIPs = 192.168.100.4/32" >> wg0.conf

echo "[Peer]" >> wg0.conf
echo "PublicKey = $(cat client/client5.key.pub)" >> wg0.conf
echo "AllowedIPs = 192.168.100.5/32" >> wg0.conf

echo "[Peer]" >> wg0.conf
echo "PublicKey = $(cat client/client6.key.pub)" >> wg0.conf
echo "AllowedIPs = 192.168.100.6/32" >> wg0.conf

echo "[Peer]" >> wg0.conf
echo "PublicKey = $(cat client/client7.key.pub)" >> wg0.conf
echo "AllowedIPs = 192.168.100.7/32" >> wg0.conf

echo "[Peer]" >> wg0.conf
echo "PublicKey = $(cat client/client8.key.pub)" >> wg0.conf
echo "AllowedIPs = 192.168.100.8/32" >> wg0.conf

echo "[Peer]" >> wg0.conf
echo "PublicKey = $(cat client/client9.key.pub)" >> wg0.conf
echo "AllowedIPs = 192.168.100.9/32" >> wg0.conf

echo "[Peer]" >> wg0.conf
echo "PublicKey = $(cat client/client10.key.pub)" >> wg0.conf
echo "AllowedIPs = 192.168.100.10/32" >> wg0.conf
```
### 开机启动和手动启动
```
systemctl enable wg-quick@wg0

#启动wg0
wg-quick up wg0
#关闭wg0
wg-quick down wg0
```
![image-2024911016469.png|500](00_sync/00vpn加密/在Linux使用vpn技术实现虚拟个人网络提高网络安全/在Linux使用vpn技术实现虚拟个人网络提高网络安全/image-2024911016469.png)
客户端地址
https://www.wireguard.com/install/
https://github.com/wgredlong/WireGuard
客户端配置，可以使用脚本
```
#!/bin/bash

# 确保client文件夹存在
mkdir -p client

# 提示用户输入客户端编号
read -p "请输入客户端编号: " client_number

# 检查输入的有效性（可选，确保是正整数）
if ! [[ "$client_number" =~ ^[0-9]+$ ]]; then
    echo "错误：请输入有效的客户端编号（正整数）"
    exit 1
fi

# 生成客户端配置文件的名称
conf_file="client/client${client_number}.conf"

# 创建或清空配置文件
> "$conf_file"

# 写入公共部分
echo "[Interface]" > "$conf_file"
echo "PrivateKey = $(cat client/client${client_number}.key)" >> "$conf_file"
echo "Address = 192.168.100.${client_number}" >> "$conf_file"
echo "MTU = 1420" >> "$conf_file"
echo "[Peer]" >> "$conf_file"
echo "PublicKey = $(cat server.key.pub)" >> "$conf_file"
echo "AllowedIPs = 192.168.100.0/24" >> "$conf_file"
echo "Endpoint = 公网ip:50814" >> "$conf_file"

# 打印配置文件内容到终端
echo "Configuration for client ${client_number}:"
cat "$conf_file"

echo "Configuration for client ${client_number} has been written to ${conf_file}"
```
需要的配置文件
![image-2024913924408.png|350](00_sync/00vpn加密/在Linux使用vpn技术实现虚拟个人网络提高网络安全/在Linux使用vpn技术实现虚拟个人网络提高网络安全/image-2024913924408.png)
## 客户端连接
![image-2024914045439.png|225](00_sync/00vpn加密/在Linux使用vpn技术实现虚拟个人网络提高网络安全/在Linux使用vpn技术实现虚拟个人网络提高网络安全/image-2024914045439.png)
![image-2024914627845.png|300](00_sync/00vpn加密/在Linux使用vpn技术实现虚拟个人网络提高网络安全/在Linux使用vpn技术实现虚拟个人网络提高网络安全/image-2024914627845.png)
手机上是
![f5389efcec3446228eccfce3bb6572e.jpg|200](00_sync/00vpn加密/在Linux使用vpn技术实现虚拟个人网络提高网络安全/在Linux使用vpn技术实现虚拟个人网络提高网络安全/f5389efcec3446228eccfce3bb6572e.jpg)
![10fed95fbfdfae4d94d703efee06dc3.jpg|225](00_sync/00vpn加密/在Linux使用vpn技术实现虚拟个人网络提高网络安全/在Linux使用vpn技术实现虚拟个人网络提高网络安全/10fed95fbfdfae4d94d703efee06dc3.jpg)
然后我们组成网络后，手机即使是流量可以使用组网的私网地址进行访问服务了
![image-2024914929228.png|250](00_sync/00vpn加密/在Linux使用vpn技术实现虚拟个人网络提高网络安全/在Linux使用vpn技术实现虚拟个人网络提高网络安全/image-2024914929228.png)
服务端也可以看到，两个异地用户已经组成虚拟局域网环境
![image-202491525121.png|423](00_sync/00vpn加密/在Linux使用vpn技术实现虚拟个人网络提高网络安全/在Linux使用vpn技术实现虚拟个人网络提高网络安全/image-202491525121.png)
需要注意的是，配置完成后最后ping一下服务端，不然不会上线的，也不会连通

## 推荐:docker方法更为方便
https://hub.docker.com/r/linuxserver/wireguard
```
docker run -d \
  --name=wg-easy \
  -e WG_HOST=这里是公网ip  \
  -e PASSWORD=这里是密码  \
  -e WG_DEFAULT_ADDRESS=192.168.200.x \
  -e WG_DEFAULT_DNS=114.114.114.114 \
  -e WG_ALLOWED_IPS=192.168.200.0/24 \
  -e WG_PERSISTENT_KEEPALIVE=10 \
  -v ~/.wg-easy:/etc/wireguard \
  -p 51820:51820/udp \
  -p 51821:51821/tcp \
  --cap-add=NET_ADMIN \
  --cap-add=SYS_MODULE \
  --sysctl="net.ipv4.conf.all.src_valid_mark=1" \
  --sysctl="net.ipv4.ip_forward=1" \
  --restart unless-stopped \
  weejewel/wg-easy
```
参考:
https://gitee.com/spoto/wireguard
	
# 方法二 openvpn
Open VPN 通过IKEV2、 UDP、TCP或Stealth在端口上进行连接
## 服务端搭建
```
sudo apt-get -y install openvpn libssl-dev openssl
sudo apt-get -y install easy-rsa
```
![image-20249271026820.png|475](00_sync/00vpn%E5%8A%A0%E5%AF%86/%E5%9C%A8Linux%E4%BD%BF%E7%94%A8vpn%E6%8A%80%E6%9C%AF%E5%AE%9E%E7%8E%B0%E8%99%9A%E6%8B%9F%E4%B8%AA%E4%BA%BA%E7%BD%91%E7%BB%9C%E6%8F%90%E9%AB%98%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8/%E5%9C%A8Linux%E4%BD%BF%E7%94%A8vpn%E6%8A%80%E6%9C%AF%E5%AE%9E%E7%8E%B0%E8%99%9A%E6%8B%9F%E4%B8%AA%E4%BA%BA%E7%BD%91%E7%BB%9C%E6%8F%90%E9%AB%98%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8/image-20249271026820.png)
## 制作证书
```
sudo mkdir /etc/openvpn/easy-rsa/ 
cd /etc/openvpn/easy-rsa/
sudo cp -r /usr/share/easy-rsa/* /etc/openvpn/easy-rsa/
```
当然，我们也可以直接在/usr/share/easy-rsa/制作相关的证书，但是为了后续的管理证书的方便，我们还是把easy-rsa放在了openvpn的启动目录下。
![image-20249271518370.png](00_sync/00vpn%E5%8A%A0%E5%AF%86/%E5%9C%A8Linux%E4%BD%BF%E7%94%A8vpn%E6%8A%80%E6%9C%AF%E5%AE%9E%E7%8E%B0%E8%99%9A%E6%8B%9F%E4%B8%AA%E4%BA%BA%E7%BD%91%E7%BB%9C%E6%8F%90%E9%AB%98%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8/%E5%9C%A8Linux%E4%BD%BF%E7%94%A8vpn%E6%8A%80%E6%9C%AF%E5%AE%9E%E7%8E%B0%E8%99%9A%E6%8B%9F%E4%B8%AA%E4%BA%BA%E7%BD%91%E7%BB%9C%E6%8F%90%E9%AB%98%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8/image-20249271518370.png)
把这些改掉
sudo cp vars.example vars
编辑vars
```
#set_var EASYRSA_REQ_COUNTRY    "US"
#set_var EASYRSA_REQ_PROVINCE   "California"
#set_var EASYRSA_REQ_CITY   "San Francisco"
#set_var EASYRSA_REQ_ORG    "Copyleft Certificate Co"
#set_var EASYRSA_REQ_EMAIL  "me@example.net"
#set_var EASYRSA_REQ_OU     "My Organizational Unit"

#set_var EASYRSA_REQ_COUNTRY    "US"
#set_var EASYRSA_REQ_PROVINCE   "HB"
#set_var EASYRSA_REQ_CITY   "HEBEI"
#set_var EASYRSA_REQ_ORG    "xyblue"
#set_var EASYRSA_REQ_EMAIL  "邮箱"
#set_var EASYRSA_REQ_OU     "xyblue"

```
末尾添加 export KEY_NAME=”vpnairgens”这个要记住下，我们下面在制作Server端证书时，会使用到
```
#添加的
export KEY_NAME="vpnairgens"
```
![image-20249271928673.png|425](00_sync/00vpn%E5%8A%A0%E5%AF%86/%E5%9C%A8Linux%E4%BD%BF%E7%94%A8vpn%E6%8A%80%E6%9C%AF%E5%AE%9E%E7%8E%B0%E8%99%9A%E6%8B%9F%E4%B8%AA%E4%BA%BA%E7%BD%91%E7%BB%9C%E6%8F%90%E9%AB%98%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8/%E5%9C%A8Linux%E4%BD%BF%E7%94%A8vpn%E6%8A%80%E6%9C%AF%E5%AE%9E%E7%8E%B0%E8%99%9A%E6%8B%9F%E4%B8%AA%E4%BA%BA%E7%BD%91%E7%BB%9C%E6%8F%90%E9%AB%98%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8/image-20249271928673.png)
查看文档描述知道制作方法
```
cat /usr/share/doc/easy-rsa/README.Debian | grep ./
```
![image-20249272132292.png](00_sync/00vpn%E5%8A%A0%E5%AF%86/%E5%9C%A8Linux%E4%BD%BF%E7%94%A8vpn%E6%8A%80%E6%9C%AF%E5%AE%9E%E7%8E%B0%E8%99%9A%E6%8B%9F%E4%B8%AA%E4%BA%BA%E7%BD%91%E7%BB%9C%E6%8F%90%E9%AB%98%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8/%E5%9C%A8Linux%E4%BD%BF%E7%94%A8vpn%E6%8A%80%E6%9C%AF%E5%AE%9E%E7%8E%B0%E8%99%9A%E6%8B%9F%E4%B8%AA%E4%BA%BA%E7%BD%91%E7%BB%9C%E6%8F%90%E9%AB%98%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8/image-20249272132292.png)
```
./easyrsa init-pki
sudo chmod 777 */
./easyrsa build-ca nopass
```
![image-20249272245623.png](00_sync/00vpn%E5%8A%A0%E5%AF%86/%E5%9C%A8Linux%E4%BD%BF%E7%94%A8vpn%E6%8A%80%E6%9C%AF%E5%AE%9E%E7%8E%B0%E8%99%9A%E6%8B%9F%E4%B8%AA%E4%BA%BA%E7%BD%91%E7%BB%9C%E6%8F%90%E9%AB%98%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8/%E5%9C%A8Linux%E4%BD%BF%E7%94%A8vpn%E6%8A%80%E6%9C%AF%E5%AE%9E%E7%8E%B0%E8%99%9A%E6%8B%9F%E4%B8%AA%E4%BA%BA%E7%BD%91%E7%BB%9C%E6%8F%90%E9%AB%98%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8/image-20249272245623.png)
貌似nopass没生效，算了不管了
![image-20249272741522.png|475](00_sync/00vpn%E5%8A%A0%E5%AF%86/%E5%9C%A8Linux%E4%BD%BF%E7%94%A8vpn%E6%8A%80%E6%9C%AF%E5%AE%9E%E7%8E%B0%E8%99%9A%E6%8B%9F%E4%B8%AA%E4%BA%BA%E7%BD%91%E7%BB%9C%E6%8F%90%E9%AB%98%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8/%E5%9C%A8Linux%E4%BD%BF%E7%94%A8vpn%E6%8A%80%E6%9C%AF%E5%AE%9E%E7%8E%B0%E8%99%9A%E6%8B%9F%E4%B8%AA%E4%BA%BA%E7%BD%91%E7%BB%9C%E6%8F%90%E9%AB%98%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8/image-20249272741522.png)
```
./easyrsa build-server-full vpnairgens nopass
```
![image-20249273358354.png|200](00_sync/00vpn%E5%8A%A0%E5%AF%86/%E5%9C%A8Linux%E4%BD%BF%E7%94%A8vpn%E6%8A%80%E6%9C%AF%E5%AE%9E%E7%8E%B0%E8%99%9A%E6%8B%9F%E4%B8%AA%E4%BA%BA%E7%BD%91%E7%BB%9C%E6%8F%90%E9%AB%98%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8/%E5%9C%A8Linux%E4%BD%BF%E7%94%A8vpn%E6%8A%80%E6%9C%AF%E5%AE%9E%E7%8E%B0%E8%99%9A%E6%8B%9F%E4%B8%AA%E4%BA%BA%E7%BD%91%E7%BB%9C%E6%8F%90%E9%AB%98%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8/image-20249273358354.png)
```
./easyrsa build-client-full airgens nopass
```
![image-20249273439831.png](00_sync/00vpn%E5%8A%A0%E5%AF%86/%E5%9C%A8Linux%E4%BD%BF%E7%94%A8vpn%E6%8A%80%E6%9C%AF%E5%AE%9E%E7%8E%B0%E8%99%9A%E6%8B%9F%E4%B8%AA%E4%BA%BA%E7%BD%91%E7%BB%9C%E6%8F%90%E9%AB%98%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8/%E5%9C%A8Linux%E4%BD%BF%E7%94%A8vpn%E6%8A%80%E6%9C%AF%E5%AE%9E%E7%8E%B0%E8%99%9A%E6%8B%9F%E4%B8%AA%E4%BA%BA%E7%BD%91%E7%BB%9C%E6%8F%90%E9%AB%98%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8/image-20249273439831.png)
其中 ca.crt private/airgens.key issued/airgens.crt三个文件是我们要使用的。
现在再为服务器生成加密交换时的Diffie-Hellman文件，如下：
```
./easyrsa gen-dh
ls pki/dh.pem -l
```
![image-20249273650502.png|425](00_sync/00vpn%E5%8A%A0%E5%AF%86/%E5%9C%A8Linux%E4%BD%BF%E7%94%A8vpn%E6%8A%80%E6%9C%AF%E5%AE%9E%E7%8E%B0%E8%99%9A%E6%8B%9F%E4%B8%AA%E4%BA%BA%E7%BD%91%E7%BB%9C%E6%8F%90%E9%AB%98%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8/%E5%9C%A8Linux%E4%BD%BF%E7%94%A8vpn%E6%8A%80%E6%9C%AF%E5%AE%9E%E7%8E%B0%E8%99%9A%E6%8B%9F%E4%B8%AA%E4%BA%BA%E7%BD%91%E7%BB%9C%E6%8F%90%E9%AB%98%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8/image-20249273650502.png)
补充文件到当前目录
```
cd /etc/openvpn
cp /usr/share/doc/openvpn/examples/sample-config-files/server.conf .  
cp easy-rsa/pki/ca.crt .
cp easy-rsa/pki/issued/vpnairgens.crt .
cp easy-rsa/pki/private/vpnairgens.key .
cp easy-rsa/pki/dh.pem .
cp easy-rsa/pki/dh.pem ./dh2048.pem
chmod 777 *
```
说明server.conf是可以修改port和tcp或者udp的 修改秘钥key文件名 修改VPN的IP地址段(也可不修改)
修改名字
```
ca ca.crt
cert server.crt
key server.key  # This file should be kept secret
为
ca ca.crt
cert vpnairgens.crt
key vpnairgens.key  # This file should be kept secret

;comp-lzo
为
comp-lzo

tls-auth ta.key 0 # This file is secret
为
;tls-auth ta.key 0 # This file is secret

;log-append  /var/log/openvpn/openvpn.log
为
log-append  /var/log/openvpn/openvpn.log


explicit-exit-notify 1
为
;explicit-exit-notify 1
```
## 运行
顺利运行
```
openvpn --config /etc/openvpn/server.con
nohup /usr/sbin/openvpn --config /etc/openvpn/server.conf &
```
![image-20249275220133.png|450](00_sync/00vpn%E5%8A%A0%E5%AF%86/%E5%9C%A8Linux%E4%BD%BF%E7%94%A8vpn%E6%8A%80%E6%9C%AF%E5%AE%9E%E7%8E%B0%E8%99%9A%E6%8B%9F%E4%B8%AA%E4%BA%BA%E7%BD%91%E7%BB%9C%E6%8F%90%E9%AB%98%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8/%E5%9C%A8Linux%E4%BD%BF%E7%94%A8vpn%E6%8A%80%E6%9C%AF%E5%AE%9E%E7%8E%B0%E8%99%9A%E6%8B%9F%E4%B8%AA%E4%BA%BA%E7%BD%91%E7%BB%9C%E6%8F%90%E9%AB%98%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8/image-20249275220133.png)
## 日志
```
	tail -f /var/log/openvpn/openvpn.log
```
![image-20249275313446.png](00_sync/00vpn%E5%8A%A0%E5%AF%86/%E5%9C%A8Linux%E4%BD%BF%E7%94%A8vpn%E6%8A%80%E6%9C%AF%E5%AE%9E%E7%8E%B0%E8%99%9A%E6%8B%9F%E4%B8%AA%E4%BA%BA%E7%BD%91%E7%BB%9C%E6%8F%90%E9%AB%98%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8/%E5%9C%A8Linux%E4%BD%BF%E7%94%A8vpn%E6%8A%80%E6%9C%AF%E5%AE%9E%E7%8E%B0%E8%99%9A%E6%8B%9F%E4%B8%AA%E4%BA%BA%E7%BD%91%E7%BB%9C%E6%8F%90%E9%AB%98%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8/image-20249275313446.png)