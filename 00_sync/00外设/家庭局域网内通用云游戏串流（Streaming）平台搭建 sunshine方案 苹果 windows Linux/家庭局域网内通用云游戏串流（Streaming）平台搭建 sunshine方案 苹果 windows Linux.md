目标及实现方法：
一台电脑家庭内网串流到电视等终端玩游戏，或者在家里任何一台内网显示设备中操控主电脑
利用开源软件sunshine主电脑当服务端，终端安装moonlight客户端实现

  1. sunshine软件，安装在主电脑上，下载自己操作系统的版本
        - https://github.com/LizardByte/Sunshine/releases
    2. 安装sunshine会提示安装手柄驱动
        - ViGEmBus_1.21.442_x64_x86_arm64.exe
    3. moonlight软件，安装在电视等终端上，下载自己操作系统版本
        - https://github.com/moonlight-stream
    4. KDE Connect类似软件，安装在手机和主电脑上，用于局域网内控制主电脑
        - https://kdeconnect.kde.org/download.html

    1. 主电脑运行sunshine软件
    2. 客户端moonlight打开内网内与主机配对，会有配对编码
    3. https://127.0.0.1:47990/ 浏览器打开左上角PIN输入2步骤的配对编码
    后续可以用KDE Connect软件手机当成鼠标键盘操作电视moonlight 作者：若雨轻盈 https://www.bilibili.com/read/cv21945448/
    
   ![image-202410222030418.png](00_sync/00%E5%A4%96%E8%AE%BE/%E5%AE%B6%E5%BA%AD%E5%B1%80%E5%9F%9F%E7%BD%91%E5%86%85%E9%80%9A%E7%94%A8%E4%BA%91%E6%B8%B8%E6%88%8F%E4%B8%B2%E6%B5%81%EF%BC%88Streaming%EF%BC%89%E5%B9%B3%E5%8F%B0%E6%90%AD%E5%BB%BA%20sunshine%E6%96%B9%E6%A1%88%20%E8%8B%B9%E6%9E%9C%20windows%20Linux/%E5%AE%B6%E5%BA%AD%E5%B1%80%E5%9F%9F%E7%BD%91%E5%86%85%E9%80%9A%E7%94%A8%E4%BA%91%E6%B8%B8%E6%88%8F%E4%B8%B2%E6%B5%81%EF%BC%88Streaming%EF%BC%89%E5%B9%B3%E5%8F%B0%E6%90%AD%E5%BB%BA%20sunshine%E6%96%B9%E6%A1%88%20%E8%8B%B9%E6%9E%9C%20windows%20Linux/image-202410222030418.png)