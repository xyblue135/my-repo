在 UNix/Linux 中比较流行的常见的 Shell 有 bash、 zsh、ksh、csh 等等， Ubuntu 终端默认使用的是 bash，默认的桌面环境是 GNOME 或者 Unity （基于 GNOME），但我们的环境中使用的分别是 zsh 和 xfce。
# 查看
```
查看shell版本
cat /etc/shells 
```

通过环境变量查看默认shell
```
echo $HOME
echo $SHELL
```
![image-20246191545214.png|400](1%E8%87%AA%E7%94%A8%E7%AC%94%E8%AE%B0%E6%97%A0%E4%B8%8A%E4%BC%A0/sh%E8%84%9A%E6%9C%AC/sh%E8%84%9A%E6%9C%AC/image-20246191545214.png)
# 示例1
在文本中sh，或者直接echo完下面这些
```
#!/bin/bash
echo "请输入姓名"
read name
echo "您好，$name"
```
![image-20247285822292.png|450](1%E8%87%AA%E7%94%A8%E7%AC%94%E8%AE%B0%E6%97%A0%E4%B8%8A%E4%BC%A0/sh%E8%84%9A%E6%9C%AC/sh%E8%84%9A%E6%9C%AC/image-20247285822292.png)
# 示例2
给参数传递文本变量信息  对应sh里面的$1 $2
```
#!/bin/bash
echo "请输入姓名"
name=$1
channel=$2
echo "您好，$name 欢迎来到 $channel"
```
运行的时候直接./sh脚本 第一个变量 第二个变量   就对应上1和2参数了
![image-20246193439746.png|300](1%E8%87%AA%E7%94%A8%E7%AC%94%E8%AE%B0%E6%97%A0%E4%B8%8A%E4%BC%A0/sh%E8%84%9A%E6%9C%AC/sh%E8%84%9A%E6%9C%AC/image-20246193439746.png)
# 更多参数示例
![image-2024619543142.png|275](1%E8%87%AA%E7%94%A8%E7%AC%94%E8%AE%B0%E6%97%A0%E4%B8%8A%E4%BC%A0/sh%E8%84%9A%E6%9C%AC/sh%E8%84%9A%E6%9C%AC/image-2024619543142.png)

# 暂时环境变量 
普通变量配合expect添加暂时的环境变量，退出回话就没了
![image-2024619845371.png](1%E8%87%AA%E7%94%A8%E7%AC%94%E8%AE%B0%E6%97%A0%E4%B8%8A%E4%BC%A0/sh%E8%84%9A%E6%9C%AC/sh%E8%84%9A%E6%9C%AC/image-2024619845371.png)

