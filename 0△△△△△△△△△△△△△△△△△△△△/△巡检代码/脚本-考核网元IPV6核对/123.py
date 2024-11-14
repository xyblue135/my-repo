import os
import re
import tkinter as tk
from tkinter import scrolledtext
from ipaddress import ip_network, ip_address

# 定义匹配IPv6地址段的正则表达式
ipv6_pattern = re.compile(r'(?P<ipv6_addr>[0-9a-fA-F:]+/\d+)')

def find_ipv6_in_files(target_ipv6_list, root_dir):
    matched_segments = {}
    for ipv6 in target_ipv6_list:
        matched_segments[ipv6] = []

    # 遍历指定目录中的所有文件
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.txt'):
                filepath = os.path.join(dirpath, filename)
                with open(filepath, 'r') as file:
                    content = file.read()
                    matches = ipv6_pattern.findall(content)
                    for match in matches:
                        for target_ipv6 in target_ipv6_list:
                            if is_ipv6_in_subnet(target_ipv6, match):
                                matched_segments[target_ipv6].append((match, filename))

    return matched_segments

def is_ipv6_in_subnet(ipv6, subnet):
    network = ip_network(subnet, strict=False)
    address = ip_address(ipv6)
    
    return address in network

def search_ipv6():
    target_ipv6_list = ipv6_entry.get("1.0", tk.END).strip().split('\n')
    root_dir = os.path.join(os.getcwd(), '12345678')
    matches = find_ipv6_in_files(target_ipv6_list, root_dir)
    result_text.delete(1.0, tk.END)
    for i, (ipv6, match_list) in enumerate(matches.items(), start=1):
        if match_list:
            result_text.insert(tk.END, f"第{i}号：IPv6地址: {ipv6}\n")
            for segment, filename in match_list:
                result_text.insert(tk.END, f"  匹配到的段: {segment}, 文件名: {filename}\n")
        else:
            result_text.insert(tk.END, f"IPv6地址: {ipv6} 没有找到匹配的段。\n")

# 创建主窗口
root = tk.Tk()
root.title("IPv6 查找工具")

# IPv6输入框
tk.Label(root, text="输入多个IPv6地址，每行一个:").grid(row=0, column=0, padx=10, pady=5)
ipv6_entry = scrolledtext.ScrolledText(root, width=80, height=10)
ipv6_entry.grid(row=1, column=0, padx=10, pady=5)

# 搜索按钮
search_button = tk.Button(root, text="搜索", command=search_ipv6)
search_button.grid(row=2, column=0, pady=10)

# 结果显示框
result_text = scrolledtext.ScrolledText(root, width=80, height=20)
result_text.grid(row=3, column=0, padx=10, pady=10)

# 运行主循环
root.mainloop()
