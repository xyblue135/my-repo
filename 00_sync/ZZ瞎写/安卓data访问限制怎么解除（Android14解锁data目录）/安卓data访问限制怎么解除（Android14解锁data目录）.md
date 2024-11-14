在最新安卓14+系统后，系统已经限制了/Android/data应用目录授权，导致三方App已无法读取相关目录文件。为此【雪豹速清】【KB视频工厂】在最新版本中加入了Shizuku方案，通过Shizuku方案能免ROOT读取/Android/data目录下的文件，并可大幅提升扫描速度，同时支持操作SD卡和应用双开目录文件
PS1：本教程仅适用于安卓系统，由于华为鸿蒙系统没有无线调试功能，所以不能使用本教程中的无线调试来激活，需要连接电脑使用adb的方式激活，可以在Shizuku首页底部点击「了解Shizuku」来查看官方教程
PS2：本次教程以小米手机为例，不同手机品牌可能略有差异。如果您手机还没安装Shizuku，请自行搜索安装或到【雪豹速清】或【KB视频工厂】设置页面中点击Shizuku下载

1.开启开发者模式
2.激活Shizuku，通过无线调试启动
![7bd32587bbe6be39e5c1e8b451115fd6.image.png|400](00_sync/ZZ瞎写/安卓data访问限制怎么解除（Android14解锁data目录）/安卓data访问限制怎么解除（Android14解锁data目录）/7bd32587bbe6be39e5c1e8b451115fd6.image.png)
![b3104a03ba673d67f147a8bb66860f3e.image.png](00_sync/ZZ瞎写/安卓data访问限制怎么解除（Android14解锁data目录）/安卓data访问限制怎么解除（Android14解锁data目录）/b3104a03ba673d67f147a8bb66860f3e.image.png)
![f1c185efd9df6316e3a49169c84d97b0.image.png](00_sync/ZZ瞎写/安卓data访问限制怎么解除（Android14解锁data目录）/安卓data访问限制怎么解除（Android14解锁data目录）/f1c185efd9df6316e3a49169c84d97b0.image.png)
![5c99f754743f97bcd43c6353eca2a13c.image.png](00_sync/ZZ瞎写/安卓data访问限制怎么解除（Android14解锁data目录）/安卓data访问限制怎么解除（Android14解锁data目录）/5c99f754743f97bcd43c6353eca2a13c.image.png)
![4c27ada67ac13f42c680fa7de9271a88.image.png](00_sync/ZZ瞎写/安卓data访问限制怎么解除（Android14解锁data目录）/安卓data访问限制怎么解除（Android14解锁data目录）/4c27ada67ac13f42c680fa7de9271a88.image.png)
总结
#通过无线调试启动：点击“输入配对码”后立刻提示失败

#MIUI（小米、POCO）

在系统设置的“通知管理”-“通知显示设置”将通知样式切换为“原生样式”。

#通过无线调试启动/通过连接电脑启动：adb 权限受限

#MIUI（小米、POCO）

在“开发者选项”中开启“USB 调试（安全设置）”。注意，这和“USB 调试”是两个分开的选项。

#ColorOS（OPPO & OnePlus）

在“开发者选项”中关闭“权限监控”。

#Flyme（魅族）

在“开发者选项”中关闭“Flyme 支付保护”。