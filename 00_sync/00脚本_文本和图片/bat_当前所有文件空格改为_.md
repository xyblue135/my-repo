非递归bat
```
@echo off
setlocal enabledelayedexpansion

:: 获取当前脚本的名字
set "scriptName=%~nx0"

:: 遍历当前目录中的所有文件
for %%f in (*.*) do (
    set "filename=%%f"
    
    :: 跳过当前正在运行的脚本
    if /i "%%f"=="%scriptName%" (
        echo Skipping script: %%f
        continue
    )

    :: 检查文件名中是否包含空格
    if not "x!filename: =!"=="x!filename!" (
        :: 替换空格为下划线
        set "newname=!filename: =_!"

        :: 重命名文件
        echo Renaming "%%f" to "!newname!"
        ren "%%f" "!newname!"
    ) else (
        echo No spaces found in: %%f
    )
)

endlocal
pause
```
递归sh
```
#!/bin/bash

# 获取当前脚本的名字
script_name=$(basename "$0")

# 定义一个函数来递归处理目录
process_directory() {
    local dir="$1"
    # 遍历目录中的所有文件
    for file in "$dir"/*; do
        # 跳过当前正在运行的脚本
        if [[ -f "$file" && "$(basename "$file")" == "$script_name" ]]; then
            echo "Skipping script: $file"
            continue
        fi
        
        # 获取文件名
        filename=$(basename "$file")
        
        # 检查文件名中是否包含空格
        if [[ "$filename" =~ [[:space:]] ]]; then
            # 替换空格为下划线
            newname="${filename// /_}"
            
            # 重命名文件
            mv "$file" "${file%/*}/$newname"
            echo "Renamed \"$file\" to \"${file%/*}/$newname\""
        else
            echo "No spaces found in: $file"
        fi
    done
    
    # 递归处理子目录
    for subdir in "$dir"/*/; do
        if [[ -d "$subdir" ]]; then
            process_directory "$subdir"
        fi
    done
}

# 开始处理当前目录
process_directory .
```