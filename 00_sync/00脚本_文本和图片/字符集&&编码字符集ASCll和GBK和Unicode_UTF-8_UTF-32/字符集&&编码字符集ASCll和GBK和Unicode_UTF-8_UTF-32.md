# ASCll字符集
ASCll(American Standard Code for Information Interchange)：美国信息交换标准代码，包括了英文、符号等。
ASCll是用一个字节来存储数据的8bit
![image-202312195821138.png](00_sync/00脚本_文本和图片/字符集&&编码字符集ASCll和GBK和Unicode_UTF-8_UTF-32/字符集&&编码字符集ASCll和GBK和Unicode_UTF-8_UTF-32/image-202312195821138.png)
# GBK字符集
GBK(汉字内码扩展标准,国标)
汉字编码字符集,共2万多个字符,GBK中一个中文字符编码是两个字节形式的存储.
GBK是兼容了ASCll字符集的.
## FAQ
### `我a你`解码的时候应该怎么解?
1. GBK规定第一位为1才可以
2. ![[1需要放入网站的笔记/z已完成/z字符集ASCll和GBK和Unicode_UTF-8_UTF-32 1/字符集/Pasted image 20231219020151.png]]
3. 可以看到ASCll字符集都是0开头的,第127位(最后一位)是01111111
4. ASCll字符的11111111不是字符集,最高位是被用来表示控制信息的，而不是字符!
### GBK字符集一个字符占用2Byte,8bit
也就是说,最高可以容纳2^15(去除规定第一位为1),所以共有32768个字符可以使用.2w是合理的.
![image-2023121999635.png](00_sync/00脚本_文本和图片/字符集&&编码字符集ASCll和GBK和Unicode_UTF-8_UTF-32/字符集&&编码字符集ASCll和GBK和Unicode_UTF-8_UTF-32/image-2023121999635.png)
## 小记
GBK已经快被GB18030-2022所取代了?
# Unicode字符集
国际组织规定的,可以容纳世界所有文字,符号的字符集.
## UTF-32
这家伙4个字节表示一个字符,这能装的也太多了吧!!!!
但是这也太奢侈了,好多空间都没用到!!!!,通信效率变低了.
## UTF-8
可变长度编码方案,共分为4个长度取:1个字节,2个字节,3个字节,4个字节.
兼容ASCll,占用1个字节
不能说兼容GBK,是一种改的,因为是占用3个字节.汉字的话.
```
a我m       #观看下面编码表示
```
![image-202312191931710.png](00_sync/00脚本_文本和图片/字符集&&编码字符集ASCll和GBK和Unicode_UTF-8_UTF-32/字符集&&编码字符集ASCll和GBK和Unicode_UTF-8_UTF-32/image-202312191931710.png)
![image-20231219295816.png](00_sync/00脚本_文本和图片/字符集&&编码字符集ASCll和GBK和Unicode_UTF-8_UTF-32/字符集&&编码字符集ASCll和GBK和Unicode_UTF-8_UTF-32/image-20231219295816.png)
#### BOM
这个概念挺重要的，尤其是在win系统上编辑文件的时候。就比如我们用excel和wps打开csv文件时候总是乱码和不兼容，这个时候我们用bom可以完美规避这个问题，也不需要写繁琐的脚本和其它东西了。
##### UTF-8 BOM:
字节顺序标记（BOM）是Unicode标准中定义的一种特殊的标记，用于标识文件是以何种字节序存储的Unicode文本。对于UTF-8编码来说，BOM并不是必需的，因为UTF-8本身并不依赖于字节序。但是，有些软件会在UTF-8文件的开头添加BOM，以便明确表示这是一个UTF-8编码的文件。UTF-8 BOM由三个特定的字节组成：EF BB BF。如果一个UTF-8文件以这三个字节开始，那么它就包含了BOM。
##### 无BOM:
无BOM的UTF-8文件就是指没有这些起始字节的UTF-8编码文件。
在很多情况下，UTF-8文件默认是不带BOM的，因为BOM在UTF-8中主要起到标识的作用，而UTF-8编码本身已经足够清晰地表明了字符集。不带BOM的UTF-8文件在大多数现代软件中都能被正确识别为UTF-8编码，而且不会在文件开头引入额外的不可见字符，这对于某些场景是非常重要的，比如在网络传输中或者作为编程语言的源代码文件。
##### 具体用哪个
使用BOM：在某些环境中，比如Windows上的某些旧版软件可能需要BOM才能正确识别UTF-8编码。此外，如果你确定文件只会在支持BOM的环境中使用，那么可以考虑使用BOM。
不使用BOM：对于Web开发、编程源代码、数据交换格式（如JSON、XML）等，通常推荐不使用BOM，因为它可能导致解析问题。例如，在JSON中，开头的BOM会使得整个字符串无效；在HTML中，BOM可能会被当作内容的一部分显示出来。
## 编码格式强制前缀
![image-202312192254331.png](00_sync/00脚本_文本和图片/字符集&&编码字符集ASCll和GBK和Unicode_UTF-8_UTF-32/字符集&&编码字符集ASCll和GBK和Unicode_UTF-8_UTF-32/image-202312192254331.png)
所以我的编码为`1110 0110` `10 001000` `10  010001`
# 总结
![image-202312193432225.png](00_sync/00脚本_文本和图片/字符集&&编码字符集ASCll和GBK和Unicode_UTF-8_UTF-32/字符集&&编码字符集ASCll和GBK和Unicode_UTF-8_UTF-32/image-202312193432225.png)
# 注意
我们在编码和解码的时候
## 使用GBK编码后转为UTF-8()
![image-202312193742289.png](00_sync/00脚本_文本和图片/字符集&&编码字符集ASCll和GBK和Unicode_UTF-8_UTF-32/字符集&&编码字符集ASCll和GBK和Unicode_UTF-8_UTF-32/image-202312193742289.png)
# 编码解码不一致
![image-202312194018335.png](00_sync/00脚本_文本和图片/字符集&&编码字符集ASCll和GBK和Unicode_UTF-8_UTF-32/字符集&&编码字符集ASCll和GBK和Unicode_UTF-8_UTF-32/image-202312194018335.png)
可以看到解码出现了问题,我们用`chcp`查看一下我们的cmd的解码是什么,可以看到936为GBK编码的.
![image-202312194145368.png](00_sync/00脚本_文本和图片/字符集&&编码字符集ASCll和GBK和Unicode_UTF-8_UTF-32/字符集&&编码字符集ASCll和GBK和Unicode_UTF-8_UTF-32/image-202312194145368.png)
![image-202312194541629.png](00_sync/00脚本_文本和图片/字符集&&编码字符集ASCll和GBK和Unicode_UTF-8_UTF-32/字符集&&编码字符集ASCll和GBK和Unicode_UTF-8_UTF-32/image-202312194541629.png)

