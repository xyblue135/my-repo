### 自动登录sh
```
#!/usr/bin/expect -f
set timeout 30   #超时参数
set pswd "Sino@telecom66"
spawn ssh -l root 10.126.219.34 -p 22
expect "*password*"
send "$pswd\r"
interact
```