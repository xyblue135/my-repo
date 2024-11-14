# 用户

## 添加用户

```

adduser newuser

useradd -m newuser   #推荐此列

```

## 添加用户（不推荐）

也可以可以这样，不过不推荐！

```

echo 'xyblue:x:1000:1000:xyblue:/home/xyblue:/bin/ash' >> /etc/passwd

echo 'xyblue:x:1000:' >> /etc/group

mkdir /home/xyblue

```

设置密码

```

passwd xyblue

```

## 切换用户

```

su 用户名

```

## 删除用户

  

```

sudo userdel yonghu

```

可能会遇到进程正在被使用的情况

![Pasted-image-20231210025850.png](00_sync/00linux/Linux下分配用户及其赋权/Linux下分配用户及其赋权/Pasted-image-20231210025850.png)

我们使用这两个任一杀死进程或结束用户所有进程

```

kill -9 29423(进程ID)

pkill -u xyblue

```

之后再删除即可

```

sudo userdel yonghu

```

需要注意，默认会保留Home下的目录，推荐手动删除.

## 修改账户密码

```

sudo password yonghu

```

  

# 用户组

默认创建用户xyblue，会有一个组也叫需要xyblue

## 创建一个用户组

```

groupadd boys

```

## 用户添加到用户组

```

useradd -m -g boys ming

```

-m是创建home目录，-g表示再添加新用户，同时将用户加到boys组

  

## 修改用户组

```

usermod -g root xyblue

usermod -aG root xyblue

```

- `usermod -g root xyblue` 会将用户 `xyblue` 的主要组更改为 `root` 组。

- `usermod -aG root xyblue` 将用户 `xyblue` 添加到 `root` 组之外的其他组。

# 查看

##

## 看用户所属的组

  

使用

```

groups

```

命令可以查看当前用户所属的用户组。

  

若要查看其他用户所属的组，可以使用如下命令：

```

groups username

```

查看所有用户和组？

```

cat /etc/group

```

![Pasted-image-20231210032249.png](00_sync/00linux/Linux下分配用户及其赋权/Linux下分配用户及其赋权/Pasted-image-20231210032249.png)

## 查看用户列表

![Pasted-image-20231210032201.png](00_sync/00linux/Linux下分配用户及其赋权/Linux下分配用户及其赋权/Pasted-image-20231210032201.png)
# 给用户添加权限
如创建新用户后给予可以使用sudo的root权限
```
sudo usermod -aG sudo xyblue2
```