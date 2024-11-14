import pandas as pd

def find_duplicate_cells(excel_file, output_file):
    # 加载Excel文件
    try:
        df = pd.read_excel(excel_file, header=None)
    except Exception as e:
        print(f"Error reading the file: {e}")
        return
    
    # 初始化一个字典来存储重复值及其位置
    duplicates = {}
    
    # 遍历数据框的每一个单元格
    for idx, row in df.iterrows():
        for col, value in enumerate(row):
            # 忽略空值
            if pd.isnull(value):
                continue
            
            # 构建单元格位置标识，如"A1", "B2"
            cell_position = f"{chr(ord('A')+col)}{idx+1}"
            
            # 检查值是否已存在于字典中，即是否重复
            if str(value) in duplicates:
                duplicates[str(value)].append(cell_position)
            else:
                duplicates[str(value)] = [cell_position]
    
    # 将重复值及其位置信息写入文本文件
    with open(output_file, 'w') as f:
        for value, positions in duplicates.items():
            if len(positions) > 1:  # 只写入重复的项
                f.write(f"Value '{value}' is duplicated at positions: {', '.join(positions)}\n")
    
    print(f"Duplicate cell analysis completed. Results saved to '{output_file}'.")

# 指定待检测的Excel文件路径和输出结果的文本文件路径
excel_file_path = '123456.xls'
output_text_path = 'duplicate_cells_report.txt'
find_duplicate_cells(excel_file_path, output_text_path)