![image-20231219476813.png](00_sync/00脚本_文本和图片/字符集&&编码字符集ASCll和GBK和Unicode_UTF-8_UTF-32/字符集&&编码字符集ASCll和GBK和Unicode_UTF-8_UTF-32/image-20231219476813.png)
![image-202312194756783.png](00_sync/00脚本_文本和图片/字符集&&编码字符集ASCll和GBK和Unicode_UTF-8_UTF-32/字符集&&编码字符集ASCll和GBK和Unicode_UTF-8_UTF-32/image-202312194756783.png)
![image-202312194812741.png](00_sync/00脚本_文本和图片/字符集&&编码字符集ASCll和GBK和Unicode_UTF-8_UTF-32/字符集&&编码字符集ASCll和GBK和Unicode_UTF-8_UTF-32/image-202312194812741.png)
![image-202312194838786.png](00_sync/00脚本_文本和图片/字符集&&编码字符集ASCll和GBK和Unicode_UTF-8_UTF-32/字符集&&编码字符集ASCll和GBK和Unicode_UTF-8_UTF-32/image-202312194838786.png)

# 成功
![image-202312195135512.png](00_sync/00脚本_文本和图片/字符集&&编码字符集ASCll和GBK和Unicode_UTF-8_UTF-32/字符集&&编码字符集ASCll和GBK和Unicode_UTF-8_UTF-32/image-202312195135512.png)