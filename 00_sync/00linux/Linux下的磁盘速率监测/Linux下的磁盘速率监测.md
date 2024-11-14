
# dstat 【推荐】
实时监测，但是不好的点就是不能反映哪块硬盘
```
sudo apt-get install dstat
dstat 【推荐】
dstat -d
```
![image-2024112447646.png|375](00_sync/00linux/Linux%E4%B8%8B%E7%9A%84%E7%A3%81%E7%9B%98%E9%80%9F%E7%8E%87%E7%9B%91%E6%B5%8B/Linux%E4%B8%8B%E7%9A%84%E7%A3%81%E7%9B%98%E9%80%9F%E7%8E%87%E7%9B%91%E6%B5%8B/image-2024112447646.png)
paging--
- **in**: 每秒从磁盘读入内存的页面数。
- **out**: 每秒从内存写入磁盘的页面数。
 ---system--
- **int**: 每秒发生的中断次数。
- **csw**: 每秒发生的上下文切换次数。
![image-20241122922535.png|325](00_sync/00linux/Linux%E4%B8%8B%E7%9A%84%E7%A3%81%E7%9B%98%E9%80%9F%E7%8E%87%E7%9B%91%E6%B5%8B/Linux%E4%B8%8B%E7%9A%84%E7%A3%81%E7%9B%98%E9%80%9F%E7%8E%87%E7%9B%91%E6%B5%8B/image-20241122922535.png)
# iostat【推荐】
```
sudo apt-get install sysstat
iostat -dx 1命令来查看每秒钟的磁盘读写速率。-d表示只显示设备（磁盘）相关的统计信息，-x表示显示扩展统计信息，1表示每1秒刷新一次数据。
```
![image-20241123411743.png](00_sync/00linux/Linux%E4%B8%8B%E7%9A%84%E7%A3%81%E7%9B%98%E9%80%9F%E7%8E%87%E7%9B%91%E6%B5%8B/Linux%E4%B8%8B%E7%9A%84%E7%A3%81%E7%9B%98%E9%80%9F%E7%8E%87%E7%9B%91%E6%B5%8B/image-20241123411743.png)
# iotop
```
sudo apt-get install iotop
sudo iotop
```
![image-2024112274045.png](00_sync/00linux/Linux%E4%B8%8B%E7%9A%84%E7%A3%81%E7%9B%98%E9%80%9F%E7%8E%87%E7%9B%91%E6%B5%8B/Linux%E4%B8%8B%E7%9A%84%E7%A3%81%E7%9B%98%E9%80%9F%E7%8E%87%E7%9B%91%E6%B5%8B/image-2024112274045.png)

# nmon
```
sudo apt-get install nmon
nmon
```
![image-2024112315835.png](00_sync/00linux/Linux%E4%B8%8B%E7%9A%84%E7%A3%81%E7%9B%98%E9%80%9F%E7%8E%87%E7%9B%91%E6%B5%8B/Linux%E4%B8%8B%E7%9A%84%E7%A3%81%E7%9B%98%E9%80%9F%E7%8E%87%E7%9B%91%E6%B5%8B/image-2024112315835.png)
![image-20241123052972.png](00_sync/00linux/Linux%E4%B8%8B%E7%9A%84%E7%A3%81%E7%9B%98%E9%80%9F%E7%8E%87%E7%9B%91%E6%B5%8B/Linux%E4%B8%8B%E7%9A%84%E7%A3%81%E7%9B%98%E9%80%9F%E7%8E%87%E7%9B%91%E6%B5%8B/image-20241123052972.png)