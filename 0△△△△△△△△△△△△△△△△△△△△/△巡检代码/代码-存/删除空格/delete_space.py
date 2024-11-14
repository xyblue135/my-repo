def remove_spaces_from_file(file_path):
    """从文件中删除所有空格"""
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    
    data_no_spaces = data.replace(' ', '')  # 删除所有空格
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(data_no_spaces)

if __name__ == "__main__":
    file_path = '2.csv'  # 替换为你的文件路径
    remove_spaces_from_file(file_path)
    print(f"已从文件 {file_path} 中删除所有空格。")
