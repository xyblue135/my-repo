import subprocess
import os

# 定义要执行的脚本列表
scripts_to_run = ['1liucheng.py', '2_95liucheng.py']

# 遍历脚本列表并逐个执行
for script in scripts_to_run:
    script_path = os.path.join(os.getcwd(), script)  # 构建完整的脚本路径
    try:
        subprocess.run(['python3', script_path], check=True)
        print(f"'{script}' 已成功执行。")
    except subprocess.CalledProcessError as e:
        print(f"执行 '{script}' 时发生错误: {e}")

print("所有脚本执行完毕。")