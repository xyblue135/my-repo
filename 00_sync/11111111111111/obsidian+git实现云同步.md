# Git以及GUI下载地址
git下载地址:https://git-scm.com/
sourcetree下载地址:https://www.sourcetreeapp.com/
# 本地端
首先确立一个git文件夹拉取文件
```
# 创建仓库
git init
# 使用gitbash或者gitcmd拉取
https://gitee.com/xyblue/qr-code-website-redirect.git
```
创建仓库
![image-2024616329349.png](3可以放入网站的笔记/obsidian+git实现云同步/obsidian+git实现云同步/image-2024616329349.png)
克隆仓库
![image-20246163434675.png|175](3可以放入网站的笔记/obsidian+git实现云同步/obsidian+git实现云同步/image-20246163434675.png)
![image-20246163450589.png](3可以放入网站的笔记/obsidian+git实现云同步/obsidian+git实现云同步/image-20246163450589.png)
后面的样子一直输入指令有点麻烦了，而且git的命令也挺多了，推荐使用带GUI的
```
git config --global user.name "xyblue"
git config --global user.email "XXXXXX@qq.com"
mkdir git_test
cd git_test
git init 
touch README.md
git add README.md
git commit -m "first commit"
git remote add origin https://gitee.com/xyblue/git_test.git
git push -u origin "master"
cd existing_git_repo
git remote add origin https://gitee.com/xyblue/git_test.git
git push -u origin "master"
```
# 本地端GUI
相关软件source tree
复制仓库的下载地址
![image-20246164945961.png|475](3可以放入网站的笔记/obsidian+git实现云同步/obsidian+git实现云同步/image-20246164945961.png)
![image-2024616361872.png|325](3可以放入网站的笔记/obsidian+git实现云同步/obsidian+git实现云同步/image-2024616361872.png)
复制到软件新建
![image-20246164954243.png|275](3可以放入网站的笔记/obsidian+git实现云同步/obsidian+git实现云同步/image-20246164954243.png)
![image-20246165333516.png|350](3可以放入网站的笔记/obsidian+git实现云同步/obsidian+git实现云同步/image-20246165333516.png)
在创建文件夹修改后会自动检测出来此时点击暂存所有就可以实现git add的操作
![image-2024616371774.png](3可以放入网站的笔记/obsidian+git实现云同步/obsidian+git实现云同步/image-2024616371774.png)
下面类似于聊天栏的东西是git commit的操作
![image-20246165957871.png](3可以放入网站的笔记/obsidian+git实现云同步/obsidian+git实现云同步/image-20246165957871.png)
推送：这里本地是master 远端也是master，这里可能要涉及登录。
![image-2024616048477.png](3可以放入网站的笔记/obsidian+git实现云同步/obsidian+git实现云同步/image-2024616048477.png)
这边推送的话，是你gitee或者github的账号密码，如果使用账号密码登录将 不需要 密钥对。
![image-2024616396117.png](3可以放入网站的笔记/obsidian+git实现云同步/obsidian+git实现云同步/image-2024616396117.png)
https://help.gitee.com/base/account/SSH%E5%85%AC%E9%92%A5%E8%AE%BE%E7%BD%AE
![image-202461627356.png](3可以放入网站的笔记/obsidian+git实现云同步/obsidian+git实现云同步/image-202461627356.png)![image-20246162740242.png](3可以放入网站的笔记/obsidian+git实现云同步/obsidian+git实现云同步/image-20246162740242.png)
成功push
![image-20246162826599.png](3可以放入网站的笔记/obsidian+git实现云同步/obsidian+git实现云同步/image-20246162826599.png)
拉取
![image-20246164342489.png](3可以放入网站的笔记/obsidian+git实现云同步/obsidian+git实现云同步/image-20246164342489.png)
# 杂谈
貌似现在可以直接登录账号而不需要配置密钥了
## 配置密钥对（可选）
powershell&git bash
```
# 生成密钥
ssh-keygen -t ed25519 -C "Gitee SSH Key"
# 下面输出回车三下
Generating public/private ed25519 key pair.  
Enter file in which to save the key (/home/git/.ssh/id_ed25519):  
Enter passphrase (empty for no passphrase):  
Enter same passphrase again:  
Your identification has been saved in /home/git/.ssh/id_ed25519  
Your public key has been saved in /home/git/.ssh/id_ed25519.pub  
The key fingerprint is:  
SHA256:ohDd0OK5WG2dx4gST/j35HjvlJlGHvihyY+Msl6IC8I Gitee SSH Key  
The key's randomart image is:  
+--[ED25519 256]--+  
| .o |  
| .+oo |  
| ...O.o + |  
| .= * = +. |  
| .o +..S*. + |  
|. ...o o..+* * |  
|.E. o . ..+.O |  
| . . ... o =. |  
| ..oo. o.o |  
+----[SHA256]-----+
```
在用户.ssh文件夹，公钥是需要放到服务器的，id_ed25519.pub
![image-20246163044532.png](3可以放入网站的笔记/obsidian+git实现云同步/obsidian+git实现云同步/image-20246163044532.png)
https://gitee.com/profile/sshkeys
![image-20246163134403.png](3可以放入网站的笔记/obsidian+git实现云同步/obsidian+git实现云同步/image-20246163134403.png)
linux公钥位置
```
ssh-keygen -t ed25519 -C "Gitee SSH Key"
ls ~/.ssh/
cat ~/.ssh/id_ed25519.pub
```
