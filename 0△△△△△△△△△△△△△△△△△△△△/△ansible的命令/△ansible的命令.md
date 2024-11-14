10.126.219.34
# 进入rule的
#查看户隧

/home/ctcc_cmd 36500 tn "show tunnel_info stat"

	 |grep -a ipv4' -b

telnet 127.1 36500 \r tn \r 
show tunnel_info stat \r  start upfip_stat \r
# 用户组
```
ansible up_oula -m shell -a ' grep -E "^admin|zhangjinsheng|liweining|cmcczccj|gkptchmm|sino:" /etc/passwd ; echo "-------------------------------------------------------------";'
```
# 批量添加81.70.185.56的相关策略
```

ansible up_16 -m shell -a '/home/ctcc_cmd 36500 ru "new action id 18001 type agile label access_log" ' -b
ansible up_16 -m shell -a '/home/ctcc_cmd 36500 ru "new acl action id 18001 sip 0 dip 81.70.185.56  sport 0 dport 0 l4proto 0" ' -b
ansible up_16 -m shell -a '/home/ctcc_cmd 36500 ru "new action id 18002 type agile label recovery_white" ' -b
ansible up_16 -m shell -a '/home/ctcc_cmd 36500 ru "new acl action id 18002 sip 0 dip 81.70.185.56  sport 0 dport 0 l4proto 0" ' -b
ansible up_16 -m shell -a '/home/ctcc_cmd 36500 ru "new action id 18003 type agile label black_sample" ' -b
ansible up_16 -m shell -a '/home/ctcc_cmd 36500 ru "new acl action id 18003 sip 0 dip 81.70.185.56  sport 0 dport 0 l4proto 0" ' -b
# 查看规则
ansible up_16 -m shell -a '/home/ctcc_cmd 36500 ru "show ac id 18001" |grep -a ipv4' -b
ansible up_16 -m shell -a '/home/ctcc_cmd 36500 ru "show ac id 18002" |grep -a ipv4' -b
ansible up_16 -m shell -a '/home/ctcc_cmd 36500 ru "show ac id 18003" |grep -a ipv4' -b


#删除桂策
ansible up_16 -m shell -a '/home/ctcc_cmd 36500 ru "delete ac id 18001" ' -b
ansible up_16 -m shell -a '/home/ctcc_cmd 36500 ru "delete ac id 18002" ' -b
ansible up_16 -m shell -a '/home/ctcc_cmd 36500 ru "delete ac id 18003" ' -b

```
# 看success的还原数量
```
	ansible up_16 -m shell -a "cd /home/data/log_bak/anvs_des/20240619/success && zgrep -a '|FTP|' *20240619* | awk -F '|' '{if (\$38 != \"\") print \$38 }' |wc -l && echo -------------------------------------------------------------"

ansible up_16 -m shell -a "cd /home/data/log_bak/anvs_des/20240619/success && zgrep -a '|FTP|' *20240619* | awk -F '|' '{if (\$38 != \"\") print \$38 }' && echo -------------------------------------------------------------"

ansible up_16 -m shell -a "cd /home/data/log_bak/anvs_des/20240613/success && zgrep -a '|FTP|' *20240613* | awk -F '|' '{if (\$38 != \"\") print \$38 }' |wc -l && echo -------------------------------------------------------------" 

ansible up_16 -m shell -a "cd /home/data/log_bak/anvs_des/20240613/success && zgrep -a '|FTP|' *20240613* | awk -F '|' '{if (\$38 != \"\") print \$38 }' && echo -------------------------------------------------------------"

```



ansible up_16 -m shell -a "cd /home/data/log_bak/anvs_des/20240618/success && zgrep -a '|http|' *20240618* | awk -F '|' '{if (\$38 != \"\") print \$38 }' |wc -l && echo -------------------------------------------------------------"


	ansible up_16 -m shell -a "cd /home/data/log_bak/anvs_des/20240619/success && zgrep -a '|http|' *20240619* | awk -F '|' '{if (\$38 != \"\") print \$38 }' |tail - 5 && echo -------------------------------------------------------------"


# 查看ansible的用户组
这个是防止乱序的，但是会影响性能
```
cat /etc/ansible/hosts
```


