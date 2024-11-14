```
sudo nano /etc/apt/sources.list
#去找51行
deb http://archive.ubuntu.com/ubuntu focal main restricted
deb-src http://archive.ubuntu.com/ubuntu focal main restricted
# 确保每一行以 `deb` 或 `deb-src` 开头，并且正确地包含 URL 和存储库信息。如果有拼写错误、缺少部分或有额外的字符，请进行修正。
```
sudo apt update