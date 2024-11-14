#!/bin/bash
# 时间
CURRENT_DATE=$(date +"%Y-%m-%d") # 文件夹-天
CURRENT_TIME=$(date +"%Y-%m-%d-%H-%M-%S") # 日志-秒
LOG_DIR="./xunjian_log/$CURRENT_DATE" # 目录精确到日志
#---------------------1.注意文件夹的命名----------------------------------------------
LOGFILE="$LOG_DIR/sjz_kaifaqu_$CURRENT_TIME.log" # 日志精确到秒
mkdir -p "$LOG_DIR" # 创建精确到天  目录

/usr/bin/expect << EOF
set timeout -1
log_file $LOGFILE

# 分割
#puts "----------------------------------------------------------------------------------------------------------"
#----------------------------2.注意IP是否是交换机的---------------------------------------------------
#交换机IP核查[检查区域]
puts "===============ji_fang河北石家庄开发区机房sjz_kaifaqu 10.126.219.132"
spawn ssh -o HostKeyAlgorithms=+ssh-rsa -o PubkeyAcceptedKeyTypes=+ssh-rsa weihu@10.126.219.132
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
    send "ping -c 1 192.168.250.9\r"
    send "ping -c 1 192.168.250.10\r"
    send "ping ipv6  -c 1 2409:8005:2801:3B00:5::100\r"
    send "ping ipv6  -c 1 2409:8005:2801:3B00:5::101\r"

    send "ping -c 1 192.168.102.25\r"
    send "ping -c 1 192.168.102.26\r"
    send "ping ipv6  -c 1 2409:8005:2801:300:2::100\r"
    send "ping ipv6  -c 1 2409:8005:2801:300:2::101\r"

    send "ping -c 1 192.168.5.1\r"
    send "ping -c 1 192.168.5.2\r"
    send "ping ipv6  -c 1 2409:8005:2A01:1900:101::100\r"
    send "ping ipv6  -c 1 2409:8005:2A01:1900:101::101\r"

    send "ping -c 1 192.168.4.1\r"
    send "ping -c 1 192.168.4.2\r"
    send "ping ipv6  -c 1 2409:8004:2810:1050::100\r"
    send "ping ipv6  -c 1 2409:8004:2810:1050::101\r"

    send "ping -c 1 192.168.2.33\r"
    send "ping -c 1 192.168.2.34\r"
    send "ping ipv6  -c 1 2409:8004:2811:1010::100\r"
    send "ping ipv6  -c 1 2409:8004:2811:1010::101\r"

    send "ping -c 1 192.168.4.5\r"
    send "ping -c 1 192.168.4.6\r"
    send "ping ipv6  -c 1 2409:8004:2810:1030::100\r"
    send "ping ipv6  -c 1 2409:8004:2810:1030::101\r"

    # exit
    send "exit\r"
}
}
expect eof
EOF
