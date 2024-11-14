import re

def extract_md5_values(input_file, output_file):
    """从输入文件中提取MD5数值并写入输出文件"""
    md5_pattern = re.compile(r'^[a-fA-F0-9]{32}$')
    md5_values = []

    try:
        with open(input_file, 'r') as file:
            for line in file:
                line = line.strip()
                if md5_pattern.match(line):
                    md5_values.append(line)

        with open(output_file, 'w') as file:
            for md5 in md5_values:
                file.write(md5 + '\n')

        print(f"已成功提取 {len(md5_values)} 个MD5数值到 {output_file}")

    except FileNotFoundError:
        print(f"文件 {input_file} 不存在。")
    except Exception as e:
        print(f"处理文件时出错: {e}")

if __name__ == "__main__":
    input_file = 'input.txt'
    output_file = 'output.txt'
    extract_md5_values(input_file, output_file)
