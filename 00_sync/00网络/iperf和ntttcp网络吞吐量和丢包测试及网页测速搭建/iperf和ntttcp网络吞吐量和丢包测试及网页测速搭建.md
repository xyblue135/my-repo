# ntttcp
https://github.com/microsoft/ntttcp
https://github.com/microsoft/ntttcp-for-linux
我喜欢用这个，因为iperf3最便捷，但是40G和100G测速的时候和cpu中断就有着巨大的关系了，会导致跑不满带宽,且因为用Cygwin编译的Linux软件在Windows下性能受限，所以任一端会受限

防火墙放行入站流量的命令提示符代码：
```
netsh advfirewall firewall add rule program=c:\tools\ntttcp.exe name="ntttcp" protocol=any dir=in action=allow enable=yes profile=ANY
# 删除命令
netsh advfirewall firewall delete rule name="ntttcp"
```
linux编译
```
进入src
make
```
![image-202410282346699.png|500](00_sync/00网络/iperf和ntttcp网络吞吐量和丢包测试及网页测速搭建/iperf和ntttcp网络吞吐量和丢包测试及网页测速搭建/image-202410282346699.png)
ntttcp -r
ntttcp -s 192.168.3.101
![image-202410285724590.png|400](00_sync/00网络/iperf和ntttcp网络吞吐量和丢包测试及网页测速搭建/iperf和ntttcp网络吞吐量和丢包测试及网页测速搭建/image-202410285724590.png)
![image-202410285719860.png|400](00_sync/00网络/iperf和ntttcp网络吞吐量和丢包测试及网页测速搭建/iperf和ntttcp网络吞吐量和丢包测试及网页测速搭建/image-202410285719860.png)
参考中文:即可知道性能瓶颈在发送端还是接收端了
![image-20241028584306.png|275](00_sync/00网络/iperf和ntttcp网络吞吐量和丢包测试及网页测速搭建/iperf和ntttcp网络吞吐量和丢包测试及网页测速搭建/image-20241028584306.png)
需要注意linux和win之间无法测试目前，只能wintowin linuxtolinux
# iperf
## 安装iperf3 
https://github.com/ar51an/iperf3-win-builds/releases
linux直接用包下载就可以
![image-202410283916836.png](00_sync/00网络/iperf和ntttcp网络吞吐量和丢包测试及网页测速搭建/iperf和ntttcp网络吞吐量和丢包测试及网页测速搭建/image-202410283916836.png)
![image-202410283930379.png](00_sync/00网络/iperf和ntttcp网络吞吐量和丢包测试及网页测速搭建/iperf和ntttcp网络吞吐量和丢包测试及网页测速搭建/image-202410283930379.png)
## 测试命令
```
iperf3 -s
iperf3 -c 192.168.3.100
```
![image-202410284120383.png|375](00_sync/00网络/iperf和ntttcp网络吞吐量和丢包测试及网页测速搭建/iperf和ntttcp网络吞吐量和丢包测试及网页测速搭建/image-202410284120383.png)
## 参数说明
共用参数
```
<code class="language-plaintext hljs">-f [k|m|K|M] 分别表示以Kbits, Mbits, KBytes, MBytes显示报告，默认以Mbits为单位,eg:iperf -c 222.35.11.23 -f K
-i sec 以秒为单位显示报告间隔，eg:iperf -c 222.35.11.23 -i 2
-l 缓冲区大小，默认是8KB,eg:iperf -c 222.35.11.23 -l 16
-m 显示tcp最大mtu值
-o 将报告和错误信息输出到文件eg:iperf -c 222.35.11.23 -o c:\iperflog.txt
-p 指定服务器端使用的端口或客户端所连接的端口eg:iperf -s -p 9999;iperf -c 222.35.11.23 -p 9999
-u 使用udp协议
-w 指定TCP窗口大小，默认是8KB
-B 绑定一个主机地址或接口（当主机有多个地址或接口时使用该参数）
-C 兼容旧版本（当server端和client端版本不一样时使用）
-M 设定TCP数据包的最大mtu值
-N 设定TCP不延时
-V 传输ipv6数据包</code>
```
客户端参数
```
<code class="language-plaintext hljs">-c //在客户端模式下运行
-u //使用UDP而不是TCP
--sctp //使用 SCTP 而不是 TCP（Linux、FreeBSD 和 Solaris）
-b //UDP模式使用的带宽，单位bits/sec。此选项与-u选项相关。默认值是1 Mbit/sec
-t //设置传输的总时间。Iperf在指定的时间内，重复的发送指定长度的数据包。默认是10秒钟。
-n //要传输的字节数,通常情况，Iperf按照10秒钟发送数据。-n参数跨越此限制，按照指定次数发送指定长度的数据，而不论该操作耗费多少时间。
-k //要传输的块（数据包）数
-i //要读取或写入的缓冲区的长度。TCP 的默认值为 128 KB，UDP 的默认值为 8 KB
-r //分别进行双向测试
-P //大写字母P，要运行的并行客户端流的数量
-d //同时进行双向传输测试
-n //指定传输的字节数，eg:iperf -c 222.35.11.23 -n 100000
-r //单独进行双向传输测试
-t //测试时间，默认10秒,eg:iperf -c 222.35.11.23 -t 5
-F //指定需要传输的文件
-T //指定ttl值</code>

`-f` 选项用于指定输出结果的格式单位 kmg/比特 KMG/字节
```
## 参数举例
```
# 以服务端模式运行，设置监控时间2秒，并指定端口为8888 
iperf3 -s -i 2 -p 8888
# 以客户端模式运行，host：port为服务端信息，输出结果以MB显示，每个1秒打印一次，共计5秒，忽略前3秒的结果，反向模式运行【让服务端进行发送】
iperf3 -c 192.168.3.100 -p 8888 -f m -i 1 -t 5 -O 3 -R
# 测试udp模式 加-u参数
iperf3 -c 192.168.3.101 -p 8888 -f m -i 2 -t 10 -O 5 -u -R
# 指定比特率和传输内容大小，测试结果应无限接近指定值 -b 传输速率 -n要传输多少
iperf3 -c 192.168.3.101 -p 8888 -f m -i 1 -b 1000M -n 100M -u
```
![image-202410284622189.png|270](00_sync/00网络/iperf和ntttcp网络吞吐量和丢包测试及网页测速搭建/iperf和ntttcp网络吞吐量和丢包测试及网页测速搭建/image-202410284622189.png)
![image-202410284733990.png|450](00_sync/00网络/iperf和ntttcp网络吞吐量和丢包测试及网页测速搭建/iperf和ntttcp网络吞吐量和丢包测试及网页测速搭建/image-202410284733990.png)
![image-202410284832309.png|425](00_sync/00网络/iperf和ntttcp网络吞吐量和丢包测试及网页测速搭建/iperf和ntttcp网络吞吐量和丢包测试及网页测速搭建/image-202410284832309.png)
# librespeed
https://hub.docker.com/r/linuxserver/librespeed
```
version: '3.8'

services:
  librespeed:
    image: lscr.io/linuxserver/librespeed:latest
    container_name: librespeed
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
      - PASSWORD=123456
      - DB_TYPE=sqlite # 使用默认的 SQLite 数据库
    volumes:
      - /home/0000/soft/librespeed/config:/config
    ports:
      - 80:80
    restart: unless-stopped
```