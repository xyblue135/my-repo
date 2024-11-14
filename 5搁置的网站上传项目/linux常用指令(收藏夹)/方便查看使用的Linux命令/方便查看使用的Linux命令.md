# 查看功率
## powerstat
```
sudo apt install powerstat
sudo powerstat
```
powerstat是测量电池功耗的,需要把电池拔了,这里面我测了一个我的平板,还有一个笔记本.(都是息屏状态),功耗真的低
```
sudo apt install powerstat
sudo powerstat   
#这款包测得是电池的一款时间的cpu功率，必须用电池的才可以。
```
![image-20242131212127.png|52](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/2023_7_31方便查看使用的Linux命令/image-20242131212127.png)![image-20242131342587.png|394](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/2023_7_31方便查看使用的Linux命令/image-20242131342587.png)
## s-tui
```
sudo s-tui
```
![image-2024213178133.png|725](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/2023_7_31方便查看使用的Linux命令/image-2024213178133.png)
## acpi
```
sudo acpi -V
```
![image-2024213160901.png|575](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/2023_7_31方便查看使用的Linux命令/image-2024213160901.png)
## powertop
```
sudo powertop
# 注意:为热量单位
```
![image-2024213149929.png|675](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/2023_7_31方便查看使用的Linux命令/image-2024213149929.png)

# 查看/更改cpu频率
## 查看cpu频率 
```
sudo apt install cpufrequtils
cpufreq-info
```
这个貌似频率会不太准,建议使用实时监测的.
![image-20242185917553.png](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/方便查看使用的Linux命令/image-20242185917553.png)
## 更改cpu频率
```
`sudo cpufreq-set -g performance`  
`sudo cpufreq-set -g powersave` # 一共有很多种模式，但是也需要支持才可以，比如我的cpufreq-info只有两种模式
性能大概在4.5GHZ,省电在800MHZ-3GHZ浮动
```
![image-202421813115.png](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/方便查看使用的Linux命令/image-202421813115.png)

## 实时查看cpu频率
```
sudo apt install linux-tools-common
```
 如果跟我一样出现错误，请按照指示下载对应的linux-tools，如我按照指示安装即可。
![image-2024214150766.png](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/2023_7_31方便查看使用的Linux命令/image-2024214150766.png)
 按照提示来下载
```
sudo apt install linux-tools-6.5.0-17-generic 
```
紧接着就可以使用命令查看了
```
watch -n 1 sudo cpupower monitor
```
![image-2024214247552.png|575](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/2023_7_31方便查看使用的Linux命令/image-2024214247552.png)
# 检测温度
这个应该很熟悉了
```
sudo apt install sensors
```
![image-2024213502510.png|300](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/2023_7_31方便查看使用的Linux命令/image-2024213502510.png)
# 休眠挂载内存/硬盘
```
sudo systemctl suspend   #挂载到内存，极速开机
sudo systemctl hibernate  ##需要Swap分区才可以,挂载到硬盘，不极速开机，但是现在毕竟固态了，比以前机械快多了。
```
![image-2024218821955.png|625](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/方便查看使用的Linux命令/image-2024218821955.png)
# 看端口状态
```
sudo lsof -i :5000
```
```
sudo lsof -i :5000   #这个命令使用 lsof 工具来查看所有正在使用端口 5000 的进程情况。lsof 是 "list open files" 的缩写，可以列出系统当前打开的文件、目录和网络连接等信息
sudo netstat -tuln | grep 5000 #使用 netstat 工具来显示网络状态信息，其中 `-tuln` 参数表示显示 TCP 连接、UDP 连接、监听状态，并且以数字形式显示端口号。通过管道 `|` 和 `grep 5000`，筛选出包含 "5000" 的行，即端口为 5000 的相关信息。
	sudo ss -tuln | grep 5000 使用 netstat 工具来显示网络状态信息，其中 `-tuln` 参数表示显示 TCP 连接、UDP 连接、监听状态，并且以数字形式显示端口号。通过管道 `|` 和 `grep 5000`，筛选出包含 "5000" 的行，即端口为 80 的相关信息。
```
![image-202421812178.png](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/方便查看使用的Linux命令/image-202421812178.png)
PS:`netstat` 和 `ss` 命令默认不会显示与监听端口关联的进程信息。它们只显示网络相关的信息，而不包括进程信息。SS有个128是可以连接的最大数量。
示例1
![image-202421421876.png](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/2023_7_31方便查看使用的Linux命令/image-202421421876.png)
示例2
![image-20242181550959.png](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/方便查看使用的Linux命令/image-20242181550959.png)
# 挂起进程
## nohup
以下命令将使用nohup进行挂起，但是我不怎么用这个，因为一但SSH断开连接也将无法使用jobs看到挂起的进程。更推荐加入启动项和tmux
```
sudo nohup /usr/bin/frpc -c /usr/bin/frpc-99wol.ini &
sudo nohup python3 app.py &
sudo nohup ./start.sh &
sudo jobs #查看进程
jobs  #查看进程
```
## nohup进程查看
关闭jobs
```
kill %3
kill -9 %3
sudo kill -9 `jobs -p %3`
```
命令首先使用 `jobs -p %3` 找到作业号为3的进程的PID，然后将该PID传递给 `kill` 命令来终止该进程。

