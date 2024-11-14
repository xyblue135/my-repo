管道是一种通信机制，通常用于进程间的通信（也可通过 socket 进行网络通信），它表现出来的形式就是将前面每一个进程的输出（stdout）直接作为下一个进程的输入（stdin）。
管道又分为匿名管道和具名管道,我们在使用一些过滤程序时经常会用到的就是匿名管道，在命令行中由 `|` 分隔符表示，`|` 在前面的内容中我们已经多次使用到了。具名管道简单的说就是有名字的管道，通常只会在源程序中用到具名管道。下面我们就将通过一些常用的可以使用管道的过滤程序来帮助你熟练管道的使用。
#  less 行形式读取
内容太多，用行来看
```
ls -al /etc
ls -al /etc | less
```
![image-2024764917856.png|350](2需要放入网站的笔记/Linux下的管道/Linux下的管道/image-2024764917856.png)
# cut 分隔
正常情况下的cat
![image-202477211106.png](2需要放入网站的笔记/Linux下的管道/Linux下的管道/image-202477211106.png)
cut`命令支持以下主要选项：
- `-d` 或 `--delimiter`：指定字段分隔符，默认为制表符。例如，`-d ':'` 将使用冒号作为分隔符。
- `-f` 或 `--fields`：选择指定的字段或字段范围。例如，`-f 1,3` 将输出第一和第三个字段。
使用cut来进行过滤后的数据
```
cut /etc/passwd -d : -f 1
	cut /etc/passwd '-d' : -f '1' #`'-d'` 和 `': '` 被shell解释为两个独立的参数，这并不是`cut`命令期望的。`cut`命令期望`-d`后面紧跟一个字符作为分隔符，而不是将其视为两个独立的参数。但是需要注意，如果不是:了而是|，就还是加上引号吧，不然会被错误解释
```
![image-2024772852789.png](2需要放入网站的笔记/Linux下的管道/Linux下的管道/image-2024772852789.png)
值得注意的是，如果要分隔的符号有管道符这种的话，十分建议加上引号
![image-202477256584.png](2需要放入网站的笔记/Linux下的管道/Linux下的管道/image-202477256584.png)即使在简单的情况下，使用引号也是一个好习惯。这样可以确保无论参数内容如何变化，命令都能按照预期的方式工作。
如何打印字符
- `-b` 或 `--bytes`：以字节为单位进行切割。例如，`-b 1-10` 将输出每个输入行的前10个字节。
 字节是计算机中最小的数据单位之一，通常由8位(bit)组成。在二进制系统中，一个字节可以表示从0到255（即2的8次方减1）的数值。字节是存储和传输数据的基本单位，无论是数字、字母、符号还是其他任何形式的信息，都可以被编码成一系列的字节。
- `-c` 或 `--characters`：以字符为单位进行切割。例如，`-c 1-10` 将输出每个输入行的前10个字符。
映射关系，字符是指我们在书写、打印或显示中看到的任何符号，如字母、数字、标点符号等。在计算机中，字符需要被编码成数字形式才能被处理。最常用的字符编码标准之一是ASCII（美国信息交换标准代码），它定义了128个字符与7位或8位二进制数的映射关系，足以覆盖英文及常用符号。
```
#  打印前五个字符（包含第五个）

cut /etc/passwd -c -5 

# 打印前五个之后的字符（包含第五个）

cut /etc/passwd -c 5- 

# 打印第第五个字符

cut /etc/passwd -c 5 

# 打印第二-第五个字符

