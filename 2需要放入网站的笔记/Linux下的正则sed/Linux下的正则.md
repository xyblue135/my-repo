# 说明
```
> **正则表达式**，又称正规表示式、正规表示法、正规表达式、规则表达式、常规表示法（英语：Regular Expression，在代码中常简写为 regex、regexp 或 RE），计算机科学的一个概念。正则表达式使用单个字符串来描述、匹配一系列符合某个句法规则的字符串。在很多文本编辑器里，正则表达式通常被用来检索、替换那些符合某个模式的文本。
> 许多程序设计语言都支持利用正则表达式进行字符串操作。例如，在 Perl 中就内建了一个功能强大的正则表达式引擎。正则表达式这个概念最初是由 UNIX 中的工具软件（例如`sed`和`grep`）普及开的。正则表达式通常缩写成“regex”，单数有 regexp、regex，复数有 regexps、regexes、regexen。
```
我们有这样一个文本文件，包含 `shiyanlou` 和 `shilouyan` 这两个字符串，同样一个表达式：
```
shi*
正则表达式中 `*` 表示匹配前面的子表达式（这里就是它前面一个字符）零次或多次，比如它可以匹配 `sh`，`shii`，`shish`，`shiishi` 等等，而作为通配符表示匹配通配符后面任意多个任意字符，所以它可以匹配 `shiyanlou` 和 `shilouyan` 两个字符。
```
# sed
`sed` 工具在 man 手册里面的全名为"sed - stream editor for filtering and transforming text "，意即，用于过滤和转换文本的流编辑器。
## 外参数
```
|-i|将直接修改输入文件内容，而不是打印到标准输出设备| 也就是说不加这个参数只会echo而不会去更改文件

|-r|使用扩展正则表达式，默认为标准正则表达式|

|-n|安静模式，只打印受影响的行，默认打印输入数据的全部内容| 通常跟P 特定行一块去用
 
|-e|用于在脚本中添加多个执行命令一次执行，在命令行中执行多个命令通常不需要加该参数|

|-f filename|指定执行 filename 文件中的命令|

```
### -i参数示例
![image-2024712740213.png|400](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8B%E7%9A%84%E6%AD%A3%E5%88%99sed/Linux%E4%B8%8B%E7%9A%84%E6%AD%A3%E5%88%99/image-2024712740213.png)
![image-20247125412575.png|400](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8B%E7%9A%84%E6%AD%A3%E5%88%99sed/Linux%E4%B8%8B%E7%9A%84%E6%AD%A3%E5%88%99/image-20247125412575.png)
### -n配合p行示例
`-n` 选项在 `sed` 中启用安静模式，即不自动打印每一行。结合 `p` 命令，可以只打印特定的行。
![image-2024712147165.png](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8B%E7%9A%84%E6%AD%A3%E5%88%99sed/Linux%E4%B8%8B%E7%9A%84%E6%AD%A3%E5%88%99/image-2024712147165.png)
打印包含特定模式的行，例如包含单词 `happy` 的行。
![image-202471236206.png|450](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8B%E7%9A%84%E6%AD%A3%E5%88%99sed/Linux%E4%B8%8B%E7%9A%84%E6%AD%A3%E5%88%99/image-202471236206.png)
## 内参数

