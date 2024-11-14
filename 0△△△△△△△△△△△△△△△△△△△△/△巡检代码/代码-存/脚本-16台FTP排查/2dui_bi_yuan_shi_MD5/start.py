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
                else:
                    print(f"过滤掉的不符合MD5格式的信息: {line}")

        with open(output_file, 'w') as file:
            for md5 in md5_values:
                file.write(md5 + '\n')

        print(f"已成功提取 {len(md5_values)} 个MD5数值到 {output_file}")

    except FileNotFoundError:
        print(f"文件 {input_file} 不存在。")
    except Exception as e:
        print(f"处理文件时出错: {e}")

def compare_files(output_file, reference_file, result_file):
    """比较两个文件并生成验证结果文件"""
    try:
        with open(output_file, 'r') as file:
            output_lines = [line.strip() for line in file if line.strip()]

        with open(reference_file, 'r') as file:
            reference_lines = set(line.strip() for line in file if line.strip())

        with open(result_file, 'w') as file:
            for line in output_lines:
                if line in reference_lines:
                    file.write(f"{line} 存在\n")
                else:
                    file.write(f"{line} 不存在\n")

        print(f"已成功生成验证结果文件 {result_file}")

    except FileNotFoundError as e:
        print(f"文件不存在: {e.filename}")
    except Exception as e:
        print(f"处理文件时出错: {e}")

if __name__ == "__main__":
    input_file = 'shu_ju_chu_liinput.txt'
    output_file = 'shu_ju_chu_output.txt'
    reference_file = 'wu_shan_yuanshi_50md5.txt'
    result_file = 'yanzheng.txt'
    
    # 提取MD5数值
    extract_md5_values(input_file, output_file)
    
    # 对比文件内容并生成验证结果
    compare_files(output_file, reference_file, result_file)
