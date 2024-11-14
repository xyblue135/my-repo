# 检查JAVA
首先我们输入`java -version` 如果`not found`的话,则未安装java.然厚我们选择我们需要的版本安装即可.
![image-202312175531781.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-202312175531781.png)
![image-202312175821952.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-202312175821952.png)
# Java说明
### JDK
JDK 的英文全称是 Java Development Kit。JDK是用于制作程序和Java应用程序的软件开发环境。Java 开发人员可以在 Windows、macOS、Solaris 和 Linux 上使用，是一个跨平台编程语言。JDK 帮助他们编写和运行 Java 程序。可以在同一台计算机上安装多个 JDK 版本。
### JRE
JRE 的英文全称是 Java Runtime Environment。JRE 是一个旨在运行其他软件的软件(有点绕口)。它包含类库、加载器类和 JVM。简单来说，如果你想运行 Java 程序，你需要 JRE。如果您不是程序员，则无需安装 JDK，只需安装 JRE 即可运行 Java 程序。不过，所有 JDK 版本都与 Java Runtime Environment 捆绑在一起，因此无需在 PC 单独下载和安装 JRE。JRE 的完整形式是 Java 运行时环境。
### JVM
JVM 的英文全称是Java Virtual Machine。JVM 是一个引擎，它提供运行时环境驱动 Java 代码或应用程序。它将 Java 字节码转换为机器语言。JVM 是 Java 运行环境 (JRE) 的一部分。它不能单独下载和安装。要安装 JVM，您需要安装 JRE。JVM的就是Java虚拟机。
在许多其他编程语言中，编译器为特定系统生成机器代码。但是，Java 编译器则称为 JVM 虚拟机生成代码。
## 为什么要使用
### 为什么要使用 JDK?
以下是使用JDK的重要原因：
- JDK 包含编写 Java 程序所需的工具，以及执行它们的 JRE。
- 它包括编译器、Java 应用程序启动器、Appletviewer 等。
- 编译器将用 Java 编写的代码转换为字节码。
- Java 应用程序打开一个 JRE，加载必要的类，并执行它的 main 方法。
### 为什么要使用 JRE?
以下是使用 JRE 的重要原因：
- JRE 包含类库、JVM 和其他支持文件。它不包含任何用于 Java 开发的工具，如调试器、编译器等。
- 它使用重要的包和类，如 math、swingetc、util、lang、awt 和运行时库。
- 如果您必须运行 Java 程序，就必须在您的系统中安装 JRE。
### 为什么选择JVM?
以下是使用 JVM 的重要原因：
- JVM 提供了一种独立于平台的方式来执行 Java 源代码。
- 它有许多库、工具和框架。
- 一旦你运行 Java 程序，你就可以在任何平台上运行并节省大量时间。
- JVM 带有 JIT(Just-in-Time)编译器，可将 Java 源代码转换为机器语言。因此，它比常规应用程序运行得更快。
## 特点
### JDK的特点
以下是 JDK的重要特性：
- 它使您能够在单个 catch 块中处理多个扩展。
- JDK 包含了 JRE 的所有特性。
- 它包含开发工具，例如编译器、调试器等。
- JDK 提供了开发和执行 Java 源代码的环境。
- 它可以安装在 Windows、Unix 和 Mac 操作系统上。
- 菱形运算符可用于指定泛型类型接口，而不是编写确切的类型接口。
### JRE的特点
以下是 JRE 的重要特性：
- Java 运行时环境是 JVM 实际运行所使用的一组工具。
- JRE 包含部署技术，包括 Java Web Start 和 Java Plug-in。
- 开发人员可以轻松地在 JRE 中运行源代码，但不能编写和编译 Java 程序。
- 它包括集成库，如 Java 数据库连接 (JDBC)、远程方法调用 (RMI)、Java 命名和目录接口 (JNDI) 等。
- JRE 有 JVM 和 Java HotSpot 虚拟机客户端。
## JVM的特点
以下是 JVM 的重要特性：
- 它使您能够在云环境或设备中运行应用程序。
- Java 虚拟机将字节码转换为特定于机器的代码。
- 它提供了基本的 Java 功能，如内存管理、安全性、垃圾收集等。
- JVM 通过使用 Java Runtime Environment 提供的库和文件来运行程序。
- JDK 和 JRE 都包含 Java 虚拟机。
- 它可以逐行执行java程序，因此也称为解释器。
- JVM 易于定制，例如，您可以为其分配最小和最大内存。
- 它独立于硬件和操作系统。因此，您可以编写一次 java 程序并在任何地方运行。
## 区别
- JDK是一个软件开发工具包，而JRE是一个允许Java程序运行的软件包，JVM则是一个执行字节码的环境。
- JDK的全称是Java Development Kit，JRE的全称是Java Runtime Environment，而JVM的全称是Java Virtual Machine。
- JDK 是平台相关的，JRE 也是平台相关的，但是 JVM 不是平台相关的。
- JDK 包含开发、调试等工具。JRE 包含类库和其他支持文件，而软件开发工具不包含在 JVM 中。
- JDK 附带安装程序，另一方面，JRE 仅包含执行源代码的环境，而 JVM 捆绑在软件 JDK 和 JRE 中。


