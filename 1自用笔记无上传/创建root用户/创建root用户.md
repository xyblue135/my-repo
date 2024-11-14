sudo useradd xyblue
sudo passwd xyblue
****
sudo usermod -aG sudo newuser
验证:
su - xyblue
sudo ls /root



awk -F: '($3 == "0") {print $1}' /etc/passwd

sudo cat /etc/sudoers

	sudo visudo
ls -l /etc/sudoers.d/


检查所有sudo用户
grep '^sudo:.*$' /etc/group
getent group sudo


# 更加推荐
sudo adduser xyblue
sudo adduser root
![image-20246184418945.png](1自用笔记无上传/创建root用户/创建root用户/image-20246184418945.png)
赋权
```
sudo usermod -aG sudo xyblue  #允许使用sudo su
grep '^sudo:.*$' /etc/group
getent group sudo
```
![image-20246184649168.png](1自用笔记无上传/创建root用户/创建root用户/image-20246184649168.png)
需要注意ubuntu没有root用户，所以切换过来显示的是ubuntu，最高权限
![image-20246184814851.png](1自用笔记无上传/创建root用户/创建root用户/image-20246184814851.png)


# 结局方法
比如我们在使用ubuntu的时候 默认用户已经创建且是位于sudoer组的
![image-202410234323686.png|450](1%E8%87%AA%E7%94%A8%E7%AC%94%E8%AE%B0%E6%97%A0%E4%B8%8A%E4%BC%A0/%E5%88%9B%E5%BB%BAroot%E7%94%A8%E6%88%B7/%E5%88%9B%E5%BB%BAroot%E7%94%A8%E6%88%B7/image-202410234323686.png)
可以看到在sudo组
![image-202410234341116.png|449](1%E8%87%AA%E7%94%A8%E7%AC%94%E8%AE%B0%E6%97%A0%E4%B8%8A%E4%BC%A0/%E5%88%9B%E5%BB%BAroot%E7%94%A8%E6%88%B7/%E5%88%9B%E5%BB%BAroot%E7%94%A8%E6%88%B7/image-202410234341116.png)
编辑/etc/passwd进行提权
![image-202410234831265.png](1%E8%87%AA%E7%94%A8%E7%AC%94%E8%AE%B0%E6%97%A0%E4%B8%8A%E4%BC%A0/%E5%88%9B%E5%BB%BAroot%E7%94%A8%E6%88%B7/%E5%88%9B%E5%BB%BAroot%E7%94%A8%E6%88%B7/image-202410234831265.png)
这样xyblue用户就一直是以root形式登陆了
![image-202410234914474.png](1%E8%87%AA%E7%94%A8%E7%AC%94%E8%AE%B0%E6%97%A0%E4%B8%8A%E4%BC%A0/%E5%88%9B%E5%BB%BAroot%E7%94%A8%E6%88%B7/%E5%88%9B%E5%BB%BAroot%E7%94%A8%E6%88%B7/image-202410234914474.png)


