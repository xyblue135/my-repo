alias：仅在当前 shell 会话中有效，并且只影响命令行的输入。它不会改变环境变量的值。
export：设置的环境变量不仅在当前 shell 会话中有效，而且会影响到子进程。例如，当你运行一个程序时，该程序会继承这些环境变量。
# Linux
## alias别名
自带的alias有这7个
grep 筛选 egrep支持正则表达式 fgrep仅支持固定字符串 la ls+隐藏文件的展示
![image-20241028192419.png|500](00_sync/00linux/Linux和Win下alias定义别名和export变量/Linux和Win下alias定义别名变量/image-20241028192419.png)
### 临时定义
双引号也可以
```
alias d='docker ps -a'
```
![image-202410282552698.png|525](00_sync/00linux/Linux和Win下alias定义别名和export变量/Linux和Win下alias定义别名变量/image-202410282552698.png)
### 取消变量
```
unalias 名字
```
![image-202410282929367.png](00_sync/00linux/Linux和Win下alias定义别名和export变量/Linux和Win下alias定义别名变量/image-202410282929367.png)

### 修改用户的alias
这边存储变量常见的有六个，这里我就放了一个
```
cat ~/.bashrc
nano ~/.bashrc
source ~/.bashrc
```
推荐在这里添加 # some more lsC  注意变量后面跟空格连着呢
```
alias ffmpeg='/home/0000/soft/ffmpeg/ffmpeg-6.0.1-amd64-static/ffmpeg'
alias dps='sudo docker ps --format "table {{.ID}}\t{{.Image}}\t{{.Ports}}\t{{.Status}}\t{{.Names}}" -a'
```
![image-202410283318838.png](00_sync/00linux/Linux和Win下alias定义别名和export变量/Linux和Win下alias定义别名变量/image-202410283318838.png)

### 示例
比如打这条过滤的docker的ps命令是很麻烦的, 这里就将重要东西提前了
```
alias dps='sudo docker ps --format "table {{.ID}}\t{{.Image}}\t{{.Ports}}\t{{.Status}}\t{{.Names}}" -a'
```
![image-202410283734274.png](00_sync/00linux/Linux和Win下alias定义别名和export变量/Linux和Win下alias定义别名变量/image-202410283734274.png)
1. **格式化模板**：
    - `{{.ID}}`：容器的 ID。
    - `{{.Image}}`：容器使用的镜像。
    - `{{.Ports}}`：容器映射的端口。
    - `{{.Status}}`：容器的状态。
    - `{{.Names}}`：容器的名称。
2. **`\t`**：
    - `\t` 是制表符（Tab），用来分隔每一列的内容。
## export变量
### 单个
```
export http_proxy="http://127.0.0.1:7890"
export https_proxy="http://127.0.0.1:7890"
```
如果用alias是完全不行的，变量和别名完全不一样
![image-20241153837281.png|425](00_sync/00linux/Linux和Win下alias定义别名和export变量/Linux和Win下alias定义别名和export变量/image-20241153837281.png)
持久化的话，跟alias一样，去改~/bash等
```
~/.bashrc
```
### 追加目录
```
个人推荐下面这个一个
这个是追加到末尾的↓
export PATH=$PATH:/usr/local/cuda-12.6/bin
追加到前面
export PATH=/usr/local/cuda-12.6/bin:$PATH



追加到前面，并且具有判断
export PATH=/usr/local/cuda-12.6/bin${PATH:+:${PATH}}
使用 ${PATH:+:${PATH}} 语法的好处在于它可以确保在拼接 PATH 时，即使 PATH 变量为空，也不会在结果中引入多余的冒号。例如，如果直接写成 export PATH=/usr/local/cuda-12.6/bin:$PATH，当 PATH 为空时，结果会变成 export PATH=/usr/local/cuda-12.6/bin:，这样会在 PATH 的末尾多出一个不必要的冒号。
```
### 区别
export jieya="/home/jieya"：适用于存储路径信息或在脚本中引用路径，便于管理和修改。
export PATH=$PATH:/home：适用于需要频繁使用的**可执行文件**，使得这些文件可以在任何地方直接调用。


也就是说如果我哦有一个start.sh，在/home里面，我要是使用
export jieya="/home/jieya  我直接 jieya   123.tar.gz  是不能用的
export PATH=$PATH:/home 我直接 jieya   123.tar.gz  是可以正确执行的,**所以这个适合放一些可执行文件**
# 其它
## 还有一个推荐的办法$PATH【将程序放到/usr/bin】
`/usr/bin` 通常包含在 `PATH` 环境变量中，这样系统在执行命令时会自动搜索该目录。`PATH` 变量包含多个目录，当你在命令行输入命令时，系统会按照 `PATH` 中的顺序查找可执行文件。
```
echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin
看到这上面的顺序，如果变量名字相同，从这个上面递归
```
`/usr/bin` 本身不是一个环境变量，但它是许多环境变量（如 `PATH`）的一部分，影响程序的执行和命令的查找。
创建的符号链接可以被任何脚本或程序直接调用，就像调用系统自带的命令一样。
**可能会造成冲突**：如果系统中已经存在同名的命令或链接，可能会导致冲突。



# WIN
查看环境变量
![image-202410314553309.png](00_sync/00linux/Linux和Win下alias定义别名和export变量/Linux和Win下alias定义别名变量/image-202410314553309.png)
不推荐命令行的添加了，其实不太方便也不安全
![image-202410314838384.png](00_sync/00linux/Linux和Win下alias定义别名和export变量/Linux和Win下alias定义别名变量/image-202410314838384.png)