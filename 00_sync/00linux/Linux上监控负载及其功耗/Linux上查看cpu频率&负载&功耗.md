# 查看当前cpu频率
```
cat /proc/cpuinfo
查看当前cpu频率↓ 
cat /proc/cpuinfo | grep "cpu MHz"
grep -E '^model name|^cpu MHz' /proc/cpuinfo
lscpu | grep "MHz"
```
![image-202410125054530.png|475](00_sync/00linux/Linux%E4%B8%8A%E7%9B%91%E6%8E%A7%E8%B4%9F%E8%BD%BD%E5%8F%8A%E5%85%B6%E5%8A%9F%E8%80%97/Linux%E4%B8%8A%E6%9F%A5%E7%9C%8Bcpu%E9%A2%91%E7%8E%87&%E8%B4%9F%E8%BD%BD&%E5%8A%9F%E8%80%97/image-202410125054530.png)
# 查看当前功耗
```
cat /sys/class/power_supply/BAT0/power_now
echo "$(cat /sys/class/power_supply/BAT0/power_now) / 1000000" | bc -l
```
![image-202410125114908.png|500](00_sync/00linux/Linux%E4%B8%8A%E7%9B%91%E6%8E%A7%E8%B4%9F%E8%BD%BD%E5%8F%8A%E5%85%B6%E5%8A%9F%E8%80%97/Linux%E4%B8%8A%E6%9F%A5%E7%9C%8Bcpu%E9%A2%91%E7%8E%87&%E8%B4%9F%E8%BD%BD&%E5%8A%9F%E8%80%97/image-202410125114908.png)

# 修改电源模式【用这个】
```
cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor

改为performrmance模式

for CPUFREQ in /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor; do
	[ -f $CPUFREQ ] || continue
	echo -n performance > $CPUFREQ
done


改为powersave模式
for CPUFREQ in /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor; do
	[ -f $CPUFREQ ] || continue
	echo -n powersave > $CPUFREQ
done

```
1. performance: 顾名思义只注重效率，将 CPU 频率固定工作在其支持的最高运行频率上，而不动态调节。
2. Userspace: 最早的 cpufreq 子系统通过 userspace governor 为用户提供了这种灵活性。系统将变频策略的决策权交给了用户态应用程序，并提供了相应的接口供用户态应用程序调节 CPU 运行频率使用。也就是长期以来都在用的那个模式。可以通过手动编辑配置文件进行配置
3. powersave: 将 CPU 频率设置为最低的所谓 “省电” 模式，CPU 会固定工作在其支持的最低运行频率上。因此这两种 governors 都属于静态 governor，即在使用它们时 CPU 的运行频率不会根据系统运行时负载的变化动态作出调整。这两种 governors 对应的是两种极端的应用场景，使用 performance governor 是对系统高性能的最大追求，而使用 powersave governor 则是对系统低功耗的最大追求。
4. ondemand: 按需快速动态调整 CPU 频率， 一有 cpu 计算量的任务，就会立即达到最大频率运行，等执行完毕就立即回到最低频率；ondemand：userspace 是内核态的检测，用户态调整，效率低。而 ondemand 正是人们长期以来希望看到的一个完全在内核态下工作并且能够以更加细粒度的时间间隔对系统负载情况进行采样分析的 governor。 在 ondemand governor 监测到系统负载超过 up_threshold 所设定的百分比时，说明用户当前需要 CPU 提供更强大的处理能力，因此 ondemand governor 会将 CPU 设置在最高频率上运行。但是当 ondemand governor 监测到系统负载下降，可以降低 CPU 的运行频率时，到底应该降低到哪个频率呢？ ondemand governor 的最初实现是在可选的频率范围内调低至下一个可用频率，例如 CPU 支持三个可选频率，分别为 1.67GHz、1.33GHz 和 1GHz ，如果 CPU 运行在 1.67GHz 时 ondemand governor 发现可以降低运行频率，那么 1.33GHz 将被选作降频的目标频率。
5. conservative: 与 ondemand 不同，平滑地调整 CPU 频率，频率的升降是渐变式的, 会自动在频率上下限调整，和 ondemand 的区别在于它会按需分配频率，而不是一味追求最高频率；
## ## 注意

这个配置重启后会失效。如果需要持久化，可以设置开机自动运行本命令，或通过修改bios配置达到目的。

# 其余工具
## 统计功耗
## 自带命令
```
#!/bin/bash
# 无限循环，每秒记录一次当前功耗
while true; do
  echo "$(date): $(echo "$(cat /sys/class/power_supply/BAT0/power_now) / 1000000" | bc -l) W" >> 1.txt
  sleep 1
done
cpupower【持续显示】
```
## cpupower
https://www.cnblogs.com/devilmaycry812839668/p/13982891.html
sudo apt install linux-tools-common
![image-20242135538566.png|475](00_sync/00linux/Linux上监控负载及其功耗/Linux上监控负载及其功耗/image-20242135538566.png)
 如果跟我一样出现错误，请按照指示下载对应的linux-tools，如我
 sudo apt install linux-tools-6.5.0-17-generic
 按照youmay那里给的提示安装对应辅助包
![image-20242135552976.png](00_sync/00linux/Linux上监控负载及其功耗/Linux上监控负载及其功耗/image-20242135552976.png)
### CPU实时频率查看
```
watch -n 1 sudo cpupower monitor
```
![image-20247273524445.png|475](00_sync/00linux/Linux上监控负载及其功耗/Linux上监控负载及其功耗/image-20247273524445.png)
![image-2024727353953.png|475](00_sync/00linux/Linux上监控负载及其功耗/Linux上监控负载及其功耗/image-2024727353953.png)
```
sudo cpupower -c all frequency-info
```
![image-20247273553612.png|450](00_sync/00linux/Linux上监控负载及其功耗/Linux上监控负载及其功耗/image-20247273553612.png)
可以看到当前的CPU支持  performance 和  powersave  两种模式，当前的模式为  powersave
####   设置所有CPU为性能模式【不建议用这个】
```
sudo cpupower -c all frequency-set -g performance
```
![image-20247273728711.png|475](00_sync/00linux/Linux上监控负载及其功耗/Linux上监控负载及其功耗/image-20247273728711.png)
####   设置所有CPU为节能模式
```
sudo cpupower -c all frequency-set -g powersave
```
![image-2024727389346.png|475](00_sync/00linux/Linux上监控负载及其功耗/Linux上监控负载及其功耗/image-2024727389346.png)
#### 补充
```
cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
watch -n -1 "cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
cpupower frequency-info
```