# 安装
我这里安装的为jdk8
```
sudo apt install openjdk-8-jre-headless
```
![image-20231217457675.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-20231217457675.png)
等待安装完成.
![image-20231217510181.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-20231217510181.png)
```
java -version #检查是否正确安装
```
![image-2023121765774.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-2023121765774.png)
# 使用IDEA编译一个文件
![image-202312171131629.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-202312171131629.png)
![image-202312171412157.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-202312171412157.png)
![image-20231217169961.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-20231217169961.png)
## 验证运行.jar
使用任意方式将做好的jar导入ubunutu
![image-202312171958489.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-202312171958489.png)
然后即可运行此打包完毕的jar
```
java -jar test.jar
```
![image-202312172016666.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-202312172016666.png)
## 验证运行class
命令:
```
java -cp your_program.jar your.mainclass
```
## 失败原因
程序需要访问系统文件的话,如/etc,需要使用root权限来运行,chmod
程序涉及端口使用,如80,也需要root来运行.
# java启动脚本
```
xyblue@xyblue-virtual-machine:~$ java -jar /home/xyblue/1test/test.jar
我叫xyblue
我叫xyblue2
我叫xyblue3
```
对于上述命令来说,还是有点不太方便的说.且到了后期带的参数会比较多,不太适合.除非你真的是天才!
## SH脚本
```
#!/bin/sh

# GO to the script'sdirectory
WORKDIR=$(cd $(dirname $0); pwd)
cd $WORKDIR

# Set the environment if necessary
# export JAVA_HOME-/opt/openjdk8
# export PATH=/opt/openjdk8/bin:$PATH

# Set JVM options
export JAVA_OPTS="-Xmx1024m -XX:MaxMetaspaceSize1024m"

# Run the program
java -jar test.jar


# java -cp jar1:jar2:jar3 my.Helloworld

```
![image-20231217344191.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-20231217344191.png)
1. `WORKDIR=$(cd $(dirname $0); pwd)`：这一行获取脚本所在的目录，并将其保存在 `WORKDIR` 变量中。
2. `cd $WORKDIR`：切换到脚本所在的目录，以确保脚本在正确的工作目录中运行。
3. `Set the environment if necessaryexport` `JAVA_HOME-/opt/openjdk8``export PATH=/opt/openjdk8/bin:$PATH`这些都是环境变量的设置,没有在默认的/usr/bin里面安装java的话,才需要解除这些的注释.
4. 设置了一些环境变量，例如 `JAVA_OPTS`，其中配置了 Java 虚拟机的一些参数（比如堆内存大小等）。
5. 使用 `java -jar test.jar` 命令来运行 `test.jar` 文件，这是一个可执行的 Java JAR 文件。
6. LF,是linux的换行规则,
7. **LF（\n）**：在 Unix、Linux 和 macOS 等类 Unix 系统中，通常使用 LF（换行符）来表示行的结束。
8. **CR（\r）+ LF（\n）**：在早期的 Macintosh 系统中，换行符通常由 CR（回车符）和 LF（换行符）组合成 CR LF 来表示。 
9. **CR（\r）**：在老式的 MacOS（Mac OS 9 及之前版本）中，通常使用 CR（回车符）来表示行的结束。


