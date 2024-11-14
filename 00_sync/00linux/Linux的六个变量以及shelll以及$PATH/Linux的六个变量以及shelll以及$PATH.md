# $PATH
`/usr/bin` 通常包含在 `PATH` 环境变量中，这样系统在执行命令时会自动搜索该目录。`PATH` 变量包含多个目录，当你在命令行输入命令时，系统会按照 `PATH` 中的顺序查找可执行文件。
```
echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin
```
`/usr/bin` 本身不是一个环境变量，但它是许多环境变量（如 `PATH`）的一部分，影响程序的执行和命令的查找。
创建的符号链接可以被任何脚本或程序直接调用，就像调用系统自带的命令一样。
**可能会造成冲突**：如果系统中已经存在同名的命令或链接，可能会导致冲突。
![image-2024111294632.png](00_sync/00linux/Linux%E7%9A%84%E5%85%AD%E4%B8%AA%E5%8F%98%E9%87%8F%E4%BB%A5%E5%8F%8Ashelll%E4%BB%A5%E5%8F%8A$PATH/Linux%E7%9A%84%E5%85%AD%E4%B8%AA%E5%8F%98%E9%87%8F%E4%BB%A5%E5%8F%8Ashelll%E4%BB%A5%E5%8F%8A$PATH/image-2024111294632.png)
# 用户变量
##  1. `~/.bashrc`【推荐】

- **用途**：用于交互式的非登录 Shell（例如在打开一个新的终端或在命令行中输入 `bash` 时）。
- **特点**：适合放置别名、路径、函数等会频繁使用的命令设置。
- **加载方式**：默认在非登录 Shell 启动时加载。

##  2. `~/.bash_profile`

- **用途**：用于交互式的登录 Shell（例如在登录时，或者通过 SSH 登录时）。
- **特点**：一般用于设置用户环境变量和初始化路径。
- **加载方式**：默认在登录时加载。如果系统没有找到 `~/.bash_profile`，它会尝试加载 `~/.profile`。

##  3. `~/.profile`

- **用途**：用于 POSIX 兼容的 Shell（例如 `sh`），或者当没有特定的 Bash 配置文件时。
- **特点**：作为通用的登录配置文件，用于系统兼容性。
- **加载方式**：通常只在登录 Shell 中加载。如果系统找不到 `~/.bash_profile`，会默认加载 `~/.profile`。
# 全局变量

## 1.`/etc/bash.bashr】`【推荐】

**作用**：
- `/etc/bash.bashrc` 是一个全局的配置文件，它只对所有用户的交互式 shell 会话生效。
- 它通常用于设置全局的 shell 选项、别名、命令提示符等。
**适用范围**：
- 适用于所有用户的交互式 shell 会话，不适用于非交互式 shell。
## 2. **`/etc/environment`**：
 **作用**：
- `/etc/environment` 是一个全局的配置文件，它用于设置全局的环境变量。
- 这些环境变量会被所有用户的 shell 会话继承。
**适用范围**：
- 适用于所有用户的 shell 会话，无论是否为交互式 shell。
## 3. `/etc/profile`
**作用**：
- `/etc/profile` 是一个全局的配置文件，它对所有用户的 shell 会话生效，无论是登录 shell 还是非登录 shell。
- 它通常用于设置全局的环境变量、路径和一些初始设置。
**适用范围**：
- 适用于所有用户的 shell 会话，无论是否为登录 shell。

# shell登陆方式
## **登录 shell**：
加载 `/etc/profile` 和 `~/.bash_profile` 或 `~/.profile`。
## **非登录 shell**：
加载 `/etc/profile` 和 `~/.profile`。
## **交互式 shell**：
加载 `/etc/bash.bashrc` 和 `~/.bashrc`。
# 查看系统中的shell
```
cat /etc/shells
```
![image-20241028523584.png](00_sync/00linux/Linux的六个变量以及shelll以及$PATH/Linux的六个变量以及shelll以及$PATH/image-20241028523584.png)
# 查看当前所用shell
```
# 系统环境变量
echo $SHELL
# 正在执行脚本的命令 也就是如果切换shell类型可以看到
echo $0
# $1 2 3 就是传递给这个脚本的第一第二第三个参数了   
```
注意大写
![image-202410285337730.png](00_sync/00linux/Linux的六个变量以及shelll以及$PATH/Linux的六个变量以及shelll以及$PATH/image-202410285337730.png)
切换为rbash shell命令  就可以用echo $0 看到当前shell类型 
![image-20241028571272.png](00_sync/00linux/Linux的六个变量以及shelll/Linux的六个变量以及shelll以及$PATH/image-20241028571272.png)
# 编写脚本
```
#!/binbash
下面的都好说了
你用什么shell代码就怎么写
```
给所有用户执行权限
```
chmod a+x 123.sh
```
但是不加权限也可以直接bash执行
```
bash 123.sh
```
# 常见的shell
##  1. **Bash (Bourne Again Shell)**

- **特性**：最常用的Shell，继承了Bourne Shell的语法，并添加了许多增强功能，例如命令补全、历史记录等。
- **文件**：常用配置文件有`~/.bashrc`、`~/.bash_profile`和`/etc/bash.bashrc`。
- **应用**：多数Linux发行版的默认Shell，适合脚本编写和日常使用。

##  2. **Zsh (Z Shell)**

- **特性**：功能丰富，支持更强的命令补全、拼写检查、主题配置和插件系统（通过Oh My Zsh等框架）。
- **文件**：常用配置文件有`~/.zshrc`。
- **应用**：深受开发者喜爱，尤其是在自定义和交互体验方面。

##  3. **Ksh (Korn Shell)**

- **特性**：兼容Bourne Shell，添加了C Shell中的一些特性，适合写脚本，性能高。
- **文件**：常用配置文件有`~/.kshrc`、`~/.profile`。
- **应用**：在AIX、HP-UX等系统中常见，用于专业环境和脚本编写。

##  4. **Fish (Friendly Interactive Shell)**

- **特性**：用户友好的设计，默认支持语法高亮、自动建议和命令补全。
- **文件**：常用配置文件有`~/.config/fish/config.fish`。
- **应用**：适合新手和开发者，配置简单且美观。

##  5. **Csh (C Shell)**

- **特性**：语法类似C语言，适合习惯C语言语法的用户。
- **文件**：常用配置文件有`~/.cshrc`。
- **应用**：较少使用，多见于某些老式Unix系统。

##  6. **Tcsh (Enhanced C Shell)**

- **特性**：C Shell的增强版，增加了命令补全、历史记录等功能。
- **文件**：常用配置文件有`~/.tcshrc`、`~/.cshrc`。
- **应用**：主要用于老的Unix环境，兼容性较好。

##  7. **Dash (Debian Almquist Shell)**

- **特性**：一个轻量级、执行效率高的Shell，主要用于系统启动脚本中。
- **文件**：共享Bourne Shell的配置文件，如`~/.profile`。
- **应用**：在Debian和Ubuntu中用作默认的`/bin/sh`。

##  8. **PowerShell**

- **特性**：由微软开发，专为Windows设计，但也支持Linux和macOS。支持对象管道和复杂任务自动化。
- **文件**：配置文件通常位于`$PROFILE`路径。
- **应用**：多用于Windows环境的系统管理和自动化。

