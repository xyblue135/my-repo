import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import chardet
import os

# 函数：检测文件编码
def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        result = chardet.detect(file.read())
    return result['encoding']

# 路径到CSV文件
csv_file_path = 'start.csv'

# 检测CSV文件的编码
file_encoding = detect_encoding(csv_file_path)
print(f"Detected encoding: {file_encoding}")

# 使用检测到的编码读取CSV文件
try:
    df = pd.read_csv(csv_file_path, encoding=file_encoding)
except Exception as e:
    print(f"Error occurred while reading the CSV file: {e}")
    exit(1)

# 检查'IP'列是否存在
if 'IP' not in df.columns:
    print("Column 'IP' not found in the DataFrame")
    exit(1)

# 提取IP地址和丢包数据
ip_column = 'IP'
ip_addresses = df[ip_column]
packet_loss_data = df.iloc[:, 1:]  # 假设丢包数据从第二列开始

# 转换时间戳为字符串形式，以便在图表中显示
time_labels = packet_loss_data.columns

# 设置中文字体，确保在图表中显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 创建主文件夹 'IP'
main_folder = 'IP'
os.makedirs(main_folder, exist_ok=True)

# 创建图表并调整大小
for i in range(len(ip_addresses)):
    plt.figure(figsize=(12, 8))  # 调整图表的大小
    
    plt.plot(time_labels, packet_loss_data.iloc[i], label=ip_addresses[i])
    last_value = packet_loss_data.iloc[i, -1]
    plt.text(time_labels[-1], last_value, ip_addresses[i], fontsize=8, ha='left', va='center')
    
    plt.xlabel('时间')
    plt.ylabel('丢包量')
    plt.title(f'{ip_addresses[i]} 丢包量变化')
    
    # 仅每 10 个时间点显示一个标签
    plt.xticks(range(0, len(time_labels), 10), time_labels[::10], rotation=45)
    
    plt.grid(True)
    plt.tight_layout()
    
    # 保存为高清图片
    try:
        filename = os.path.join(main_folder, f'{ip_addresses[i]}_packet_loss.png')
        plt.savefig(filename, dpi=300)
        print(f"Plot saved successfully as '{filename}'.")
    except Exception as e:
        print(f"Error occurred while saving the figure: {e}")
    
    # 关闭当前图表以节省内存
    plt.close()