# Tomcat
### 单独使用Apache Tomcat
Tomcat本身是一个Java程序.
Apache Tomcat 是一个用于托管 Java Web 应用程序的容器，它可以独立运行并处理 Java Servlet 和 JavaServer Pages（JSP）。Tomcat 提供了一个完整的 Web 服务器环境，可以部署和运行 Java Web 应用程序。
### 什么时候需要使用Apache
然而，有时在实际项目中，可能会使用 Apache HTTP Server 作为反向代理（Reverse Proxy），将请求转发给 Tomcat。这种配置可以用于负载均衡、安全性配置、静态内容服务、URL 重写等。在这种情况下，Apache HTTP Server 用作前端服务器，而 Tomcat 作为后端服务器处理 Java Web 应用程序。但这不是必须的，完全可以使用 Tomcat 作为独立的 Web 服务器来托管和运行 Java Web 应用程序。
### Tomcat版本选择
Java8对应的一般为Tomcat8.x版本
Tomcat下载地址:
https://tomcat.apache.org/download-80.cgi
版本对应清单:
https://blog.csdn.net/ThinkWon/article/details/102622738
![image-202312174115948.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-202312174115948.png)
1. **Core**：
    - **zip 和 tar.gz**：这些是核心发行版的压缩文件，包含了 Tomcat 的基本内容，可以在 Unix/Linux 和 Windows 等系统上使用。通常包括了 Tomcat 的运行时文件、配置和启动脚本等。
    - **Windows 版本**：特定于 Windows 平台的压缩文件，分为 32 位和 64 位版本，还包括 Windows 安装程序，便于在 Windows 上快速部署和运行 Tomcat。
2. **Full Documentation**：
    - 包含完整文档的分发版本，通常是 Tomcat 的核心版本，同时包含了完整的文档，以便用户深入了解和使用 Tomcat。
3. **Deployer**：
    - 部署工具的分发版本，通常用于将已编译的 WAR 文件或其他应用程序部署到 Tomcat 服务器。
4. **Extras**：
    - 提供一些额外的组件或工具，例如 Web 服务相关的 JAR 文件，可能是一些扩展或附加功能的分发版本。
5. **Embedded**：
    - 针对嵌入式系统或者特定应用场景的版本，通常是压缩文件形式，用于嵌入到其他应用程序中使用 Tomcat 的核心组件。
### 安装tomcat
下载完成后移动至可使用目录
![image-202312171351233.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-202312171351233.png)
```
tar -axvf apche-tomcat-8.5.97.tar.gz  #解压压缩包
mv apache-tomcat-8.5.97 tomcat #将解压出来的文件夹改名为tomcat
```
### 运行tomcat
在bin目录下面的`startup.sh`即可启动
![image-202312171524915.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-202312171524915.png)
![image-202312171550365.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-202312171550365.png)
查看是否有可执行权限,如果无,记得`chmod +x`就可以启动了
![image-202312171923702.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-202312171923702.png)
有started即正在运行中.
# 监控Tomcat 
## ps
```
ps -ef | grep java     
```
- `ps` 是一个用于显示当前进程状态的命令。
- `-ef` 选项用于指示 `ps` 显示所有进程的信息。`-e` 表示显示所有进程，`-f` 表示显示完整的进程信息。
- `|` 是管道符号，将一个命令的输出传递给另一个命令作为输入。
- `grep java` 是一个用于搜索文本的命令。在这里，它被用于过滤 `ps` 命令的输出，只显示包含 "java" 字符串的行。
![image-20231217243576.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-20231217243576.png)
1. 第一行输出是你的 Java 进程。
    - 用户名 `xyblue` 拥有一个 `java` 进程，进程 ID (PID) 为 `50478`。
    - 这是一个 Java 应用程序，其命令行参数显示了 Java 虚拟机的一些配置信息，比如指定的日志配置文件、类路径、临时目录等等。
    - 该进程的命令行参数包含了 Tomcat 的启动信息，这可能是一个正在运行的 Tomcat 服务器。