# Tmux
这里只介绍一部分，其它的在我另外一篇文章有全命令
## 创建会话
```
tmux
tmux new -s 名字
```
## 离开会话
```
ctrl+b  d     #分离会话
```
## 删除会话
```
ctrl+d                         #删除会话
tmux kill-session -t 会话名字
```
## 查看/重新连接会话
```
ctrl+b  s
tmux ls
tmux attach -t 名称      #重新连接会话
```
## 更改会话名字
```
首先连接原始会话，并ctrl+b $即可
```
## 多窗口
```
ctrl+b c     #创建新窗口  creat
ctrl+b p     #切换上一个窗口  previous
ctrl+b n     #切换下一个窗口 next
ctrl+b w     #从列表中选择窗口，上下左右选择  windows
ctrl+b ，#    窗口重命名
```
## 多窗格
```
ctrl+b %     #左右划分
ctrl+b "     #上下划分
ctrl+b <arrow key>     #光标切换窗格
ctrl+b z     #当前窗格全屏显示
ctrl+b x     #关闭当前窗格
------以下两个命令不建议使用了,很容易记混-------------
ctrl+b ;     #切换上一个窗口
ctrl+b o     #切换下一个窗口
```
# 开机启动项
## 方法一：systemed系统
如果不知道，可以通过命令验证是否为systemed系统
```
systemctl --version
```
![image-2024220488551.png](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/方便查看使用的Linux命令/image-2024220488551.png)
我需要创建的服务单元的名字为1palworld,注意后缀，不能为sh
```
sudo vim /etc/systemd/system/1palworld.service
```
输入
```
[Unit]

Description=Run a Custom Script at Startup

After=default.target


[Service]

ExecStart=/mnt/2shjiaoben/1si_chuang_ko/palworld_si_jiaoben.sh


[Install]

WantedBy=default.target                     
```
- `Description`：描述服务的简短说明。
- `After`：指定服务所依赖的其他单元，这里使用 `network.target` 表示需要在网络可用后启动。
- `ExecStart`：指定要运行的脚本或命令的路径。在这里，我们使用 `/bin/bash` 来执行 Bash 脚本，并使用 `-c` 参数来执行命令字符串。
- ~~`WorkingDirectory`：指定服务运行时的工作目录。~~ # 可以省略
- `Restart`：指定服务在退出后是否自动重启。  # 可以省略
- `WantedBy`：指定服务所属的启动级别。
给以权限
```
sudo chmod -x 
```
重新启动配置
```
sudo systemctl daemon-reload     #systemctl daemon-reload
```
启动服务
```
sudo systemctl start 1palworld.service
sudo systemctl enable 1palworld.service  #加入启动项
```
可以看到我这边启动失败了，因为我使用了tmux的sh使用了tmux的窗口
```
systemctl list-units --type=service  #查看服务
sudo journalctl -u 1palworld.service  #查看日志
```
![image-20242202819636.png](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/方便查看使用的Linux命令/image-20242202819636.png)
这样的话我们需要一个伪终端来使用
```
[Unit]
Description=Run a Custom Script at Startup
After=default.target

[Service]
Type=forking
ExecStart=/usr/bin/tmux new-session -d -s palworld '/mnt/2shjiaoben/1si_chuang_ko/palworld_si_jiaoben.sh'

[Install]
WantedBy=default.target
```
使用了`Type=forking`以表示服务以forking方式启动。在`ExecStart`行中，我们使用了`/usr/bin/tmux new-session -d -s palworld`命令来创建一个名为`palworld`的tmux会话，并在其中运行脚本`/mnt/2shjiaoben/1si_chuang_ko/palworld_si_jiaoben.sh`。这将在后台创建tmux会话并运行脚本。
删除启动项目 停止-禁用（防止自加载）-删除 重加载服务
```
sudo systemctl stop 1palworld.service
sudo systemctl disable 1palworld.service
sudo rm /etc/systemd/system/1palworld.service
sudo systemctl daemon-reload
```
至此，systemed的启动项就结束了
## 方法二 RCON
cron table
**/etc/crontab：** 这是系统范围的 `cron` 配置文件，包含了系统的周期性任务和计划。
**/var/spool/cron/crontabs**,这是用户专属的
```
crontab -e  #编辑当前用户
sudo crontab -u username -e  #编辑其它用户
```
需要注意的是，虽然 `@reboot` 任务会在系统启动后执行，但它们可能会在其他系统服务完全初始化之前执行。因此，在撰写 `@reboot` 任务时，确保所需的系统资源和服务都已经准备就绪是很重要的。
# 启动/查看service
在 Systemd 中，服务单元的配置文件通常位于 `/etc/systemd/system` 或 `/usr/lib/systemd/system` 目录下，以 `.service` 扩展名结尾。这些配置文件中包含了服务的名称、描述、启动命令、依赖关系等信息。
```
systemctl start <service>      #启动一个服务
systemctl stop <service>       #停止一个服务
systemctl restart <service>    # 重启一个服务
systemctl status <service>    # 查看一个服务的状态等。
```
![image-2024218612155.png](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/方便查看使用的Linux命令/image-2024218612155.png)
## 查看所有service
```
systemctl list-units --type=service   # 列出所有正在运行的服务
systemctl list-unit-files --type=service  # 列出所有的服务
```
![image-202421991380.png](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/方便查看使用的Linux命令/image-202421991380.png)
# 查看安装的服务
```
service --status-all #方便看自己安装的
```
![image-202421995141.png](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/方便查看使用的Linux命令/image-202421995141.png)

