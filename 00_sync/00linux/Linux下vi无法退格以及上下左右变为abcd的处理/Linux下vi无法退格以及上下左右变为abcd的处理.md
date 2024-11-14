这个与兼容模式有关
```
xyblue@xyblue-Default-string:~/test$ cat ~/.vimrc
set nocp

修改

xyblue@xyblue-Default-string:~/test$ echo 'set backspace=indent,eol,start' >> ~/.vimrc
xyblue@xyblue-Default-string:~/test$ cat ~/.vimrc
set nocp
set backspace=indent,eol,start
```
# 临时设置
在 `vi` 或 `vim` 中打开文件，然后输入以下命令：
```
冒号那里
set backspace=indent,eol,start
```
这将在当前会话中启用 Backspace 功能。
#  永久设置
```
echo 'set backspace=indent,eol,start' >> ~/.vimrc
```

# 补充说明
- **兼容模式**：在兼容模式下，`vim` 的行为尽可能模仿经典的 `vi`，禁用了许多 `vim` 的增强功能。
- **非兼容模式**：启用了 `vim` 的所有增强功能，包括对方向键的正确处理。
`set nocp` 的作用
`set nocp` 命令用于禁用兼容模式，启用 `vim` 的所有增强功能，包括：
1. **正确处理方向键**：在非兼容模式下，方向键可以正常工作，不会显示 `A`、`B`、`C` 和 `D` 字符。
2. **启用更多功能**：非兼容模式启用了 `vim` 的许多其他功能，如语法高亮、智能缩进和扩展的命令集等。
为什么使用 `>>` 而不是 `>`？
- **`>>`**：追加模式。将新的内容追加到文件末尾，不会删除文件中已有的内容。
- **`>`**：覆盖模式。会覆盖文件中已有的内容，可能会导致 `.vimrc` 文件中的其他设置丢失。
通过添加 `set nocp` 并重新加载 `.vimrc` 文件，`vim` 将以非兼容模式运行，从而解决方向键显示 `A`、`B`、`C` 和 `D` 字符的问题。