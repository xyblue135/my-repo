# 引入
在我们日常使用csv文件的时候,经常出现编码问题,就比如我需要格式化我jellyfin视频库中的视频名字来能够正确搜刮封面，而我又迫切需要excel的ctrl+e自动识别填充功能，这是我不用其它能正确打开utf无bom编辑器的重点所在。
![image-202411101448483.png](00_sync/00%E8%84%9A%E6%9C%AC_%E6%96%87%E6%9C%AC%E5%92%8C%E5%9B%BE%E7%89%87/VBA%E5%AE%8F%E5%9B%BA%E5%AE%9Aexcel%E6%89%93%E5%BC%80csv%E6%96%87%E4%BB%B6%E4%B8%BAutf-8/VBA%E5%AE%8F%E5%9B%BA%E5%AE%9Aexcel%E6%89%93%E5%BC%80csv%E6%96%87%E4%BB%B6%E4%B8%BAutf-8/image-202411101448483.png)
但如果使用其他编辑器或者转编码工具还是不方便，也为我需要的是快速填充这个功能,下面这些转换都要点一次才可以使，非常麻烦在配合批量改名字的时候用。我们可以用宏的方式，但是抱歉，我觉得还是不太方便。
![image-202411101551884.png](00_sync/00%E8%84%9A%E6%9C%AC_%E6%96%87%E6%9C%AC%E5%92%8C%E5%9B%BE%E7%89%87/VBA%E5%AE%8F%E5%9B%BA%E5%AE%9Aexcel%E6%89%93%E5%BC%80csv%E6%96%87%E4%BB%B6%E4%B8%BAutf-8/VBA%E5%AE%8F%E5%9B%BA%E5%AE%9Aexcel%E6%89%93%E5%BC%80csv%E6%96%87%E4%BB%B6%E4%B8%BAutf-8/image-202411101551884.png)
![image-202411101830769.png|175](00_sync/00%E8%84%9A%E6%9C%AC_%E6%96%87%E6%9C%AC%E5%92%8C%E5%9B%BE%E7%89%87/VBA%E5%AE%8F%E5%9B%BA%E5%AE%9Aexcel%E6%89%93%E5%BC%80csv%E6%96%87%E4%BB%B6%E4%B8%BAutf-8/VBA%E5%AE%8F%E5%9B%BA%E5%AE%9Aexcel%E6%89%93%E5%BC%80csv%E6%96%87%E4%BB%B6%E4%B8%BAutf-8/image-202411101830769.png)
## 解决方法
在导出的时候就使用utf-8-bom编码
用py的话是
写入文件时：encoding='utf-8-sig' 会自动在文件开头添加BOM。
读取文件时：encoding='utf-8-sig' 会自动识别并移除BOM。
# 批量换名代码
```
import os
import csv
import shutil

def list_files_to_csv(directory, csv_file):
    # 清空csv文件
    with open(csv_file, mode='w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        # 写入表头
        writer.writerow(['Original Filename', 'New Filename'])
        # 遍历指定目录下的所有文件（不包括子目录）
        for filename in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, filename)):
                # 写入原始文件名到第一列
                writer.writerow([filename, ''])

def rename_files_from_csv(directory, csv_file):
    # 从csv文件读取新的文件名并重命名
    with open(csv_file, mode='r', newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            original_filename = row['Original Filename']
            new_filename = row['New Filename'].strip()
            if new_filename:  # 如果新文件名非空
                original_path = os.path.join(directory, original_filename)
                new_path = os.path.join(directory, new_filename)
                # 重命名文件
                shutil.move(original_path, new_path)

if __name__ == "__main__":
    directory = input("请输入本地计算机的地址: ")
    csv_file = '1.csv'

    # 第一步：列出文件到CSV
    list_files_to_csv(directory, csv_file)
    print(f"文件列表已保存到 {csv_file}，请编辑此文件以提供新的文件名。")
    
    # 等待用户完成编辑
    input("当你准备好继续时，请在此处输入'yes': ")
    
    # 第二步：重命名文件
    rename_files_from_csv(directory, csv_file)
    print("文件重命名已完成！")
```

