#!/bin/bash
# 时间
CURRENT_DATE=$(date +"%Y-%m-%d") # 文件夹-天
CURRENT_TIME=$(date +"%Y-%m-%d-%H-%M-%S") # 日志-秒
LOG_DIR="./xunjian_log/$CURRENT_DATE" # 目录精确到日志
#---------------------1.注意文件夹的命名----------------------------------------------
LOGFILE="$LOG_DIR/hs_renminlu_$CURRENT_TIME.log" # 日志精确到秒
mkdir -p "$LOG_DIR" # 创建精确到天  目录

/usr/bin/expect << EOF
set timeout -1
log_file $LOGFILE

# 分割
#puts "----------------------------------------------------------------------------------------------------------"
#----------------------------2.注意IP是否是交换机的---------------------------------------------------
#交换机IP核查[检查区域]
puts "===============ji_fang河北衡水人民路机房hs_renminlu 10.126.220.51"
spawn ssh -o HostKeyAlgorithms=+ssh-rsa -o PubkeyAcceptedKeyTypes=+ssh-rsa weihu@10.126.220.51
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
    send "ping -c 1 192.168.205.69\r"
    send "ping -c 1 192.168.205.70\r"
    send "ping ipv6  -c 1 2409:8005:2805:900:3::100\r"
    send "ping ipv6  -c 1 2409:8005:2805:900:3::101\r"

    send "ping -c 1 192.168.205.77\r"
    send "ping -c 1 192.168.205.78\r"
    send "ping ipv6  -c 1 2409:8005:2805:30::100\r"
    send "ping ipv6  -c 1 2409:8005:2805:30::101\r"

    # exit
    send "exit\r"
}
}
expect eof
EOF
