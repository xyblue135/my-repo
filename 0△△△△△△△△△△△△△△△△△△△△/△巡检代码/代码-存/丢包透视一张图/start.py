import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import chardet

# 函数：检测文件编码
def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        result = chardet.detect(file.read())
    return result['encoding']

# 路径到CSV文件
csv_file_path = 'input.csv'

# 检测CSV文件的编码
file_encoding = detect_encoding(csv_file_path)
print(f"Detected encoding: {file_encoding}")

# 使用检测到的编码读取CSV文件
try:
    df = pd.read_csv(csv_file_path, encoding='gbk')
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

# 设置中文字体，确保在图表中显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 创建图表并调整大小
plt.figure(figsize=(12, 40))  # 调整图表的大小

# 使用颜色映射
colors = cm.tab10.colors

# 绘制数据
for i in range(len(ip_addresses)):
    plt.plot(packet_loss_data.columns, packet_loss_data.iloc[i], color=colors[i % len(colors)], label=ip_addresses[i])
    last_value = packet_loss_data.iloc[i, -1]
    plt.text(packet_loss_data.columns[-1], last_value, ip_addresses[i], fontsize=8, ha='left', va='center')

plt.xlabel('时间')
plt.ylabel('丢包率')
plt.title('IP地址 丢包率变化')
plt.xticks(rotation=45)

plt.grid(True)
plt.tight_layout()

# 保存为高清图片
try:
    plt.savefig('ip_packet_loss.png', dpi=300)
    print("Plot saved successfully as 'ip_packet_loss.png'.")
except Exception as e:
    print(f"Error occurred while saving the figure: {e}")

# 显示图表
plt.show()
