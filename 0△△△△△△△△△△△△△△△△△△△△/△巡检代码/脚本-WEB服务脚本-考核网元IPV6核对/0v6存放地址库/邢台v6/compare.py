import os

def read_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def check_txt_files(directory):
    txt_files = [file for file in os.listdir(directory) if file.endswith('.txt')]
    num_files = len(txt_files)
    file_contents = {}

    for file_name in txt_files:
        file_path = os.path.join(directory, file_name)
        content = read_txt(file_path)
        if content in file_contents:
            file_contents[content].append(file_name)
        else:
            file_contents[content] = [file_name]

    duplicate_contents = {content: files for content, files in file_contents.items() if len(files) > 1}

    if duplicate_contents:
        print("以下文档具有相同的内容：")
        for content, files in duplicate_contents.items():
            print("内容:")
            print(content)
            print("出现在以下文件中:")
            for file in files:
                print("- " + file)
            print()
    else:
        print("所有文档的内容都是独一无二的。")

if __name__ == "__main__":
    current_directory = os.getcwd()
    print("当前文件夹路径：", current_directory)
    check_txt_files(current_directory)