|     |                       |
| --- | --------------------- |
| `s` | 行内替换                  |
| `c` | 整行替换                  |
| `i` | 插入到指定行的前面             |
| `a` | 插入到指定行的后面             |
| `p` | 打印指定行，通常与 `-n` 参数配合使用 |
| `d` | 删除指定行                 |
| g   | 【必须会的全局】              |
sed执行命令格式
```
[n1][,n2]command 
[n1][~step]command
```
其中一些命令可以加上作用范围
```
sed -i 's/sad/happy/g' test 
# g 表示全局范围 
sed -i 's/sad/happy/4' test 
# 4 表示指定行中的第四个匹配字符串
```
### -i前参数配合s/行内替换
```
将每一行的sad替换为happy
sed -i 's/sad/happy/' test
```
![image-2024712843915.png|400](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8B%E7%9A%84%E6%AD%A3%E5%88%99sed/Linux%E4%B8%8B%E7%9A%84%E6%AD%A3%E5%88%99/image-2024712843915.png)
### -i前参数配合c\整行替换【清空已有行，谨慎操作】
注意正斜杠和反斜杠
```

sed -i 'c\sad+++happy' test
```
![image-20247121332902.png|425](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8B%E7%9A%84%E6%AD%A3%E5%88%99sed/Linux%E4%B8%8B%E7%9A%84%E6%AD%A3%E5%88%99/image-20247121332902.png)
### d/删除特定行
```
删除带有happy的行
sed -i '/happy/d' test
```
![image-20247121615203.png|375](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8B%E7%9A%84%E6%AD%A3%E5%88%99sed/Linux%E4%B8%8B%E7%9A%84%E6%AD%A3%E5%88%99/image-20247121615203.png)
### i插入数据到到行前
```
sed -i '/sad/i\sad+' test
```
![image-20247121844970.png|300](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8B%E7%9A%84%E6%AD%A3%E5%88%99sed/Linux%E4%B8%8B%E7%9A%84%E6%AD%A3%E5%88%99/image-20247121844970.png)
### a插入到行后
```
sed -i '/sad/a\sad-' test
```
![image-20247122033614.png|350](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8B%E7%9A%84%E6%AD%A3%E5%88%99sed/Linux%E4%B8%8B%E7%9A%84%E6%AD%A3%E5%88%99/image-20247122033614.png)
## 进阶结合面命令
### 打印行数
```
# 打印2-5行 
nl passwd | sed -n '2,5p' 
# 打印奇数行 
nl passwd | sed -n '1~2p'
```
---
### 行内替换
```
sed -n 's/:/|/gp' passwd
```
![image-20247123116286.png|325](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8B%E7%9A%84%E6%AD%A3%E5%88%99sed/Linux%E4%B8%8B%E7%9A%84%E6%AD%A3%E5%88%99/image-20247123116286.png)
### 删除行数
```
#删除某一行
nl passwd | grep "xyblue" 
# 删除第30行 
sed -i '30d' passwd
```
![image-202471232538.png](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8B%E7%9A%84%E6%AD%A3%E5%88%99sed/Linux%E4%B8%8B%E7%9A%84%E6%AD%A3%E5%88%99/image-202471232538.png)
# grep
# awk 分割
```
awk的命令是基于pattern模式和action（动作）来完成的
pattern {action}
`awk` 处理文本的方式，是将文本分割成一些“字段”，然后再对这些字段进行处理，默认情况下，awk 以空格作为一个字段的分割符，不过这不是固定的，你可以任意指定分隔符。
awk [-F fs] [-v var=value] [-f prog-file | 'program text'] [file...]
```
它太强大了
AWK 是一种优良的文本处理工具，Linux 及 Unix 环境中现有的功能最强大的数据处理引擎之一。其名称得自于它的创始人 Alfred Aho（阿尔佛雷德·艾侯）、Peter Jay Weinberger（彼得·温伯格）和 Brian Wilson Kernighan（布莱恩·柯林汉)姓氏的首个字母 `AWK`，三位创建者已将它正式定义为“样式扫描和处理语言”。它允许你创建简短的程序，这些程
序读取输入文件、为数据排序、处理数据、对输入执行计算以及生成报表，还有无数其他的功能。最简单地说，AWK 是一种用于处理文本的编程语言工具。
在大多数 Linux 发行版上面，实际我们使用的是 gawk（GNU awk，awk 的 GNU 版本），在我们的环境中 ubuntu 上，默认提供的是 mawk，不过我们通常可以直接使用 awk 命令（awk 语言的解释器），因为系统已经为我们创建好了 awk 指向 mawk 的符号链接。
符号链接';
![image-20247125736303.png](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8B%E7%9A%84%E6%AD%A3%E5%88%99sed/Linux%E4%B8%8B%E7%9A%84%E6%AD%A3%E5%88%99/image-20247125736303.png)
## 示例1
分割的是以space和tab为分割符的
```
ps
ps |awk '{print $3}'
```
![image-20247125632620.png|400](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8B%E7%9A%84%E6%AD%A3%E5%88%99sed/Linux%E4%B8%8B%E7%9A%84%E6%AD%A3%E5%88%99/image-20247125632620.png)
## 示例2
自定义加----
![image-2024713651196.png|300](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8B%E7%9A%84%E6%AD%A3%E5%88%99sed/Linux%E4%B8%8B%E7%9A%84%E6%AD%A3%E5%88%99/image-2024713651196.png)
## 示例3
配合docker进行数据处理，如处理id的命令，批量start或者stop的
![image-20247131350956.png](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8B%E7%9A%84%E6%AD%A3%E5%88%99sed/Linux%E4%B8%8B%E7%9A%84%E6%AD%A3%E5%88%99/image-20247131350956.png)
示例4
匹配启停docker
```
sudo docker ps -a |awk '{print $1' |tail -n+2 |xargs -i {} sudo dcoekr start {}
```
![image-20247133749700.png](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8B%E7%9A%84%E6%AD%A3%E5%88%99sed/Linux%E4%B8%8B%E7%9A%84%E6%AD%A3%E5%88%99/image-20247133749700.png)