# 日志监控

## tail
例:监控系统日志,显示最后十行
```
sudo tail /var/log/syslog   #查看系统日志
sudo tail -f /var/log/syslog  #实时查看系统日志
```
![image-20242183534552.png](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/方便查看使用的Linux命令/image-20242183534552.png)
## journalctl
```
sudo journalctl       #查看所有日志
sudo journalctl -f    #实时监控日志
sudo journalctl -u ssh.service   #查看特定单元的日志（例如，`ssh` 服务）
sudo journalctl --since "2024-02-17 00:00:00" --until "2024-02-18 00:00:00"  #查看特定时间范围内的日志
```
## 区别
tail看文件生成的那种舒服,journalctl看service那种舒服.
- `tail` 只能按行显示日志文件的内容，无法对日志进行过滤、搜索或解析。它简单实用，适用于查看文本日志的尾部。
- `journalctl` 允许你使用各种选项来过滤、搜索和解析日志。你可以根据不同的条件过滤日志，例如按时间范围、单元、日志级别等过滤。
- `tail` 是一个通用工具，在几乎所有的类 UNIX 系统中都可用，并且可以监控任何文本文件。
- `journalctl` 则是 `systemd` 的一部分，因此只能在使用 `systemd` 作为初始化系统的 Linux 发行版上使用。
# Top
传统top
![image-20242214114719.png](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/方便查看使用的Linux命令/image-20242214114719.png)
- **Shift + M：** 根据内存使用量进行排序，将内存使用最高的进程显示在顶部。
- **Shift + P：** 根据 CPU 使用率进行排序，将 CPU 使用率最高的进程显示在顶部。
- **Shift + T：** 根据运行时间进行排序，将运行时间最长的进程显示在顶部。
- **Shift + H：** 显示/隐藏帮助屏幕，其中包含更多的操作信息。
1. **htop**： `htop` 是 `top` 的增强版，提供了更加直观和交互式的界面。它允许用户通过鼠标或键盘进行交互，并提供了更多的功能，如在进程列表中显示树形结构、可视化显示 CPU 和内存使用情况等。
2. ![image-20242191335342.png](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/方便查看使用的Linux命令/image-20242191335342.png)
3. **glances**： `glances` 是一个功能丰富的系统监视工具，它可以显示有关 CPU、内存、磁盘、网络等各个方面的详细信息。与 `top` 和 `htop` 不同，`glances` 提供了一个全局的系统概览，并且可以通过 Web 接口进行远程访问。
4. ![image-20242191539315.png](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/方便查看使用的Linux命令/image-20242191539315.png)
5. **atop**： `atop` 提供了类似于 `top` 的实时性能监视功能，但它还可以记录系统活动的历史数据，以便后续分析。`atop` 可以显示有关 CPU、内存、磁盘、网络等方面的详细信息，并且可以根据不同的时间间隔进行数据记录。
6. ![image-20242191349571.png](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/方便查看使用的Linux命令/image-20242191349571.png)
7. **nmon**： `nmon` 是一个轻量级的系统监视工具，它可以显示有关 CPU、内存、磁盘、网络等方面的实时信息。`nmon` 提供了一个交互式的界面，用户可以使用键盘来切换不同的显示模式和详细信息。
![image-20242191636633.png](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/方便查看使用的Linux命令/image-20242191636633.png)
# 电池管理
```
who -b  #最后一次启动时间
uptime  #查看系统运行时间 
cat /etc/systemd/logind.conf   #查看电源管理设置
systemctl status systemd-logind.service  #查看当前的电源管理策略
```
# 彻底关闭眠、挂起、混合休眠等
```
systemctl status sleep.target  #查看电源状态
systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target
```
![image-202421923117.png](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/方便查看使用的Linux命令/image-202421923117.png)
恢复
```
sudo rm /etc/systemd/system/sleep.target /etc/systemd/system/suspend.target /etc/systemd/system/hibernate.target /etc/systemd/system/hybrid-sleep.target
# 可不输入此命令,为删除软链接
sudo systemctl unmask sleep.target suspend.target hibernate.target hybrid-sleep.target  #恢复默认状态
sudo systemctl daemon-reload
```
# 查看IO
```
sudo apt install iotop
sudo iotop
```
# touch
创建一个文件而不打开
如`touch 123.txt`
# 查看内存
```
free
free -h
```
# lscpu
查看超线程
![image-2024220433351.png](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/方便查看使用的Linux命令/image-2024220433351.png)