# 查看当天success还原数量
```
cd /home/data/log_bak/anvs_des/20240606/success
zgrep -a "|FTP|" *20240606* |awk -F "|" '{print $38}' |wc -l

ansible up_16 -m shell -a ' cd /home/data/log_bak/anvs_des/20240606/success zgrep -a "|FTP|" *20240606* |awk -F "|" '{print $1}' echo "-------------------------------------------------------------";'

ansible up_16 -m shell -a "cd /home/data/log_bak/anvs_des/20240607/success && zgrep -a 99930410000744 && echo -------------------------------------------------------------"

ansible up_16 -m shell -a "cd /home/data/log_bak/anvs_des/20240607/success && zgrep -a '|FTP|' *20240607* | awk -F '|' '{print \$1}' && echo -------------------------------------------------------------"

ansible up_16 -m shell -a "cd /home/data/log_bak/anvs_des/20240605/success && zgrep -a '|HTTP|' *20240605* | awk -F '|' '{print \$38}' | wc -l && echo -------------------------------------------------------------"

ansible up_16 -m shell -a "cd /home/data/log_bak/anvs_des/20240605/success && zgrep -a '|SMTP|' *20240605* | awk -F '|' '{print \$38}' | wc -l && echo -------------------------------------------------------------"
ansible up_16 -m shell -a "cd /home/data/log_bak/anvs_des/20240605/success && zgrep -a '|IMAP|' *20240605* | awk -F '|' '{print \$38}' | wc -l && echo -------------------------------------------------------------"
ansible up_16 -m shell -a "cd /home/data/log_bak/anvs_des/20240605/success && zgrep -a '|FTP|' *2024060511* | awk -F '|' '{print \$38}' | wc -l && echo -------------------------------------------------------------"


 ansible up_16 -m shell -a 'cd /home/data/is_access_log ;cat *20240619* |grep sino-telecom.cn |tail -2' -b && echo -------------------------------------------------------------"
 
  ansible up_16 -m shell -a 'cd /home/data/is_access_log ;cat |grep sino-telecom.cn |tail -2' -b && echo -------------------------------------------------------------"


再access目录的
ansible up_16 -m shell -a 'cd /home/data/is_access_log && { cat * | grep sino-telecom.cn | tail -20; } && echo -------------------------------------------------------------'

ansible up_16 -m shell -a 'cd /home/data/log_bak/anvs_des/20240619/success && { cat * | grep sino-telecom.cn | tail -3; } && echo -------------------------------------------------------------'



```
# 查看当天success还原MD5
```
ansible up_16 -m shell -a "cd /home/data/log_bak/anvs_des/20240605/success && zgrep -a '|SMTP|' *2024060511* | awk -F '|' '{if ($38 != "") print $38}' && echo -------------------------------------------------------------"
转换8
ansible up_16 -m shell -a "cd /home/data/log_bak/anvs_des/20240613/success && zgrep -a '|FTP|' *20240613* | awk -F '|' '{if (\$38 != \"\") print \$38 }' |wc -l && echo -------------------------------------------------------------"

ansible up_16 -m shell -a "cd /home/data/log_bak/anvs_des/20240605/success && zgrep -a '|FTP|' *2024060511* | awk -F '|' '{if (\$38 != \"\") print \$38}' && echo -------------------------------------------------------------"



ansible up_16 -m shell -a "cd /home/data/log_bak/anvs_des/20240612/success && zgrep -a '|HTTP|' *2024060612* | awk -F '|' '{if (\$38 != \"\") print \$38}' && echo -------------------------------------------------------------"



```
# 清理丢包

 ansible up-all -m shell -a '/home/ctcc_cmd 36500 udpi "clear all_stat"' -b
# 看状态
 ansible husui -m shell -a 'systemctl status tnlinfo_proxy |grep running' -b
 ansible up-all -m shell -a 'systemctl status logtar |grep running ' -b

# 看cp还是nave
ansible up-all -m shell -a 'systemctl status upload |grep running ' -b

# 看upp
确认里面的数据包含在里面 结合三个
ansible up-all -m shell -a 'netstat -anp|grep anvs_upp' -b

# 查看FTP
```
#看一个日期FTP
ansible up_16 -m shell -a "cd /home/data/log_bak/anvs_des/20240607/success && zgrep -a '|FTP|' *20240607* | awk -F '|' '{if (\$38 != \"\") print \$38}' && echo -------------------------------------------------------------"
```
![image-202467519274.png](0%E5%85%B3%E4%BA%8E%E5%85%AC%E5%8F%B8%E6%AD%A3%E5%9C%A8%E8%BF%9B%E8%A1%8C%E7%9A%84%E4%BA%8B%E6%83%85/ansible%E7%9A%84%E5%91%BD%E4%BB%A4/image-202467519274.png)



