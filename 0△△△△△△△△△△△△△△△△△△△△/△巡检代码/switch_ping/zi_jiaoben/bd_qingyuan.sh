#!/bin/bash
# 时间
CURRENT_DATE=$(date +"%Y-%m-%d") # 文件夹-天
CURRENT_TIME=$(date +"%Y-%m-%d-%H-%M-%S") # 日志-秒
LOG_DIR="./xunjian_log/$CURRENT_DATE" # 目录精确到日志
#---------------------1.注意文件夹的命名----------------------------------------------
LOGFILE="$LOG_DIR/bd_qingyuan_$CURRENT_TIME.log" # 日志精确到秒
mkdir -p "$LOG_DIR" # 创建精确到天  目录

/usr/bin/expect << EOF
set timeout -1
log_file $LOGFILE

# 分割
#puts "----------------------------------------------------------------------------------------------------------"
#----------------------------2.注意IP是否是交换机的---------------------------------------------------
puts "===============ji_fang河北保定清苑机房bd_qingyuan    10.126.219.6"
#交换机IP核查[检查区域]
spawn ssh -o HostKeyAlgorithms=+ssh-rsa -o PubkeyAcceptedKeyTypes=+ssh-rsa weihu@10.126.219.6
expect {
"yes/no" {
    send "yes\r"
    exp_continue
}
"password:" {
    send "admin@h3c.com\r"
}
}
expect {
-re {<[^>]*>} {
    # ping
    send "ping -c 1 192.168.205.33\r"
    send "ping -c 1 192.168.205.34\r"
    send "ping ipv6  -c 1 2409:8005:2806:900:3::100\r"
    send "ping ipv6  -c 1 2409:8005:2806:900:3::101\r"

    send "ping -c 1 192.168.255.249\r"
    send "ping -c 1 192.168.255.250\r"
    send "ping ipv6  -c 1 2409:8005:2A06:1900:103::100\r"
    send "ping ipv6  -c 1 2409:8005:2A06:1900:103::101\r"

    send "ping -c 1 192.168.102.33\r"
    send "ping -c 1 192.168.102.34\r"
    send "ping ipv6  -c 1 2409:8005:2801:300:2::300\r"
    send "ping ipv6  -c 1 2409:8005:2801:300:2::301\r"

    send "ping -c 1 192.168.205.37\r"
    send "ping -c 1 192.168.205.38\r"
    send "ping ipv6  -c 1 2409:8004:2806:70::100\r"
    send "ping ipv6  -c 1 2409:8004:2806:70::101\r"

    send "ping -c 1 192.168.4.17\r"
    send "ping -c 1 192.168.4.18\r"
    send "ping ipv6  -c 1 2409:8004:2860:1010::100\r"
    send "ping ipv6  -c 1 2409:8004:2860:1010::101\r"

    # exit
    send "exit\r"
}
}
expect eof
EOF
