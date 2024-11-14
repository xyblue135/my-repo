import re

def parse_ping_output(logfile):
    with open(logfile, 'r') as file:
        lines = file.readlines()

    successful_pings = []
    unsuccessful_pings = []

    host_pattern = re.compile(r'ping (?:-c \d+ )?([\d\w\.\:]+)')
    stats_pattern = re.compile(r'(\d+) packet\(s\) transmitted, (\d+) packet\(s\) received, (\d+(\.\d+)?)% packet loss')
    round_trip_pattern = re.compile(r'round-trip min/avg/max/std-dev = (.+)')

    current_host = None
    current_ip = None

    for i, line in enumerate(lines):
        host_match = host_pattern.search(line)
        if host_match:
            current_host = host_match.group(1)
            ip_match = re.search(r'(\d+\.\d+\.\d+\.\d+|\S+:\S+)', line)
            current_ip = ip_match.group(1) if ip_match else current_host

        stats_match = stats_pattern.search(line)
        if stats_match:
            packets_transmitted = int(stats_match.group(1))
            packets_received = int(stats_match.group(2))
            packet_loss = float(stats_match.group(3))

            if packets_received == 0:
                unsuccessful_pings.append((current_host, current_ip))
            else:
                round_trip_times = ""
                if i + 1 < len(lines):
                    round_trip_match = round_trip_pattern.search(lines[i + 1])
                    if round_trip_match:
                        round_trip_times = round_trip_match.group(1)

                successful_pings.append({
                    "host": current_host,
                    "ip": current_ip,
                    "packets_transmitted": packets_transmitted,
                    "packets_received": packets_received,
                    "packet_loss": packet_loss,
                    "round_trip_times": round_trip_times
                })

    return successful_pings, unsuccessful_pings

def write_success_results(successful_pings, success_file):
    with open(success_file, 'w') as file:
        file.write("Successful Pings:\n")
        for ping in successful_pings:
            file.write(f"Host: {ping['host']}\n")
            file.write(f" (IP: {ping['ip']})\n")
            file.write(f"Packets: {ping['packets_transmitted']} transmitted, {ping['packets_received']} received, {ping['packet_loss']}% packet loss\n")
            file.write(f"Round-trip min/avg/max/std-dev = {ping['round_trip_times']}\n")
            file.write("-" * 80 + "\n")

def write_failed_results(unsuccessful_pings, failed_file):
    with open(failed_file, 'w') as file:
        file.write("Unsuccessful Pings:\n")
        for host, ip in unsuccessful_pings:
            file.write(f"Host: {host}\n")
            file.write(f" (IP: {ip})\n")
            file.write("-" * 80 + "\n")

def main():
    logfile = 'print.txt'  # 输入日志文件
    success_file = 'success.txt'  # 输出成功ping结果的文件
    failed_file = 'failed.txt'  # 输出失败ping结果的文件

    successful_pings, unsuccessful_pings = parse_ping_output(logfile)
    write_success_results(successful_pings, success_file)
    write_failed_results(unsuccessful_pings, failed_file)

if __name__ == "__main__":
    main()

