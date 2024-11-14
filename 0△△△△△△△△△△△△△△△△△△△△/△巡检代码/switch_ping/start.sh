#!/bin/bash


> print.txt

# 按顺序执行脚本，并将所有输出重定向到print.txt文件中
./zi_jiaoben/sjz_kaifaqu.sh 2>&1 | tee -a print.txt
./zi_jiaoben/sjz_dongfenglu.sh 2>&1 | tee -a print.txt
./zi_jiaoben/sjz_luquan.sh 2>&1 | tee -a print.txt

./zi_jiaoben/hs_hepinglu.sh 2>&1 | tee -a print.txt
./zi_jiaoben/hs_renminlu.sh 2>&1 | tee -a print.txt

./zi_jiaoben/hd_quanqiutong.sh 2>&1 | tee -a print.txt
./zi_jiaoben/hd_yidongdasha.sh 2>&1 | tee -a print.txt

./zi_jiaoben/xt_donghuan.sh 2>&1 | tee -a print.txt
./zi_jiaoben/xt_zonghelou.sh 2>&1 | tee -a print.txt

./zi_jiaoben/cz_yidongdalou.sh 2>&1 | tee -a print.txt
./zi_jiaoben/cz_shuniulou.sh 2>&1 | tee -a print.txt

./zi_jiaoben/bd_shujuzhongxin.sh 2>&1 | tee -a print.txt
./zi_jiaoben/bd_qingyuan.sh 2>&1 | tee -a print.txt
./zi_jiaoben/bd_jindilu.sh 2>&1 | tee -a print.txt

./zi_jiaoben/cd_kaifaqu.sh 2>&1 | tee -a print.txt
./zi_jiaoben/cd_wulielu.sh 2>&1 | tee -a print.txt

./zi_jiaoben/qhd_shengchanlou.sh 2>&1 | tee -a print.txt
./zi_jiaoben/qhd_zonghelou.sh 2>&1 | tee -a print.txt

./zi_jiaoben/zjk_baoshanjie.sh 2>&1 | tee -a print.txt
./zi_jiaoben/zjk_weisanlu.sh 2>&1 | tee -a print.txt

./zi_jiaoben/ts_fengnan.sh 2>&1 | tee -a print.txt
./zi_jiaoben/ts_tianyuan.sh 2>&1 | tee -a print.txt

./zi_jiaoben/lf_shujuzhongxin.sh 2>&1 | tee -a print.txt
./zi_jiaoben/lf_yidongdalou.sh 2>&1 | tee -a print.txt
./zi_jiaoben/cuowu_yanzheng.sh 2>&1 |tee -a print.txt


echo "All scripts have been executed." 2>&1 | tee -a print.txt





python3 print_guolv.py

# 返回过滤完成的消息
echo "Filtering completed."

