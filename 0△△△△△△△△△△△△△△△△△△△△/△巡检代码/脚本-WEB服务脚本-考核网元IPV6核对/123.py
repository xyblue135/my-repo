import os
import re
from flask import Flask, request, render_template_string
from ipaddress import ip_network, ip_address

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def search_ipv6():
    result_text = ""
    if request.method == 'POST':
        target_ipv6_list = request.form['ipv6_addresses'].strip().split('\n')
        root_dir = os.path.join(os.getcwd(), '12345678')
        matches = find_ipv6_in_files(target_ipv6_list, root_dir)
        for i, (ipv6, match_list) in enumerate(matches.items(), start=1):
            if match_list:
                result_text += f"<p>第{i}号：IPv6地址: {ipv6}</p>"
                for segment, filename in match_list:
                    result_text += f"<p>  匹配到的段: {segment}, 文件名: {filename}</p>"
            else:
                result_text += f"<p>IPv6地址: {ipv6} 没有找到匹配的段。</p>"

    return render_template_string('''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <title>河北v6匹配网元web</title>
          </head>
          <body>
            <div class="container">
              <h1>IPv6 查找工具</h1>
              <form method="post">
                <div class="form-group">
                  <label for="ipv6_addresses"></label>
                  <textarea class="form-control" id="ipv6_addresses" name="ipv6_addresses" rows="10"></textarea>
                </div>
                <button type="submit" class="btn btn-primary">检索</button>
              </form>
              <div class="mt-4">
                {{ result_text|safe }}
              </div>
            </div>
          </body>
        </html>
    ''', result_text=result_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=25560)
