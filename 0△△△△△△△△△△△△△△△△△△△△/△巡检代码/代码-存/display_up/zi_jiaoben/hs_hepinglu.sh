#!/bin/bash
# 时间
CURRENT_DATE=$(date +"%Y-%m-%d") # 文件夹-天
CURRENT_TIME=$(date +"%Y-%m-%d-%H-%M-%S") # 日志-秒
LOG_DIR="./xunjian_log/$CURRENT_DATE" # 目录精确到日志
#---------------------1.注意文件夹的命名----------------------------------------------
LOGFILE="$LOG_DIR/hs_hepinglu_$CURRENT_TIME.log" # 日志精确到秒
mkdir -p "$LOG_DIR" # 创建精确到天  目录
/usr/bin/expect << EOF
set timeout -1
log_file $LOGFILE
# 分割
#puts "----------------------------------------------------------------------------------------------------------"
#----------------------------2.注意IP是否是交换机的---------------------------------------------------
puts "ji_fang河北衡水和平路机房hs_hepinglu 10.126.220.35"
spawn ssh -o HostKeyAlgorithms=+ssh-rsa -o PubkeyAcceptedKeyTypes=+ssh-rsa weihu@10.126.220.35
expect {
    "yes/no" { send "yes\r"; exp_continue }
    "password:" { send "admin@h3c.com\r" }
}
expect ">"
send "display interface GigabitEthernet1/0/3 brief\r"
expect ">"
send "display interface GigabitEthernet1/0/9 brief\r"
expect ">"
send "exit\r"
send "echo hs_hepinglu=========================================================================================================\r"
expect eof
EOF