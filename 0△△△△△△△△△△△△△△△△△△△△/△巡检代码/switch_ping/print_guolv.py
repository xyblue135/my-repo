import re

def parse_ping_output(logfile):
    with open(logfile, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    successful_pings = []
    unsuccessful_pings = []
    special_lines = []

    host_pattern = re.compile(r'ping (?:-c \d+ )?([\d\w\.\:]+)')
    stats_pattern = re.compile(r'(\d+) packet\(s\) transmitted, (\d+) packet\(s\) received, (\d+(\.\d+)?)% packet loss')
    round_trip_pattern = re.compile(r'round-trip min/avg/max/std-dev = (.+)')

    current_host = None
    current_ip = None
    current_line_number = None

    for i, line in enumerate(lines):
        line_number = i + 1  # 行号从1开始

        # Check for special lines containing '==============='
        if '===============' in line:
            special_lines.append((line_number, line))

        host_match = host_pattern.search(line)
        if host_match:
            current_host = host_match.group(1)
            ip_match = re.search(r'(\d+\.\d+\.\d+\.\d+|\S+:\S+)', line)
            current_ip = ip_match.group(1) if ip_match else current_host
            current_line_number = line_number

        stats_match = stats_pattern.search(line)
        if stats_match:
            packets_transmitted = int(stats_match.group(1))
            packets_received = int(stats_match.group(2))
            packet_loss = float(stats_match.group(3))

            if packets_received == 0:
                unsuccessful_pings.append((current_line_number, current_host, current_ip))
            else:
                round_trip_times = ""
                if i + 1 < len(lines):
                    round_trip_match = round_trip_pattern.search(lines[i + 1])
                    if round_trip_match:
                        round_trip_times = round_trip_match.group(1)

                successful_pings.append({
                    "line_number": current_line_number,
                    "host": current_host,
                    "ip": current_ip,
                    "packets_transmitted": packets_transmitted,
                    "packets_received": packets_received,
                    "packet_loss": packet_loss,
                    "round_trip_times": round_trip_times
                })

    return successful_pings, unsuccessful_pings, special_lines

def write_results(successful_pings, unsuccessful_pings, special_lines, success_file, failed_file):
    all_results = []

    # Add special lines
    for line_number, line in special_lines:
        all_results.append((line_number, f"Special Line: {line}"))

    # Add successful pings
    for ping in successful_pings:
        result = (ping["line_number"], f"Line: {ping['line_number']}\n"
                                       f"Host: {ping['host']} (IP: {ping['ip']})\n"
                                       f"Packets: {ping['packets_transmitted']} transmitted, {ping['packets_received']} received, {ping['packet_loss']}% packet loss\n"
                                       f"Round-trip min/avg/max/std-dev = {ping['round_trip_times']}\n"
                                       + "-" * 80 + "\n")
        all_results.append(result)

    # Add unsuccessful pings
    for line_number, host, ip in unsuccessful_pings:
        result = (line_number, f"Line: {line_number}\n"
                               f"Host: {host} (IP: {ip})\n"
                               + "-" * 80 + "\n")
        all_results.append(result)

    # Sort all results by line number
    all_results.sort(key=lambda x: x[0])

    # Write to success and failed files
    with open(success_file, 'w', encoding='utf-8') as success, open(failed_file, 'w', encoding='utf-8') as failed:
        for line_number, result in all_results:
            if "Special Line" in result:
                success.write(result)
                failed.write(result)
            elif "received, 0.0% packet loss" in result:
                success.write(result)
            else:
                failed.write(result)

def main():
    logfile = 'print.txt'  # 输入日志文件
    success_file = '000success.txt'  # 输出成功ping结果的文件
    failed_file = '000failed.txt'  # 输出失败ping结果的文件

    successful_pings, unsuccessful_pings, special_lines = parse_ping_output(logfile)
    write_results(successful_pings, unsuccessful_pings, special_lines, success_file, failed_file)

if __name__ == "__main__":
    main()