# 重新加载资源管理器/ systemd
```
sudo systemctl daemon-reload

```
# 查看发行版信息
```
cat /etc/lsb-release
```
![image-20242204328982.png](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/方便查看使用的Linux命令/image-20242204328982.png)
# 查看内核
```
uname -r
```
![image-20242204457306.png](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/方便查看使用的Linux命令/image-20242204457306.png)

# echo
输出
# head
默认输出为文本前10行,加管道可以任意设置
head [OPTION]... [FILE]...
```
head 123456.txt
head 5 123456.txt   #看前五行 
head -n 5 123456.txt   #看前五行  尽可能保留加参数-n的习惯,不然管道|不认的.
head -c 100 123456.txt   #看前100字节

echo "Hello World" | head -n 1   #打印echo的第一行

head 2 1.txt 2.txt  #看两个文本的前2行
head -n 2 1.txt 2.txt  #看两个文本的前2行

head -q 1.txt 2.txt   #不显示文件名字
```
# cat
最常见的,不用说,看文档的输出
```
cat 文件名
echo "Hello World" | cat -n
```
# more
分页看文档的,q为退出,Enter为向下滚动一行
```
more 123.txt
more -d filename.txt  #显示百分比信息,尽可能使用-d参数
head -n 100 123.txt | more  #more配合head只想看前100行,必须加-n的参数
```
# less 
可以上下滚动看文档我很喜欢,q为退出,也可以使用pgup和pgdn,`less [参数] 文件`
更多参数查看
https://www.runoob.com/linux/linux-comm-less.html
```
less 123.txt
```
PS查看你进程用less分页显示
```
ps -ef |less
```
查看命令历史使用记录并通过less分页显示
```
history | less
```
浏览多文件
```
less log2013.log log2014.log.
输入 ：n后，切换到 log2014.log  
输入 ：p 后，切换到log2013.log
```
文件查找/pattern，我的用不了，不知道为什么。
# ln 
创建硬链接和软链接(符号链接)的
硬链接指向同一文件的实际内容，但是具有不同的文件名和路径。对于硬链接，所有链接都指向相同的物理数据块，因此更改其中一个链接也会更改其他链接。硬链接不能链接目录，只能链接文件。
符号链接就是win的快捷方式
```
ln source_file target_file  #硬链接,别理解为ctrl+c和ctrl+v,因为这些文件会同步更改,且不占用磁盘可用空间 ,所以可以作增量存储
ln -s source_file target_file  #软链接
```
区别:
软链接（符号链接）的优点包括：
1. **跨文件系统**：软链接可以链接到另一个文件系统中的文件或目录，而硬链接不能跨越文件系统。
2. **灵活性**：软链接可以链接到不存在的目标，也可以链接到目录，而硬链接只能链接到文件。
3. **可读性**：软链接可以直观地显示链接的目标路径，便于理解。
缺点:
1. **依赖性**：软链接依赖于目标文件或目录的存在，如果目标文件被删除或移动，软链接可能会失效。
2. **性能开销**：访问软链接需要额外的系统调用和解析过程，可能会稍微降低性能。
相比之下，硬链接的优点是：
1. **节省磁盘空间**：硬链接不会占用额外的磁盘空间，因为所有链接共享相同的数据块。
2. **稳定性**：硬链接与原始文件之间的关联更为紧密，不存在软链接依赖目标文件的问题。
但是，硬链接也有一些限制：
1. **不能跨文件系统**：硬链接只能链接到同一文件系统中的文件。
2. **不适用于目录**：硬链接只能链接文件，不能链接目录。.

