1. `ls`：列出当前目录中的文件和文件夹。
2. `cd`：切换到指定目录。 cd /mnt
3. <font color="#9bbb59">`pwd`</font>：显示当前工作目录的路径。
4. `mkdir`：创建一个新的目录。
5. `rm`：删除文件或目录。
6. `cp`：复制文件或目录。  cp source.txt /mnt/destination
7. `mv`：移动文件或目录，也可用于重命名文件或目录。
8. `cat`：显示文件的内容。
9. `grep`：在文件中搜索指定的模式。
10. `chmod`：修改文件或目录的权限。
11. `chown`：修改文件或目录的所有者。
12. `chgrp`：修改文件或目录的所属组。
13. `tar`：打包和解压缩文件。
14. `ssh`：通过 SSH 连接到远程主机。
15. `ping`：向目标主机发送 ICMP 回显请求以测试网络连通性。
16. `ifconfig`：显示和配置网络接口信息。
17. `netstat`：显示网络连接、路由表和网络接口统计信息。
18. `ps`：显示当前运行的进程。
19. `top`：实时显示系统资源使用情况和运行的进程列表。
20. `kill`：终止运行的进程。
21. `man`：查看命令的手册页。
22. `sudo`：以超级用户权限执行命令。
23. `apt-get`（适用于基于 Debian 的发行版）或 `yum`（适用于基于 Red Hat 的发行版）：包管理器，用于安装、更新和删除软件包。
24.  netstat -tln 。 查看开放的端口


ifconfig ens33 down 关闭网口

1、Ctrl+Alt+T打开终端，输入`sudo ufw status`回车，[查看防火墙状态](https://so.csdn.net/so/search?q=%E6%9F%A5%E7%9C%8B%E9%98%B2%E7%81%AB%E5%A2%99%E7%8A%B6%E6%80%81&spm=1001.2101.3001.7020)：inactive是关闭，active是开启。

2、使用`sudo ufw enable`开启防火墙。

3、使用`sudo ufw disable`[关闭防火墙](https://so.csdn.net/so/search?q=%E5%85%B3%E9%97%AD%E9%98%B2%E7%81%AB%E5%A2%99&spm=1001.2101.3001.7020)。