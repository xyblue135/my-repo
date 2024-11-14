```
sudo apt update
sudo apt install mysql-server
```

```
sudo systemctl status mysql
sudo systemctl start mysql
sudo ufw allow 3306/tcp
sudo netstat -tulnp | grep mysql
```

编辑配置文件
通常是`/etc/mysql/my.cnf`或`/etc/my.cnf` 但是我这个是在/etc/mysql/mysql.conf.d的文件夹里面
![image-20248315235573.png](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8A%E9%85%8D%E7%BD%AEsql%E6%9C%8D%E5%8A%A1%E5%99%A8%E9%85%8D%E5%90%88win%E8%BF%9E%E6%8E%A5/Linux%E4%B8%8A%E9%85%8D%E7%BD%AEsql%E6%9C%8D%E5%8A%A1%E5%99%A8%E9%85%8D%E5%90%88win%E8%BF%9E%E6%8E%A5/image-20248315235573.png)

把bind-address注释掉或者设置为0.0.0.0
![image-2024831547254.png](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8A%E9%85%8D%E7%BD%AEsql%E6%9C%8D%E5%8A%A1%E5%99%A8%E9%85%8D%E5%90%88win%E8%BF%9E%E6%8E%A5/Linux%E4%B8%8A%E9%85%8D%E7%BD%AEsql%E6%9C%8D%E5%8A%A1%E5%99%A8%E9%85%8D%E5%90%88win%E8%BF%9E%E6%8E%A5/image-2024831547254.png)
```
sudo systemctl restart mysql
```

修改密码
```必须有sudo
如果用-p root root 可以登陆的话，就不用修改密码了
sudo mysql -u root -p
sudo mysql -u root
```

![image-2024831731894.png](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8A%E9%85%8D%E7%BD%AEsql%E6%9C%8D%E5%8A%A1%E5%99%A8%E9%85%8D%E5%90%88win%E8%BF%9E%E6%8E%A5/Linux%E4%B8%8A%E9%85%8D%E7%BD%AEsql%E6%9C%8D%E5%8A%A1%E5%99%A8%E9%85%8D%E5%90%88win%E8%BF%9E%E6%8E%A5/image-2024831731894.png)
修改密码
```
ALTER USER 'root'@'localhost' IDENTIFIED BY 'root';
ALTER USER 'root'@'localhost' IDENTIFIED BY '123456';
alter user root@localhost identified by'123456';
ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_secure_password';
FLUSH PRIVILEGES;
EXIT;
```
![image-2024831924171.png](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8A%E9%85%8D%E7%BD%AEsql%E6%9C%8D%E5%8A%A1%E5%99%A8%E9%85%8D%E5%90%88win%E8%BF%9E%E6%8E%A5/Linux%E4%B8%8A%E9%85%8D%E7%BD%AEsql%E6%9C%8D%E5%8A%A1%E5%99%A8%E9%85%8D%E5%90%88win%E8%BF%9E%E6%8E%A5/image-2024831924171.png)

# 错误1698解决:
![image-20248312932161.png](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8A%E9%85%8D%E7%BD%AEsql%E6%9C%8D%E5%8A%A1%E5%99%A8%E9%85%8D%E5%90%88win%E8%BF%9E%E6%8E%A5/Linux%E4%B8%8A%E9%85%8D%E7%BD%AEsql%E6%9C%8D%E5%8A%A1%E5%99%A8%E9%85%8D%E5%90%88win%E8%BF%9E%E6%8E%A5/image-20248312932161.png)
修改身份插件为mysql_native_password
```
sudo mysql
SELECT user, host, plugin FROM mysql.user WHERE user = 'root';
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123456';
FLUSH PRIVILEGES;
```
正常登录
![image-20248313059156.png|475](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8A%E9%85%8D%E7%BD%AEsql%E6%9C%8D%E5%8A%A1%E5%99%A8%E9%85%8D%E5%90%88win%E8%BF%9E%E6%8E%A5/Linux%E4%B8%8A%E9%85%8D%E7%BD%AEsql%E6%9C%8D%E5%8A%A1%E5%99%A8%E9%85%8D%E5%90%88win%E8%BF%9E%E6%8E%A5/image-20248313059156.png)
# 客户端连接问题解决
## 确保bind_address被注释掉
## 确保将local改为%
```
update user set host="%" where user="root"
flush privileges
```
配合SELECT User, Host FROM mysql.user;检查
![image-20248313415355.png](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8A%E9%85%8D%E7%BD%AEsql%E6%9C%8D%E5%8A%A1%E5%99%A8%E9%85%8D%E5%90%88win%E8%BF%9E%E6%8E%A5/Linux%E4%B8%8A%E9%85%8D%E7%BD%AEsql%E6%9C%8D%E5%8A%A1%E5%99%A8%E9%85%8D%E5%90%88win%E8%BF%9E%E6%8E%A5/image-20248313415355.png)
![image-20248315028104.png](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8A%E9%85%8D%E7%BD%AEsql%E6%9C%8D%E5%8A%A1%E5%99%A8%E9%85%8D%E5%90%88win%E8%BF%9E%E6%8E%A5/Linux%E4%B8%8A%E9%85%8D%E7%BD%AEsql%E6%9C%8D%E5%8A%A1%E5%99%A8%E9%85%8D%E5%90%88win%E8%BF%9E%E6%8E%A5/image-20248315028104.png)
# 常用检测
### 查询 `mysql.user` 表
```
ELECT User FROM mysql.user;
```
![image-20248315541364.png](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8A%E9%85%8D%E7%BD%AEsql%E6%9C%8D%E5%8A%A1%E5%99%A8%E9%85%8D%E5%90%88win%E8%BF%9E%E6%8E%A5/Linux%E4%B8%8A%E9%85%8D%E7%BD%AEsql%E6%9C%8D%E5%8A%A1%E5%99%A8%E9%85%8D%E5%90%88win%E8%BF%9E%E6%8E%A5/image-20248315541364.png)
### 查询主机信息
```
SELECT User, Host FROM mysql.user;
```
![image-20248315654315.png](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8A%E9%85%8D%E7%BD%AEsql%E6%9C%8D%E5%8A%A1%E5%99%A8%E9%85%8D%E5%90%88win%E8%BF%9E%E6%8E%A5/Linux%E4%B8%8A%E9%85%8D%E7%BD%AEsql%E6%9C%8D%E5%8A%A1%E5%99%A8%E9%85%8D%E5%90%88win%E8%BF%9E%E6%8E%A5/image-20248315654315.png)
### 计算用户数量
```
SELECT COUNT(*) FROM mysql.user;
SELECT User, Host FROM mysql.user WHERE User = 'your_username';
```