```
import subprocess
import re

def get_excel_pids():
    # 使用tasklist命令查找所有EXCEL.EXE进程
    result = subprocess.run(['tasklist', '/FI', 'IMAGENAME eq EXCEL.EXE'], stdout=subprocess.PIPE, text=True)
    
    # 解析输出以提取PID
    pids = []
    for line in result.stdout.splitlines():
        match = re.search(r'\s+(\d+)\s+Console', line)
        if match:
            pid = int(match.group(1))
            pids.append(pid)
    return pids

def kill_process(pids):
    # 遍历PID列表，终止每个进程
    for pid in pids:
        try:
            subprocess.run(['taskkill', '/PID', str(pid), '/F'], check=True)
            print(f"成功终止PID为{pid}的进程。")
        except subprocess.CalledProcessError as e:
            print(f"无法终止PID为{pid}的进程: {e}")

def main():
    # 获取所有Excel进程的PID
    excel_pids = get_excel_pids()
    if excel_pids:
        print("找到以下Excel进程:")
        for pid in excel_pids:
            print(f"PID: {pid}")
        
        # 终止Excel进程
        kill_process(excel_pids)
    else:
        print("没有找到Excel进程。")

if __name__ == "__main__":
    main()
```
代码中已有自动打开excel，ctrl+s保存excel后，自动kill excel进程
![image-202411103111665.png](00_sync/00%E8%84%9A%E6%9C%AC_%E6%96%87%E6%9C%AC%E5%92%8C%E5%9B%BE%E7%89%87/VBA%E5%AE%8F%E5%9B%BA%E5%AE%9Aexcel%E6%89%93%E5%BC%80csv%E6%96%87%E4%BB%B6%E4%B8%BAutf-8/VBA%E5%AE%8F%E5%9B%BA%E5%AE%9Aexcel%E6%89%93%E5%BC%80csv%E6%96%87%E4%BB%B6%E4%B8%BAutf-8/image-202411103111665.png)


# BOM概念
这个概念挺重要的，尤其是在win系统上编辑文件的时候。就比如我们用excel和wps打开csv文件时候总是乱码和不兼容，这个时候我们用bom可以完美规避这个问题，也不需要写繁琐的脚本和其它东西了。
## UTF-8 BOM:
字节顺序标记（BOM）是Unicode标准中定义的一种特殊的标记，用于标识文件是以何种字节序存储的Unicode文本。对于UTF-8编码来说，BOM并不是必需的，因为UTF-8本身并不依赖于字节序。但是，有些软件会在UTF-8文件的开头添加BOM，以便明确表示这是一个UTF-8编码的文件。UTF-8 BOM由三个特定的字节组成：EF BB BF。如果一个UTF-8文件以这三个字节开始，那么它就包含了BOM。
## 无BOM:
无BOM的UTF-8文件就是指没有这些起始字节的UTF-8编码文件。
在很多情况下，UTF-8文件默认是不带BOM的，因为BOM在UTF-8中主要起到标识的作用，而UTF-8编码本身已经足够清晰地表明了字符集。不带BOM的UTF-8文件在大多数现代软件中都能被正确识别为UTF-8编码，而且不会在文件开头引入额外的不可见字符，这对于某些场景是非常重要的，比如在网络传输中或者作为编程语言的源代码文件。
## 具体用哪个
使用BOM：在某些环境中，比如Windows上的某些旧版软件可能需要BOM才能正确识别UTF-8编码。此外，如果你确定文件只会在支持BOM的环境中使用，那么可以考虑使用BOM。
不使用BOM：对于Web开发、编程源代码、数据交换格式（如JSON、XML）等，通常推荐不使用BOM，因为它可能导致解析问题。例如，在JSON中，开头的BOM会使得整个字符串无效；在HTML中，BOM可能会被当作内容的一部分显示出来。