cut /etc/passwd -c 2-5
```
字符和字节的关系：
在ASCII编码中，每个字符正好对应一个字节，因为ASCII字符集只需要最多128个值，所以一个字节（8位）足够表示全部ASCII字符。但是，随着全球化的需要，出现了许多非英语语言，如中文、日语、韩文等，这些语言的字符数量远远超过128个，需要使用更多位来表示，这就引入了多字节编码的概念。
例如，UTF-8（Unicode Transformation Format）编码是一种变长编码方案，它可以使用1到4个字节来表示一个字符。对于ASCII字符，UTF-8编码与ASCII完全兼容，每个字符仍占一个字节；而对于非英文字符，UTF-8会使用2、3或4个连续的字节来表示一个字符。
因此，当我们说"字节组成了字符"时，指的是在多字节编码体系中，一个字符可能由一个或多个连续的字节构成。在处理文本数据时，理解这一点非常重要，因为不当的处理可能会导致字符被截断或解析错误，从而产生乱码。
#  grep 过滤
不看123里面的123456
```
cat 123 |grep -v 123456
```
配合管道
```
ls -al /etc | grep "config"
```
-r 递归查找
-n 匹配行数
-I 忽略二进制，基本没啥含义，还慢
```
grep [命令选项]... 用于匹配的表达式 [文件]...
grep -rnI "xyblue" ~
grep -rnI "xyblue"
```

查看环境变量中以 "xyblue" 结尾的字符串
```
export | grep ".*xyblue$"
```
查看环境变量包含 "xyblue"
```
export | grep "xyblue"
```
![image-2024795739226.png|235](2需要放入网站的笔记/Linux下的管道/Linux下的管道/image-2024795739226.png)
 ## | grep 和直接grep的区别
![image-202479175452.png|300](2需要放入网站的笔记/Linux下的管道/Linux下的管道/image-202479175452.png)
# wc 行数 字符/节
```
行数 wc -l /etc/passwd 
单词数 wc -w /etc/passwd 
字节数 wc -c /etc/passwd 
字符数 wc -m /etc/passwd 
最长行字节数 wc -L /etc/passw
```
配合管道 |
```
ls -dl /etc/*/ | wc -l
ls -dl /etc/*  | wc -l
ls -dl /etc/   | wc -l

ls -dl /etc/*/ | wc -l`   ：统计 `/etc` 目录中子目录的数量。
ls -dl /etc/*  | wc -l    ：统计 `/etc` 目录中所有文件和子目录的数量。
ls -dl /etc/   | wc -l    ：只统计 `/etc` 目录本身（即 1 个）。
```
![image-2024792354299.png|300](2需要放入网站的笔记/Linux下的管道/Linux下的管道/image-2024792354299.png)
# sort排序
顺序排序'
逆向排序
`-r`默认sort是升序的，现在要求降序,N
```
顺序排序
cat /etc/passwd | sort
反转排序
cat /etc/passwd | sort -r
```
特定字段排序
`-t':'`：指定 `:` 作为字段分隔符。
`-k 1`：指定按照第一个字段进行排序。 `sort` 会跳过这些空格并识别第一个非空白字符后的部分作为第一列。
`-n`：默认情况下是按照字典进行排序的，-n可以指定进行数值排序。对需要比较有用
```
cat /etc/passwd | sort -t':' -k 3
```
# uniq去重
!!!!!uniq只能删除重复的行 所以前面一般都要加好sort默认字典排序 或者sort-r 顺序反转 sort-n 数值排序
| uniq 去重的
![image-20247967674.png|156](2需要放入网站的笔记/Linux下的管道/Linux下的管道/image-20247967674.png)
进阶用法
```
history | cut -c 8- | cut -d ' ' -f 1 | sort | uniq
history | cut -c 8- | cut -d ' ' -f 1 | sort -u
输出重复过的行（重复的只输出一个）及重复次数 
history | cut -c 8- | cut -d ' ' -f 1 | sort | uniq -dc 
cat chong |sort | uniq -dc
输出所有重复的行
history | cut -c 8- | cut -d ' ' -f 1 | sort | uniq -D
cat chong |sort | uniq -D
```

