import pandas as pd
import os

def create_txt_files_from_excel(excel_file):
    df = pd.read_excel(excel_file, usecols='A', header=None)  # 读取 Excel 文件的 A 列数据
    column_data = df.iloc[:, 0]  # 提取 A 列的数据

    for folder_name in column_data:
        file_path = str(folder_name) + ".txt"  # 使用文件名加上 ".txt" 后缀
        with open(file_path, "w") as file:
            file.write("")  # 写入一个空字符串，创建空的 .txt 文件
        print(f"已创建文件: {file_path}")

# 请将下面一行的 'your_excel_file.xlsx' 替换为你的实际 Excel 文件路径
create_txt_files_from_excel('./123.xlsx')