2. 第二行是你用来查找进程的 `grep` 命令自身产生的结果。
    - 它会显示所有包含字符串 "java" 的进程，包括你所查找的 `java` 进程，因此它也会显示在结果中。
在这个输出中，第一行显示了一个 `java` 进程，即Tomcat服务器
## netstat
![image-202312173020344.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-202312173020344.png)
  
这个命令 `netstat -anp | grep 8080` 用于列出所有正在监听端口 `8080` 的网络连接或服务。在你的输出中，显示了如下信息：
- `tcp6` 表示这是一个 IPv6 的 TCP 协议连接。
- `:::8080` 表示正在监听的端口号是 `8080`，`:::` 表示所有 IPv6 地址的连接都在监听这个端口。
- `LISTEN` 表示这是一个处于监听状态的连接。
- `50478/java` 显示了正在监听端口 `8080` 的进程，其进程 ID (PID) 为 `50478`，且该进程是一个 Java 进程。
- 可以看到50478进程正在使用8080端口,所以是Tomcat在使用.但每次启动Tomcat的进程号是随机分配的.
## 开放端口
使用以下命令来操作,虽然你也可以直接关闭防火墙.
```
sudo ufw allow 8080 #放行8080
sudo ufw status #查看防火墙状态.
```
![image-202312173010683.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-202312173010683.png)
## 验证网站
![image-20231217324422.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-20231217324422.png)
## 关闭Tomcat
```
cd /home/xyblue/1test/tomcat/bin/   #相对路径
./shutdown.sh
```

```
/home/xyblue/1test/tomcat/bin/shutdown.sh         #绝对路径
```
![image-202312181152292.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-202312181152292.png)
![image-202312181452456.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-202312181452456.png)
![image-202312181518404.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-202312181518404.png)
# 配置Tomcat
修改前需要提前备份server.xml文件
![image-202312185847463.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-202312185847463.png)
## 测试开放端口
测试开发端口一般指定的为80端口,选择性更改.
![image-20231218825445.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-20231218825445.png)
![image-202312181011271.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-202312181011271.png)

## 更改网站
![image-202312183311360.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-202312183311360.png)
我们可以把网站更改到其他目录下面运行,比如我现在的/opt/www/ROOT
注意:必须是ROOT
![image-20231218275689.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-20231218275689.png)
接下来把写好的网站复制到linux系统中即可.
![image-20231218347893.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-20231218347893.png)
![image-20231218345657.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-20231218345657.png)
可能遇到的问题.
![image-202312182712634.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-202312182712634.png)
## 给予权限
我们给以选择给766或者700权限
```
sudo chmod +766 ROOT/
sudo chmod +766 -R ROOT
```
## 解压
### 法一
```
tar unzip 压缩名字       #请根据自己格式选择格式的解压参数
mv /path/to/A/* /path/to/B/   #移动目录到上层去
```
### 法二(不保留解压名)
```
unzip -j your_file.zip -d /your/destination/folder   #解压到指定目录
unzip -j your_file.zip -d .             #解压到此目录
```
因为直接解压的话还需要移动目录,比较费时间(小文件)
默认情况下会保留压缩包中的文件结构，包括文件夹的名称。
![image-20231218548675.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-20231218548675.png)
## 重启
修改完毕后,重启Tomcat服务即可,根据自己路径.
![image-20231218383896.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-20231218383896.png)
## 查看日志
是否成功,我们使用cat 查看日志
![image-20231218411699.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-20231218411699.png)

可以看到在尝试绑定到端口 80 时开始出现错误。这是因为低于 1024 的端口需要 root/admin 权限。
我们用ROOT来启动Tomcat
```
sudo ./startup.sh
```
成功
![image-202312182543194.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-202312182543194.png)