# Which
搜索系统的`PATH`环境变量中列出的目录，找到并显示与命令相关联的第一个实际可执行文件的路径。
![image-20242204417395.png](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/方便查看使用的Linux命令/image-20242204417395.png)
# Where
shell的内置命令，其功能类似于`which`命令，用于查找可执行文件的位置。但是，它并不是在所有的Unix系统中都可用。`whereis` 命令可能被错误地称为 `where`，`whereis` 用于定位二进制文件、源码文件以及帮助文件。
# Who
`who`命令用于显示当前登录系统的用户信息。它显示当前系统上所有已登录用户的列表，包括用户名、登录时间、登录的终端等信息。
![image-20242205451165.png](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/方便查看使用的Linux命令/image-20242205451165.png)
![image-20242205559987.png](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/方便查看使用的Linux命令/image-20242205559987.png)
# Find
`find` 是 Linux 和类 Unix 系统中的一个非常强大的命令，用于在文件系统中搜索文件和目录。`find` 命令可以根据指定的条件搜索文件，并执行相应的操作。
```
find [path...] [expression]
find /path/to/search -name "filename"  #搜名字
find /mnt -name '*Last*'   #模糊查找
```

```
find /path/to/search -type f  #搜类型，普通文件
find /path/to/search -perm 644  #搜权限
find /path/to/search -size +1M  #搜大小
find /path/to/search -type f -name "*.txt"   #组合搜索
```
# Vi和Vim
`vim` 是 `vi` 的增强版,都文本编辑器

