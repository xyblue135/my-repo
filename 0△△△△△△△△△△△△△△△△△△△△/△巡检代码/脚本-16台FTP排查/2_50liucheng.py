import os
import shutil
import subprocess

# 在1liucheng目录下执行python3 start.py
start_script_name = 'start.py'
try:
    subprocess.run(['python3', start_script_name], check=True, cwd='1liucheng')
    print("1liucheng/start.py 已成功执行。")
except subprocess.CalledProcessError:
    print("执行 1liucheng/start.py 时发生错误。")

# 复制1liucheng/output.txt到2liucheng/50对比/input.txt
source_output_path = os.path.join('1liucheng', 'output.txt')
target_input_path = os.path.join('2liucheng', '50对比', 'input.txt')

# 确保目标目录存在
os.makedirs(os.path.dirname(target_input_path), exist_ok=True)

try:
    shutil.copy2(source_output_path, target_input_path)
    print(f"'{source_output_path}' 的内容已复制到 '{target_input_path}'。")
except FileNotFoundError:
    print(f"'{source_output_path}' 文件不存在。")

# 在2liucheng/50对比目录下执行python3 start.py
try:
    subprocess.run(['python3', start_script_name], check=True, cwd=os.path.join('2liucheng', '50对比'))
    print("2liucheng/50对比/start.py 已成功执行。")
except subprocess.CalledProcessError:
    print("执行 2liucheng/50对比/start.py 时发生错误。")

print("所有操作已完成。")