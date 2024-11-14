import re
from datetime import datetime

# 获取当前时间
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 读取文件内容
with open('print.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 初始化输出内容
success_lines = [f"{current_time}\n"]
failed_lines = [f"{current_time}\n"]

# 定义匹配模式
up_pattern = re.compile(r'\w+/0/\d+\s+UP')
down_pattern = re.compile(r'\w+/0/\d+\s+DOWN')
spawn_pattern = re.compile(r'^spawn ssh.*')
ji_fang_pattern = re.compile(r'ji_fang')

# 遍历文件内容
for i, line in enumerate(lines):
    if up_pattern.search(line) or ji_fang_pattern.search(line):
        if spawn_pattern.search(line):
            success_lines.append('-' * 90 + '\n')
        success_lines.append(f"Line {i + 1}: {line}")
    if down_pattern.search(line) or ji_fang_pattern.search(line):
        if spawn_pattern.search(line):
            failed_lines.append('-' * 90 + '\n')
        failed_lines.append(f"Line {i + 1}: {line}")

# 添加结束时间
success_lines.append(f"{current_time}\n")
failed_lines.append(f"{current_time}\n")

# 将结果写入文件
with open('success.txt', 'w', encoding='utf-8') as success_file:
    success_file.writelines(success_lines)

with open('failed.txt', 'w', encoding='utf-8') as failed_file:
    failed_file.writelines(failed_lines)

print("过滤完成，结果已保存到 success.txt 和 failed.txt 文件中。")

