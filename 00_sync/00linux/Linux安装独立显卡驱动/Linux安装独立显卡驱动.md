# 查看环境
先过滤下显示设备硬件，判断是否正常
```
lshw -numeric -C display
```
![image-202410311418208.png](00_sync/00linux/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/image-202410311418208.png)
# 官网正规下载 
https://www.nvidia.cn/geforce/drivers
![image-20241031144693.png|350](00_sync/00linux/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/image-20241031144693.png)
下载完成之后应该是一个run的文件,尽可能下载稳定版吧
# 卸载环境
```
apt-get purge nvidia*
sudo apt-get remove –purge nvidia*
```

```
sudo nano /etc/modprobe.d/blacklist-nouveau.conf
```
# 禁用nouveau驱动
添加内容禁用Linux内核中的`nouveau`驱动的，`nouveau`是一个针对NVIDIA GPU的开源驱动程序。在某些情况下，禁用`nouveau`可以避免与专有的NVIDIA闭源驱动程序之间的冲突，从而使得NVIDIA专有驱动能够更好地工作。
查看是否在加载nouveau驱动
```
lsmod | grep nouveau
```
![image-20241031181689.png|400](00_sync/00linux/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/image-20241031181689.png)
```
sudo gedit /etc/modprobe.d/blacklist.conf

```
添加如下，也不需要改回来
```
blacklist nouveau
```
![image-2024115646291.png|425](00_sync/00linux/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/image-2024115646291.png)
或者用下面的,都是用来禁用nouveau驱动的
sudo nano /etc/modprobe.d/blacklist-nouveau.conf
```
blacklist nouveau
options nouveau modeset=0
```
并且更新
```
sudo update-initramfs -u
```
# 禁用安全启动
重启之前记得先禁用bios里面的安全启动 secure boot【注意不是TPM】
![4f269496e6d3f1982545fa405c9dab4.jpg|425](00_sync/00linux/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/4f269496e6d3f1982545fa405c9dab4.jpg)
后再检查性爱我们刚才禁用的nouveau是否正在运行,如果是空的就可以了
```
lsmod | grep nouveau
```
![image-2024115116422.png|450](00_sync/00linux/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/image-2024115116422.png)
# 安装英伟达显卡驱动程序
```
ubuntu-drivers devices #这个是可以联网下载下来安装的，不过我直接从官网安装了
```
安装的时候我们要关闭图形化，切换到3级别用户就可以了
```
sudo telinit 3
```
找到最开始正规下载的run文件。+x全兴并且执行它
```
sudo sh ./NVIDIA-Linux-x86_64-390.48.run --no-opengl-files

–no-opengl-files 只安装驱动文件，不安装OpenGL文件。这个参数最重要
–no-x-check 安装驱动时不检查X服务
–no-nouveau-check 安装驱动时不检查nouveau
 后面两个参数可不加。
```
![image-20241134536.png](00_sync/00linux/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/image-20241134536.png)
1. **MIT/GPL 模块**
- **许可证**：MIT/GPL 许可证
- **特点**：
    - **开源**：内核模块的源代码是公开的，符合 GPL 许可证的要求。
    - **兼容性**：与 Linux 内核的 GPL 许可证完全兼容，可以在任何基于 GPL 的系统上使用。
    - **社区支持**：由于是开源的，可以获得社区的支持和贡献。
- **适用场景**：
    - **开源项目**：如果你正在开发一个开源项目，需要确保所有组件都是开源的。
    - **企业环境**：如果你的工作环境要求所有软件都必须符合开源许可。
2. **NVIDIA Proprietary 模块**
- **许可证**：NVIDIA 专有许可证
- **特点**：
    - **闭源**：内核模块的源代码是封闭的，不对外公开。
    - **性能优化**：NVIDIA 通常会对专有模块进行更深入的优化，以提供最佳的性能和稳定性。
    - **专有功能**：可能包含一些专有的功能和特性，这些功能在开源模块中不可用。
- **适用场景**：
    - **性能要求高**：如果你需要最高的图形性能和稳定性，特别是在游戏、专业图形处理和机器学习等领域。
    - **企业级应用**：如果你的工作环境允许使用专有软件，并且需要 NVIDIA 提供的技术支持和服务。
继续继续！构建内核模块。
![image-2024113613293.png|375](00_sync/00linux/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/image-2024113613293.png)
安装成功
![image-2024115555222.png](00_sync/00linux/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/image-2024115555222.png)
```
nvidia-smi
```
![image-2024115051558.png](00_sync/00linux/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/image-2024115051558.png)
# 安装CUDA 工具包
https://developer.nvidia.com/cuda-downloads
这边我就用run了
![image-20241154027142.png](00_sync/00linux/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/image-20241154027142.png) 
安装完成后
![image-2024115431296.png](00_sync/00linux/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/image-2024115431296.png)
因为我已经安装了驱动程序，所以取消勾选
![image-2024115471580.png](00_sync/00linux/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/image-2024115471580.png)
安装建议
- **CUDA Toolkit 12.6**:
    - 建议选择安装。这是开发和运行 CUDA 应用程序所必需的。
- **CUDA Demo Suite 12.6**:
    - 如果您是 CUDA 新手或者想要一些示例代码来学习和参考，建议选择安装。
- **CUDA Documentation 12.6**:
    - 如果您需要详细的文档来帮助您理解和使用 CUDA，建议选择安装。
