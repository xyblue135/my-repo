
# if语句
# 基础语句
```
#!/bin/bash

# 提示用户输入猜测的数字
echo "请输入一个数字："
read guess

# 设置要猜的数字
number=100

# 比较输入的数字和设定的数字
if [[ $guess -eq $number ]]; then
    echo "√"
else
    echo "×"
fi
```
## 多分支条件判断格式
可以在if 和 else之间加入一个elif
```
#!/bin/bash

# 提示用户输入猜测的数字
echo "请输入一个数字："
read guess

# 设置要猜的数字
number=100

# 比较输入的数字和设定的数字
if [[ $guess -eq $number ]]; then
    echo "√"
elif [[ $guess -lt $number ]]; then
    echo "猜小了"
else
    echo "猜大了且错误"
fi
```
![image-202410294123674.png|358](00_sync/00linux/For%20if-else%20%E7%AD%89%E5%8F%98%E9%87%8F%E4%BD%BF%E7%94%A8/For%20if-else%20%E7%AD%89%E5%8F%98%E9%87%8F%E4%BD%BF%E7%94%A8/image-202410294123674.png)
# For循环
**for循环更适合已知次数或遍历序列的情况**
适合遍历列表数组
`${number[@]}` 引用数组的所有元素,需要注意要用花括号包裹
```
#!/bin/bash

numbers=(1 2 3 4 5)

for num in "${numbers[@]}"; do
    echo "$num"
done
```
这个我觉得就不如用while了
```
#!/bin/bash

# 使用 for 循环从 1 到 5 输出数字
for ((i=1; i<=5; i++)); do
    echo "$i"
done
```
# While循环
**while循环更适合不确定循环次数的情况**
while适合条件成立的时候一直判断
```
#!/bin/bash

# 初始化计数器
count=0
max_count=5

# 使用while循环
while [[ $count -lt $max_count ]]; do
    echo $count
    count=$((count + 1))
done
```
## 防止死循环
done前面的time=0重新清零变量防止死循环
```
#!/bin/bash
输入当前时间
time=$1
clock=60
while [[ $time -eq $clock ]]; do
        echo "时间正确"
        time=0
done
```
# continue和break
这两个都是必须放在while或者for循环中使用的
加入continue后，被循环的时候如果判断成立，就不会有任何输出，也是跳过
```
#!/bin/bash

numbers=(1 2 3 4 5 6 7 8 9)

for num in "${numbers[@]}"; do
    if [[ "$num" -lt 5 ]]; then
        # 当数字小于5 时，跳过这次循环迭代
        continue
    fi
    echo "$num"
done
```
上述输出结果为5 6 7 8 9
```
#!/bin/bash

numbers=(1 2 3 4 5 6 7 8 9)

for num in "${numbers[@]}"; do
    if [[ "$num" -ge 5 ]]; then
        # 当找到第一个大于等于 5 的数字时，跳出循环
        echo "找到了第一个大于等于 5 的数字: $num"
        break
    else
	    echo "$num"
    fi
done
```
上述结果为
1
2
3
4
找到了第一个大于等于 5 的数字: 5
# 逻辑运算符连接
与&& 或者|| 非!
```
#!/bin/bash

read number

guess=123

if [[ $number -lt $guess || $number -eq $guess ]]; then

    echo "zheng que"

else

    echo "cuo wu"

fi
```

# 普通变量不等于环境变量
```
name=xyblue
echo "$name"
```
这样的话会返回xyblue出来，但是如果sh脚本里面引入$name是根本没有用的，因为这就是个普通变量而不是环境变量
```
export name=xyblue

在脚本中编辑echo"$name"
```
这样的话脚本就可以正常输出了，需要注意，这个也仅再当前shell中生效，跟临时代理差不多，退出就失效了

