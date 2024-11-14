# LINUX
## 安装ssh
```
sudo apt update   #更新源
sudo apt upgrade   #升级已经安装的包
sudo apt-get install openssh-server    #下载openssh
dpkg -l | grep ssh    #使用 `grep` 进行筛选以找到包含 "ssh" 的软件包信息
```
![image-202312141433895.png|425](00_sync/Linux和WIN上的客户端服务端SSH的配置/Linux和WIN上的客户端服务端SSH的配置/image-202312141433895.png)
```
ps -e |grep ssh
```
如果看到sshd那说明ssh-server已经启动了。如果没有运行手动启用一下
```启用&重启
sudo /etc/init.d/ssh start
sudo service ssh start
sudo systemctl start ssh
```
## 配置SSH：
ssh-server配置文件位于/etc/ssh/sshd_config
可以修改端口号&允许以root登录&超时时间等等
```
sudo /etc/init.d/ssh stop
sudo /etc/init.d/ssh start
```

## 防火墙
同时我们也要一下防火墙
![image-202312143648302.png|475](00_sync/Linux和WIN上的客户端服务端SSH的配置/Linux和WIN上的客户端服务端SSH的配置/image-202312143648302.png)
## 附件
## 示例配置
```
# This is the sshd server system-wide configuration file.  See
# sshd_config(5) for more information.

# This sshd was compiled with PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games

# The strategy used for options in the default sshd_config shipped with
# OpenSSH is to specify options with their default value where
# possible, but leave them commented.  Uncommented options override the
# default value.

Include /etc/ssh/sshd_config.d/*.conf

#Port 22
#AddressFamily any
#ListenAddress 0.0.0.0
#ListenAddress ::

#HostKey /etc/ssh/ssh_host_rsa_key
#HostKey /etc/ssh/ssh_host_ecdsa_key
#HostKey /etc/ssh/ssh_host_ed25519_key

# Ciphers and keying
#RekeyLimit default none

# Logging
#SyslogFacility AUTH
#LogLevel INFO

# Authentication:

#LoginGraceTime 2m
#PermitRootLogin prohibit-password
#StrictModes yes
#MaxAuthTries 6
#MaxSessions 10

#PubkeyAuthentication yes

# Expect .ssh/authorized_keys2 to be disregarded by default in future.
#AuthorizedKeysFile     .ssh/authorized_keys .ssh/authorized_keys2

#AuthorizedPrincipalsFile none

#AuthorizedKeysCommand none
#AuthorizedKeysCommandUser nobody

# For this to work you will also need host keys in /etc/ssh/ssh_known_hosts
#HostbasedAuthentication no
# Change to yes if you don't trust ~/.ssh/known_hosts for
# HostbasedAuthentication
#IgnoreUserKnownHosts no
# Don't read the user's ~/.rhosts and ~/.shosts files
#IgnoreRhosts yes

# To disable tunneled clear text passwords, change to no here!
#PasswordAuthentication yes
#PermitEmptyPasswords no

# Change to yes to enable challenge-response passwords (beware issues with
# some PAM modules and threads)
KbdInteractiveAuthentication no

# Kerberos options
#KerberosAuthentication no
#KerberosOrLocalPasswd yes
#KerberosTicketCleanup yes
#KerberosGetAFSToken no

# GSSAPI options
#GSSAPIAuthentication no
#GSSAPICleanupCredentials yes
#GSSAPIStrictAcceptorCheck yes
#GSSAPIKeyExchange no

# Set this to 'yes' to enable PAM authentication, account processing,
# and session processing. If this is enabled, PAM authentication will
# be allowed through the KbdInteractiveAuthentication and
# PasswordAuthentication.  Depending on your PAM configuration,
# PAM authentication via KbdInteractiveAuthentication may bypass
# the setting of "PermitRootLogin without-password".
# If you just want the PAM account and session checks to run without
# PAM authentication, then enable this but set PasswordAuthentication
# and KbdInteractiveAuthentication to 'no'.
UsePAM yes

#AllowAgentForwarding yes
#AllowTcpForwarding yes
#GatewayPorts no
X11Forwarding yes
#X11DisplayOffset 10
#X11UseLocalhost yes
#PermitTTY yes
PrintMotd no
#PrintLastLog yes
#TCPKeepAlive yes
#PermitUserEnvironment no
#Compression delayed
#ClientAliveInterval 0
#ClientAliveCountMax 3
#UseDNS no
#PidFile /run/sshd.pid
#MaxStartups 10:30:100
#PermitTunnel no
#ChrootDirectory none
#VersionAddendum none

# no default banner path
#Banner none

# Allow client to pass locale environment variables
AcceptEnv LANG LC_*

# override default of no subsystems
Subsystem       sftp    /usr/lib/openssh/sftp-server

# Example of overriding settings on a per-user basis
#Match User anoncvs
#       X11Forwarding no
#       AllowTcpForwarding no
#       PermitTTY no
#       ForceCommand cvs server
```
# WIN
cmd或者powershell输入ssh如有有以下，代表有ssh客户端，我们就需要安装服务端
![image-202410261752690.png](00_sync/Linux%E5%92%8CWIN%E4%B8%8A%E7%9A%84%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%9C%8D%E5%8A%A1%E7%AB%AFSSH%E7%9A%84%E9%85%8D%E7%BD%AE/Linux%E5%92%8CWIN%E4%B8%8A%E7%9A%84%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%9C%8D%E5%8A%A1%E7%AB%AFSSH%E7%9A%84%E9%85%8D%E7%BD%AE/image-202410261752690.png)
![image-20241026191151.png](00_sync/Linux%E5%92%8CWIN%E4%B8%8A%E7%9A%84%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%9C%8D%E5%8A%A1%E7%AB%AFSSH%E7%9A%84%E9%85%8D%E7%BD%AE/Linux%E5%92%8CWIN%E4%B8%8A%E7%9A%84%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%9C%8D%E5%8A%A1%E7%AB%AFSSH%E7%9A%84%E9%85%8D%E7%BD%AE/image-20241026191151.png)
根据需要我们去到安装的页面，这边查看功能搜索SSH服务端
![image-202410261959452.png|375](00_sync/Linux%E5%92%8CWIN%E4%B8%8A%E7%9A%84%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%9C%8D%E5%8A%A1%E7%AB%AFSSH%E7%9A%84%E9%85%8D%E7%BD%AE/Linux%E5%92%8CWIN%E4%B8%8A%E7%9A%84%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%9C%8D%E5%8A%A1%E7%AB%AFSSH%E7%9A%84%E9%85%8D%E7%BD%AE/image-202410261959452.png)
顺便也能删除一些东西
![image-20241026227436.png|275](00_sync/Linux%E5%92%8CWIN%E4%B8%8A%E7%9A%84%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%9C%8D%E5%8A%A1%E7%AB%AFSSH%E7%9A%84%E9%85%8D%E7%BD%AE/Linux%E5%92%8CWIN%E4%B8%8A%E7%9A%84%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%9C%8D%E5%8A%A1%E7%AB%AFSSH%E7%9A%84%E9%85%8D%E7%BD%AE/image-20241026227436.png)
添加
![image-202410262254445.png|250](00_sync/Linux%E5%92%8CWIN%E4%B8%8A%E7%9A%84%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%9C%8D%E5%8A%A1%E7%AB%AFSSH%E7%9A%84%E9%85%8D%E7%BD%AE/Linux%E5%92%8CWIN%E4%B8%8A%E7%9A%84%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%9C%8D%E5%8A%A1%E7%AB%AFSSH%E7%9A%84%E9%85%8D%E7%BD%AE/image-202410262254445.png)
我足足下了半个小时，，，然后重启，是否自动开启开个人
![image-202410264817776.png|275](00_sync/Linux%E5%92%8CWIN%E4%B8%8A%E7%9A%84%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%9C%8D%E5%8A%A1%E7%AB%AFSSH%E7%9A%84%E9%85%8D%E7%BD%AE/Linux%E5%92%8CWIN%E4%B8%8A%E7%9A%84%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%9C%8D%E5%8A%A1%E7%AB%AFSSH%E7%9A%84%E9%85%8D%E7%BD%AE/image-202410264817776.png)
但是这个端口确实是很危险的端口，如果你本身密码就比较弱，又恰好有ipv6暴露的可能，配合上防火墙做好措施才是理智的
建议更换端口，不然是非常非常不安全的
![image-202410261142970.png|450](00_sync/Linux%E5%92%8CWIN%E4%B8%8A%E7%9A%84%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%9C%8D%E5%8A%A1%E7%AB%AFSSH%E7%9A%84%E9%85%8D%E7%BD%AE/Linux%E5%92%8CWIN%E4%B8%8A%E7%9A%84%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%9C%8D%E5%8A%A1%E7%AB%AFSSH%E7%9A%84%E9%85%8D%E7%BD%AE/image-202410261142970.png)
![image-202410265935891.png|475](00_sync/Linux%E5%92%8CWIN%E4%B8%8A%E7%9A%84%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%9C%8D%E5%8A%A1%E7%AB%AFSSH%E7%9A%84%E9%85%8D%E7%BD%AE/Linux%E5%92%8CWIN%E4%B8%8A%E7%9A%84%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%9C%8D%E5%8A%A1%E7%AB%AFSSH%E7%9A%84%E9%85%8D%E7%BD%AE/image-202410265935891.png)
成功ipv4
![image-2024102615661.png|375](00_sync/Linux%E5%92%8CWIN%E4%B8%8A%E7%9A%84%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%9C%8D%E5%8A%A1%E7%AB%AFSSH%E7%9A%84%E9%85%8D%E7%BD%AE/Linux%E5%92%8CWIN%E4%B8%8A%E7%9A%84%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%9C%8D%E5%8A%A1%E7%AB%AFSSH%E7%9A%84%E9%85%8D%E7%BD%AE/image-2024102615661.png)
成功ipv6
![image-202410261316308.png](00_sync/Linux%E5%92%8CWIN%E4%B8%8A%E7%9A%84%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%9C%8D%E5%8A%A1%E7%AB%AFSSH%E7%9A%84%E9%85%8D%E7%BD%AE/Linux%E5%92%8CWIN%E4%B8%8A%E7%9A%84%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%9C%8D%E5%8A%A1%E7%AB%AFSSH%E7%9A%84%E9%85%8D%E7%BD%AE/image-202410261316308.png)
linux可以scp传输给win了
![image-20241026326779.png|500](00_sync/Linux%E5%92%8CWIN%E4%B8%8A%E7%9A%84%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%9C%8D%E5%8A%A1%E7%AB%AFSSH%E7%9A%84%E9%85%8D%E7%BD%AE/Linux%E5%92%8CWIN%E4%B8%8A%E7%9A%84%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%9C%8D%E5%8A%A1%E7%AB%AFSSH%E7%9A%84%E9%85%8D%E7%BD%AE/image-20241026326779.png)
![image-20241026335690.png|450](00_sync/Linux%E5%92%8CWIN%E4%B8%8A%E7%9A%84%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%9C%8D%E5%8A%A1%E7%AB%AFSSH%E7%9A%84%E9%85%8D%E7%BD%AE/Linux%E5%92%8CWIN%E4%B8%8A%E7%9A%84%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%9C%8D%E5%8A%A1%E7%AB%AFSSH%E7%9A%84%E9%85%8D%E7%BD%AE/image-20241026335690.png)
