su root
useradd xyblue
passwd xyblue
mkdir /home/xyblue
chown xyblue:xyblue /home/xyblue
sudo chmod 700 /home/xyblue
cd /home/xyblue
vi .bashrc

    
添加cd ~                 :wq
touch .bashrc