def yuanshi_md5_md5(input_file, yuanshi_md5_file, output_file):
    """将input_file中的MD5值与yuanshi_md5_file中的MD5值进行比对，并将不匹配的MD5值写入output_file"""
    
    # 读取yuanshi_md5_file中的MD5值到一个集合
    with open(yuanshi_md5_file, 'r') as file:
        yuanshi_md5_md5_set = set(line.strip().upper() for line in file if line.strip())
    
    non_matching_md5_values = []

    # 读取input_file中的MD5值，并检查它们是否不在yuanshi_md5_md5_set中
    with open(input_file, 'r') as file:
        for line in file:
            md5 = line.strip().upper()
            if md5 not in yuanshi_md5_md5_set:
                non_matching_md5_values.append(md5)
    
    # 将不匹配的MD5值写入output_file
    with open(output_file, 'w') as file:
        for md5 in non_matching_md5_values:
            file.write(md5 + '\n')

    print(f"未匹配到 {len(non_matching_md5_values)} 个MD5值，并已写入 {output_file}")

if __name__ == "__main__":
    input_file = 'input.txt'
    yuanshi_md5_file = 'yuanshi_md5.txt'
    output_file = '对比结果.txt'
    yuanshi_md5_md5(input_file, yuanshi_md5_file, output_file)
