#!/bin/bash

# 检测当前目录是否存在 zi_jiaoben 文件夹
#if [ ! -d "zi_jiaoben" ]; then
 #   echo "Error: Directory 'zi_jiaoben' not found in the current directory."
  #  exit 1
#fi

# 重置 print.txt 文件
> print.txt

# 输出 print.txt 已清空的信息
echo "print.txt 已经被清空" | tee -a print.txt

# 记录开始时间
#START_TIME=$(date +%s)
#echo "====================1.Start time: $(date +"%Y-%m-%d %H:%M:%S")====================" | tee -a print.txt

# 按顺序执行脚本，并将所有输出重定向到 print.txt 文件中
echo "减少IO输出脚本正在执行中，预估不超过30秒" | tee -a print.txt
{
  ./zi_jiaoben/sjz_kaifaqu.sh
  ./zi_jiaoben/sjz_dongfenglu.sh
  ./zi_jiaoben/sjz_luquan.sh

  ./zi_jiaoben/hs_hepinglu.sh
  ./zi_jiaoben/hs_renminlu.sh

  ./zi_jiaoben/hd_quanqiutong.sh
  ./zi_jiaoben/hd_yidongdasha.sh

  ./zi_jiaoben/xt_donghuan.sh
  ./zi_jiaoben/xt_zonghelou.sh

  ./zi_jiaoben/cz_yidongdalou.sh
  ./zi_jiaoben/cz_shuniulou.sh

  ./zi_jiaoben/bd_shujuzhongxin.sh
  ./zi_jiaoben/bd_qingyuan.sh
  ./zi_jiaoben/bd_jindilu.sh

  ./zi_jiaoben/cd_kaifaqu.sh
  ./zi_jiaoben/cd_wulielu.sh

  ./zi_jiaoben/qhd_shengchanlou.sh
  ./zi_jiaoben/qhd_zonghelou.sh

  ./zi_jiaoben/zjk_baoshanjie.sh
  ./zi_jiaoben/zjk_weisanlu.sh

  ./zi_jiaoben/ts_fengnan.sh
  ./zi_jiaoben/ts_tianyuan.sh

  ./zi_jiaoben/lf_yidongdalou.sh
  ./zi_jiaoben/lf_shujuzhongxin.sh
  ./zi_jiaoben/cuowu_yanzheng.sh

} >> print.txt 2>&1
echo "All scripts have been executed." | tee -a print.txt

# 记录结束时间
#END_TIME=$(date +%s)
#echo "====================2.End time: $(date +"%Y-%m-%d %H:%M:%S")====================" | tee -a print.txt

# 计算并输出时间间隔
#INTERVAL=$(echo "$END_TIME - $START_TIME" | bc)
#echo "====================3.Total execution time: $INTERVAL seconds====================" | tee -a print.txt

# 检查 print.txt 是否为空
#if [ ! -s "print.txt" ]; then
 #   echo "print.txt is empty."
#else
 #   echo "print.txt has content."
#fi

# 执行 Python 脚本进行过滤
echo "正在将print.txt文档过滤出success以及failed" | tee -a print.txt
python3 print_guolv.py
echo "过滤完成" | tee -a print.txt

