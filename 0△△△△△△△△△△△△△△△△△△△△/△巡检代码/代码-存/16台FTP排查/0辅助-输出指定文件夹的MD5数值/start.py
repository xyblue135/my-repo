import os
import hashlib

def calculate_md5(file_path):
    """计算文件的MD5值"""
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception as e:
        return f"无法计算文件 {file_path} 的MD5值: {e}"

def get_files_in_folder(folder_path):
    """递归获取文件夹中的所有文件"""
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def main():
    current_script = os.path.abspath(__file__)
    current_folder = os.path.dirname(current_script)
    
    target_folder_name = "MD5存放"
    target_folder_path = os.path.join(current_folder, target_folder_name)
    output_file_path = os.path.join(current_folder, "md5输出.txt")

    if not os.path.isdir(target_folder_path):
        print(f"子文件夹 '{target_folder_name}' 不存在于当前目录下。")
        with open(output_file_path, 'w') as output_file:
            output_file.write(f"子文件夹 '{target_folder_name}' 不存在于当前目录下。\n")
        return

    with open(output_file_path, 'w') as output_file:
        files = get_files_in_folder(target_folder_path)
        for file in files:
            md5_value = calculate_md5(file)
            output_file.write(md5_value + "\n")

if __name__ == "__main__":
    main()
