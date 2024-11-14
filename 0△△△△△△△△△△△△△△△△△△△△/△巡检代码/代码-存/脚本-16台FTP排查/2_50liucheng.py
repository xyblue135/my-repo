import os
import shutil
import subprocess

def clear_directory(directory):
    """清空指定目录"""
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'清空目录 {directory} 时出错: {e}')

def is_directory_empty(directory):
    """检查目录是否为空"""
    return len(os.listdir(directory)) == 0

# 使用统一的路径分隔符构建路径
start_script_name = 'start.py'
liucheng1_directory = 'F:\\0desktop\\0桌面图标映射\\00考核网元事宜\\脚本-16台FTP排查\\1liucheng'
liucheng2_directory = 'F:\\0desktop\\0桌面图标映射\\00考核网元事宜\\脚本-16台FTP排查\\2liucheng\\50对比'

# 检查要执行的脚本文件是否存在
start_script_path1 = os.path.join(liucheng1_directory, start_script_name)
start_script_path2 = os.path.join(liucheng2_directory, start_script_name)

if not os.path.exists(start_script_path1):
    print(f"文件 '{start_script_path1}' 不存在。")
    exit()

if not os.path.exists(start_script_path2):
    print(f"文件 '{start_script_path2}' 不存在。")
    exit()

try:
    subprocess.run(['python3', start_script_name], check=True, cwd=liucheng1_directory)
    print("1liucheng/start.py 已成功执行。")
except subprocess.CalledProcessError:
    print("执行 1liucheng/start.py 时发生错误。")

# 复制1liucheng/output.txt到2liucheng/50对比/input.txt
source_output_path = os.path.join(liucheng1_directory, 'output.txt')
target_input_path = os.path.join(liucheng2_directory, '50对比', 'input.txt')

# 确保目标目录存在
os.makedirs(os.path.dirname(target_input_path), exist_ok=True)

# 清空目标目录
clear_directory(os.path.dirname(target_input_path))

# 检查目标目录是否为空
if not is_directory_empty(os.path.dirname(target_input_path)):
    print(f"目标目录 '{os.path.dirname(target_input_path)}' 未成功清空。")
else:
    try:
        shutil.copy2(source_output_path, target_input_path)
        print(f"'{source_output_path}' 的内容已复制到 '{target_input_path}'。")
    except FileNotFoundError:
        print(f"'{source_output_path}' 文件不存在。")

    # 在2liucheng/50对比目录下执行python3 start.py
    try:
        subprocess.run(['python3', start_script_name], check=True, cwd=os.path.join(liucheng2_directory, '50对比'))
        print("2liucheng/50对比/start.py 已成功执行。")
    except subprocess.CalledProcessError:
        print("执行 2liucheng/50对比/start.py 时发生错误。")

# 再次清空目标目录
clear_directory(os.path.dirname(target_input_path))

# 最后检查目标目录是否为空
if is_directory_empty(os.path.dirname(target_input_path)):
    print(f"目标目录 '{os.path.dirname(target_input_path)}' 已成功清空。")
else:
    print(f"目标目录 '{os.path.dirname(target_input_path)}' 未能清空。")

print("所有操作已完成。")
