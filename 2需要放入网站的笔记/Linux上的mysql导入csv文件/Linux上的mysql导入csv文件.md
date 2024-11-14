sudo mysql
如果使用正常数据格式编码的csv导入的时候，可能会提示以下错误。
![image-20248312454393.png](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8A%E7%9A%84mysql%E5%AF%BC%E5%85%A5csv%E6%96%87%E4%BB%B6/Linux%E4%B8%8A%E7%9A%84mysql%E5%AF%BC%E5%85%A5csv%E6%96%87%E4%BB%B6/image-20248312454393.png)
即有安全模式，不允许这个加入到表格里面，我们用
SHOW VARIABLES LIKE 'secure_file_priv';
	即可查看下安全目录，把文件移动到那个里面去即可

# 追加模式
scp D:/hcip-ospf.csv xyblue@192.168.3.181:/home/xyblue/
ssh后，将这个目录下的文件移动到传输到对应的安全目录
mv /home/xyblue/hcip-ospf.csv /var/lib/mysql-files/
其实使用winscp会好很多


```
use hcip
LOAD DATA INFILE 'var/lib/mysql-files/hcip-ospf.csv'
INTO TABLE ospf
FIELDS TERMINATED BY ''
(ti_mu);


USE hcip;
LOAD DATA INFILE '/var/lib/mysql-files/hcip-ospf.csv'
INTO TABLE ospf
FIELDS TERMINATED BY ',' -- 根据你的CSV文件的实际分隔符修改
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS -- 如果你的CSV文件的第一行是表头，可以忽略第一行
(ti_mu); -- 这里的列名应该根据你的CSV文件中的实际列名来修改

```

![image-20248312718130.png](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8A%E7%9A%84mysql%E5%AF%BC%E5%85%A5csv%E6%96%87%E4%BB%B6/Linux%E4%B8%8A%E7%9A%84mysql%E5%AF%BC%E5%85%A5csv%E6%96%87%E4%BB%B6/image-20248312718130.png)
 # 注意权限问题
 这个安全模式的权限限制是比较严格的，最好是root