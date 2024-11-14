最好用的
sudo netstat -tulnp
![image-20248314155540.png](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8A%E5%85%B3%E4%BA%8Enetstat%E7%9A%84%E4%BD%BF%E7%94%A8/Linux%E4%B8%8A%E5%85%B3%E4%BA%8Enetstat%E7%9A%84%E4%BD%BF%E7%94%A8/image-20248314155540.png)
netstat -tuln
显示所有监听的 TCP 和 UDP 端口，使用数字形式显示地址和端口。
netstat -anp
显示所有连接的套接字信息，包括监听的和非监听的，并显示 PID 和程序名称。
netstat -s
显示各个协议（如 TCP、UDP、ICMP 等）的统计信息。
netstat -r
显示当前的路由表信息。

```
-a
显示所有连接中的套接字（包括监听的和非监听的）。
-t
显示 TCP 连接。
-u
显示 UDP 连接。
-l
显示正在监听的套接字（监听状态的端口）。
-n
以数字形式显示地址和端口（不解析为主机名和服务名）。
-p
显示使用网络连接的程序的 PID 和名称（需要 `sudo` 权限）。
-r
显示路由表。
-i
显示网络接口信息及其状态。
-s
显示各个协议的统计信息。
-c
每隔一段时间持续输出网络状态信息，直到被手动停止（Ctrl+C）。
```