![image-20247985734.png|227](2需要放入网站的笔记/Linux下的管道/Linux下的管道/image-20247985734.png)
![image-202479755547.png|150](2需要放入网站的笔记/Linux下的管道/Linux下的管道/image-202479755547.png)
![image-202479431881.png|225](2需要放入网站的笔记/Linux下的管道/Linux下的管道/image-202479431881.png)
去除前八
![image-20247955306.png|275](2需要放入网站的笔记/Linux下的管道/Linux下的管道/image-20247955306.png)
# tr 删除替换
tr 命令可以用来删除一段文本信息中的某些文字。或者将其进行转换。
```
tr [option]...SET1 [SET2]
-d 删除和 set1 匹配的字符，注意不是全词匹配也不是按字符顺序匹配
ca  文件 tr -d 123456
-s 去除 set1 指定的在输入文本中连续并重复的字符
cat 文件 tr -s 123456
```
![image-2024791913466.png|200](2需要放入网站的笔记/Linux下的管道/Linux下的管道/image-2024791913466.png)
详细
删除 "hello shiyanlou" 中所有的'a'，'b'，'b' (区分大小写 )
```
echo 'hello shiyanlou' | tr -d 'olh' 
```
将"hello" 中的ll，去重为一个l
```
echo 'hello' | tr -s 'l' 
```
将输入文本，全部转换为大写或小写输出 
```
echo 123.txt |tr '[:lower:]' '[:upper:]' 
echo 'input some text here' | tr '[:lower:]' '[:upper:]' 
```
上面的'[:lower:]' '[:upper:]'你也可以简单的写作'[a-z]' '[A-Z]'，当然反过来将大写变小写也是可以的
![image-2024792530981.png|400](2需要放入网站的笔记/Linux下的管道/Linux下的管道/image-2024792530981.png)
# col 【tab 空格交互】
col 命令可以将`Tab`换成对等数量的空格键，或反转这个操作。
```
cat -A 显示更为详细  ^I为Tab  空格不会显示，需要sed -e 's/ /[SPACE]/g' 1.txt
-x 将Tab转换为空格
-h 将空格转换为Tab   同时也是默认
```
示例：
```
cat tab.txt
cat tab.txt |col -x  |cat -A
```
![image-20247103711733.png](2需要放入网站的笔记/Linux下的管道/Linux下的管道/image-20247103711733.png)
转换为这个空格貌似不太理想，还是配合sed或者exp的会好一些
![image-20247112224577.png](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8B%E7%9A%84%E7%AE%A1%E9%81%93/Linux%E4%B8%8B%E7%9A%84%E7%AE%A1%E9%81%93/image-20247112224577.png)
```
sed -e 's/ /[SPACE]/g' kongge.txt
```
![image-20247112326908.png](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8B%E7%9A%84%E7%AE%A1%E9%81%93/Linux%E4%B8%8B%E7%9A%84%E7%AE%A1%E9%81%93/image-20247112326908.png)
# join  数据库常用，合并两个文件相同{行！！}    取交集的意思
|      |                            |
| ---- | -------------------------- |
| `-t` | 指定分隔符，默认为空格                |
| `-i` | 忽略大小写的差异                   |
| `-1` | 指明第一个文件要用哪个字段来对比，默认对比第一个字段 |
| `-2` | 指明第二个文件要用哪个字段来对比，默认对比第一个字段 |
```
-i 参数
join -i file1 file2
不区分大小写
```
![image-20247114640557.png](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8B%E7%9A%84%E7%AE%A1%E9%81%93/Linux%E4%B8%8B%E7%9A%84%E7%AE%A1%E9%81%93/image-20247114640557.png)
空格和tab是不受影响的
![image-20247114934780.png|475](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8B%E7%9A%84%E7%AE%A1%E9%81%93/Linux%E4%B8%8B%E7%9A%84%E7%AE%A1%E9%81%93/image-20247114934780.png)
一图看懂
![image-2024711252152.png](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8B%E7%9A%84%E7%AE%A1%E9%81%93/Linux%E4%B8%8B%E7%9A%84%E7%AE%A1%E9%81%93/image-2024711252152.png)
常用用法
```
xyblue@xyblue sudo cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
xyblue@xyblue sudo  cat /etc/shadow
root:!:19908:0:99999:7:::
示例
sudo join -t':' /etc/passwd /etc/shadow
root:x:0:0:root:/root:/bin/bash:!:19908:0:99999:7:::::
```
# paste 【join的简单合并】
|      |                  |
| ---- | ---------------- |
| `-d` | 指定合并的分隔符，默认为 Tab |
| `-s` | 不合并到一行，每个文件为一行   |
这个分割符是输出来的，不是在文档里面的，需要注意，分隔符只能一个字符，要是要多个的话要配合sed
![image-20247114332940.png](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8B%E7%9A%84%E7%AE%A1%E9%81%93/Linux%E4%B8%8B%E7%9A%84%E7%AE%A1%E9%81%93/image-20247114332940.png)
![image-2024711745167.png](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8B%E7%9A%84%E7%AE%A1%E9%81%93/Linux%E4%B8%8B%E7%9A%84%E7%AE%A1%E9%81%93/image-2024711745167.png)
需要注意上面那个图片，如果加-s参数的话，而且1和2都是有多行的情况下
![image-2024711481862.png|425](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8B%E7%9A%84%E7%AE%A1%E9%81%93/Linux%E4%B8%8B%E7%9A%84%E7%AE%A1%E9%81%93/image-2024711481862.png)

# xarges分割数列表
> xargs 是一条 UNIX 和类 UNIX 操作系统的常用命令。它的作用是将参数列表转换成小块分段传递给其他命令，以避免参数列表过长的问题。
这个命令在有些时候十分有用，特别是当用来处理产生大量输出结果的命令如 `find`，`locate` 和 `grep` 的结果，详细用法请参看 man 文档。
```
cut -d: -f1 < /etc/passwd | sort | xargs echo
```
上面这个命令用于将 `/etc/passwd` 文件按 `:` 分割取第一个字段排序后，使用 `echo` 命令生成一个列表。
![image-20247124913235.png](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8B%E7%9A%84%E7%AE%A1%E9%81%93/Linux%E4%B8%8B%E7%9A%84%E7%AE%A1%E9%81%93/image-20247124913235.png)
也可以批量停止一些任务或者启动脚本.
```
docker ps -a |awk '{print $1}' |tail -n+2 |xargs docker stop
```

需要注意
带版本号的可能会影响判断，因为这个:号实在是太
![image-20247133436827.png](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8B%E7%9A%84%E7%AE%A1%E9%81%93/Linux%E4%B8%8B%E7%9A%84%E7%AE%A1%E9%81%93/image-20247133436827.png)
docker一键启停
![image-20247133734471.png](2%E9%9C%80%E8%A6%81%E6%94%BE%E5%85%A5%E7%BD%91%E7%AB%99%E7%9A%84%E7%AC%94%E8%AE%B0/Linux%E4%B8%8B%E7%9A%84%E7%AE%A1%E9%81%93/Linux%E4%B8%8B%E7%9A%84%E7%AE%A1%E9%81%93/image-20247133734471.png)
