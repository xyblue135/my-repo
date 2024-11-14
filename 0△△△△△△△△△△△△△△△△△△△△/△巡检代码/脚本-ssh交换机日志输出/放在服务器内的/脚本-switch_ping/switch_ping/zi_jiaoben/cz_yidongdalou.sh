#!/bin/bash
# 时间
CURRENT_DATE=$(date +"%Y-%m-%d") # 文件夹-天
CURRENT_TIME=$(date +"%Y-%m-%d-%H-%M-%S") # 日志-秒
LOG_DIR="./xunjian_log/$CURRENT_DATE" # 目录精确到日志
#---------------------1.注意文件夹的命名----------------------------------------------
LOGFILE="$LOG_DIR/cz_yidongdalou_$CURRENT_TIME.log" # 日志精确到秒
mkdir -p "$LOG_DIR" # 创建精确到天  目录

/usr/bin/expect << EOF
set timeout -1
log_file $LOGFILE

# 分割
puts "----------------------------------------------------------------------------------------------------------"
#----------------------------2.注意IP是否是交换机的---------------------------------------------------
#交换机IP核查[检查区域]
spawn ssh -o HostKeyAlgorithms=+ssh-rsa -o PubkeyAcceptedKeyTypes=+ssh-rsa weihu@10.126.219.227
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
    send "ping -c 1 192.168.206.9\r"
    send "ping -c 1 192.168.206.10\r"
    send "ping ipv6  -c 1 2409:8005:2A04:0900:604::100\r"
    send "ping ipv6  -c 1 2409:8005:2A04:0900:604::101\r"

    send "ping -c 1 192.168.205.85\r"
    send "ping -c 1 192.168.205.86\r"
    send "ping ipv6  -c 1 2409:8005:2804:900:3::100\r"
    send "ping ipv6  -c 1 2409:8005:2804:900:3::101\r"

    send "ping -c 1 192.168.205.89\r"
    send "ping -c 1 192.168.205.90\r"
    send "ping ipv6  -c 1 2409:8005:2804:900:5::100\r"
    send "ping ipv6  -c 1 2409:8005:2804:900:5::101\r"

    send "ping -c 1 192.168.205.93\r"
    send "ping -c 1 192.168.205.94\r"
    send "ping ipv6  -c 1 2409:8005:2804:900:7::100\r"
    send "ping ipv6  -c 1 2409:8005:2804:900:7::101\r"

    send "ping -c 1 192.168.250.1\r"
    send "ping -c 1 192.168.250.2\r"
    send "ping ipv6  -c 1 2409:8004:2842:1020::102\r"
    send "ping ipv6  -c 1 2409:8004:2842:1020::103\r"

    # exit
    send "exit\r"
}
}
expect eof
EOF
