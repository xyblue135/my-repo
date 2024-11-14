众所周知，压缩的命令是比较好记得，tar -xzvf 压缩名 压缩文件
但是解压的话，有
```
> tar xvf file.tar [.tar]
> tar xzvf file.tar.gz  [.tar.gz 或 .tgz（gzip 压缩）]
> tar xJvf archive.tar.xz
> tar xjvf file.tar.bz2[.tar.bz2（bzip2 压缩）]
> gunzip file.gz&&gzip -d file.gz[.gz（单独的 gzip 压缩文件）：]
> bunzip2 file.bz2&&bzip2 -d file.bz2[.bz2（单独的 bzip2 压缩文件）：]
> unxz file.xz&&xz -d file.xz[.xz（单独的 xz 压缩文件）：]
> unzip file.zip
> unrar x file.rar
> 7z x file.7z
```
等等等等
所以用一个脚本来配合解压是比较好的
```
#!/bin/bash

# 获取文件名（传入参数）
file=$1

# 获取文件后缀
extension="${file##*.}"

# 处理复合压缩格式优先级（如 tar.xz）
if [[ $file == *.tar.xz ]]; then
  echo "tar xJvf $file  # .tar.xz (xz 压缩的 tar)"
  tar xJvf "$file"
elif [[ $file == *.tar.gz ]]; then
  echo "tar xzvf $file  # .tar.gz 或 .tgz (gzip 压缩)"
  tar xzvf "$file"
elif [[ $file == *.tar.bz2 ]]; then
  echo "tar xjvf $file  # .tar.bz2 (bzip2 压缩)"
  tar xjvf "$file"
elif [[ $file == *.tar ]]; then
  echo "tar xvf $file  # .tar"
  tar xvf "$file"
# 处理单一压缩格式（不带 tar）
elif [[ $extension == "gz" ]]; then
  echo "gunzip $file  # .gz (gzip 压缩)"
  gunzip "$file"
elif [[ $extension == "bz2" ]]; then
  echo "bunzip2 $file  # .bz2 (bzip2 压缩)"
  bunzip2 "$file"
elif [[ $extension == "xz" ]]; then
  echo "unxz $file  # .xz (xz 压缩)"
  unxz "$file"
elif [[ $extension == "zip" ]]; then
  echo "unzip $file  # .zip"
  unzip "$file"
elif [[ $extension == "rar" ]]; then
  echo "unrar x $file  # .rar"
  unrar x "$file"
elif [[ $extension == "7z" ]]; then
  echo "7z x $file  # .7z"
  7z x "$file"
else
  echo "Unsupported file extension: .$extension"
fi

```
并且我们配合变量来进行使用，注意，这里必须改PATH群而不是单独的，必须export alias不能sh
```
export PATH=$PATH:/home/0000/code/sh
```
which jieya
which jieya.sh
![image-20241165433681.png](00_sync/00linux/%E5%9C%A8Linux%E6%91%86%E8%84%B1%E7%B9%81%E7%90%90%E7%9A%84%E8%A7%A3%E5%8E%8B%E5%91%BD%E4%BB%A4/%E5%9C%A8Linux%E6%91%86%E8%84%B1%E7%B9%81%E7%90%90%E7%9A%84%E8%A7%A3%E5%8E%8B%E5%91%BD%E4%BB%A4/image-20241165433681.png)