```
# 查看updpi状态




ansible --version: 查看 Ansible 版本信息。
ansible all -m ping: 检查所有主机的连通性。
ansible-playbook playbook.yml: 运行指定的 Ansible Playbook 文件。
ansible-doc module_name: 查看指定模块的帮助文档。
ansible-config view: 查看当前 Ansible 配置信息。
ansible-inventory --list: 列出当前主机清单中定义的所有主机和组。
ansible-vault create file.yml: 创建一个加密的 Ansible Vault 文件。
ansible-galaxy init role_name: 初始化一个新的 Ansible 角色。
ansible-lint playbook.yml: 检查 Ansible Playbook 文件的语法错误和最佳实践。
ansible-vault encrypt file.yml: 加密一个现有的 YAML 文件。
ansible-vault decrypt file.yml: 解密一个加密的 YAML 文件。
ansible-pull -U repository_url playbook.yml: 在目标主机上执行 Ansible Playbook 并从代码仓库拉取最新的副本。
ansible-doc -l: 列出所有可用的 Ansible 模块。
ansible-galaxy install role_name: 安装一个 Ansible 角色。
ansible-vault edit file.yml: 编辑一个已加密的 YAML 文件。
ansible-playbook playbook.yml --tags=tag_name: 只运行指定标签的任务。
ansible all -a "command": 在所有主机上运行指定的命令。
ansible all -m shell -a "command": 在所有主机上运行指定的 Shell 命令。
ansible all -m file -a "path=/path/to/file state=absent": 删除指定路径下的文件。
ansible all -m copy -a "src=file.txt dest=/path/to/dest": 将本地文件复制到远程主机。
ansible all -m yum -a "name=package state=present": 在所有主机上安装指定的 Yum 包。
ansible all -m service -a "name=service state=started": 启动指定的服务。
ansible all -m user -a "name=username state=present": 创建一个新用户。
ansible all -m command -a "echo 'hello'": 在所有主机上运行指定的命令。
ansible all -b -m apt -a "name=package state=present": 使用管理员权限在所有主机上安装指定的 Apt 包。
ansible all -i hosts_file -m ping: 使用自定义的主机清单文件，检查所有主机的连通性。
ansible-playbook playbook.yml --limit=hostname: 限制只在指定的主机上运行 Playbook。
ansible-playbook playbook.yml --check: 以模拟模式运行 Playbook，不会实际修改系统状态。
ansible-playbook playbook.yml --diff: 在执行任务时显示更改的详细信息。
ansible-vault rekey file.yml: 更改 Ansible Vault 文件的加密密码。
ansible-galaxy search search_term: 搜索 Ansible Galaxy 上可用的角色。
ansible all -m setup: 收集所有主机的系统信息。
ansible all -m debug -a "var=ansible_hostname": 打印指定变量的值。
ansible-doc -s module_name: 显示指定模块的示例用法。
ansible-galaxy init --offline role_name: 在离线模式下初始化一个新的 Ansible 角色。
ansible all --list-hosts: 列出所有主机清单中定义的主机。
ansible-vault encrypt_string 'password' --name 'var_name': 加密一个字符串并将其存储为 Ansible 变量。
ansible all -m lineinfile -a "dest=file line='text' state=present": 在文件中插入一行文本。
ansible all -m service -a "name=service state=restarted": 重新启动指定的服务。
ansible all -m package -a "name=package state=latest": 在所有主机上更新指定的软件包。
ansible all -m synchronize -a "src=/path/to/src dest=/path/to/dest": 将本地目录同步到远程主机。
ansible all -m lineinfile -a "dest=file regexp='regex' line='replacement'": 替换文件中匹配正则表达式的行。
ansible-galaxy remove role_name: 删除指定的 Ansible 角色。
ansible all -m apt_repository -a "repo='repo_url' state=present": 添加一个 Apt 仓库。
ansible all -m shell -a "echo $VAR": 打印远程主机上的环境变量的值。
ansible all -m cron -a "name='cron_job' minute='*/5' job='command'": 创建一个定时任务。
ansible-playbook playbook.yml --syntax-check: 检查 Playbook 文件的语法错误。
ansible all -m setup -a "filter=ansible_distribution*": 过滤收集的系统信息。
ansible all --become -m copy -a "src=file.txt dest=/path/to/dest"：以管理员权限将本地文件复制到远程主机。
ansible all -m file -a "path=/path/to/file owner=user group=group": 修改文件的所有者和所属组。