# PS
```
ps
ps -aux  #查看所有进程
```
查看当前进程,用于显示当前正在运行的进程信息。它的名称来自于"process status"（进程状态）的缩写。
- `ps -e`或者`-a`#用惯了docker都习惯-a：显示所有进程，而不仅仅是当前终端会话的进程。
- `ps -f`：显示完整的进程信息，包括父进程的 PID、启动时间等。
- `ps -u`：显示与指定用户名关联的进程。
- `ps -aux`：显示所有进程的详细信息，通常与 `-e` 和 `-f` 选项一起使用。
- `ps -c`用的比较多![image-20242211824579.png](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/方便查看使用的Linux命令/image-20242211824579.png)
# pstree
```
pstree -apnh //显示进程间的关系
pstree -u //显示用户名称
```
![image-20242211550230.png](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/方便查看使用的Linux命令/image-20242211550230.png)
# free
看物理内存和swap交换分区的
```
free  #看内存的
free -h  #一般我经常用这个
```
-b 　以Byte为单位显示内存使用情况。 
-k 　以KB为单位显示内存使用情况。 
-m 　以MB为单位显示内存使用情况。
-g   以GB为单位显示内存使用情况。 
-o 　不显示缓冲区调节列。 
-s<间隔秒数> 　持续观察内存使用状况。 
-t 　显示内存总和列。 
-V 　显示版本信息。
# df
显示磁盘空间使用情况”Disk Free“
```
df
df -h  #一般用这个
df -l #只显示本地
还有很多参数
```
# du
看文件大小的
```
du
du -h #易读
du -s #显示统计
du -s -h #易读方式显示统计
```
# Chmod
提权
```
sudo chmod -R 777 /mnt
sudo chmod +x /mnt/123.sh
```
# 三巨头grep
(global regular expression) 命令用于查找文件里符合条件的字符串或正则表达式。
感觉这个用的挺少的,但是用好了就是三巨头
1、在文件 file.txt 中查找字符串 "hello"，并打印匹配的行：
```
grep hello file.txt
```
2、在文件夹 dir 中递归查找所有文件中匹配正则表达式 "pattern" 的行，并打印匹配行所在的文件名和行号：
```
grep -r -n pattern dir/
```
3、在标准输入中查找字符串 "world"，并只打印匹配的行数：
```
echo "hello world" | grep -c world
```
4、在当前目录中，查找后缀有 file 字样的文件中包含 test 字符串的文件，并打印出该字符串的行。此时，可以使用如下命令：
```
grep test *file
```
5、以递归的方式查找符合条件的文件。例如，查找指定目录/etc/acpi 及其子目录（如果存在子目录的话）下所有文件中包含字符串"update"的文件，并打印出该字符串所在行的内容，使用的命令为：
```
grep -r update /etc/acpi
```
# 三巨头se
```
seq 1 10   #生成1-10
seq -w 1 10  #生成宽度相等的序列数字
```
# 三巨头awk
用于处理文本数据的强大的文本处理工具和编程语言。它可以扫描文件，按照指定的模式匹配和处理文本行，并执行用户定义的操作。
行读取输入文本文件，将每行分割成字段，然后根据用户定义的规则和动作来处理这些字段。用户可以在 `awk` 中编写处理规则，利用条件语句、循环结构和内置函数来处理文本数据。
```
awk '{print $1, $3}' filename  #这将打印每行的第一个字段和第三个字段。
awk '{sum += $1} END {print sum}' filename  #这将计算文件中第一个字段的总和，并在处理完所有行后打印结果。
awk '/pattern/' filename  #这将打印文件中匹配指定模式的行。
awk -F':' '{print $1, $3}' filename  #这将使用 `:` 作为字段分隔符，打印每行的第一个字段和第三个字段。
```
# reboot
重启
# shutdown/poweroff
定时关机
```
shutdown -h +5  #5分钟后关机
shutdown -r +5   #5分钟后重启
shutdown -c   #取消延迟关机
```
`shutdown` 提供了更多的选项来安全地关闭系统，包括在一段时间后关闭，并向用户发送警告消息，而 `poweroff` 则直接关闭系统，没有提供任何延迟或警告。通常情况下，建议使用 `shutdown` 命令来关闭系统，以便让用户有足够的时间保存工作并退出系统。
# kill
配合ps aux ps-c来使用
![image-20242211813753.png](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/方便查看使用的Linux命令/image-20242211813753.png)
```
kill PID
kill -f PID #强制停止
kill -9 PID  #超强力终止
kill -SIGKILL PID  #超强力终止
kill -l 列出所有支持的信号
```
![image-20242211620443.png](5搁置的网站上传项目/linux常用指令(收藏夹)/方便查看使用的Linux命令/方便查看使用的Linux命令/image-20242211620443.png)
# RM
不用说,sudo rm -r /
# zip
打包zip
```
zip zipfile.zip file1 file2 file3   #将file1,2,3打包为zipfile.zip
zip -r zipfile.zip /mnt/directory/       #递归压缩目录
zip zipfile.zip newfile  #添加文件
unzip -l zipfile.zip  #列出压缩包的内容
unzip zipfile.zip   #解压压缩包
zip -e zipfile.zip 文件  #使用-e参数密码保护zip文件
```
# tar.gz
压缩
```
tar -zcvf archive.tar.gz file1 file2 directory
tar -zcvf archive.tar.gz file1 file2 directory
```
解压
```
tar -zxvf archive.tar.gz
```
查看,这个反正我是不怎么用了
```
tar -ztvf archive.tar.gz
```
- `-c`：创建归档文件。
- `-z`：使用 gzip 进行压缩。
- `-v`：显示详细的操作信息。
- `-f`：指定归档文件的名称。
# WC
用于统计的
```
wc [option] [file]
wc example.txt   #行数,单词和字符
wc -l example.txt  #单行数
```
- `-l`：统计行数（lines）。
- `-w`：统计单词数（words）。
- `-c`：统计字符数（bytes）。
- `-m`：统计字符数（characters）。
- `-L`：显示文件中最长行的长度（max line length）。
# CUT
提取每一行的第一个字符
```
cut [options] [file]
cut -f 1 -d ' ' data.txt
```
- `-c, --characters=LIST`：指定要提取的字符范围。例如，`-c 1-10` 将提取每行中的第 1 到第 10 个字符。
- `-f, --fields=LIST`：指定要提取的字段范围。字段以列（column）分隔符（默认为制表符）分隔。例如，`-f 1,3` 将提取每行中的第 1 和第 3 个字段。
- `-d, --delimiter=DELIM`：指定字段分隔符。默认情况下，字段分隔符为制表符。
- `--complement`：反选操作，即提取未指定字段或字符范围之外的内容。
# Man
一本手册
```
man ls  #有关 `ls` 命令的详细信息
man -k printf 列出包含关键字 `printf` 的所有命令的手册页面。
```
# Info
又是个帮助页面，感觉比Man好用
```
info(选项)(参数)
info info  #用info查看info的帮助文档
```
-d：添加包含info格式帮助文档的目录；
-f：指定要读取的info格式的帮助文档；
-n：指定首先访问的info帮助文件的节点； 
-o：输出被选择的节点内容到指定文件。
# Help
`help` 仅适用于 shell 内置命令,内置命令的实现是通过 C 语言或类似的语言编写的，并且包含在 Shell 解释器的源代码中。
1. **cd**：改变当前工作目录。
2. **echo**：在标准输出上打印文本。
3. **exit**：终止当前 Shell 进程。
4. **export**：设置或显示环境变量。
5. **pwd**：显示当前工作目录。
6. **unset**：取消设置的环境变量或 Shell 属性。
7. **alias**：定义或显示命令别名。
8. **type**：显示命令类型。
9. **history**：显示命令历史记录。
10. **source**（或`.`）：执行脚本文件中的命令。
11. **jobs**：列出后台作业。
12. **kill**：向进程发送信号以终止它们。
13. **readonly**：设置只读 Shell 变量。
14. **set**：设置 Shell 选项。
15. **shift**：向左移动命令行参数。
16. **umask**：设置默认文件权限掩码。
17. **wait**：等待后台作业完成。
# crontab 
cron table
**/etc/crontab：** 这是系统范围的 `cron` 配置文件，包含了系统的周期性任务和计划。
**/var/spool/cron/crontabs**,这是用户专属的
```
crontab -e  #编辑当前用户
sudo crontab -u username -e  #编辑其它用户
```