- **Kernel Objects** 和 **nvidia-fs**:
    - 除非您有特定的需求，否则通常不需要选择这些选项。大多数用户可以跳过这些选项。
![image-20241155017230.png](00_sync/00linux/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/image-20241155017230.png)
这一段话记得拿去AI看一下是否兼容
![image-20241155035158.png|475](00_sync/00linux/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/image-20241155035158.png)
```
nano ~/.bashrc
```
但是现在我们还是找不到CUDA的
![image-20241154435369.png](00_sync/00linux/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/image-20241154435369.png)
这两行环境变量配置的作用是确保系统能够找到 CUDA 工具包中的可执行文件和库文件
```
export PATH=/usr/local/cuda-12.6/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-12.6/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```

```
source ~/.bashrc
```
切换终端
```
nvcc --version
```
正确安装
![image-2024115522057.png](00_sync/00linux/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/image-2024115522057.png)
```
root@xybluelinux:~# echo $PATH
/usr/local/cuda-12.6/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin
root@xybluelinux:~# echo $LD_LIBRARY_PATH
/usr/local/cuda-12.6/lib64
root@xybluelinux:~# 
```
## 验证是否正常
使用ffmpeg 配合N卡的的 hevc_nvenc
```
ffmpeg -i c测试视频.mkv -vf "scale=-2:1080,format=yuv420p10le" -c:v hevc_nvenc -b:v 60M -color_trc smpte2084 -color_primaries bt2020 -colorspace bt2020nc -c:a copy 输出.mkv
```
转码的时候功率提升，ok
![image-2024115137923.png|425](00_sync/00linux/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/image-2024115137923.png)
# cudnn
(**深度神经网络的GPU加速库,需要神经网络则安否则可以不安**)
# Docker中安装使用英伟达


## 安装NVIDIA Container Toolkit
![image-202411704438.png|343](00_sync/00linux/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/image-202411704438.png)
```
# 添加存储库
distribution=$(. /etc/os-release;echo $ID$VERSION_ID) && \
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add - && \
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

# 更新并安装 nvidia-container-toolkit
sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit
```

```
sudo systemctl restart docker
docker run --gpus all --runtime=nvidia --name=ubuntu -d -it -p 8888:8888 59ab366372d5
```
docker compose 示例 jellyfin
```
version: '3.8'

services:
  jellyfin:
    image: nyanmisaka/jellyfin
    container_name: jellyfin
    hostname: jellyfin
    volumes:
      - /home/0000/docker/jellyfin/config:/config
      - /home/xyblue_smb/jellyfin/media:/media
    environment:
      - PUID=0
      - PGID=0
    restart: unless-stopped
    network_mode: host
    devices:
      - /dev/dri:/dev/dri
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]
    runtime: nvidia
```
这个时候就会发现容器内可以用连接N卡了
![image-2024117111265.png|425](00_sync/00linux/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/image-2024117111265.png)
![image-20241171219651.png|425](00_sync/00linux/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/image-20241171219651.png)
如果后续出现又不能用的情况，或者直接就修改配置文件，免得后面出问题
sudo nano /etc/docker/daemon.json
这个源和dns不用理会，这是我自己的，注意添加的n卡path就可以
```
{
  "registry-mirrors": [
    "https://docker.rainbond.cc",
    "https://registry-1.docker.io",
    "https://docker.m.daocloud.io",
    "https://noohub.ru",
    "https://huecker.io",
    "https://dockerhub.timeweb.cloud"
  ],
  "dns": ["8.8.8.8", "8.8.4.4"],
  "runtimes": {
    "nvidia": {
      "path": "nvidia-container-runtime"
    }
  }
}

```
异常处理
![image-20241172227275.png](00_sync/00linux/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/image-20241172227275.png)
正常
![image-20241172258163.png](00_sync/00linux/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/image-20241172258163.png)
# 问题总结

## 显驱和CUDA
NVIDIA 驱动程序:
nvidia-smi 和 CUDA 都依赖于 NVIDIA 驱动程序。驱动程序是 GPU 与操作系统之间的接口，负责管理 GPU 的硬件资源。
如果您已经安装了 NVIDIA 驱动程序，并且 nvidia-smi 可以正常使用，那么驱动程序应该是已经正确安装了。
CUDA 工具包:
CUDA 工具包包含了编译器、库和工具，用于开发和运行 CUDA 应用程序。
安装 CUDA 后，您需要配置环境变量，以便在系统中使用 CUDA 工具。
## 缺少32位库
```
Unable to find a suitable destination to install 32-bit compatibility
```
执行补全操作
```
sudo dpkg --add-architecture i386
sudo apt update
sudo apt install libc6:i386
```
即可顺利安装

## gcc版本过低


![image-20241131754478.png|400](00_sync/00linux/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/image-20241131754478.png)
成功
![image-20241153918443.png|425](00_sync/00linux/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/Linux%E5%AE%89%E8%A3%85%E7%8B%AC%E7%AB%8B%E6%98%BE%E5%8D%A1%E9%A9%B1%E5%8A%A8/image-20241153918443.png)
gcc要升级到高版本，不要remove空间过多，会造成系统瘫痪
## 切换显卡&&核显
```
sudo prime-select nvidia # 切换nvidia显卡
sudo prime-select intel  # 切换intel显卡
sudo prime-select query  # 查看当前使用的显卡
`on-demand` 表示当前的配置是“按需”模式。
```