# 整体处理
用$符号和小括号的形式！！！！！！！！！！
```
#!/bin/bash
bian1=` echo 1+1 |bc`
bian2=$(echo 1+1 |bc)
echo $bian1 
echo $bian2
```
![image-202410291324102.png|298](00_sync/00linux/For%20if-else%20等变量使用/For%20if-else%20等变量使用/image-202410291324102.png)
# $变量 $0-9
示例1 计算BMI 
体重KG除以身高米的平方 也就是用bc-l保存20位浮点 $0是当前用的shell类型 $1-9是滴几个什么的 需要注意只能到第九个参数
```
root@xyblue# echo 85/1.86^2 |bc -l
24.56931437160365360157
```
## read变量
这种适用于执行脚本然后输入
```
#!/bin/bash

echo "请输入你的体重（千克）:"
read weight
echo "请输入你的身高（米）:"
read high

bmi=$(echo "$weight/$high^2" |bc -l)
echo "你的体重指数为$bmi"
```
## 顺序变量
这种适用于传递参数 执行的时候bash start.sh 123[参数1] 456[参数2] 789[参数3]
```
#!/bin/bash
echo "请输入你的身高和体重"
weight=$1
high=$2

bmi=$(echo "$1/$2^2" |bc -l)
echo "你的体重指数为$bmi"
```
# $@ 传递被传递的参数  [常见的参数]
```

```

# 附件
## 条件测试字符
### 浮点比较操作符
```
#!/bin/bash
# 整数比较操作符
# -eq: 等于
[[ $a -eq $b ]]
# -ne: 不等于
[[ $a -ne $b ]]
# -lt: 小于
[[ $a -lt $b ]]
# -le: 小于等于
[[ $a -le $b ]]
# -gt: 大于
[[ $a -gt $b ]]
# -ge: 大于等于
[[ $a -ge $b ]]
```
### 字符串比较操作符
```

# ==: 等于
[[ "$a" == "$b" ]]
# !=: 不等于
[[ "$a" != "$b" ]]
# <: 字符串小于（按字典顺序）
[[ "$a" < "$b" ]]
# >: 字符串大于（按字典顺序）
[[ "$a" > "$b" ]]
```
### 文件测试操作符
```

# -f: 判断是否为普通文件
[[ -f "$file" ]]
# -d: 判断是否为目录
[[ -d "$file" ]]
# -e: 判断文件或目录是否存在
[[ -e "$file" ]]
# -r: 判断是否有读权限
[[ -r "$file" ]]
# -w: 判断是否有写权限
[[ -w "$file" ]]
# -x: 判断是否有执行权限
[[ -x "$file" ]]
```

```
# 逻辑操作符
# -a: 逻辑与（AND）
[[ -f "$file" -a -r "$file" ]]
# -o: 逻辑或（OR）
[[ -f "$file" -o -d "$file" ]]

# 位置参数操作符
# -z: 字符串为空（长度为零）
[[ -z "$str" ]]
# -n: 字符串非空（长度不为零）
[[ -n "$str" ]]

# 模式匹配操作符（仅 [[ ... ]] 支持）
# *: 匹配任意数量的任意字符
[[ "$str" == "prefix*" ]]
# ?: 匹配单个任意字符
[[ "$str" == "pre?ix" ]]
# []: 字符类
[[ "$str" == "[abc]" ]]

# 正则表达式匹配操作符（仅 [[ ... ]] 支持）
# =~: 正则表达式匹配
[[ "$str" =~ ^prefix ]]
```
## 逻辑运算符
1. **逻辑与 (`&&`)**：
    - 用于连接两个表达式，只有当两个表达式都为真时，整个表达式才为真。
```
[[ $a -gt 0 && $b -lt 10 ]]
```
2. **逻辑或 (`||`)**：
```
[[ $a -gt 0 || $b -lt 10 ]]
```
3. **逻辑非 (`!`)**：
```
[[ ! $a -eq 0 ]]
```
# 计算扩展
```
递增
((i++)) 和 i=i+1 和 i=$((i + 1)) 是一样的
```