# Tomcat脚本
## 自带的
### startup.sh
### shutdown.sh
### catalia.sh(实际上,startup.sh和shutdown.sh都是调用了catalia.sh)
`catalina.sh`附带`start`,`stop`,`run`参数分别可以启动Tomcat,停止Tomcat,以及调试(前台输出)Tomcat.
![image-202312184523927.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-202312184523927.png)
![image-202312184858549.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-202312184858549.png)
![image-202312184929151.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-202312184929151.png)
# Win系统中的Tomcat
下载完成后直接启动可能缺少环境变量,可以去oracle直接安装下载,或者去bellsoft之类的网站下载.
![image-2023121935609.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-2023121935609.png)
![image-20231219418138.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-20231219418138.png)
我这里就直接下载一个压缩包的形式,自己改环境变量吧.
https://bell-sw.com/pages/downloads/#jdk-17-lts
![image-2023121987444.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-2023121987444.png)
我们打开`startup.bat`文档可以看到,这个文档这两行的信息表示:
- `if exist`：这是一个条件语句，用于检查指定路径下的文件或文件夹是否存在。
- `"%CATALINA_HOME%\bin\catalina.bat"`：这是要检查存在性的路径。`%CATALINA_HOME%` 是一个环境变量，表示 Apache Tomcat 的安装目录。
- `goto okHome`：如果指定路径下的文件存在，就跳转到脚本中标签为 `okHome` 的位置执行后续的代码。
这行代码的目的是检查 `%CATALINA_HOME%\bin\catalina.bat` 这个文件是否存在。如果存在，脚本将执行 `okHome` 标签下的代码；如果不存在，将会执行 `okHome` 标签之后的代码（如果有的话）或者直接跳过相关部分。
![image-20231219740489.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-20231219740489.png)
然后我们跳转到`catalina.bat`,可以看到
![image-202312191234357.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-202312191234357.png)
1. `rem Get standard environment variables`：注释，说明接下来的代码段获取标准环境变量。
2. `if not exist "%CATALINA_BASE%\bin\setenv.bat" goto checkSetenvHome`：检查 `%CATALINA_BASE%\bin\setenv.bat` 文件是否存在。如果文件不存在，将跳转到标签 `checkSetenvHome`。
3. `call "%CATALINA_BASE%\bin\setenv.bat"`：如果 `setenv.bat` 存在于 `%CATALINA_BASE%\bin` 目录中，将会调用该批处理文件。
4. `goto setenvDone`：跳转到标签 `setenvDone`，跳过后续代码段。
5. `:checkSetenvHome`：标签，用于标记一个条件分支的开始。
6. `if exist "%CATALINA_HOME%\bin\setenv.bat" call "%CATALINA_HOME%\bin\setenv.bat"`：检查 `%CATALINA_HOME%\bin\setenv.bat` 文件是否存在，如果存在，则调用该批处理文件。
7. `:setenvDone`：标签，标记了环境变量处理完成的位置。
8. 类似地，后续部分也是类似的条件判断和处理，但是针对的是 Java 环境变量。它会检查 `%CATALINA_HOME%\bin\setclasspath.bat` 文件是否存在，如果存在则调用该文件来设置 Java 的类路径。如果文件不存在，则输出错误信息并跳到结束标签 `end`。
## 总体来说
这段脚本用于检查和调用一些环境变量相关的批处理文件，以确保程序执行所需的环境设置正确。
启动文件startup.bat → catalina.bat → setclasspath.bat，setclasspath.bat 里读取系统的环境变量。
## 解决方法
### 修改setclasspath.bat 文件
因为这个bat会读取环境变量的数值,因此我们帮助这个bat声明一下就可以了.
![image-202312192349120.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-202312192349120.png)
![image-202312192452495.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-202312192452495.png)
![image-202312192419475.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-202312192419475.png)
![image-202312192435242.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-202312192435242.png)
成功
![image-202312195225503.png](00_sync/00linux/Linux上Java_tomcat_sh/Linux上Java_tomcat_sh/image-202312195225503.png)
