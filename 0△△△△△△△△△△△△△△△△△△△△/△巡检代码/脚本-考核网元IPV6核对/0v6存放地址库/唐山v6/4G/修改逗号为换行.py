import os

# 获取当前目录下的所有文件
files = os.listdir()

# 遍历每个文件
for file_name in files:
    if file_name.endswith('.txt'):  # 仅处理文本文件
        # 读取文档内容
        with open(file_name, 'r') as file:
            content = file.read()

        # 替换逗号为换行符
        content = content.replace(',', '\n')

        # 将修改后的内容写入原文档
        with open(file_name, 'w') as file:
            file.write(content)