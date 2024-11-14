# 镜像分层
可以看到下图在下载redis的时候出现了一个a2abf6c4d29d:Already exists说明这一层(添加安装包,依赖,配置等)镜像在nginx或者在mysql存在,故可以省去下载.
![image-2024254526103.png](3可以放入网站的笔记/Linux上dockerfile基础操作/基础dockerfile操作/image-2024254526103.png)
# 基础结构

![image-2024255216895.png](3可以放入网站的笔记/Linux上dockerfile基础操作/基础dockerfile操作/image-2024255216895.png)
# 如何构建
`docker build -t myImage:1.0 .`
`里面有个点,是当前目录`
-t是起名字,:后面不接的话就是latest

# 
![image-202425811628.png](3可以放入网站的笔记/Linux上dockerfile基础操作/基础dockerfile操作/image-202425811628.png)
# 开始构建
![image-2024251335502.png](3可以放入网站的笔记/Linux上dockerfile基础操作/基础dockerfile操作/image-2024251335502.png)
在使用Dockerfile的时候   .    后面不加就是默认使用Dockerfile的名字
![image-2024251239336.png](3可以放入网站的笔记/Linux上dockerfile基础操作/基础dockerfile操作/image-2024251239336.png)
构建好镜像后docker run容器
![image-2024251816807.png](3可以放入网站的笔记/Linux上dockerfile基础操作/基础dockerfile操作/image-2024251816807.png)
查看日志 
docker logs ID
docker logs -f ID  # 实时更新
![image-2024252124762.png](3可以放入网站的笔记/Linux上dockerfile基础操作/基础dockerfile操作/image-2024252124762.png)
![image-202425211132.png](3可以放入网站的笔记/Linux上dockerfile基础操作/基础dockerfile操作/image-202425211132.png)
