在windows上面Docker使用久了,即使使用了词条命令
docker system prune
也会C盘爆满
但是当在Windows中使用WSL2作为Docker后端引擎的时候，情况就会稍微复杂一些了。
因为WSL2本质上来说是虚拟机，对于每个虚拟机，Windows会创建`vhdx`后缀的磁盘镜像文件，用于存储其内容，类似于vmdk、vdi，用过虚拟机的同学应该都不陌生。

这种镜像文件的特点是支持自动扩容，但是一般不会自动缩容。因此一旦Docker镜像文件过多，引起镜像扩容，即使再使用`docker system prune`清理虚拟机中的镜像文件，也不会释放出已经占用的系统磁盘空间了。

镜像文件虽然一般不会自动压缩，但是支持手动压缩。

首先寻找到对应的镜像文件，在系统中搜索`ext4.vhdx`文件，可以搜索到多条记录，Docker对应的镜像文件一般是在`C:\Users\<你的用户名>\AppData\Local\Docker\wsl\data\ext4.vhdx`这个位置。

找到这个文件之后，进行压缩即可。
```
wsl --shutdown
diskpart
```
# open Diskpart in new window
```
select vdisk file="{Path to vhdx}\ext4.vhdx"
attach vdisk readonly
compact vdisk
detach vdisk
exit
```
比如我的:
```
wsl --shutdown
diskpart
select vdisk file="C:\Users\13519\AppData\Local\Docker\wsl\data\ext4.vhdx"
attach vdisk readonly
compact vdisk
detach vdisk
exit
```
![Pasted-image-20231209182821.png](00_sync/00linux/收缩WSL2的大小/收缩WSL2的大小/Pasted-image-20231209182821.png)