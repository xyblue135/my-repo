import re
import pandas as pd

def parse_logs(log_file):
    with open(log_file, 'r') as file:
        data = file.read()

    blocks = data.split('-------------------------------------------------------------')
    log_entries = []
    current_ip = None

    for block in blocks:
        if not block.strip():
            continue

        lines = block.strip().split('\n')
        for line in lines:
            if re.match(r'^\d+\.\d+\.\d+\.\d+ \| CHANGED \|', line):
                current_ip = line.split(' ')[0]
            elif re.match(r'^\d{4}-\d{2}-\d{2}', line):
                log_entries.append([current_ip] + line.split('|'))

    return log_entries

def logs_to_excel(log_entries, output_file):
    # Calculate the maximum number of fields in the data
    max_fields = max(len(entry) for entry in log_entries)

    # Define columns dynamically based on the max_fields
    columns = ['IP'] + [f'Field{i}' for i in range(1, max_fields)]

    # Ensure all entries have the same number of columns by padding with empty strings
    for entry in log_entries:
        while len(entry) < max_fields:
            entry.append('')

    df = pd.DataFrame(log_entries, columns=columns)

    # Create an empty row after each IP block
    ip_blocks = df.groupby('IP')
    final_df = pd.DataFrame(columns=columns)
    for ip, block in ip_blocks:
        final_df = pd.concat([final_df, block, pd.DataFrame([[''] * len(columns)], columns=columns)], ignore_index=True)

    final_df.to_excel(output_file, index=False)

# File paths
log_file = 'logs.txt'
output_file = 'logs.xlsx'

# Parse logs and generate Excel file
log_entries = parse_logs(log_file)
logs_to_excel(log_entries, output_file)
