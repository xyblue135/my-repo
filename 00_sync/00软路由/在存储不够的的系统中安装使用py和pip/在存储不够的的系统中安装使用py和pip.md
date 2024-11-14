# 软路由
## 安装包管理工具

首先我们更新一下包管理器，由于我使用的是openwrt，所以包管理器为opkg，不同linux有着不同的管理工具，如apt-get,yum,dnf等等
```
opkg updata
opkg install python3
python --version
```
来查看我们的python版本
![123|450](00_sync/00软路由/在存储不够的的系统中安装使用py和pip/在存储不够的的系统中安装使用py和pip/2023_10_10在软硬路由的系统中安装使用py_pip_脚本/Pastedimage20231119162052.png)
但是pip目前还没有安装 如果有wget的命令的话，那更为方便
```
https://pypi.org/project/pip/#files
```
在这个网站找到合适的pip版本并下载。
![123|275](00_sync/00软路由/在存储不够的的系统中安装使用py和pip/在存储不够的的系统中安装使用py和pip/2023_10_10在软硬路由的系统中安装使用py_pip_脚本/Pastedimage20231119162856.png)

然后通过scp或者web等将其放入到路由器的存储中
```
cd /tmpupload
tar -zxvf pip-23.3.1.tar.gz
```
![123|275](00_sync/00软路由/在存储不够的的系统中安装使用py和pip/在存储不够的的系统中安装使用py和pip/2023_10_10在软硬路由的系统中安装使用py_pip_脚本/Pastedimage20231119163144.png)
解压出来后，我们就可以执行此命令安装pip了
```
python setup.py install
```
![123|375](00_sync/00软路由/在存储不够的的系统中安装使用py和pip/在存储不够的的系统中安装使用py和pip/2023_10_10在软硬路由的系统中安装使用py_pip_脚本/Pastedimage20231119163352.png)
如果你安装失败，可能是缺少setuptools 需要下载拷贝进来并解压使用
https://pypi.org/project/pip/#files
```
python setup.py install
```
来安装setuptools即可，这边可以看到pip的命令可以使用了，但这里显示的并不是所有包。
![123|250](00_sync/00软路由/在存储不够的的系统中安装使用py和pip/在存储不够的的系统中安装使用py和pip/2023_10_10在软硬路由的系统中安装使用py_pip_脚本/7.1.png)
我们可以在这里查看系统范围全局的python包
```
cd /usr/lib/python3.10/site-packages
```
![123|600](00_sync/00软路由/在存储不够的的系统中安装使用py和pip/在存储不够的的系统中安装使用py和pip/2023_10_10在软硬路由的系统中安装使用py_pip_脚本/Pastedimage20231119163926.png)
用户级别的在
```
cd /.local/lib/python<version>/site-packages
```
然后我们验证下pip可不可以使用。
![123](00_sync/00软路由/在存储不够的的系统中安装使用py和pip/在存储不够的的系统中安装使用py和pip/2023_10_10在软硬路由的系统中安装使用py_pip_脚本/Pastedimage20231119164123.png)
ok
# 只有RAM的路由
就是如果我们刷机传统路由器的话，非x86框架。比我的128MB内存是没办法安装完整版的py的，而且重启后数据也会丢失，但如果不编译内核的话，可以考虑此方法使用python这边我用的老毛子的padavan进行演示。
![123](00_sync/00软路由/在存储不够的的系统中安装使用py和pip/在存储不够的的系统中安装使用py和pip/2023_10_10在软硬路由的系统中安装使用py_pip_脚本/Pastedimage20231119164234.png)
首先我们需要将RAM转为ROM来存储脚本。首先我们开放老毛子的SSH服务来方便我们配置。
![123](00_sync/00软路由/在存储不够的的系统中安装使用py和pip/在存储不够的的系统中安装使用py和pip/2023_10_10在软硬路由的系统中安装使用py_pip_脚本/Pastedimage20231119170345.png)
进来之后其实可以看到是个类似Linux系统的shell，是BusyBox的一部分，
![123](00_sync/00软路由/在存储不够的的系统中安装使用py和pip/在存储不够的的系统中安装使用py和pip/2023_10_10在软硬路由的系统中安装使用py_pip_脚本/Pastedimage20231119170407.png)
但是没有`lsb_release -a`, `cat /etc/os-release`等一系列的命令，也没有`apt`、`yum`、`dpkg`、`rpm` 等软件包管理的工具，在这种情况下应该是没办法安装[python](https://so.csdn.net/so/search?q=python&spm=1001.2101.3001.7020)的。所以我们需要找一个可用的package management tool。但在安装前我们需要规划空间给存储,改一下挂载点。
```
mount -t tmpfs -o size=60M tmpfs /opt/
```
这条命令可以让内存60MB给存储用，如果觉得不适合，请酌情增大或减小。不要太小，会无法安装python，pip等。
```
wget http://pkg.entware.net/binaries/mipsel/installer/opkg -O /opt/bin/opkg
chmod 755 /opt/bin/opkg
wget http://bin.entware.net/mipselsf-k3.4/installer/opkg.conf -O /opt/etc/opkg.conf
cd /opt/bin
./opkg update
wget https://archive.openwrt.org/barrier_breaker/14.07/ramips/mt7620a/packages/base/opkg_9c97d5ecd795709c8584e972bfdf3aee3a5b846d-7_ramips_24kec.ipk
```
![123|550](00_sync/00软路由/在存储不够的的系统中安装使用py和pip/在存储不够的的系统中安装使用py和pip/2023_10_10在软硬路由的系统中安装使用py_pip_脚本/Pastedimage20231119170523.png)
安装好ipk后(opkg是一个轻量级的包管理工具，它与IPK文件格式配合使用)OK,这样我们就可以安装python了
```
opkg install python3
```
![123](00_sync/00软路由/在存储不够的的系统中安装使用py和pip/在存储不够的的系统中安装使用py和pip/2023_10_10在软硬路由的系统中安装使用py_pip_脚本/Pastedimage20231119170529.png)
成功安装后我们可以通过scp将脚本传过来并且运行了，至于pip的话和上述软路由说明的手动安装或者使用wget。
# 后记
## 后台运行
这条命令可以让python再后台运行
```
nohup python ./jiaoben.py &
```
你也可以借助tmux来保持运行
![123](00_sync/00软路由/在存储不够的的系统中安装使用py和pip/在存储不够的的系统中安装使用py和pip/2023_10_10在软硬路由的系统中安装使用py_pip_脚本/Pastedimage20231119171412.png)
## 查看包管理工具
```
opkg list-installed
```
## 建议用编译好的可执行文件
win上有exe，linux上的为