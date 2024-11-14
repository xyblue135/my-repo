#!/bin/bash
# 时间
CURRENT_DATE=$(date +"%Y-%m-%d") # 文件夹-天
CURRENT_TIME=$(date +"%Y-%m-%d-%H-%M-%S") # 日志-秒
LOG_DIR="./xunjian_log/$CURRENT_DATE" # 目录精确到日志
#---------------------1.注意文件夹的命名----------------------------------------------
LOGFILE="$LOG_DIR/bd_jindi_$CURRENT_TIME.log" # 日志精确到秒
mkdir -p "$LOG_DIR" # 创建精确到天  目录

/usr/bin/expect << EOF
set timeout -1
log_file $LOGFILE

# 分割
#puts "----------------------------------------------------------------------------------------------------------"
#----------------------------2.注意IP是否是交换机的---------------------------------------------------
puts "===============ji_fang河北保定金迪路机房bd_jindilu   10.126.219.195"
#交换机IP核查[检查区域]
spawn ssh -o HostKeyAlgorithms=+ssh-rsa -o PubkeyAcceptedKeyTypes=+ssh-rsa weihu@10.126.219.195
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
    send "ping -c 1 192.168.205.25\r"
    send "ping -c 1 192.168.205.26\r"
    send "ping ipv6  -c 1 2409:8005:2806:900:1::100\r"
    send "ping ipv6  -c 1 2409:8005:2806:900:1::101\r"

    send "ping -c 1 192.168.255.253\r"
    send "ping -c 1 192.168.255.254\r"
    send "ping ipv6  -c 1 2409:8005:2A06:1900:101::100\r"
    send "ping ipv6  -c 1 2409:8005:2A06:1900:101::100\r"

    send "ping -c 1 192.168.205.29\r"
    send "ping -c 1 192.168.205.30\r"
    send "ping ipv6  -c 1 2409:8005:2806:900:7::100\r"
    send "ping ipv6  -c 1 2409:8005:2806:900:7::101\r"

    # exit
    send "exit\r"
}
}
expect eof
EOF
