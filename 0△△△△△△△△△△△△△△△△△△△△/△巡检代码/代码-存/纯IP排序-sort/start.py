def read_and_process_file(file_path):
    """读取文件，删除空格并排序IP和流量"""
    ip_traffic = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file if line.strip()]
    
    print("Read lines:", lines)  # 调试信息
    
    # 处理文件内容，删除空格并组织成字典
    i = 0
    while i < len(lines):
        ip = lines[i]
        if (i + 1) < len(lines):
            traffic = lines[i + 1]
            if traffic.isdigit():
                ip_traffic[ip] = int(traffic)
                i += 2
            else:
                i += 1
        else:
            i += 1

    print("IP Traffic Dict:", ip_traffic)  # 调试信息
    
    # 对IP地址进行排序
    sorted_ip_traffic = dict(sorted(ip_traffic.items()))
    
    return sorted_ip_traffic

def write_sorted_data(file_path, sorted_data):
    """将排序后的数据写回文件"""
    with open(file_path, 'w', encoding='utf-8') as file:
        for ip, traffic in sorted_data.items():
            file.write(f"{ip} {traffic}\n")
            print(f"Writing: {ip} {traffic}")  # 调试信息

if __name__ == "__main__":
    input_file = 'input.txt'  # 输入文件路径
    output_file = 'sorted_output.txt'  # 输出文件路径
    
    sorted_data = read_and_process_file(input_file)
    write_sorted_data(output_file, sorted_data)
    
    print(f"数据处理完成，已保存至 {output_file}")