# 永久环境变量
bash的永久变量
![image-20246194329787.png](1%E8%87%AA%E7%94%A8%E7%AC%94%E8%AE%B0%E6%97%A0%E4%B8%8A%E4%BC%A0/sh%E8%84%9A%E6%9C%AC/sh%E8%84%9A%E6%9C%AC/image-20246194329787.png)
![image-2024619508124.png|400](1%E8%87%AA%E7%94%A8%E7%AC%94%E8%AE%B0%E6%97%A0%E4%B8%8A%E4%BC%A0/sh%E8%84%9A%E6%9C%AC/sh%E8%84%9A%E6%9C%AC/image-2024619508124.png)
可能有的需要重新生效一下
source bash.bashrc 或者..bash.bashrc
![image-2024619524290.png|475](1%E8%87%AA%E7%94%A8%E7%AC%94%E8%AE%B0%E6%97%A0%E4%B8%8A%E4%BC%A0/sh%E8%84%9A%E6%9C%AC/sh%E8%84%9A%E6%9C%AC/image-2024619524290.png)
# 命令简化alias
![image-20246191212326.png|450](1%E8%87%AA%E7%94%A8%E7%AC%94%E8%AE%B0%E6%97%A0%E4%B8%8A%E4%BC%A0/sh%E8%84%9A%E6%9C%AC/sh%E8%84%9A%E6%9C%AC/image-20246191212326.png)
输出公式里面的变量
随机输出1-10 
![image-20246191443115.png|450](1%E8%87%AA%E7%94%A8%E7%AC%94%E8%AE%B0%E6%97%A0%E4%B8%8A%E4%BC%A0/sh%E8%84%9A%E6%9C%AC/sh%E8%84%9A%E6%9C%AC/image-20246191443115.png)
![image-20246191454226.png|425](1%E8%87%AA%E7%94%A8%E7%AC%94%E8%AE%B0%E6%97%A0%E4%B8%8A%E4%BC%A0/sh%E8%84%9A%E6%9C%AC/sh%E8%84%9A%E6%9C%AC/image-20246191454226.png)
# 用户赋值read 
read是赋值给一个变量的
![image-202461917595.png](1%E8%87%AA%E7%94%A8%E7%AC%94%E8%AE%B0%E6%97%A0%E4%B8%8A%E4%BC%A0/sh%E8%84%9A%E6%9C%AC/sh%E8%84%9A%E6%9C%AC/image-202461917595.png)
# if语句
if语句 注意空格
```
if [[ ]];then
        echo "猜对了"
fi
```
![image-20246191944227.png|375](1%E8%87%AA%E7%94%A8%E7%AC%94%E8%AE%B0%E6%97%A0%E4%B8%8A%E4%BC%A0/sh%E8%84%9A%E6%9C%AC/sh%E8%84%9A%E6%9C%AC/image-20246191944227.png)
![image-20246191928533.png|350](1%E8%87%AA%E7%94%A8%E7%AC%94%E8%AE%B0%E6%97%A0%E4%B8%8A%E4%BC%A0/sh%E8%84%9A%E6%9C%AC/sh%E8%84%9A%E6%9C%AC/image-20246191928533.png)



# 关于
|          |                                                           |
| -------- | --------------------------------------------------------- |
| `set`    | 显示当前 Shell 所有变量，包括其内建环境变量（与 Shell 外观等相关），用户自定义变量及导出的环境变量。 |
| `env`    | 显示与当前用户相关的环境变量，还可以让命令在指定环境中运行。                            |
| `export` | 显示从 Shell 中导出成环境变量的变量，也能通过它将自定义变量导出为环境变量。                 |
|          |                                                           |
![image-2024712124876.png](1%E8%87%AA%E7%94%A8%E7%AC%94%E8%AE%B0%E6%97%A0%E4%B8%8A%E4%BC%A0/sh%E8%84%9A%E6%9C%AC/sh%E8%84%9A%E6%9C%AC/image-2024712124876.png)

环境变量的目录
```
ubuntu@VM-8-3-ubuntu:~$ echo $PATH
/home/ubuntu/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
ubuntu@VM-8-3-ubuntu:~$
```
# vimdiff使用
![image-2024712459931.png](1%E8%87%AA%E7%94%A8%E7%AC%94%E8%AE%B0%E6%97%A0%E4%B8%8A%E4%BC%A0/sh%E8%84%9A%E6%9C%AC/sh%E8%84%9A%E6%9C%AC/image-2024712459931.png)
# 永久变量位置
`/etc/bashrc`（有的 Linux 没有这个文件） 和 `/etc/profile` ，它们分别存放的是 shell 变量和环境变量。还有要注意区别的是每个用户目录下的一个隐藏文件：
# 用户的变量位置
这个 .profile 只对当前用户永久生效。因为它保存在当前用户的 Home 目录下，当切换用户时，工作目录可能一并被切换到对应的目录中，这个文件就无法生效。而写在 `/etc/profile` 里面的是对所有用户永久生效，所以如果想要添加一个永久生效的环境变量，只需要打开 `/etc/profile`，在最后加上你想添加的环境变量就好啦。
![image-202471288877.png](1%E8%87%AA%E7%94%A8%E7%AC%94%E8%AE%B0%E6%97%A0%E4%B8%8A%E4%BC%A0/sh%E8%84%9A%E6%9C%AC/sh%E8%84%9A%E6%9C%AC/image-202471288877.png)
# 查看环境变量
echo $PATH