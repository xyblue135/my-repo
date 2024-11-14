![image-202474323598.png](00_sync/00linux/Linux下的三种帮助命令/Linux下的三种帮助命令/image-202474323598.png)
exit is a shell bu
> **内建命令**实际上是 shell 程序的一部分，其中包含的是一些比较简单的 Linux 系统命令，这些命令是写在 bash 源码的 builtins 里面的，由 shell 程序识别并在 shell 程序内部完成运行，通常在 Linux 系统加载运行时 shell 就被加载并驻留在系统内存中。而且解析内部命令 shell 不需要创建子进程，因此其执行速度比外部命令快。比如：history、cd、exit 等等。
 
 vim is /usr/bin/vim
 ls is aliased to 'ls -- oclor =auto'
> **外部命令**是 Linux 系统中的实用程序部分，因为实用程序的功能通常都比较强大，所以其包含的程序量也会很大，在系统加载时并不随系统一起被加载到内存中，而是在需要时才将其调入内存。虽然其不包含在 shell 中，但是其命令执行过程是由 shell 程序控制的。外部命令是在 Bash 之外额外安装的，通常放在/bin，/usr/bin，/sbin，/usr/sbin 等等。比如：ls、vi 等。

# HELP
ls --help
who --help
# MAN
直接在手册上看的，这个看到的会比HELP更多
man ls
man who
man 没有内建与外部命令的区分，因为 man 工具是显示系统手册页中的内容，也就是一本电子版的字典
# info
信息量更大了 联网的百科全书.是 GNU 的超文本帮助系统，能够更完整的显示出 GNU 信息。所以得到的信息当然更多++
```
info sudo apt-get update 
sudo apt-get install info
info ls
```
