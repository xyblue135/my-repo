def find_max_traffic_per_ip(input_file, output_file):
    # 用于存储每个IP的最大流量
    max_traffic_dict = {}

    # 读取文件并处理数据
    with open(input_file, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            ip = parts[0]
            # 假定从第二个元素开始都是流量数据
            flows = [float(flow) for flow in parts[1:] if flow]
            if flows:  # 确保有流量数据才处理
                max_traffic = max(flows) if flows else 0
                # 更新或添加到字典中
                if ip in max_traffic_dict:
                    max_traffic_dict[ip] = max(max_traffic_dict[ip], max_traffic)
                else:
                    max_traffic_dict[ip] = max_traffic

    # 将结果写入新的TXT文件
    with open(output_file, 'w') as output:
        for ip, max_traffic in max_traffic_dict.items():
            output.write(f"{ip},{max_traffic}\n")

    print(f"每个IP的最大流量已保存至：{output_file}")

# 输入和输出文件路径
input_file_path = 'input.txt'
output_file_path = 'output.txt'

# 调用函数
find_max_traffic_per_ip(input_file_path, output_file_path)