
# 流程
## 下载
下载新的python包并解压
https://www.python.org/
https://www.python.org/ftp/python/3.10.12/
https://www.python.org/downloads/release/python-3102/
https://pip.pypa.io/en/stable/installation/
![image-202410285330443.png](3%E5%8F%AF%E4%BB%A5%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/%E3%80%90%E6%84%9F%E8%A7%89%E6%9C%89%E9%97%AE%E9%A2%98%E3%80%91%E5%8F%8C%E7%89%88%E6%9C%ACpython/%E5%8F%8C%E7%89%88%E6%9C%ACpython/image-202410285330443.png)

从pip网站中下载get-pip.py下来
![image-202410282918231.png|425](3%E5%8F%AF%E4%BB%A5%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/%E3%80%90%E6%84%9F%E8%A7%89%E6%9C%89%E9%97%AE%E9%A2%98%E3%80%91%E5%8F%8C%E7%89%88%E6%9C%ACpython/%E5%8F%8C%E7%89%88%E6%9C%ACpython/image-202410282918231.png)

![image-202410282821247.png|550](3%E5%8F%AF%E4%BB%A5%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/%E3%80%90%E6%84%9F%E8%A7%89%E6%9C%89%E9%97%AE%E9%A2%98%E3%80%91%E5%8F%8C%E7%89%88%E6%9C%ACpython/%E5%8F%8C%E7%89%88%E6%9C%ACpython/image-202410282821247.png)
## 执行代码安装pip
关闭系统代理
```
python get-pip.py
python.exe get-pip.py --no-warn-script-location 可选忽略警告
```
![image-202410283145469.png](3%E5%8F%AF%E4%BB%A5%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/%E3%80%90%E6%84%9F%E8%A7%89%E6%9C%89%E9%97%AE%E9%A2%98%E3%80%91%E5%8F%8C%E7%89%88%E6%9C%ACpython/%E5%8F%8C%E7%89%88%E6%9C%ACpython/image-202410283145469.png)
解压目录会多出
![image-20241028326845.png](3%E5%8F%AF%E4%BB%A5%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/%E3%80%90%E6%84%9F%E8%A7%89%E6%9C%89%E9%97%AE%E9%A2%98%E3%80%91%E5%8F%8C%E7%89%88%E6%9C%ACpython/%E5%8F%8C%E7%89%88%E6%9C%ACpython/image-20241028326845.png)
- `Lib` 是用来存放可供导入的模块和包的地方，包含了标准库和第三方库。
- `Scripts` 是存放可直接在命令行运行的可执行文件的地方，通常用于包管理和其他命令行工具。
考虑到我平常用python或者python3 都代表python3的话，复制三份出来,也可以修改alias才完成
## 修改文件信息
修改这个文件的信息`python313._pth` 添加一行即可
```
python313.zip
.

# Uncomment to run site.main() automatically
#import site
Lib\site-packages
```
## 检查pip安装情况
```
python -m pip --version
```
![image-202410293945946.png|450](3%E5%8F%AF%E4%BB%A5%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/%E3%80%90%E6%84%9F%E8%A7%89%E6%9C%89%E9%97%AE%E9%A2%98%E3%80%91%E5%8F%8C%E7%89%88%E6%9C%ACpython/%E5%8F%8C%E7%89%88%E6%9C%ACpython/image-202410293945946.png)
```
python -m pip list
```
![image-20241029192679.png|475](3%E5%8F%AF%E4%BB%A5%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/%E3%80%90%E6%84%9F%E8%A7%89%E6%9C%89%E9%97%AE%E9%A2%98%E3%80%91%E5%8F%8C%E7%89%88%E6%9C%ACpython/%E5%8F%8C%E7%89%88%E6%9C%ACpython/image-20241029192679.png)
## python和pip环境变量
将这两个路径添加到环境变量
![image-202410292029734.png|391](3%E5%8F%AF%E4%BB%A5%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/%E3%80%90%E6%84%9F%E8%A7%89%E6%9C%89%E9%97%AE%E9%A2%98%E3%80%91%E5%8F%8C%E7%89%88%E6%9C%ACpython/%E5%8F%8C%E7%89%88%E6%9C%ACpython/image-202410292029734.png)
至此免安装的版本就完成了。
必须要添加好，不然插件的命令就不方便使用了
![image-20241029423158.png](3%E5%8F%AF%E4%BB%A5%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/%E3%80%90%E6%84%9F%E8%A7%89%E6%9C%89%E9%97%AE%E9%A2%98%E3%80%91%E5%8F%8C%E7%89%88%E6%9C%ACpython/%E5%8F%8C%E7%89%88%E6%9C%ACpython/image-20241029423158.png)
# 双版本安装
按照一样的套路下载其它版本并更新环境变量即可
左侧为我全局变量的 右侧为未天津爱全局变量的，要是右侧搞全局变量需要控制好变量名字才可以
![image-20241029281119.png](3%E5%8F%AF%E4%BB%A5%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/%E3%80%90%E6%84%9F%E8%A7%89%E6%9C%89%E9%97%AE%E9%A2%98%E3%80%91%E5%8F%8C%E7%89%88%E6%9C%ACpython/%E5%8F%8C%E7%89%88%E6%9C%ACpython/image-20241029281119.png)
# 其他问题
# 不建议全部绿色版
我们使用诸如nuitka编译的时候绿色版将无法进行，也就是嵌入式不可以
![image-202410292530890.png](3%E5%8F%AF%E4%BB%A5%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/%E3%80%90%E6%84%9F%E8%A7%89%E6%9C%89%E9%97%AE%E9%A2%98%E3%80%91%E5%8F%8C%E7%89%88%E6%9C%ACpython/%E5%8F%8C%E7%89%88%E6%9C%ACpython/image-202410292530890.png)
## where多变量
我设置好变量后发现桌面shell无法找到变量，即where python出现两个路径，优先匹配的上面的，但是那个文件无法删除。查了一下，这是微软商店里面的，可以放心删除。
![image-202410295737907.png|450](3%E5%8F%AF%E4%BB%A5%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/%E3%80%90%E6%84%9F%E8%A7%89%E6%9C%89%E9%97%AE%E9%A2%98%E3%80%91%E5%8F%8C%E7%89%88%E6%9C%ACpython/%E5%8F%8C%E7%89%88%E6%9C%ACpython/image-202410295737907.png)
![image-202410293051359.png](3%E5%8F%AF%E4%BB%A5%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/%E3%80%90%E6%84%9F%E8%A7%89%E6%9C%89%E9%97%AE%E9%A2%98%E3%80%91%E5%8F%8C%E7%89%88%E6%9C%ACpython/%E5%8F%8C%E7%89%88%E6%9C%ACpython/image-202410293051359.png)
这样就只有一个了

## 占位符
注意占位符 需要删除掉
![image-20241029115616.png](3%E5%8F%AF%E4%BB%A5%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/%E3%80%90%E6%84%9F%E8%A7%89%E6%9C%89%E9%97%AE%E9%A2%98%E3%80%91%E5%8F%8C%E7%89%88%E6%9C%ACpython/%E5%8F%8C%E7%89%88%E6%9C%ACpython/image-20241029115616.png)
## 卸载python
注意:必须使用安装包来卸载python，这样不会出现太多问题

## 加速站点
1. 清华大学镜像站：
```
pip install nuitka -i https://pypi.tuna.tsinghua.edu.cn/simple
```
2. 西北工业大学镜像站：
```
pip install requests -i https://mirrors.nwpu.edu.cn/pypi/web/simple/
```
3. 华中科技大学镜像站：
```
pip install requests -i https://pypi.mirrors.ustc.edu.cn/simple/
```
4. 阿里云镜像：
```
pip install requests -i https://mirrors.aliyun.com/pypi/simple/
```
全局可以通过编辑用户目录下的`.pip/pip.conf`文件（如果不存在则创建）来实现：只能写一个
```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
不能写两个
```
## 如代码有python和python3
如代码有python和python3嵌套等行为，需要复制一个出来。

