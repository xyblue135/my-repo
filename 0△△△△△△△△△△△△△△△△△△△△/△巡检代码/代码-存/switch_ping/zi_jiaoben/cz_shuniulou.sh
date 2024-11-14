#!/bin/bash
# 时间
CURRENT_DATE=$(date +"%Y-%m-%d") # 文件夹-天
CURRENT_TIME=$(date +"%Y-%m-%d-%H-%M-%S") # 日志-秒
LOG_DIR="./xunjian_log/$CURRENT_DATE" # 目录精确到日志
#---------------------1.注意文件夹的命名----------------------------------------------
LOGFILE="$LOG_DIR/cz_shuniulou_$CURRENT_TIME.log" # 日志精确到秒
mkdir -p "$LOG_DIR" # 创建精确到天  目录

/usr/bin/expect << EOF
set timeout -1
log_file $LOGFILE

# 分割
#puts "----------------------------------------------------------------------------------------------------------"
#----------------------------2.注意IP是否是交换机的---------------------------------------------------
puts "===============ji_fang河北沧州枢纽楼机房cz_shuniulou 10.126.219.211"
#交换机IP核查[检查区域]
spawn ssh -o HostKeyAlgorithms=+ssh-rsa -o PubkeyAcceptedKeyTypes=+ssh-rsa weihu@10.126.219.211
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
    send "ping -c 1 192.168.207.9\r"
    send "ping -c 1 192.168.207.10\r"
    send "ping ipv6  -c 1 2409:8005:2A04:0900:808::100\r"
    send "ping ipv6  -c 1 2409:8005:2A04:0900:808::101\r"

    send "ping -c 1 192.168.205.81\r"
    send "ping -c 1 192.168.205.82\r"
    send "ping ipv6  -c 1 2409:8005:2804:900:1::100\r"
    send "ping ipv6  -c 1 2409:8005:2804:900:1::101\r"

    send "ping -c 1 192.168.205.97\r"
    send "ping -c 1 192.168.205.98\r"
    send "ping ipv6  -c 1 2409:8005:2804:900:9::100\r"
    send "ping ipv6  -c 1 2409:8005:2804:900:9::101\r"

    send "ping -c 1 192.168.205.101\r"
    send "ping -c 1 192.168.205.102\r"
    send "ping ipv6  -c 1 2409:8004:2804:10::100\r"
    send "ping ipv6  -c 1 2409:8004:2804:10::101\r"

    send "ping -c 1 192.168.250.9\r"
    send "ping -c 1 192.168.250.10\r"
    send "ping ipv6  -c 1 2409:8004:2842:1020::100\r"
    send "ping ipv6  -c 1 2409:8004:2842:1020::101\r"

    # exit
    send "exit\r"
}
}
expect eof
EOF
