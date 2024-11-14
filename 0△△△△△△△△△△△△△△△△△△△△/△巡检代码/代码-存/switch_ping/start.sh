#!/bin/bash

cd /home/liweining/0000xun_jian/switch_ping/zi_jiaoben
> print.txt

./sjz_kaifaqu.sh 2>&1 | tee -a print.txt
./sjz_dongfenglu.sh 2>&1 | tee -a print.txt
./sjz_luquan.sh 2>&1 | tee -a print.txt

./hs_hepinglu.sh 2>&1 | tee -a print.txt
./hs_renminlu.sh 2>&1 | tee -a print.txt

./hd_quanqiutong.sh 2>&1 | tee -a print.txt
./hd_yidongdasha.sh 2>&1 | tee -a print.txt

./xt_donghuan.sh 2>&1 | tee -a print.txt
./xt_zonghelou.sh 2>&1 | tee -a print.txt

./cz_yidongdalou.sh 2>&1 | tee -a print.txt
./cz_shuniulou.sh 2>&1 | tee -a print.txt

./bd_shujuzhongxin.sh 2>&1 | tee -a print.txt
./bd_qingyuan.sh 2>&1 | tee -a print.txt
./bd_jindilu.sh 2>&1 | tee -a print.txt

./cd_kaifaqu.sh 2>&1 | tee -a print.txt
./cd_wulielu.sh 2>&1 | tee -a print.txt

./qhd_shengchanlou.sh 2>&1 | tee -a print.txt
./qhd_zonghelou.sh 2>&1 | tee -a print.txt

./zjk_baoshanjie.sh 2>&1 | tee -a print.txt
./zjk_weisanlu.sh 2>&1 | tee -a print.txt

./ts_fengnan.sh 2>&1 | tee -a print.txt
./ts_tianyuan.sh 2>&1 | tee -a print.txt

./lf_shujuzhongxin.sh 2>&1 | tee -a print.txt
./lf_yidongdalou.sh 2>&1 | tee -a print.txt
./cuowu_yanzheng.sh 2>&1 |tee -a print.txt


echo "=================已写入print.txt================="
python3 print_guolv.py
echo "==================已过滤================="





