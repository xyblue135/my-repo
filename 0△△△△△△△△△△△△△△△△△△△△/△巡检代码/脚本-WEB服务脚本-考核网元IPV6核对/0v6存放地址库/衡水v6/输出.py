import os

# 获取当前目录下所有txt文件
txt_files = [file for file in os.listdir('.') if file.endswith('.txt')]

# 遍历每个txt文件并替换逗号为换行符
for file_name in txt_files:
    file_path = os.path.join('.', file_name)
    
    # 打开文件并读取内容
    with open(file_path, 'r') as file:
        content = file.read()
    
    # 替换逗号为换行符
    content = content.replace(',', '\n')
    
    # 将修改后的内容写回文件
    with open(file_path, 'w') as file:
        file.write(content)