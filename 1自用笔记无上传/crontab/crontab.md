# 启动
sudo cron -f &
![image-20246232020125.png](1%E8%87%AA%E7%94%A8%E7%AC%94%E8%AE%B0%E6%97%A0%E4%B8%8A%E4%BC%A0/crontab/crontba/image-20246232020125.png)


“ % ” 在 crontab 文件中，有结束命令行、换行、重定向的作用，前面加 ” \ ” 符号转义，否则，“ % ” 符号将执行其结束命令行或者换行的作用，并且其后的内容会被做为标准输入发送给前面的命令。

看crontab 进程

ps aux | grep cron
pgrep cron


危险：
crontab -l  查看当前用户的定时任务 
crontab -r 永远不要执行，这是删除所有定时任务

危险：
crontab目录
`/etc/crontab`
1. `/etc/cron.daily`，目录下的脚本会每天执行一次，在每天的 6 点 25 分时运行；
2. `/etc/cron.hourly`，目录下的脚本会每个小时执行一次，在每小时的 17 分钟时运行；
3. `/etc/cron.monthly`，目录下的脚本会每月执行一次，在每月 1 号的 6 点 52 分时运行；
4. `/etc/cron.weekly`，目录下的脚本会每周执行一次，在每周第七天的 6 点 47 分时运行；