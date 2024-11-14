sudo apt remove 包名
sudo apt purge 包名 这个是彻底删除 不保留配置文件
sudo apt autoremove 不需要加包名 冗余包自动卸载
这个东西最烦的是下载一个df-h lsblk就会有这些
lsblk | grep -v 'snap'
df -h | grep -v 'snap'

| 工具             | 说明                                                |
| -------------- | ------------------------------------------------- |
| `install`      | 其后加上软件包名，用于安装一个软件包                                |
| `update`       | 从软件源镜像服务器上下载/更新用于更新本地软件源的软件包列表                    |
| `upgrade`      | 升级本地可更新的全部软件包，但存在依赖问题时将不会升级，通常会在更新之前执行一次 `update` |
| `dist-upgrade` | 解决依赖关系并升级（存在一定危险性）                                |
| `remove`       | 移除已安装的软件包，包括与被移除软件包有依赖关系的软件包，但不包含软件包的配置文件         |
| `autoremove`   | 移除之前被其他软件包依赖，但现在不再被使用的软件包                         |
| `purge`        | 与 remove 相同，但会完全移除软件包，包含其配置文件                     |
| `clean`        | 移除下载到本地的已经安装的软件包，默认保存在 `/var/cache/apt/archives/` |
| `autoclean`    | 移除已安装的软件的旧版本软件包                                   |


| 参数                   | 说明                                                                  |
| -------------------- | ------------------------------------------------------------------- |
| `-y`                 | 自动回应是否安装软件包的选项，在一些自动化安装脚本中使用这个参数将十分有用                               |
| `-s`                 | 模拟安装                                                                |
| `-q`                 | 静默安装方式，指定多个 `q` 或者 `-q=#`，`#` 表示数字，用于设定静默级别，这在你不想要在安装软件包时屏幕输出过多时很有用 |
| `-f`                 | 修复损坏的依赖关系                                                           |
| `-d`                 | 只下载不安装                                                              |
| `--reinstall`        | 重新安装已经安装但可能存在问题的软件包                                                 |
| `--install-suggests` | 同时安装 APT 给出的建议安装的                                                   |
|                      |                                                                     |
|                      |                                                                     |

重新安装
sudo apt-get --reinstall install --
更新软件源 sudo apt-get update 
升级没有依赖问题的软件包 sudo apt-get upgrade 
升级并解决依赖关系 sudo apt-get dist-upgrade


`apt` 和 `apt-get` 都是用于管理 Debian 和 Ubuntu 系统软件包的命令行工具，但它们之间有一些重要的区别。`apt` 是较新的工具，旨在统一和简化包管理命令，而 `apt-get` 是较老的工具，提供了更细粒度的控制


# dpkg 介绍

> dpkg 是 Debian 软件包管理器的基础，它被伊恩·默多克创建于 1993 年。dpkg 与 RPM 十分相似，同样被用于安装、卸载和供给和 .deb 软件包相关的信息。
> dpkg 本身是一个底层的工具。上层的工具，像是 APT，被用于从远程获取软件包以及处理复杂的软件包关系。"dpkg"是"Debian Package"的简写。

我们经常可以在网络上见到以`deb`形式打包的软件包，就需要使用`dpkg`命令来安装。

`dpkg`常用参数介绍：
```
|参数|说明|
|:--|:--|
|`-i`|安装指定 deb 包|
|`-R`|后面加上目录名，用于安装该目录下的所有 deb 安装包|
|`-r`|remove，移除某个已安装的软件包|
|`-I`|显示 `deb` 包文件的信息|
|`-s`|显示已安装软件的信息|
|`-S`|搜索已安装的软件包|
|`-L`|显示已安装软件包的目录信息|
```

# 修复依赖
我们先使用`apt-get`加上`-d`参数只下载不安装，下载 emacs 编辑器的 deb 包：
```bash
sudo apt-get update
sudo apt-get -d install -y emacs
```
下载完成后，我们可以查看/var/cache/apt/archives/目录下的内容，如下图：
![image-202475371045.png|425](1自用笔记无上传/安装参数(install%20remove%20purge%20clean)/安装参数（包含）/image-202475371045.png)
sudo cp emacs*.deb /home/emacs
![image-2024753844879.png](1自用笔记无上传/安装参数(install%20remove%20purge%20clean)/安装参数（包含）/image-2024753844879.png)
可以看到有五个，五个依赖?一个个使用dpkg将无法安装
![image-202475409335.png|425](1自用笔记无上传/安装参数(install%20remove%20purge%20clean)/安装参数（包含）/image-202475409335.png)
如何解决，使用
sudo apt-get -f install -y 
`sudo apt-get -f install -y` 是一个用于修复软件包依赖关系的命令
![image-2024754058312.png](1自用笔记无上传/安装参数(install%20remove%20purge%20clean)/安装参数（包含）/image-2024754058312.png)
安装成功
卸载：
sudo apt-get remove emacs
sudo apt-get purge emacs
