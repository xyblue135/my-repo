import os

# 清空1liucheng/input.txt的内容
file_path_1liucheng = os.path.join('1liucheng', 'input.txt')
if os.path.exists(file_path_1liucheng) and os.path.isfile(file_path_1liucheng):
    with open(file_path_1liucheng, 'w') as file:
        file.truncate()
    print(f"'{file_path_1liucheng}' 的内容已被清空。")
else:
    print(f"'{file_path_1liucheng}' 文件不存在。")

# 遍历2liucheng目录下的特定子文件夹并清空input.txt内容
parent_dir = '2liucheng'
target_folders = ['50对比', '95对比']
for root, dirs, files in os.walk(parent_dir):
    for folder in target_folders:
        if folder in dirs:
            input_txt_path = os.path.join(root, folder, 'input.txt')
            if os.path.exists(input_txt_path) and os.path.isfile(input_txt_path):
                with open(input_txt_path, 'w') as file:
                    file.truncate()
                print(f"'{input_txt_path}' 的内容已被清空。")
            else:
                print(f"'{input_txt_path}' 文件不存在。")

# 将当前目录下的FTP.txt内容复制到1liucheng/input.txt
ftp_txt_path = os.path.join(os.getcwd(), '每次需要input的FTP.txt')
if os.path.exists(ftp_txt_path) and os.path.isfile(ftp_txt_path):
    with open(ftp_txt_path, 'r') as ftp_file:
        ftp_content = ftp_file.read()
    input_txt_path_1liucheng = os.path.join('1liucheng', 'input.txt')
    with open(input_txt_path_1liucheng, 'w') as input_file:
        input_file.write(ftp_content)
    print(f"'{ftp_txt_path}' 的内容已复制到 '{input_txt_path_1liucheng}'。")
else:
    print(f"'{ftp_txt_path}' 文件不存在。")

print("所有操作已完成。")