# 引入
	Linux加载后，它将初始化硬件和设备驱动，然后运行第一个进程init，init根据配置文件继续引导进程，而通常情况下，修改放置在
```
/etc/rc
/etc/rc.d
/etc/rc?.d
```
![image-20242204456379.png](00_sync/00linux/Linux配置开机启动项的三种方法/Linux配置开机启动项的三种方法/image-20242204456379.png)
# systemed

如果不知道，可以通过命令验证是否为systemed系统
```
systemctl --version
```
![image-20242204136715.png](00_sync/00linux/Linux配置开机启动项的三种方法/Linux配置开机启动项的三种方法/image-20242204136715.png)
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
- `ExecStart`：指定要运行的脚本或命令的路径。在这里，我们使用 `/bin/bash` 来执行 Bash 脚本，并使用 `-c` 参数来执行命令字符串。-+
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
sudo systemctl start 1palworld.service  #检测能否正常运行
sudo systemctl enable 1palworld.service  #加入启动项
```
![image-20242212254975.png](00_sync/00linux/Linux配置开机启动项的三种方法/Linux配置开机启动项的三种方法/image-20242212254975.png)
```
systemctl list-units --type=service  #查看服务
sudo journalctl -u 1palworld.service  #查看日志
```
![image-20242204145620.png](00_sync/00linux/Linux配置开机启动项的三种方法/Linux配置开机启动项的三种方法/image-20242204145620.png)
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
`sudo systemctl start 1palworld.service`
至此，systemed的启动项就结束了
# Crontab【喜欢】
cron table
**/etc/crontab：** 这是系统范围的 `cron` 配置文件，包含了系统的周期性任务和计划。
**/var/spool/cron/crontabs**,这是用户专属的
```
crontab -e  #编辑当前用户
sudo crontab -u username -e  #编辑其它用户
需要注意的是，虽然 `@reboot` 任务会在系统启动后执行，但它们可能会在其他系统服务完全初始化之前执行。因此，在撰写 `@reboot` 任务时，确保所需的系统资源和服务都已经准备就绪是很重要的。
# RC
`/etc/rc.d/rc.local` 文件会在 Linux 系统各项服务都启动完毕之后再被运行。所以你想要自己的脚本在开机后被运行的话，可以将自己脚本路径加到该文件里。
```

![image-202422173958.png|400](00_sync/00linux/Linux配置开机启动项的三种方法/Linux配置开机启动项的三种方法/image-202422173958.png)
# rc.local

`rc.local` 是一个特殊的脚本，它通常位于 `/etc/rc.local` 或 `/etc/rc.d/rc.local`，用于执行开机启动任务。这个脚本会在系统启动完成前执行。您可以在这个脚本中添加需要启动的程序或脚本。

# 自定义脚本

在 `/etc/profile` 或 `/etc/environment` 中添加命令来启动程序。这些脚本会在用户登录时执行，但不适合用来启动系统服务。