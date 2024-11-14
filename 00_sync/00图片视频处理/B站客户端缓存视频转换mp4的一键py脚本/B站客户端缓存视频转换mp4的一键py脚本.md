环境:ffmpeg python
https://ffmpeg.org/
https://docs.python.org/
文件
![[00_sync/00图片视频处理/B站客户端缓存视频转换mp4的一键py脚本/----/bilibili.zip]]
![cd87a923610158ce4c0108cc47f7e05.png|450](00_sync/00图片视频处理/B站客户端缓存视频转换mp4的一键py脚本/B站客户端缓存视频转换mp4的一键py脚本/cd87a923610158ce4c0108cc47f7e05.png)
相关代码:
```
@echo off

REM 执行第一个 Python 脚本
python 0.py

REM 
timeout /t 2 /nobreak
REM python3 1.py

timeout /t 2 /nobreak
REM 
REM python3 2.py

timeout /t 2 /nobreak
REM 
REM python3 3.py

timeout /t 2 /nobreak
REM 
REM python3 4.py

REM 提示脚本执行完毕
echo 看所有视频文件夹
pause

```

```
import os

def rename_and_modify(directory):
    # 递归处理目录及其子目录下的所有 .m4s 文件
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.m4s'):
                file_path = os.path.join(root, filename)
                rename_m4s_file(file_path)
                remove_leading_zeros(file_path)

def rename_m4s_file(file_path):
    # 获取文件所在目录和文件名
    directory = os.path.dirname(file_path)
    base_name = os.path.basename(file_path)
    
    # 重命名文件为顺序编号
    index = 1
    new_name = f"{index}.m4s"
    new_path = os.path.join(directory, new_name)
    
    # 如果目标文件已存在，则添加序号直到找到一个不存在的文件名
    while os.path.exists(new_path):
        index += 1
        new_name = f"{index}.m4s"
        new_path = os.path.join(directory, new_name)
    
    os.rename(file_path, new_path)

def remove_leading_zeros(file_path):
    # 读取文件内容并删除开头的前9个零字符
    try:
        with open(file_path, 'rb') as f:
            content = f.read()
        
        modified_content = content[9:]  # 删除前9个字节
        
        # 将修改后的内容写回文件
        with open(file_path, 'wb') as f:
            f.write(modified_content)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

if __name__ == "__main__":
    current_directory = os.getcwd()  # 获取当前工作目录
    rename_and_modify(current_directory)

```

```
import os

def process_m4s_files(directory):
    # 遍历当前目录及其子目录下的所有文件
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(('1.m4s', '2.m4s')):
                file_path = os.path.join(root, filename)
                try:
                    # 读取文件内容
                    with open(file_path, 'r+b') as f:
                        content = f.read()
                        # 删除前9位内容（如果文件内容长度不足9位，直接清空文件）
                        f.seek(0)
                        f.truncate()
                        f.write(content[9:])
                    print(f"成功删除编码前9位：{file_path}")
                except Exception as e:
                    print(f"处理文件时出错：{file_path}")
                    print(e)

if __name__ == "__main__":
    current_directory = os.getcwd()  # 获取当前工作目录
    process_m4s_files(current_directory)

```

```
import os
import subprocess
from datetime import datetime

def rename_and_modify(directory):
    # 递归处理目录及其子目录下的所有 .m4s 文件
    for root, dirs, files in os.walk(directory):
        for dirname in dirs:
            subdir_path = os.path.join(root, dirname)
            merge_m4s_to_mp4(subdir_path)  # 对每个子目录执行合并操作

def rename_m4s_file(file_path):
    # 获取文件的创建时间
    creation_time = os.path.getctime(file_path)
    timestamp = datetime.fromtimestamp(creation_time).strftime('%Y%m%d_%H%M%S')
    
    # 获取文件所在目录和文件名
    directory = os.path.dirname(file_path)
    base_name = os.path.basename(file_path)
    
    # 构建新的文件名，包括时间戳
    new_name = f"{timestamp}_{base_name}"
    new_path = os.path.join(directory, new_name)
    
    # 如果目标文件已存在，则添加序号直到找到一个不存在的文件名
    index = 1
    while os.path.exists(new_path):
        index += 1
        new_name = f"{timestamp}_{index}_{base_name}"
        new_path = os.path.join(directory, new_name)
    
    os.rename(file_path, new_path)

def remove_leading_zeros(file_path):
    # 读取文件内容并删除开头的前9个零字符
    try:
        with open(file_path, 'rb') as f:
            content = f.read()
        
        modified_content = content[9:]  # 删除前9个字节
        
        # 将修改后的内容写回文件
        with open(file_path, 'wb') as f:
            f.write(modified_content)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

def merge_m4s_to_mp4(directory):
    # 收集所有 .m4s 文件路径
    m4s_files = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.m4s'):
                file_path = os.path.join(root, filename)
                m4s_files.append(file_path)
    
    if not m4s_files:
        print(f"No .m4s files found in {directory}")
        return
    
    # 创建输出目录 output 相对于当前工作目录
    output_directory = os.path.join(directory, 'output')
    os.makedirs(output_directory, exist_ok=True)
    
    # 获取父目录名称作为输出文件名
    parent_directory_name = os.path.basename(directory)
    output_file = os.path.join(output_directory, f"{parent_directory_name}.mp4")
    
    # 构建 ffmpeg 命令
    input_files = " ".join([f"-i \"{f}\"" for f in m4s_files])
    ffmpeg_cmd = f"ffmpeg {input_files} -codec copy \"{output_file}\""
    
    # 执行 ffmpeg 命令
    try:
        subprocess.run(ffmpeg_cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing ffmpeg command: {e}")

if __name__ == "__main__":
    current_directory = os.getcwd()  # 获取当前工作目录
    rename_and_modify(current_directory)

```

```
import os
import shutil

def copy_output_folders(directory):
    # 遍历当前目录及其子目录
    for root, dirs, files in os.walk(directory):
        for dirname in dirs:
            subdir_path = os.path.join(root, dirname)
            output_dir = os.path.join(subdir_path, 'output')
            if os.path.exists(output_dir):
                # 复制 output 文件夹中的所有文件到当前目录下的所有视频文件夹中
                copy_files_to_all_videos(output_dir)

def copy_files_to_all_videos(source_dir):
    # 创建当前目录下的所有视频文件夹，如果不存在则创建
    target_dir = os.path.join(os.getcwd(), '所有视频')
    os.makedirs(target_dir, exist_ok=True)

    # 复制 source_dir 中的所有文件到 target_dir 中
    for item in os.listdir(source_dir):
        item_path = os.path.join(source_dir, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, target_dir)
        elif os.path.isdir(item_path):
            # 如果是文件夹，递归复制其内容
            shutil.copytree(item_path, os.path.join(target_dir, item))

if __name__ == "__main__":
    current_directory = os.getcwd()  # 获取当前工作目录
    copy_output_folders(current_directory)

```

