 本文是我看到一个作者写的很好，记录一下，我进行了缩减一下，基本包含了所有用法了,原链接是
 https://rclone.cn/docs.html

## 基本语法

Rclone将一个目录树从一个存储系统同步到另一个
```
Syntax: [options] subcommand  
```
你可以在配置文件中定义任意多的存储路径。
在学习rclone时，请使用[`-i` / `--interactive`](https://rclone.cn/docs.html#interactive)标志，以避免意外的数据丢失。
## 子命令

rclone使用一个子命令系统。 比如说

|     |                                                             |
| --- | ----------------------------------------------------------- |
|     | rclone ls remote:path # 列出了一个远程【注意冒号必须有】                    |
|     | rclone copy /local/path remote:path # 复制/local/path到远程      |
|     | rclone sync -i /local/path remote:path # 将/local/path同步到远程。 |

主要的rclone命令，最常用的在前面
- [rclone config](https://rclone.cn/rclone_config.html) – 进入一个交互式配置会话.
- [rclone copy](https://rclone.cn/rclone_copy.html) – 从源文件复制到目的地，跳过已经复制的文件.
- [rclone sync](https://rclone.cn/rclone_sync.html) – 使源码和目的地相同，只修改目的地。
- [rclone bisync](https://rclone.cn/rclone_bisync.html) – 两个路径之间的[双向同步]（/bisync/）。.
- [rclone move](https://rclone.cn/rclone_move.html) – 将文件从源头移到目的地.
- [rclone delete](https://rclone.cn/rclone_delete.html) – 删除路径中的内容.
- [rclone purge](https://rclone.cn/rclone_purge.html) – 移除路径及其所有的内容.
- [rclone mkdir](https://rclone.cn/rclone_mkdir.html) – 如果路径还不存在，就建立路径.
- [rclone rmdir](https://rclone.cn/rclone_rmdir.html) – 移除路径.
- [rclone rmdirs](https://rclone.cn/rclone_rmdirs.html) – 删除路径下的任何空目录.
- [rclone check](https://rclone.cn/rclone_check.html) – 检查源文件和目的地文件是否匹配.
- [rclone ls](https://rclone.cn/rclone_ls.html) – 列出路径中所有物体的大小和路径.
- [rclone lsd](https://rclone.cn/rclone_lsd.html) – 列出路径中的所有目录/容器/buckets.
- [rclone lsl](https://rclone.cn/rclone_lsl.html) – 列出路径中所有对象的大小、修改时间和路径.
- [rclone md5sum](https://rclone.cn/rclone_md5sum.html) – 为路径中的所有对象产生一个md5sum文件.
- [rclone sha1sum](https://rclone.cn/rclone_sha1sum.html) – 为路径中的所有对象产生一个sha1sum文件.
- [rclone size](https://rclone.cn/rclone_size.html) – 返回remote:path中对象的总大小和数量。.
- [rclone version](https://rclone.cn/rclone_version.html) – 显示版本号。
- [rclone cleanup](https://rclone.cn/rclone_cleanup.html) – 如果可能的话，清理一下远程。
- [rclone dedupe](https://rclone.cn/commands/rclone_dedupe.html) – 交互式地查找重复的文件并删除/重命名它们.
- [rclone authorize](https://rclone.cn/commands/rclone_authorize.html) – 远程授权。
- [rclone cat](https://rclone.cn/rclone_cat.html) – 将任何文件串联起来，并将其发送到stdout。
- [rclone copyto](https://rclone.cn/rclone_copyto.html) – 从源文件复制到目的地，跳过已经复制的文件。
- [rclone genautocomplete](https://rclone.cn/rclone_genautocomplete.html) – 输出rclone的shell完成脚本.
- [rclone gendocs](https://rclone.cn/rclone_gendocs.html) – 输出rclone的markdown文档到提供的目录中。.
- [rclone listremotes](https://rclone.cn/rclone_listremotes.html) – 列出配置文件中的所有远程。
- [rclone mount](https://rclone.cn/rclone_mount.html) – 将远程作为一个挂载点挂载。
- [rclone moveto](https://rclone.cn/rclone_moveto.html) – 将文件或目录从源头移到目的地。
- [rclone obscure](https://rclone.cn/rclone_obscure.html) – 在rclone.conf中使用的非明文的密码。
- [rclone cryptcheck](https://rclone.cn/rclone_cryptcheck.html) – 检查一个加密的远程的完整性。
- [rclone about](https://rclone.cn/rclone_about.html) – 从远程获取配额信息。
完整的清单见[命令索引]（/commands.html）。
## 复制单个文件

rclone通常会同步或复制目录。 然而，如果源远程指向一个文件，rclone将只是复制该文件。 目标远程必须指向一个目录–如果不是的话，rclone会给出 "Failed to create file system for "remote:file": is a file not a directory "的错误。
例如，假设你有一个叫 "test.jpg "的远程文件，那么你可以像这样复制该文件
建议在复制单个文件时使用 "copy"，而不是 "sync"，它们的效果基本相同，但 "copy "使用的内存要少很多。
### remote:/path/to/dir
在大多数后端，这指的是与`remote:path/to/dir`相同的目录，这种格式应该是首选。 在极少数的远程（FTP、SFTP、Dropbox的业务）上，这将指的是一个不同的目录。 在这些情况下，没有前导词`/`的路径将指的是你的 "home "目录，有前导词`/`的路径将指的是root。
### :backend:path/to/dir

这是一种高级形式，用于即时创建远程。 `backend`应该是后台的名称或前缀（配置文件中的`type`），后台的所有配置应该在命令行（或环境变量）中提供。这里有一些例子。
```
rclone lsd --http-url https://pub.rclone.org :http:
```
要列出`https://pub.rclone.org/`根目录下的所有目录。
```
rclone lsf --http-url https://example.com :http:path/to/dir
```

要列出`https://example.com/path/to/dir/`中的文件和目录
```
rclone copy --http-url https://example.com :http:path/to/dir /tmp/dir
```
将`https://example.com/path/to/dir`中的文件和目录复制到`/tmp/dir`。
```
rclone copy --sftp-host example.com :sftp:path/to/dir /tmp/dir
```
使用sftp从相对目录`path/to/dir`中的`example.com`复制文件和目录到`/tmp/dir`。

### 连接字符串 {#connection-strings}。

上面的例子也可以用连接字符串的语法来写，所以不是作为命令行参数`--http-url https://pub.rclone.org`来提供参数，而是作为远程规范的一部分，作为一种连接字符串提供。

|   |   |
|---|---|
||rclone lsd ":http,url='https://pub.rclone.org':"|
||rclone lsf ":http,url='https://example.com':path/to/dir"|
||rclone copy ":http,url='https://example.com':path/to/dir" /tmp/dir|
||rclone copy :sftp,host=example.com:path/to/dir /tmp/dir|

这些可以应用于修改现有的远程，也可以用on the fly语法创建新的远程。这个例子相当于在远程`gdrive:`中加入`--drive-shared-with-me`参数。
```
rclone lsf "gdrive,shared_with_me:path/to/dir"
```
使用连接字符串风格的语法的主要优点是，它只适用于远程，而不是命令行中该类型的所有远程。一个常见的困惑是，试图将google drive上共享的文件复制到正常的驱动器上，这**是行不通的，因为`--drive-shared-with-me`标志同时适用于源和目的地。
```
rclone copy --drive-shared-with-me gdrive:shared-file.txt gdrive:
```
然而，使用连接字符串的语法，这确实可以工作。
```
rclone copy "gdrive,shared_with_me:shared-file.txt" gdrive:
```
请注意，连接字符串只影响即时后端选项。例如，如果gdriveCrypt是基于gdrive的加密，那么下面的命令**不会按预期工作，因为`shared_with_me`被加密后端忽略了。
```
rclone copy "gdriveCrypt,shared_with_me:shared-file.txt" gdriveCrypt:
```
连接字符串的语法如下

|     |                                                        |
| --- | ------------------------------------------------------ |
|     | remote,parameter=value,parameter2=value2:path/to/dir   |
|     | :backend,parameter=value,parameter2=value2:path/to/dir |

如果 "参数 "有": "或","，那么它必须放在引号中 `"` or  `'`, so

|   |   |
|---|---|
||remote,parameter="colon:value",parameter2="comma,value":path/to/dir|
||:backend,parameter='colon:value',parameter2='comma,value':path/to/dir|

如果一个引用值需要包括该引用，那么它应该是双倍的，所以
```
remote,parameter="with""quote",parameter2='with''quote':path/to/dir
```
这将使`parameter'成为`with "quote’，`parameter2'成为`with’quote’。

如果你不写`=参数`，那么rclone会用`=true`代替，这对标志来说非常有效。例如，要使用环境中配置的s3，你可以使用。
```
rclone lsd :s3,env_auth:
```
这相当于
```
rclone lsd :s3,env_auth=true:
```
注意，在命令行中，你可能需要在这些连接字符串周围加上`"`或`'`，以阻止shell解释其中的任何特殊字符。

如果你是一个shell高手，那么你会知道哪些字符串是可以的，哪些是不可以的，但是如果你不确定，那么就用`"`括起来，用`'`作为内引号。这种语法在所有操作系统上都适用。
```
rclone copy ":http,url='https://example.com':path/to/dir" /tmp/dir
```
在Linux/MacOS上，一些字符仍然在shell中的`"`字符串中被解释（特别是`\`和`$`以及`"`），所以如果你的字符串包含这些，你可以这样交换`"`和`'`的角色。(这种语法在Windows上不起作用)。
```
rclone copy ':http,url="https://example.com":path/to/dir' /tmp/dir
```
#### 连接字符串、配置和日志

如果你通过命令行标志、环境变量或连接字符串向后端提供额外的配置，那么rclone将根据配置的哈希值向远程的名称添加一个后缀，例如
```
rclone -vv lsf --s3-chunk-size 20M s3:
```
是否有日志信息
```
DEBUG : s3: detected overridden config - adding "{Srj1p}" suffix to name
```
这是为了让rclone在缓存后端时能够区分出修改过的远程和未修改的远程。

这应该只在日志中可以注意到。

这意味着，在飞行中的后端，如
```
rclone -vv lsf :s3,env_auth:
```
将获得自己的名字
```
DEBUG : :s3: detected overridden config - adding "{YTu53}" suffix to name
```
### 有效的远程名称

远程名称是区分大小写的，并且必须遵守以下规则。

- 可以包含数字、字母、`_`、`-`、`.`和空格。
- 不得以"-"或空格开头。
- 可能不以空间为终点。

从rclone 1.61版开始，任何Unicode数字和字母都是允许的，而在旧版本中，它被限制在普通的ASCII（0-9，A-Z，a-z）。如果你在不同的shell中使用相同的rclone配置，而这些shell可能配置了不同的字符编码，你必须谨慎地使用在所有shell中都可以书写的字符。这主要是在Windows上的问题，因为控制台传统上使用非Unicode字符集–由所谓的 "代码页 "定义。

## 引用和shell

当你向你的计算机输入命令时，你正在使用一种叫做命令行外壳的东西。 它以操作系统的特定方式解释各种字符。

下面是一些可能有助于不熟悉shell规则的用户的麻烦事

### Linux / OSX

如果你的名字中有空格或shell元字符（例如：`*`、`?`、`$`、`'`、`"`等），那么你必须引用它们。 默认情况下使用单引号`'`
```
rclone copy 'Important files?' remote:backup
```
如果你想发送一个"”，你将需要使用"""，例如。
```
rclone copy "O'Reilly Reviews" remote:backup
```
引用元字符的规则很复杂，如果你想了解全部细节，你必须查阅你的shell的手册页面。

### Windows

如果你的名字里有空格，你需要把它们放在`""里，例如。

rclone copy "E:\folder name\folder name\folder name" remote:backup

如果你是单独使用根目录，那么就不要引用它（原因见[#464](https://github.com/rclone/rclone/issues/464)），比如说

rclone copy E:\ remote:backup

## 复制名称中含有`:`的文件或目录

rclone使用`:`来标记一个远程名称。 然而，这在非Windows操作系统中是一个有效的文件名组件。 远程名称解析器只会搜索到第一个`/`的`:`，所以如果你需要对这样的文件或目录采取行动，那么就使用以`/`开头的完整路径，或者使用`./`作为当前目录的前缀。

因此，要将一个名为 "sync:me "的目录同步到一个名为 "remote: "的远程目录，请使用
```
rclone sync -i ./sync:me remote:path
```
or
```
rclone sync -i /full/path/to/sync:me remote:path
```
## 服务器端拷贝

大多数远程（但不是全部–见[概述](https://rclone.cn/overview.html#optional-features)）支持服务器端拷贝。

这意味着如果你想把一个文件夹复制到另一个文件夹，那么rclone不会下载所有的文件并重新上传；它将指示服务器将它们复制到位。
```
rclone copy s3:oldbucket s3:newbucket
```
将复制`oldbucket`的内容到`newbucket`，不需要下载和重新上传。

不支持服务器端复制的远程**将**下载并在这种情况下重新上传。

服务器端拷贝用于`sync'和`copy’，当使用`-v'标志时，将在日志中被识别。 如果远程不直接支持服务器端移动，`move`命令也可以使用它们。 这是通过发布服务器端拷贝然后删除来完成的，这比下载和重新上传要快得多。

只有在远程名称相同的情况下才会尝试服务器端拷贝。

这可以在编写脚本时使用，以便有效地进行老化的备份，例如。

|   |   |
|---|---|
||rclone sync -i remote:current-backup remote:previous-backup|
||rclone sync -i /path/to/files remote:current-backup|

## 元数据支持 {#metadata}

元数据是关于文件的数据，而不是文件的内容。 通常rclone只尽可能的保留修改时间和内容（MIME）类型。

当使用`--metadata`或`--M`标志时，Rclone支持保留文件（不是目录）上所有可用的元数据。

确切地说，哪些元数据被支持，以及这种支持意味着什么，取决于后端。支持元数据的后端在其文档中有一个元数据部分，并在[features table](https://rclone.cn/overview.html#features)中列出（例如[local](https://rclone.cn/local.html#metadata), [s3](https://rclone.cn/s3.html#metadata)

Rclone只支持元数据的一次性同步。这意味着只有当源对象发生变化并需要重新加载时，元数据才会从源对象同步到目标对象。如果元数据随后在源对象上发生了变化，但没有改变对象本身，那么它将不会被同步到目标对象。这与rclone同步`Content-Type`而不使用`--metadata`标志的方式是一致的。

当从本地同步到本地时，使用`--metadata`将保留文件属性，如文件模式、所有者、扩展属性（不是Windows）。

注意，在对象第一次上传时，可以使用`--metadata-set key=value`标志将任意的元数据添加到对象中。 这个标志可以根据需要重复多次。

### 元数据的类型

元数据被分为两种类型。系统元数据和用户元数据。

后台自己使用的元数据被称为系统元数据。例如，在本地后端，系统元数据`uid`将存储文件的用户ID，当在一个基于unix的平台上使用时。

任意的元数据被称为用户元数据，这可以根据需要进行设置。

当对象从后端复制到后端时，如果提供了系统元数据，它们将试图解释系统元数据。当对象在不同的后端之间复制时，元数据可能从用户元数据变为系统元数据。例如，从s3复制一个对象会设置`内容类型'元数据。在一个能理解这个的后端（如`azureblob’），这将成为对象的Content-Type。在一个不理解这个的后端（如`local`后端），这将成为用户元数据。然而，如果本地对象被复制回s3，内容类型将被正确设置。

### 元数据框架

Rclone实现了一个元数据框架，它可以从一个对象中读取元数据，并在对象被上传时（而且只有在上传时）将其写入对象。

这个元数据被存储为一个有字符串键和字符串值的字典。

对键的名称有一些限制（这些在将来可能会被进一步澄清）。

- 必须是小写
- 可以是`a-z``0-9`，包含`.```MARKDOWN_HASHa7185263988794ecaef531dde9f3a1e4MARKDOWN_HASH_`“。
- 长度取决于后端

每个后端可以提供它所理解的系统元数据。一些后端也可以存储任意的用户元数据。

在可能的情况下，键名是标准化的，因此，例如，可以将对象元数据从s3复制到azureblob，元数据会被适当地翻译。

一些后端对元数据的大小有限制，如果超过了这些限制，rclone会在上传时出错。

### 元数据保存

实施的目标是

1. 如果可能的话，保留元数据
2. 如果可能的话，解释元数据

1的后果是，你可以无损地将S3对象复制到本地磁盘，然后再回到S3。同样，你也可以把一个带有文件属性和xattrs的本地文件从本地磁盘复制到S3，然后再无损地复制回来。

2的后果是，你可以把带有元数据的S3对象复制到Azureblob（比如说），让元数据也出现在Azureblob对象上。

### 标准系统元数据

下面是一个标准的系统元数据表，如果合适的话，后端可以实现。

|key|description|example|
|---|---|---|
|mode|File type and mode: octal, unix style|0100664|
|uid|User ID of owner: decimal number|500|
|gid|Group ID of owner: decimal number|500|
|rdev|Device ID (if special file) => hexadecimal|0|
|atime|Time of last access: RFC 3339|2006-01-02T15:04:05.999999999Z07:00|
|mtime|Time of last modification: RFC 3339|2006-01-02T15:04:05.999999999Z07:00|
|btime|Time of file creation (birth): RFC 3339|2006-01-02T15:04:05.999999999Z07:00|
|cache-control|Cache-Control header|no-cache|
|content-disposition|Content-Disposition header|inline|
|content-encoding|Content-Encoding header|gzip|
|content-language|Content-Language header|en-US|
|content-type|Content-Type header|text/plain|

如果在元数据中提供了 "mtime "和 "content-type"，则元数据键将优先于读取源对象的 "Content-Type "或修改时间。

哈希值不包括在系统元数据中，因为已经有明确的方法来读取这些数据。

## 选项

Rclone有许多选项来控制其行为。

带参数的选项有两种传递方式：`--option=value`或`--option value`。然而，布尔（真/假）选项的行为与其他选项略有不同，`--布尔`将选项设置为`真'，没有标志则设置为`假’。 也可以指定`--boolean=false`或`--boolean=true`。 注意，`--boolean false`是无效的–这被解析为`--boolean`，`false`被解析为rclone的额外命令行参数。

### 时间或持续时间选择 {#时间-选项}

TIME或DURATION选项可以被指定为一个持续时间字符串或一个时间字符串。

持续时间字符串是一个可能有符号的十进制数字序列，每个数字都有可选的分数和单位后缀，如 "300ms"、"-1.5h "或 "2h45m"。默认单位是秒，或者以下缩写有效。

- `ms` – Milliseconds
- `s` – Seconds
- `m` – Minutes
- `h` – Hours
- `d` – Days
- `w` – Weeks
- `M` – Months
- `y` – Years

这些也可以被指定为以下格式的绝对时间。

- RFC3339 – e.g. `2006-01-02T15:04:05Z` or `2006-01-02T15:04:05+07:00`
- ISO8601 Date and time, local timezone – `2006-01-02T15:04:05`
- ISO8601 Date and time, local timezone – `2006-01-02 15:04:05`
- ISO8601 Date – `2006-01-02` (YYYY-MM-DD)

### 尺寸选项 {#尺寸选项}。

使用SIZE的选项默认使用KiB（1024字节的倍数）。 然而，可以使用后缀`B`代表Byte，`K`代表KiB，`M`代表MiB，`G`代表GiB，`T`代表TiB，`P`代表PiB。这些是二进制单位，例如：1、2*_10、2*_20、2**30。

### –备份目录=DIR

当使用 "同步"、"复制 "或 "移动 "时，任何本来会被覆盖或删除的文件都会按其原来的层次被移动到这个目录。

如果`--suffix`被设置，那么被移动的文件将被加上后缀。 如果在DIR中存在相同路径的文件（添加后缀后），那么它将被覆盖。

使用的远程必须支持服务器端的移动或复制，而且你必须使用同一个远程作为同步的目的地。 备份目录不能与目标目录重叠，否则会被过滤规则排除。

比如说

rclone sync -i /path/to/local remote:current --backup-dir remote:old

将同步`/path/to/local`到`remote:current`，但对于任何已经更新或删除的文件将被存储在`remote:old`。

如果从脚本中运行rclone，你可能想用今天的日期作为传递给`--backup-dir`的目录名来存储旧文件，或者你可能想用今天的日期传递`--suffix`。

参见 `--compare-dest` 和 `--copy-dest`。

### –bind string

用于外发连接的本地地址。 这可以是一个IPv4地址（1.2.3.4），一个IPv6地址（1234::789A）或主机名。 如果主机名不能解析或解析到一个以上的IP地址，就会出现错误。

### –bwlimit=BANDWIDTH_SPEC

该选项控制带宽限制。比如说

--bwlimit 10M

将意味着把上传和下载带宽限制在10 MiB/s。  
*_NB_这是每秒**个字节，而不是每秒**个比特。要使用单一的限制，以KiB/s为单位指定所需的带宽，或者使用后缀B|K|M|G|T|P。默认值是 "0"，意味着不限制带宽。

上传和下载带宽可以单独指定，如`--bwlimit UP:DOWN`，所以

--bwlimit 10M:100k

将意味着把上传带宽限制在10 MiB/s，下载带宽限制在100 KiB/s。两种限制都可以是 "关闭"，即没有限制，所以如果只是限制上传带宽，你可以使用

--bwlimit 10M:off

这将限制上传带宽为10 MiB/s，但下载带宽将是无限的。

如上所述，带宽限制将在rclone二进制程序运行期间持续。

也可以指定一个限制的 "时间表"，这将导致某些限制在某些时间被应用。要指定一个时间表，请将条目格式化为 "WEEKDAY-HH:MM,BANDWIDTH WEEKDAY-HH:MM,BANDWIDTH… "其中。`WEEKDAY`是可选元素。

- BANDWIDTH "可以是一个单一的数字，例如 "100k "或一对用于上传：下载的数字，例如 "10M：1M"。
- WEEKDAY "可以写成整个单词，也可以只用前三个字符。它是可选的。
- `HH:MM`是一个小时，从00:00到23:59。

为避免白天工作时间内的链接饱和，一个典型的时间表的例子可以是。

`--bwlimit "08:00,512k 12:00,10M 13:00,512k 18:00,30M 23:00,off"`

在这个例子中，传输带宽将在每天早上8点设置为512 KiB/s。中午，它将上升到10 MiB/s，并在下午1点回落到512 KiB/sec。在下午6点，带宽限制将被设置为30 MiB/s，在晚上11点，它将被完全禁用（全速）。 晚上11点和早上8点之间的任何东西都将保持无限。

一个带有 "WEEKDAY "的时间表的例子可以是。

`--bwlimit "Mon-00:00,512 Fri-23:59,10M Sat-10:00,1M Sun-20:00,off"`

这意味着，周一的传输带宽将被设定为512 KiB/s。在周五结束前，它将上升到10 MiB/s。在周六10:00，它将被设置为1 MiB/s。从周日20:00开始，它将是无限的。

没有`WEEKDAY’的时间段被扩展到整个星期。所以这个例子。

`--bwlimit "Mon-00:00,512 12:00,1M Sun-20:00,off"`

相当于这样。

`--bwlimit "Mon-00:00,512Mon-12:00,1M Tue-12:00,1M Wed-12:00,1M Thu-12:00,1M Fri-12:00,1M Sat-12:00,1M Sun-12:00,1M Sun-20:00,off"`

带宽限制适用于所有后端数据的传输。对于大多数后端，目录列表带宽也包括在内（非HTTP后端、`ftp`、`sftp`和`storj`除外）。

注意，单位是**字节/秒**，而不是**比特/秒**。通常情况下，连接是以比特/秒来衡量的–转换时要除以8。例如，假设你有一个10Mbit/s的连接，你希望rclone使用它的一半–5Mbit/s。这就是5/8 = 0.625 MiB/s，所以你要为rclone使用`--bwlimit 0.625M`参数。

在Unix系统上（Linux, macOS, …），带宽限制器可以通过向rclone发送`SIGUSR2`信号来切换。这可以消除长期运行的rclone传输的限制，并在需要时迅速恢复到`--bwlimit`指定的值。假设只有一个rclone实例在运行，你可以像这样切换限制器。

kill -SIGUSR2 $(pidof rclone)

如果你用[远程控制](https://rclone.cn/rc.html)配置rclone，那么你就可以使用动态地改变bwlimit。

rclone rc core/bwlimit rate=1M

### –bwlimit-file=BANDWIDTH_SPEC

该选项控制每个文件的带宽限制。选项见`--bwlimit`标志。

例如，使用该选项允许任何传输速度超过1 MiB/s。

--bwlimit-file 1M

这可以和`--bwlimit`一起使用。

注意，如果提供了一个时间表，文件将使用传输开始时有效的时间表。

### –buffer-size=SIZE

使用这个大小的缓冲区来加速文件传输。 每个`---传输`将使用这么多的内存进行缓冲。

当使用`mount'或`cmount’时，每个打开的文件描述符将使用这么多内存进行缓冲。 更多细节请参见[mount](https://rclone.cn/rclone_mount.html#file-buffering) 文档。

设置为 "0 "是为了禁用最小内存用量的缓冲。

注意，缓冲区的内存分配受[–use-mmap](https://rclone.cn/docs.html#use-mmap)标志的影响。

### –cache-dir=DIR

指定rclone将用于缓存的目录，以覆盖默认值。

默认值取决于操作系统。

- Windows `%LocalAppData%rclone`，如果`LocalAppData`被定义的话。
- macOS `$HOME/Library/Caches/rclone`如果定义了`HOME`的话。
- 如果定义了 "XDG_CACHE_HOME"，则Unix为"$XDG_CACHE_HOME/rclone"；如果定义了 "HOME"，则为"$HOME/.cache/rclone"。
- 回退（在所有操作系统上）到`$TMPDIR/rclone`，其中`TMPDIR`是[–temp-dir](https://rclone.cn/docs.html#temp-dir-dir)的值。

你可以使用[config paths](https://rclone.cn/rclone_config_paths.html)命令来查看当前值。

缓存目录被[VFS文件缓存](https://rclone.cn/rclone_mount.html#vfs-file-caching)挂载功能大量使用，也被[service](/rclone_serve.html，[GUI](https://rclone.cn/gui)和rclone的其他部分使用。

### –check-first

如果这个标志被设置了，那么在 "同步"、"复制 "或 "移动 "中，rclone会在进行任何传输之前做所有的检查，看文件是否需要被传输。通常情况下，rclone会尽快开始运行传输。

这个标志在IO有限的系统中很有用，因为传输会干扰检查。

当使用`--order-by`时，它对确保完美的排序也很有用。

使用这个标志可以使用更多的内存，因为它有效地将`--max-backlog`设置为无限大。这意味着在传输开始之前，所有要传输的对象的信息都被保存在内存中。

### –checkers=N

最初只是控制并行运行的文件检查器的数量，例如通过`rclone copy`。现在是一个相当普遍的并行控制，由`rclone`在多个地方使用。

注意：检查器在同步过程中对文件进行平等检查。  
对于一些存储系统（如S3、Swift、Dropbox），这可能需要大量的时间，所以它们是并行运行的。

默认情况是并行运行8个检查器。然而，如果是反应缓慢的后端，你可能需要降低（而不是增加）这个默认值，将`--检查器`设置为4个或更少的线程。如果你在文件检查阶段遇到后端服务器崩溃的情况，特别建议你这样做（例如，在后续或充值备份中，很少或没有进行文件复制，检查占用了大部分时间）。只有在监测服务器健康状况和文件检查吞吐量的情况下，才能极其谨慎地增加这一设置。

### -c, –checksum

通常情况下，rclone会查看文件的修改时间和大小，看它们是否相等。 如果你设置了这个标志，那么rclone将检查文件的哈希值和大小来确定文件是否相等。

当远程不支持设置修改时间，并且需要比仅仅检查文件大小更精确的同步时，这很有用。

当在对象上存储相同哈希类型的远程之间传输时，这非常有用，例如Drive和Swift。关于哪些远程支持哪种哈希类型，请参见[概述部分]（/overview/）中的表格。

例如`rclone --checksum sync s3:/bucket swift:/bucket`会比没有`--checksum`标志的情况下运行得更快。

当使用这个标志时，如果远程文件的mtimes不正确，rclone不会像平时那样更新mtimes。

### –color WHEN

指定何时应将颜色（和其他ANSI代码）添加到输出中。

`AUTO`（默认）只允许在输出为终端时使用ANSI代码。

`NEVER`从不允许使用ANSI代码

`ALWAYS`总是添加ANSI代码，不管输出格式如何（终端或文件）。

### –compare-dest=DIR

当使用 "sync"、"copy "或 "move "时，除了目的地的文件外，还会检查DIR。如果发现一个与源文件相同的文件，则不从源文件中复制。这对于只复制自上次备份后发生变化的文件是很有用的。

你必须使用与同步的目的地相同的远程。 比较目录不能与目标目录重叠。

见`--copy-dest`和`--backup-dir`。

### –config=CONFIG_FILE

指定rclone配置文件的位置，以覆盖默认值。例如：`rclone config --config="rclone.conf"`。

确切的默认值描述起来有点复杂，因为不同版本的rclone在保持向后兼容的同时会有一些变化，但在大多数情况下，它就像这样简单。

- `%APPDATA%/rclone/rclone.conf` on Windows
- `~/.config/rclone/rclone.conf` on other

完整的逻辑是这样的。Rclone将在以下任何位置寻找现有的配置文件，按优先顺序排列。

1. `rclone.conf` (在程序目录中，rclone的可执行文件是)
2. `%APPDATA%/rclone/rclone.conf` (仅在Windows上)
3. `$XDG_CONFIG_HOME/rclone/rclone.conf` (在所有系统上，包括Windows)
4. `~/.config/rclone/rclone.conf` (见下文对~符号的解释)
5. `~/.rclone.conf`

如果没有找到现有的配置文件，那么将在以下位置创建一个新的配置文件。

- 在Windows上。上面列出的位置2，除非万一`APPDATA’没有被定义，那么将使用位置4。
- 在Unix上。如果定义了`XDG_CONFIG_HOME’，则位置为3，否则位置为4。
- 当rclone目录不能被创建时，回退到位置5（在所有操作系统上），但如果没有找到主目录，那么相对于当前工作目录的路径`.rclone.conf`将被作为最后的手段使用。

上述路径中的`~`符号代表任何操作系统上当前用户的主目录，其值定义如下。

- 在Windows上：如果定义了`%HOME%`，则为`%USERPROFILE%`，否则为`%HOMEDRIVE%/%HOMEPATH%`。
- 在Unix上：如果定义了`$HOME’，则通过在操作系统特定的用户数据库中查找当前用户。  
    (例如passwd文件），否则就使用shell命令`cd && pwd`的结果。

如果你运行`rclone配置文件`，你会看到默认的位置是什么。

事实上，与rclone可执行文件在同一目录下的现有文件`rclone.conf`总是被优先考虑的，这意味着很容易在 "便携式 "模式下运行，将rclone可执行文件下载到一个可写目录，然后在同一目录下创建一个空文件`rclone.conf`。

如果位置被设置为空字符串`""`或文件名为`notfound`的路径，或者在Windows系统中用数值`NUL`表示的os null设备和在Unix系统中用数值`/dev/null`表示的os null设备，那么rclone将只保留内存中的配置文件。

文件格式是基本的[INI](https://en.wikipedia.org/wiki/INI_file#Format)：文本的章节，由"[section]"标题引导，后面是单独的 "key=value "条目。在rclone中，每个远程由它自己的部分代表，部分名称定义了远程的名称。选项被指定为 "key=value "条目，其中key是选项名称，没有"–backend-"前缀，小写，用"_"代替"-"。例如，选项`--mega-hard-delete`对应于键`hard_delete`。只有后端选项可以被指定。 一个特殊的，也是必须的键`type`标识了[存储系统](https://rclone.cn/overview.html)，其中的值是由命令`rclone help backends`返回的内部小写名称。评论在行首用`;`或`#`表示。

例子。

|   |   |
|---|---|
||[megaremote]|
||type = mega|
||user = you@example.com|
||pass = PDPcQVVjVtzFY-GTdDFozqBhTdsPg3qH|

请注意，密码是以[obscured](https://rclone.cn/rclone_obscure.html)形式出现的。另外，许多存储系统使用基于令牌的认证而不是密码，这需要额外的步骤。使用交互式命令`rclone config`，而不是手动编辑配置文件，更容易，也更安全。

配置文件通常包含登录信息，因此应该有限制性的权限，以便只有当前用户可以阅读它。你也可以选择[加密](https://rclone.cn/docs.html#configuration-encryption)该文件。

当使用基于令牌的认证时，配置文件必须是可写的，因为Rclone需要更新里面的令牌。

### –contimeout=TIME

设置连接超时。这应该是go time的格式，看起来像`5s`代表5秒，`10m`代表10分钟，或者`3h30m`。

连接超时是rclone等待连接到远程对象存储系统的时间。 它是  
`1m` by default.

### –copy-dest=DIR

当使用`sync',`copy’或`move’时，除了目的地之外，还会检查DIR的文件。如果发现一个与源文件相同的文件，该文件会在服务器端从DIR复制到目的地。这对增量备份很有用。

使用的远程必须支持服务器端拷贝，而且你必须使用同一个远程作为同步的目的地。 比较目录不能与目标目录重叠。

参见`--比较-目的地`和`--备份-目录`。

### –dedupe-mode MODE

运行重复计算命令的模式。 `交互式'、`跳过’、`第一'、`最新’、`最旧'、`重命名’中的一种。 默认是 "交互式"。  
关于这些选项的含义，请看dedupe命令的更多信息。

### –disable FEATURE,FEATURE,…

这将禁用一个逗号分隔的可选功能列表。例如，禁用服务器端的移动和服务器端的复制使用。

--disable move,copy

这些功能可以放在任何情况下。

要看到哪些功能可以被禁用的列表，请使用。

--disable help

请看概览[features](https://rclone.cn/overview.html#features)和[optional features](https://rclone.cn/overview.html#optional-features)，以了解哪个功能做什么。

这个标志在调试和特殊情况下很有用（比如Google Drive将服务器端拷贝的总量限制在100GiB/天）。

### –disable-http2

这将阻止rclone尝试使用HTTP/2（如果可用）。由于[Go标准库的问题](https://github.com/golang/go/issues/37373)，这有时会加快传输速度。

### –dscp VALUE

指定一个连接中使用的DSCP值或名称。这可以帮助QoS系统识别流量类别。允许使用BE、EF、DF、LE、CSx和AFxx。

参见[differentiated services](https://en.wikipedia.org/wiki/Differentiated_services)的描述以了解这个字段。将此设置为1（LE），将流量识别为SCAVENGER类，可以避免在支持DiffServ的网络中占用过多的带宽（[RFC 8622](https://tools.ietf.org/html/rfc8622)）。

例如，如果你在路由器上配置了QoS来正确处理LE。运行中。

rclone copy --dscp LE from:/from to:/to

将使其优先级低于通常的互联网流量。

这个选项在Windows上没有作用（见[golang/go#42728](https://github.com/golang/go/issues/42728)）。

### -n, –dry-run

做一个没有永久性变化的试运行。 用它来看看rclone会做什么，而不用实际去做。 在设置 "sync "命令时很有用，该命令会删除目的地的文件。

### –expect-continue-timeout=TIME

如果请求有 "Expect: 100-continue "头，这指定了在完全写入请求头后等待服务器的第一个响应头的时间量。不是所有的后端都支持使用这个。

零意味着没有超时，并导致立即发送正文，而不等待服务器的批准。 这个时间不包括发送请求头的时间。

默认是`1s'。 设置为`0`则禁用。

### –error-on-no-transfer

默认情况下，如果没有错误，rclone将以返回代码0退出。

这个选项允许rclone在源文件和目的文件之间没有传输文件的情况下返回退出代码9。这允许在脚本中使用rclone，如果数据被复制，则触发后续动作，如果没有则跳过。

注意：启用这个选项会使一个通常不致命的错误变成一个可能致命的错误–请检查并相应地调整你的脚本!

### –fs-cache-expire-duration=TIME

当通过API使用rclone时，rclone默认在 "fs cache "中对创建的远程进行5分钟的缓存。这意味着如果你在同一个远程上重复操作，那么rclone就不必再从头开始建立它，这使它更有效率。

这个标志设置了远程缓存的时间。如果你把它设置为 "0"（或负数），那么rclone将完全不缓存远程。

注意，如果你使用了一些标志，例如`--backup-dir`，如果这个标志被设置为`0`，rclone可能会建立两个远程（一个用于源或目标，一个用于`--backup-dir`，以前可能只建立一个。

### –fs-cache-expire-interval=TIME

这控制了rclone检查远程缓存过期的频率。 更多信息见上面的`--fs-cache-expire-duration`文档。默认值是60秒，设置为0可以禁止过期。

### –header

为所有交易添加一个HTTP头。该标志可以重复使用以添加多个头信息。

如果你想只为上传添加头信息，使用`--header-upload`，如果你想只为下载添加头信息，使用`--header-download`。

这个标志支持所有基于HTTP的后端，即使是那些不被`--header-upload`和`--header-download`支持的后端，所以可以作为一种变通方法，供那些谨慎的人使用。

rclone ls remote:test --header "X-Rclone: Foo" --header "X-LetMeIn: Yes"

### –header-download

为所有下载交易添加一个HTTP头。该标志可以重复使用以添加多个头。

rclone sync -i s3:test/src ~/dst --header-download "X-Amz-Meta-Test: Foo" --header-download "X-Amz-Meta-Test2: Bar"

关于目前支持的后端，请参见GitHub问题[这里](https://github.com/rclone/rclone/issues/59)。

### –header-upload

为所有上传交易添加一个HTTP头。该标志可以重复使用以添加多个标头。

rclone sync -i ~/src s3:test/dst --header-upload "Content-Disposition: attachment; filename='cool.html'" --header-upload "X-Amz-Meta-Test: FooBar"

关于目前支持的后端，请参见GitHub问题[这里](https://github.com/rclone/rclone/issues/59)。

### –human-readable

Rclone命令将大小（如字节数）和数量（如文件数）的值输出为_原始数字，或以_人类可读*的格式输出。

在人类可读的格式中，数值被缩放为更大的单位，用数值后面的后缀来表示，并四舍五入到三位小数。Rclone一贯使用二进制单位（2的幂）表示大小，使用十进制单位（10的幂）表示计数。 大小的单位前缀是根据IEC标准符号，例如`Ki`表示kibi。 与字节单位一起使用，`1 KiB`表示1024字节。在列表类型的输出中，只有单位前缀附加在数值上（例如：`9.762Ki`），而在更多的文本输出中，显示完整的单位（例如：`9.762 KiB`）。对于计数，使用SI标准符号，例如，前缀`k`代表公斤。与文件计数一起使用，`1k`表示1000个文件。

各种[list](https://rclone.cn/rclone_ls.html)命令默认输出原始数字，选项`--human-readable`将使它们以人类可读的格式输出数值（带有短单位前缀）。

[about](https://rclone.cn/rclone_about.html)命令默认输出人类可读格式，有一个命令专用的选项`--full`来代替输出原始数字。

命令[size](https://rclone.cn/rclone_size.html)在同一输出中同时输出人类可读的数字和原始数字。

[tree](https://rclone.cn/rclone_tree.html)命令也考虑了`--人可读'，但它不会使用与其他命令完全相同的符号。它四舍五入到小数点后一位，并使用单字母后缀，例如：`K`而不是`Ki`。其原因是它依赖于一个外部库。

交互式命令[ncdu](https://rclone.cn/rclone_ncdu.html)默认显示为人类可读格式，并响应`u`键以切换人类可读格式。

### –ignore-case-sync

使用这个选项将导致rclone在同步时忽略文件的大小写，所以当现有的文件名相同时，即使大小写不同，文件也不会被复制/同步。

### –ignore-checksum

通常情况下，rclone会检查传输文件的校验和是否匹配，如果不匹配就会出现 "传输时损坏 "的错误。

你可以使用这个选项来跳过这个检查。 只有当你遇到 "传输时被破坏 "的错误信息，并且你确定你可能想传输可能被破坏的数据时，你才应该使用它。

### –ignore-existing

使用这个选项将使rclone无条件地跳过目的地上存在的所有文件，无论这些文件的内容如何。

虽然这不是一个普遍推荐的选项，但在你的文件因加密而改变的情况下，它可能是有用的。然而，它不能在传输被中断的情况下纠正部分传输。

当执行`move`/`moveto`命令时，当目的地存在相同名称的文件时，这个标志将使源位置的跳过文件保持不变。

### –ignore-size

通常情况下，rclone会查看文件的修改时间和大小，看它们是否相等。 如果你设置了这个标志，那么rclone将只检查修改时间。 如果`--checksum`被设置，那么它只检查校验和。

它还会使rclone在传输后跳过验证大小是否相同的问题。

这对于从OneDrive传输文件很有用，因为OneDrive有时会错误地报告图像文件的大小（更多信息见[#399](https://github.com/rclone/rclone/issues/399)）。

### -I, –ignore-times

使用这个选项将导致rclone无条件地上传所有文件，而不管文件在目的地的状态如何。

通常情况下，rclone会跳过任何具有相同修改时间和相同大小的文件（如果使用`--checksum`，则具有相同的校验值）。

### –immutable

将源文件和目标文件视为不可改变的，不允许修改。

设置了这个选项后，文件将按要求被创建和删除，但现有的文件将永远不会被更新。 如果现有的文件在源文件和目标文件之间不匹配，rclone将给出错误提示  
`Source and destination exist but do not match: immutable file modified`.

注意，只有传输文件的命令（如`同步`，`复制`，`移动`）受此行为影响，只有修改是不允许的。 文件仍然可以明确地被删除（例如：`delete',`purge’）或隐含地被删除（例如：`sync',`move’）。 如果希望避免删除和修改，可以使用`copy --immutable`。

这对于不可改变的或只附加的数据集（特别是备份档案）来说是非常有用的，因为修改意味着损坏，不应该被传播。

### -i / –interactive {#interactive}

这个标志可以用来告诉rclone，你希望在破坏性操作之前进行手动确认。

建议你在学习rclone时使用这个标志，特别是在`rclone sync`时。

比如说

|   |   |
|---|---|
||$ rclone delete -i /tmp/dir|
||rclone: delete "important-file.txt"?|
||y) Yes, this is OK (default)|
||n) No, skip this|
||s) Skip all delete operations with no more questions|
||!) Do all delete operations with no more questions|
||q) Exit rclone now.|
||y/n/s/!/q> n|

这些选项意味着

- `y`: **是**，这个操作应该继续进行。你也可以按Return键来实现这个操作。除非你选择`s`或`！`，否则每次都会问你。
- `n`: **不**，不要做这个操作。除非你选择`s`或`！`，否则每次都会被问到。
- `s`: **跳过**下面所有这种类型的操作，没有问题了。这在rclone退出之前都是有效的。如果有任何不同类型的操作，你会被提示这些操作。
- `!`: **做所有**以下的操作，没有问题了。如果你已经决定不介意rclone做这种操作，那就很有用。这在rclone退出之前是有效的。如果有任何不同类型的操作，你会被提示进行这些操作。
- `q`: **现在就退出**rclone，以备不时之需!

### –leave-root

在rmdirs过程中，它不会删除根目录，即使它是空的。

### –log-file=FILE

记录所有rclone的输出到FILE。 这在默认情况下是不激活的，这对于追踪同步的问题和`-v`标志相结合是很有用的。 更多信息见[日志部分](https://rclone.cn/docs.html#logging)。

如果FILE存在，rclone将追加到它。

注意，如果你使用`logrotate`程序来管理rclone的日志，那么你应该使用`copytruncate`选项，因为rclone没有一个信号来旋转日志。

### –log-format LIST

逗号分隔的日志格式选项的列表。可接受的选项有`date`, `time`, `microseconds`, `pid`, `longfile`, `shortfile`, `UTC`。任何其他关键词都将被默默地忽略。`pid`将用进程标识符来标记日志信息，这对`rclone mount --daemon`很有用。其他可接受的选项在[go documentation](https://pkg.go.dev/log#pkg-constants)中解释。 默认的日志格式是"`date`,`time`"。

### –log-level LEVEL

这设置了rclone的日志级别。 默认的日志级别是`NOTICE`。

`DEBUG`等同于`-vv`。它输出大量的调试信息–对于bug报告和真正发现rclone在做什么很有用。

`INFO`等同于`-v`。它输出关于每次传输的信息，默认情况下每分钟打印一次统计信息。

`NOTICE`是默认的日志级别，如果没有提供日志标志。当事情正常进行时，它的输出量很小。它输出警告和重大事件。

`ERROR`等同于`-q`。它只输出错误信息。

### –use-json-log

这就把rclone的日志格式切换为JSON。json日志的字段是level, msg, source, time。

### –low-level-retries NUMBER

这控制了rclone进行低级重试的次数。

低级重试是用来重试一个失败的操作–通常是一个HTTP请求。 例如，这可能是上传一个大文件的一个块。 你会在日志中看到低级重试的`-v`标志。

然而，如果你有很多低级重试，你可能希望减少这个值，这样rclone就会更快地进入高级重试（见`--retries`标志）。

用`--low-level-retries 1`禁用低级重试。

### –max-backlog=N

这是同步/复制/移动队列中允许的最大积压文件，以便被检查或转移。

这可以任意设置得很大。 它只在队列使用时才会使用内存。 注意，当积压文件被使用时，它将使用N KiB数量级的内存。

设置这个值可以使rclone更准确地计算出有多少文件在等待，给出更准确的估计完成时间，并使`--order-by`工作得更准确。

设置为小，将使rclone与远程的列表更加同步，这可能是理想的。

设置为负数将使积压的文件尽可能多。

### –max-delete=N

这告诉rclone不要删除超过N个文件。 如果超过了这个限制，那么将产生一个致命的错误，rclone将停止正在进行的操作。

### –max-depth=N

这修改了所有命令的递归深度，除了purge。

因此，如果你执行`rclone --max-depth 1 ls remote:path`，你将只看到顶级目录下的文件。 使用`--最大深度2`意味着你将看到前两层目录中的所有文件，以此类推。

由于历史原因，`lsd`命令默认使用`–最大深度’为1 –你可以用命令行标志覆盖它。

你可以使用这个命令来禁止递归（使用`–最大深度1’）。

注意，如果你和`--sync`和`--delete-excluded`一起使用这个命令，没有被递归的文件将被视为排除在外，并将在目的地被删除。 如果你不确定会发生什么，请先用`--dry-run`进行测试。

### –max-duration=TIME

当Rclone运行到指定的时间时，它将停止调度新的传输。

默认为关闭。

当达到限制时，任何现有的传输将完成。

如果达到传输限制，Rclone不会以错误退出。

### –max-transfer=SIZE

Rclone在达到指定大小时将停止传输。 默认为关闭。

当达到限制时，所有传输将立即停止。

如果达到传输限制，Rclone将以退出代码8退出。

## –metadata / -M

设置这个标志可以让rclone将元数据从源文件复制到目标文件。对于本地后端，这是所有权、权限、xattr等。参见[#metadata](https://rclone.cn/%E5%85%83%E6%95%B0%E6%8D%AE%E9%83%A8%E5%88%86)以获得更多信息。

### –metadata-set key=value

上传时添加元数据`key`=`value`。这可以根据需要重复多次。参见[#metadata](https://rclone.cn/%E5%85%83%E6%95%B0%E6%8D%AE%E9%83%A8%E5%88%86)以获得更多信息。

### –cutoff-mode=hard|soft|cautious

这修改了`--max-transfer`的行为，默认为`--cutoff-mode=hard`。

指定`--cutoff-mode=hard`将在Rclone达到极限时立即停止传输。

指定`--cutoff-mode=soft`将在Rclone达到极限时停止启动新的传输。

指定`--cutoff-mode=cautious`将试图防止Rclone达到极限。

### –modify-window=TIME

当检查一个文件是否被修改时，这是一个文件可以有的最大时间差，并且仍然被认为是等同的。

默认值是`1ns`，除非被远程重写。 例如，OS X只将修改时间存储到最接近的第二位，所以如果你正在向OS X文件系统读写，这将是默认的`1s’。

这个命令行标志允许你覆盖这个计算的默认值。

### –multi-thread-cutoff=SIZE

当下载文件到本地后端超过这个大小时，rclone将使用多个线程来下载文件（默认为250M）。

Rclone预先分配文件（在unix上使用`fallocate(FALLOC_FL_KEEP_SIZE)`，在Windows上使用`NTSetInformationFile`，两者都不需要时间），然后每个线程直接在正确位置写入文件。 这意味着rclone不会创建碎片化或稀疏的文件，在传输结束时也不会有任何装配时间。

用于下载的线程数量由以下因素控制  
`--multi-thread-streams`.

如果你希望看到关于线程的信息，请使用`-vv`。

这将与`sync`/`copy`/`move`命令和朋友`copyto`/`moveto`一起工作。 多线程下载将与`rclone mount`和`rclone serve`一起使用，如果`--vfs-cache-mode`被设置为`writes`或以上。

**NB**这***只适用于本地目标，但也适用于任何来源。

**NB**多线程拷贝在本地到本地的拷贝中是禁用的，因为没有多线程拷贝会更快，除非明确设置`--多线程-streams`。

**NB**在Windows上使用多线程下载将导致产生的文件是[稀疏](https://en.wikipedia.org/wiki/Sparse_file)。使用`--local-no-sparse`来禁用稀疏文件（这可能导致下载开始时的长时间延迟）或使用`--multi-thread-streams 0`禁用多线程下载。

### –multi-thread-streams=N

当使用多线程下载时（见上文"–多线程截止"），这设置了使用的最大流的数量。 设置为 "0 "可以禁止多线程下载（默认为4）。

rclone究竟使用多少流来下载取决于文件的大小。为了计算下载流的数量，Rclone用文件的大小除以`--多线程截止点`，然后四舍五入，直到`--多线程-流`设定的最大值。

因此，如果`--多线程截止250M`和`--多线程-流4`是有效的（默认值）。

- 0..250 MiB files will be downloaded with 1 stream
- 250..500 MiB files will be downloaded with 2 streams
- 500..750 MiB files will be downloaded with 3 streams
- 750+ MiB files will be downloaded with 4 streams

### –no-check-dest

`--no-check-dest`可以与`move`或`copy`一起使用，它使rclone在复制文件时完全不检查目的地。

这意味着

- 目的地未被列出，从而最大限度地减少了API调用。
- 文件总是被传送
- 这可能会导致在允许的远程设备上出现重复的情况（如Google Drive）。
- 建议使用"–重试1"，否则重试时将重新传输所有内容。

如果你知道没有一个文件在目的地，这个标志对于尽量减少交易是有用的。

这是一个专门的标志，大多数用户应该忽略它。

### –no-gzip-encoding

不要设置`Accept-Encoding: gzip`。 这意味着rclone不会自动向服务器索取压缩文件。如果你设置了服务器以`Content-Encoding: gzip’返回文件，但你上传了压缩文件，这很有用。

在正常操作中没有必要设置这个，这样做会降低rclone的网络传输效率。

### –no-traverse

`--no-traverse`标志控制在使用`copy`或`move`命令时是否遍历目标文件系统。`--no-traverse`与`sync`不兼容，如果你用`sync`提供它，将被忽略。

如果你只复制少量的文件（或过滤大部分文件）和/或在目的地有大量的文件，那么`--no-traverse`将停止rclone列出目的地并节省时间。

然而，如果你正在复制大量的文件，特别是如果你正在进行复制，考虑到很多文件没有改变，不需要复制，那么你不应该使用`--no-traverse`。

参见[rclone copy](https://rclone.cn/rclone_copy.html)，了解如何使用它的例子。

### –no-unicode-normalization

在同步程序中不要对文件名中的unicode字符进行标准化处理。

有时，操作系统会以分解的形式存储包含单码字的文件名（特别是macOS）。一些云存储系统会重新组合单码，如果数据被复制到本地文件系统，就会导致重复的文件。

使用这个标志将禁用该功能，将每个unicode字符视为唯一。例如，默认情况下，é和é将被规范化为同一个字符。使用`--no-unicode-normalization`，它们将被视为唯一的字符。

### –no-update-modtime

当使用这个标志时，如果远程文件的修改时间不正确，rclone不会像通常那样更新它们。

如果远程文件也在与其他工具同步（例如Google Drive客户端），就可以使用这个标志。

### –order-by string

`--order-by`标志控制在`rclone sync`、`rclone copy`和`rclone move`中处理积压文件的顺序。

按顺序的字符串是这样构成的。 第一部分描述被测量的方面。

- `size` – 按文件的大小排序
- `name` – 按文件的完整路径排序
- `modtime` – 按文件的修改日期排序

这可以有一个用逗号附加的修饰语。

- `ascending` or `asc` – 顺序，以便先处理最小的（或最老的）。
- `descending` or `desc` – 顺序，以便先处理最大的（或最新的）。
- `mixed` – 顺序，以便在某些线程中先处理最小的，在其他线程中处理最大的。

如果修改器是 "混合"，那么它可以有一个可选的百分比（默认为 "50"），例如，"size,mixed,25"，这意味着25%的线程应该取最小的项目，75%取最大的。先取最小的线程将总是先取最小的，同样地，先取最大的线程也是如此。混合 "模式对于在传输大小文件的混合过程中最大限度地减少传输时间非常有用–大文件被保证上传线程和带宽，小文件将被连续处理。

如果没有提供修饰符，那么顺序就是 "升序"。

比如说

- `--order-by size,desc` – 先发送最大的文件
- `--order-by modtime,ascending` – 先发送最古老的文件
- `--order-by name` – 先按路径的字母顺序发送文件

如果没有提供`---order-by`标志，或者提供的是一个空字符串，那么将使用默认的排序，即扫描的排序。 对于`---检查器1`，这主要是按字母顺序排列的，但是对于默认的`---检查器8`，则有些随机。

#### Limitations

`--order-by`标志并不对数据进行单独的传递。 这意味着它可能不按指定的顺序传输一些文件，如果

- 在积压的文件中没有文件，或者源文件还没有被完全扫描。
- 积压的文件超过[–max-backlog](https://rclone.cn/docs.html#max-backlog-n)。

Rclone会尽力传输它所拥有的最好的文件，所以在实践中这不应该造成问题。 把`--order-by`看作是一个最佳努力的标志，而不是一个完美的排序。

如果你想要完美的排序，那么你需要指定[–check-first](https://rclone.cn/docs.html#check-first)，它将在传输任何文件之前首先找到所有需要传输的文件。

### –password-command SpaceSepList

这个标志提供了一个程序，它应该在运行时提供配置密码。这是对rclone提示密码或设置`RCLONE_CONFIG_PASS`变量的一种替代。

它的参数应该是一个带有空格的参数列表的命令。如果其中一个参数有空格，那么用`"`"括起来，如果你想在参数中使用字面的`"`，那么用`"`括起来，然后把`"`"加倍。更多信息见[CSV编码](https://godoc.org/encoding/csv)。

鸡蛋

|   |   |
|---|---|
||--password-command echo hello|
||--password-command echo "hello with space"|
||--password-command echo "hello with ""quotes"" and space"|

参见[配置加密](https://rclone.cn/docs.html#configuration-encryption)以获得更多信息。

参见[Wiki上的Windows PowerShell例子](https://github.com/rclone/rclone/wiki/Windows-Powershell-use-rclone-password-command-for-Config-file-password)。

### -P, –progress

这个标志使rclone在终端的静态块中更新统计信息，提供传输的实时概况。

任何日志信息都会在静态块的上方滚动。 日志信息将把静态块推到终端的底部，在那里它将保持不变。

通常情况下，这是每500mS更新一次，但这个周期可以用`--stats`标志覆盖。

这可以与`--stats-one-line`标志一起使用，以获得更简单的显示。

注意：在Windows上，直到[这个bug](https://github.com/Azure/go-ansiterm/issues/26)被修复，当使用`--progress`时，所有非ASCII字符将被替换成`.`。

### –progress-terminal-title

这个标志，当与`-P/--progress`一起使用时，将打印字符串`ETA: %s`到终端标题。

### -q, –quiet

这个标志将限制rclone的输出只包括错误信息。

### –refresh-times

`--refresh-times`标志可以用来更新现有文件的修改时间，当它们在不支持哈希值的后端不同步时。

如果你上传的文件有不正确的时间戳，而你现在希望纠正它们，这就很有用。

这个flag **只** 对不支持哈希值的目的地（如`crypt`）很有用。

这可以用于任何同步命令`sync`，`copy`或`move`。

要使用这个标志，你需要做一个修改时间的同步（所以不能使用`---仅尺寸`或`---校验`）。当使用"—仅尺寸 "或"—校验 "时，该标志将没有效果。

如果使用这个标志，当rclone上传文件时，它会检查目的地是否有一个现有的文件。如果这个文件的大小与源文件相匹配（如果有的话，还有校验和），但时间戳不同，那么rclone将更新目标文件的时间戳，而不是重新上传它。如果校验和不匹配，rclone将上传新文件。如果没有校验和（例如在`crypt`后端），rclone将更新时间戳。

注意，有些远程在不重新上传文件的情况下不能设置修改时间，所以这个标志对它们来说不太有用。

通常情况下，如果你在做修改时间同步，只要远程支持校验，rclone就会更新修改时间而不需要`--refresh-times`。 **和** 文件上的校验和匹配。然而，如果没有校验和，rclone将上传文件，而不是设置时间戳，因为这是安全行为。

### –retries int

重试整个同步过程，如果它失败了这么多次（默认为3次）。

一些远程设备可能不可靠，重试几次有助于捡起因错误而没有传输的文件。

用`--retries 1`禁用重试。

### –retries-sleep=TIME

这设置了由`--retries`指定的每次重试的间隔时间。

默认是`0`。使用`0`来禁用。

### –server-side-across-configs

允许服务器端的操作（例如复制或移动）在不同的配置下工作。

如果你想在两个使用相同后端但配置不同的远程之间进行服务器端的复制或移动，这可能很有用。

请注意，这不是默认启用的，因为rclone不容易知道它是否能在任何两个配置之间工作。

### –size-only

通常情况下，rclone会查看文件的修改时间和大小，看它们是否相等。 如果你设置了这个标志，那么rclone将只检查大小。

这对于从Dropbox传输被桌面同步客户端修改过的文件非常有用，因为桌面同步客户端不会像rclone那样设置修改时间的校验。

### –stats=TIME

传输数据的命令（`sync',`copy’, `copyto',`move’, `moveto’）将定期打印数据传输统计，以显示其进度。

这设置了间隔时间。

默认是`1m`。使用`0`来禁用。

如果你设置了统计间隔，那么所有的命令都可以显示统计信息。 这在运行其他命令时很有用，例如`check`或`mount`。

统计信息默认以`INFO`级别记录，这意味着它们不会显示在默认的`NOTICE`级别。 使用`--stats-log-level NOTICE`或`-v`来显示它们。 参见[日志部分](https://rclone.cn/docs.html#logging)了解更多关于日志级别的信息。

注意，在macOS上，你可以发送一个SIGINFO（通常在终端中是ctrl-T）来使统计信息立即打印。

### –stats-file-name-length integer

默认情况下，`--stats`输出将截断超过40个字符的文件名和路径。 这相当于提供`--stats-file-name-length 40`。使用`--stats-file-name-length 0`来禁用stats打印的文件名的任何截断。

### –stats-log-level string

显示`--统计'输出的日志级别。 这可以是`DEBUG`，`INFO`，`NOTICE`，或`ERROR`。 默认是 "INFO"。 这意味着在默认的日志级别是 "NOTICE"，统计信息不会显示 - 如果你想让它们显示，那么使用`–stats-log-level NOTICE’。 参见[日志部分](https://rclone.cn/docs.html#logging)了解更多关于日志级别的信息。

### –stats-one-line

当指定这一点时，rclone将统计信息浓缩成一行，只显示最重要的统计信息。

### –stats-one-line-date

当指定这一点时，rclone会启用单行统计，并在显示前加上一个日期字符串。默认是`2006/01/02 15:04:05 -`

### –stats-one-line-date-format

当指定这一点时，rclone会启用单行统计，并在显示前加上一个用户提供的日期字符串。日期字符串必须用引号括起来。关于日期格式化的语法，请遵循[golang specs](https://golang.org/pkg/time/#Time.Format)。

### –stats-unit=bits|bytes

默认情况下，数据传输率将以每秒的字节数打印。

该选项允许以每秒比特为单位打印数据传输率。

数据传输量仍将以字节为单位报告。

速率被报告为二进制单位，而不是SI单位。所以1 Mbit/s等于1,048,576 bit/s，而不是1,000,000 bit/s。

默认是 "bytes"。

### –suffix=SUFFIX

当使用 "同步"、"复制 "或 "移动 "时，任何会被覆盖或删除的文件将被加上后缀。 如果有一个相同路径的文件（在后缀被添加后），那么它将被覆盖。

使用的远程必须支持服务器端的移动或复制，而且你必须使用同一个远程作为同步的目的地。

这是在当前目录下或`--backup-dir`中使用文件添加后缀。更多信息见`--backup-dir`。

比如说

rclone copy -i /path/to/local/file remote:current --suffix .bak

将复制`/path/to/local`到`remote:current`，但对于任何已经更新或删除的文件都会添加.bak。

如果使用 "rclone sync "的"–后缀 "而不使用"–备份目录"，建议在过滤规则中排除后缀，否则 "同步 "将删除备份文件。

rclone sync -i /path/to/local/file remote:current --suffix .bak --exclude "*.bak"

### –suffix-keep-extension

当使用`--suffix`时，设置这个会使rclone把SUFFIX放在它所备份的文件的扩展名前面，而不是后面。

因此，假设我们有`--suffix -2019-01-01`，如果没有这个标志，`file.txt`将被备份为`file.txt-2019-01-01`，而有这个标志，它将被备份为`file-2019-01-01.txt`。 这对于确保后缀的文件仍然可以被打开是有帮助的。

### –syslog

在有能力的操作系统上（不是Windows或Plan9），将所有日志输出发送到syslog。

这对在脚本中运行rclone或`rclone mount`很有用。

### –syslog-facility string

指定rclone将用来存放临时文件的目录，以覆盖默认的目录。确保该目录存在并且有可访问的权限。

默认情况下，操作系统的临时目录将被使用： – 在Unix系统上，`$TMPDIR`如果非空，否则`/tmp`； – 在Windows上，`%TMP%`、`%TEMP%`、`%USERPROFILE%`中第一个非空值，或者Windows目录。

当用这个选项覆盖默认值时，在Unix系统上，指定的路径将被设置为环境变量`TMPDIR'的值，在Windows上则为`TMP’和`TEMP’。

你可以使用[config paths](https://rclone.cn/commands/rclone_config_paths/)命令来查看当前值。

### –temp-dir=DIR

指定rclone将用来存放临时文件的目录，以覆盖默认的目录。确保该目录存在并且有可访问的权限。

默认情况下，操作系统的临时目录将被使用： – 在Unix系统上，`$TMPDIR`如果非空，否则`/tmp`； – 在Windows上，`%TMP%`、`%TEMP%`、`%USERPROFILE%`中第一个非空值，或者Windows目录。

当用这个选项覆盖默认值时，在Unix系统上，指定的路径将被设置为环境变量`TMPDIR'的值，在Windows上则为`TMP’和`TEMP’。

你可以使用[config paths](https://rclone.cn/commands/rclone_config_paths/)命令来查看当前值。

### –tpslimit float

将每秒的交易量限制在这个数字。默认值是0，用于表示每秒无限制的交易。

交易大致上被定义为一个API调用；它的确切含义将取决于后端。对于基于HTTP的后端，它是一个HTTP PUT/GET/POST/等等及其响应。对于FTP/SFTP来说，它是一个通过TCP进行的往返交易。

例如，使用`--tpslimit 10`将rclone限制在每秒10个事务，或者使用`--tpslimit 0.5`每2秒一个事务。

当rclone每秒的交易数量导致云存储提供商出现问题时（例如，让你被禁止或速率限制），可以使用这个方法。

这对`rclone mount`非常有用，可以控制使用它的应用程序的行为。

这个限制适用于所有基于HTTP的后端以及FTP和SFTP后端。它不适用于本地后端或Storj后端。

参见`--tpslimit-burst`。

### –tpslimit-burst int

`--tpslimit`的最大交易突发数（默认为`1`）。

通常情况下，`--tpslimit`将精确地完成指定的每秒交易数。 然而，如果你提供了`--tps-burst`，那么rclone可以从空闲时保存一些事务，提供最多为所提供参数的突发。

例如，如果你提供`--tpslimit-burst 10`，那么如果rclone空闲的时间超过10*`-tpslimit`，那么它可以在再次被限制之前快速完成10个事务。

这可以用来提高`--tpslimit`的性能，而不改变每秒钟的长期平均交易数。

### –track-renames

默认情况下，rclone不会跟踪重命名的文件，所以如果你在本地重命名一个文件然后同步到远程，rclone会删除远程的旧文件并上传一个新的副本。

使用`--track-renames`的rclone同步就像正常的同步一样，但会跟踪那些存在于目的地但不存在于源端（通常会被删除）的对象，以及那些存在于源端但不存在于目的地（通常会被转移）的对象。 这些对象就成为重命名的候选对象。

在同步之后，rclone使用指定的`--track-renames-strategy`对仅有源对象和仅有目的对象进行匹配，并重新命名目的对象或转移源对象并删除目的对象。`--track-renames`是无状态的，就像所有rclone的同步。

要使用这个标志，目的地必须支持服务器端拷贝或服务器端移动，要使用基于哈希值的`--track-renames-strategy`（默认），源和目的地必须有一个兼容的哈希值。

如果目的地不支持服务器端拷贝或移动，rclone将退回到默认行为，并在控制台记录一个错误信息。

如果`---track-renames-strategy`包括`hash`，那么`---track-renames`目前不支持加密的目的地。

请注意，`--track-renames`与`--no-traverse`不兼容，它使用额外的内存来跟踪所有重命名候选者。

还要注意的是，`--track-renames`与`--delete-before`不兼容，它将选择`--delete-after`而不是`--delete-during`。

### –track-renames-strategy (hash,modtime,leaf,size)

这个选项改变了`---跟踪---重命名`的文件匹配标准。

匹配是由逗号分隔的这些标记的选择来控制的。

- `modtime` – 文件的修改时间 – 不是所有的后端都支持的
- `hash` – 文件内容的哈希值 – 不是所有的后端都支持的
- `leaf` – 文件的名称，不包括其目录名称
- `size` – 文件的大小（这个总是启用的）。

默认选项是`hash`。

使用`--track-renames-strategy modtime,leaf`会根据修改时间、文件名的叶子和大小来匹配文件。

使用`--track-renames-strategy modtime`或`leaf`可以使`--track-renames`支持加密的目的地。

注意，加密目的地不支持 "哈希 "策略。

### –delete-(before,during,after)

这个选项允许你在同步文件夹时指定目的地的文件何时被删除。

指定值"–delete-before "将删除目的地上的所有文件，但在开始传输任何新的或更新的文件之前，源文件上没有。这在文件系统中使用了两个通道，一个用于删除，一个用于复制。

指定`--delete-during`将在检查和上传文件时删除文件。这是最快的选项，使用最少的内存。

指定`--delete-after`（默认值）将延迟删除文件，直到所有新的/更新的文件被成功传输。 要删除的文件在复制过程中被收集，然后在复制过程成功完成后删除。 要删除的文件被保存在内存中，所以这种模式可能会使用更多的内存。 这是最安全的模式，因为它只在随后没有错误的情况下才会删除文件。 如果在开始删除之前有错误，那么你将得到 "由于有IO错误，所以不删除文件 "的消息。

### –fast-list

当做任何涉及到目录列表的事情时（例如：`sync',`copy’, `ls’-事实上几乎所有的命令），rclone通常会列出一个目录，并在使用更多的目录列表来处理任何子目录之前处理它。 这可以被并行化，并且使用最少的内存快速工作。

然而，有些远程有办法在一个（或少量）事务中列出一个目录下的所有文件。 这些往往是基于桶的远程（例如S3、B2、GCS、Swift）。

如果你使用`--fast-list`标志，那么rclone将使用这种方法来列出目录。 这将对列表产生以下后果。

- 它 **将** 使用少量流量（如果你付钱的话很重要）
- 它 **将** 使用更多的内存。 Rclone必须将整个列表加载到内存中。
- 它 _可能_ 更快，因为它使用较少的流量
- 它 _可能_ 更慢，因为它不能被并行化

rclone在使用和不使用`--fast-list`的情况下，结果应该是一样的。

如果你为交易付费，并且可以将整个同步列表放入内存，那么推荐使用`--fast-list`。 如果你有一个非常大的同步要做，那么不要使用`--fast-list`，否则你的内存就会耗尽。

如果你在一个不支持`--fast-list的远程设备上使用`–fast-list，那么rclone就会忽略它。

### –timeout=TIME

这设置了IO空闲超时。 如果一个传输已经开始，但在这个时间段内处于空闲状态，它将被视为中断并断开连接。

默认是`5m`。 设置为 "0 "表示禁用。

### –transfers=N

要并行运行的文件传输的数量。 如果远程有很多超时，把它设置成一个较小的数字有时是有用的，如果你有很多带宽和一个快速的远程，把它设置成一个较大的数字。

默认是并行运行4个文件传输。

如果你想控制单个文件的传输，请看 –多线程-流。

### -u, –update

这将迫使rclone跳过任何存在于目的地的文件，并且其修改时间比源文件新。

当传输到不直接支持修改时间的远程时（或者当使用`---use-server-modtime`以避免额外的API调用时），这对避免不必要的传输很有用，因为它比`---size-only`的检查更准确，比使用`---checksum`更快。在这样的远程（或当使用`--use-server-modtime`时），检查的时间将是上传的时间。

如果现有的目标文件的修改时间比源文件的修改时间早，如果大小不同，它将被更新。如果大小相同，如果校验和不同或不可用，它将被更新。

如果现有的目标文件的修改时间与源文件的修改时间相同（在计算的修改窗口内），如果大小不同，它将被更新。在这种情况下，除非提供`--checksum`标志，否则不会检查校验和。

在所有其他情况下，文件将不会被更新。

考虑使用`--modify-window`标志来补偿源和后端之间的时间偏差，对于不支持mod时间，而使用上传时间的后端。然而，如果后端不支持校验，注意在时间偏差窗口内同步或复制仍可能导致额外的传输，以保证安全。

### –use-mmap

如果这个标志被设置，那么rclone将使用由Unix平台上的mmap分配的匿名内存和Windows平台上的VirtualAlloc分配的传输缓冲区（大小由`-buffer-size`控制）。 像这样分配的内存不在Go heap上，当它用完后可以立即返回给操作系统。

如果没有设置这个标志，rclone将使用Go的内存分配器分配和释放缓冲区，这可能会使用更多的内存，因为内存页返回给操作系统的速度较慢。

这可能不是在所有的平台上都能很好的工作，所以默认是禁用的；将来可能会默认启用。

### –use-server-modtime

一些对象存储的后端（如Swift、S3）不保留文件修改时间（modtime）。在这些后端，rclone将原始的修改时间作为附加的元数据存储在对象上。默认情况下，当操作需要修改时间的时候，它会调用API来获取元数据。

使用这个标志可以禁用额外的API调用，而依靠服务器的修改时间。在使用`--update`从本地到远程同步的情况下，知道本地文件比最后上传到远程的时间要新就足够了。在这些情况下，这个标志可以加快进程，减少必要的API调用次数。

在没有使用`--update`的情况下，在同步操作中使用这个标志会导致所有在最后一次上传时间以外的任何时间修改的文件被再次上传，这可能不是你想要的。

### -v, -vv, –verbose

使用`-v`，rclone会告诉你每个被传输的文件和少量的重要事件。

使用`-vv`时，rclone将变得非常冗长，告诉你它考虑和传输的每个文件。 请在发送bug报告时附上此设置的日志。

当把verbosity设置为环境变量时，对`-v`和`-v`分别使用`RCLONE_VERBOSE=1`或`RCLONE_VERBOSE=2`。

### -V, –version

打印版本号

## SSL/TLS选项

rclone建立的外发SSL/TLS连接可以通过这些选项来控制。 例如，这对HTTP或WebDAV后端来说非常有用。Rclone HTTP服务器对SSL/TLS有自己的一套配置，你可以在他们的文档中找到。

### –ca-cert string

这将加载PEM编码的证书颁发机构的证书，并使用它来验证rclone所连接的服务器的证书。

如果你已经生成了用本地CA签名的证书，那么你将需要这个标志来连接到使用这些证书的服务器。

### –client-cert string

这将加载PEM编码的客户方证书。

这用于[相互TLS认证](https://en.wikipedia.org/wiki/Mutual_authentication)。

当使用这个标志时，也需要`--client-key`标志。

### –client-key string

这将加载用于相互TLS认证的PEM编码的客户端私钥。 与`--client-cert`一起使用。

### –no-check-certificate=true/false

`--no-check-certificate`控制客户端是否验证服务器的证书链和主机名。 如果`--no-check-certificate`为真，TLS接受服务器提供的任何证书和该证书中的任何主机名。 在这种模式下，TLS容易受到中间人的攻击。

这个选项的默认值是 "false"。

**这应该只用于测试。**

## 配置加密

你的配置文件包含登录你的云服务的信息。这意味着你应该把你的`rclone.conf`文件放在一个安全的地方。

如果你所处的环境不可能这样做，你可以在配置中添加一个密码。这意味着你必须在每次启动rclone时提供密码。

要给你的rclone配置添加密码，请执行`rclone config`。

|   |   |
|---|---|
||>rclone config|
||Current remotes:|
|||
||e) Edit existing remote|
||n) New remote|
||d) Delete remote|
||s) Set configuration password|
||q) Quit config|
||e/n/d/s/q>|

Go into `s`, Set configuration password:

|   |   |
|---|---|
||e/n/d/s/q> s|
||Your configuration is not encrypted.|
||If you add a password, you will protect your login information to cloud services.|
||a) Add Password|
||q) Quit to main menu|
||a/q> a|
||Enter NEW configuration password:|
||password:|
||Confirm NEW password:|
||password:|
||Password set|
||Your configuration is encrypted.|
||c) Change Password|
||u) Unencrypt configuration|
||q) Quit to main menu|
||c/u/q>|

你的配置现在被加密了，每次你启动rclone时，你都必须提供密码。在同一菜单中，你可以改变密码或完全取消配置的加密。

如果你丢失了密码，就没有办法恢复配置了。

rclone使用[nacl secretbox](https://godoc.org/golang.org/x/crypto/nacl/secretbox)，它又使用XSalsa20和Poly1305，用密匙加密法对你的配置进行加密和认证。密码经过SHA-256散列，产生secretbox的密钥。散列的密码不被储存。

虽然这提供了非常好的安全性，但如果你的加密的rclone配置包含敏感信息，我们不建议将其存储在公共场合，也许除非你使用非常强的密码。

如果在你的环境中是安全的，你可以设置`RCLONE_CONFIG_PASS`环境变量来包含你的密码，在这种情况下，它将被用于解密配置。

你可以通过脚本为一个会话设置这个密码。 对于类似unix的系统，将其保存在一个名为`set-rclone-password`的文件中。

|   |   |
|---|---|
||#!/bin/echo Source this file don't run it|
|||
||read -s RCLONE_CONFIG_PASS|
||export RCLONE_CONFIG_PASS|

然后在你想使用该文件时，将其作为源文件。 在shell中，你可以做`source set-rclone-password`。 然后它将询问你的密码并将其设置在环境变量中。

另一种提供密码的方法是提供一个脚本，它将检索密码并打印在标准输出上。 这个脚本应该有一个完全指定的路径名称，并且不依赖任何环境变量。 该脚本可以通过`--password-command="..."`命令行参数或`RCLONE_PASSWORD_COMMAND`环境变量提供。

一个有用的例子是使用`passwordstore`应用程序来检索密码。

export RCLONE_PASSWORD_COMMAND="pass rclone/config"

如果`passwordstore`密码管理器持有rclone配置的密码，使用脚本的方法意味着密码主要由`passwordstore`系统保护，而不会被嵌入到脚本中，也不能用标准的命令来检查。 在长期运行的rclone会话中，密码的副本很可能被无辜地捕获到日志文件或终端滚动缓冲区，等等。 使用脚本提供密码的方法，可以大大增强配置密码的安全性。

如果你在脚本中运行rclone，除非你使用`--password-command`方法，否则你可能想禁用密码提示。要做到这一点，可以向rclone传递参数`--ask-password=false`。如果`RCLONE_CONFIG_PASS`不包含一个有效的密码，并且`--password-command`没有被提供，这将使rclone失败而不是询问密码。

每当运行可能受配置文件中的选项影响的命令时，rclone会根据[上面](https://rclone.cn/docs.html#config-config-file)描述的规则寻找一个现有的文件，并加载任何它发现的文件。如果发现一个加密的文件，这包括解密它，可能的后果是出现密码提示。当执行一个命令行时，你知道实际上没有使用这样一个配置文件的任何东西，你可以通过覆盖位置来避免它被加载，例如，用文件中的一个特殊值用于仅有内存的配置。由于只有后端选项可以存储在配置文件中，所以对于不对后端进行操作的命令，例如`genautocomplete'，这通常是不必要的。然而，对于那些通常对后端进行操作，但不参考存储的远程的命令，例如列出本地文件系统的路径，或[连接字符串](#connection-strings)，它将是相关的。`rclone –config="" ls .`

## 开发商的选择

这些选项在开发或调试rclone时非常有用。 还有一些更具体的远程选项，这里没有记录，用于测试。 这些选项以远程名称开头，例如：`--drive-test-option`–见相关远程的文档。

### –cpuprofile=FILE

将CPU配置文件写入文件。 这可以用 "go tool pprof "进行分析。

#### –dump flag,flag,flag

`--dump`标志需要一个逗号分隔的标志列表，以转储相关信息。

请注意，如果go标准库的自动gzip编码是有效的，那么包括`Accept-Encoding'在内的一些头信息在请求中可能是不正确的，响应中可能不会显示`Content-Encoding’。在这种情况下，请求的主体将在显示之前被压缩。

可用的标志是：。

#### –dump headers

倾倒HTTP头文件，删除 "授权："行。可能仍然包含敏感信息。 可以是非常冗长的。 只对调试有用。

如果你想得到 "授权："头信息，请使用`--dump auth`。

#### –dump bodies

倾倒HTTP头和正文 – 可能包含敏感信息。 可以是非常冗长的。 只对调试有用。

注意，主体是在内存中缓冲的，所以不要把它用于巨大的文件。

#### –dump requests

像`--dump bodies`一样，但会转储请求体和响应头信息。 对于调试下载问题很有用。

#### –dump responses

像`--dump bodies`一样，但会转储响应体和请求头信息。对于调试上传问题很有用。

#### –dump auth

转储HTTP头文件 – 将包含敏感信息，如`授权：`头文件 – 使用`--转储头文件`来转储没有`授权：`头文件。 可以非常冗长。 只对调试有用。

#### –dump filters

倾倒过滤器到输出。 这对了解包括和排除选项的确切过滤内容很有用。

#### –dump goroutines

这将在命令的最后跳出一个正在运行的go-routines的列表到标准输出。

#### –dump openfiles

这在命令的最后转储了一个打开的文件的列表。 它使用`lsof`命令来做，所以你需要安装该命令来使用它。

### –memprofile=FILE

将内存配置文件写入文件。这可以用 "go tool pprof "进行分析。

## 筛选

对于过滤选项

- `--delete-excluded`
- `--filter`
- `--filter-from`
- `--exclude`
- `--exclude-from`
- `--exclude-if-present`
- `--include`
- `--include-from`
- `--files-from`
- `--files-from-raw`
- `--min-size`
- `--max-size`
- `--min-age`
- `--max-age`
- `--dump filters`
- `--metadata-include`
- `--metadata-include-from`
- `--metadata-exclude`
- `--metadata-exclude-from`
- `--metadata-filter`
- `--metadata-filter-from`

见[过滤部分]（/filtering.html）。

## 远程控制

关于远程控制选项和如何远程控制rclone的说明

- `--rc`
- and anything starting with `--rc-`

见[远程控制部分]（/rc.html）。

## log

rclone有4个级别的日志：`ERROR`，`NOTICE`，`INFO`和`DEBUG`。

默认情况下，rclone会记录到标准错误。 这意味着你可以重定向标准错误，仍然可以看到rclone命令的正常输出（例如，`rclone ls`）。

默认情况下，rclone会产生`错误`和`通知`级别的信息。

如果你使用`-q`标志，rclone将只产生`错误’信息。

如果你使用`-v`标志，rclone将产生`错误'、`通知’和`信息’消息。

如果你使用`-vv`标志，rclone将产生`错误`、`通知`、`信息`和`调试`消息。

你也可以用`--log-level`标志来控制日志级别。

如果你使用`--log-file=FILE`选项，rclone将把`错误'、`信息’和`调试’信息和标准错误一起重定向到FILE。

如果你使用`--syslog`标志，那么rclone将记录到syslog，`--syslog-facility`控制它使用哪个设施。

Rclone在所有的日志信息前都用大写字母标明其级别，例如INFO，这使得它很容易在日志文件中搜索不同种类的信息。

## 退出代码

如果在命令执行过程中发生任何错误，rclone将以非零的退出代码退出。 这使得脚本可以检测到rclone操作失败的情况。

在启动阶段，如果在配置中检测到一个错误，rclone将立即退出。 在退出之前总是会有一条日志信息。

当rclone运行时，它将在运行过程中积累错误，并且只有在（重试之后）仍然有失败的传输时，才会以非零退出代码退出。 对于每一个被计算的错误，都会有一个高优先级的日志信息（用`-q`可见），显示信息和导致问题的文件。在开始重试时，也会显示一个高优先级的信息，所以用户可以看到任何以前的错误信息在重试后可能无效了。如果rclone已经做了重试，如果重试成功，它将记录一个高优先级的信息。

### 退出代码列表

- `0` – 成功
- `1` – 语法或用法错误
- `2` – 未归类的错误
- `3` – 未找到目录
- `4` – 未找到文件
- `5` – 暂时性错误（更多的重试可能会修复）（重试错误）。
- `6` – 不太严重的错误（如来自dropbox的461个错误）（NoRetry错误）。
- `7` – 致命的错误（更多的重试也无法解决的错误，如账户被暂停）（致命的错误）。
- `8` – 转移超过了 –max-transfer所设定的限制。
- `9` – 操作成功，但没有传输文件

## 环境变量

Rclone可以完全使用环境变量进行配置。 这些变量可以用来为选项或配置文件条目设置默认值。

### 选择

rclone中的每个选项都可以通过环境变量设置其默认值。

要找到环境变量的名称，首先，取长的选项名称，去掉前面的`--`，将`-`改为`_`，大写，并在前面加上`RCLONE_`。

例如，如果要总是设置"–统计5s"，可以设置环境变量 "RCLONE_STATS=5s"。 如果你在命令行上设置统计，这将覆盖环境变量的设置。

或者为了总是使用驱动器中的垃圾`--驱动器使用垃圾`，设置`RCLONE_DRIVE_USE_TRASH=true`。

口令略有不同，相当于`--verbose`或`-v`的环境变量是`RCLONE_VERBOSE=1`，或者对于`-vv`，`RCLONE_VERBOSE=2`。

选项和环境变量使用相同的解析器，因此它们的形式完全相同。

环境变量设置的选项可以用`-vv`标志查看，例如`rclone version -vv`。

### 配置文件

你可以在单个远程的基础上为配置文件中的值设置默认值。配置项的名称在每个后端页面中都有记录。

为了找到环境变量的名称，你需要设置，取`RCLONE_CONFIG_`+远程的名称+`_`+配置文件选项的名称，并使其全部大写。

例如，在没有配置文件的情况下，配置一个名为`mys3:`的S3远程（使用unix的方式设置环境变量）。

|   |   |
|---|---|
||$ export RCLONE_CONFIG_MYS3_TYPE=s3|
||$ export RCLONE_CONFIG_MYS3_ACCESS_KEY_ID=XXX|
||$ export RCLONE_CONFIG_MYS3_SECRET_ACCESS_KEY=XXX|
||$ rclone lsd mys3:|
||-1 2016-09-21 12:54:21        -1 my-bucket|
||$ rclone listremotes \| grep mys3|
||mys3:|

注意，如果你想使用环境变量来创建一个远程，你必须像上面那样创建`..._TYPE`变量。

请注意，使用环境变量创建的远程名称是不区分大小写的，这与[上面](https://rclone.cn/docs.html#valid-remote-names)所记录的存储在配置文件中的常规远程不同。  
你必须在环境变量中用大写字母写名字，但从上面的例子可以看出，它将被列出，并可以用小写字母访问，而你也可以用大写字母指代同一个远程。

|   |   |
|---|---|
||$ rclone lsd mys3:|
||-1 2016-09-21 12:54:21        -1 my-bucket|
||$ rclone lsd MYS3:|
||-1 2016-09-21 12:54:21        -1 my-bucket|

注意，你只能设置直接的后端选项，所以RCLONE_CONFIG_MYS3CRYPT_ACCESS_KEY_ID没有作用，如果myS3Crypt是一个基于S3远程的加密远程。然而RCLONE_S3_ACCESS_KEY_ID将设置所有使用S3的远程的访问密钥，包括myS3Crypt。

还要注意的是，现在rclone有了[连接字符串](https://rclone.cn/docs.html#connection-strings)，使用这些字符串可能更容易，这使得上面的例子

rclone lsd :s3,access_key_id=XXX,secret_access_key=XXX:

### 优先权

后台配置的各种不同方法是按这个顺序读取的，并使用第一个有数值的方法。

- 连接字符串中的参数，例如：`myRemote,skip_links:`。
- 在命令行中提供的标志值，例如`--skip-links`。
- 远程特定的环境变量，例如`RCLONE_CONFIG_MYREMOTE_SKIP_LINKS`（见上文）。
- 后台特定的环境变量，例如`RCLONE_LOCAL_SKIP_LINKS`。
- 后台通用环境变量，例如`RCLONE_SKIP_LINKS`。
- 配置文件，例如：`skip_links = true`。
- 默认值，例如 "false"–这些不能被改变。

因此，如果在命令行上同时提供`--skip-links`和环境变量`RCLONE_LOCAL_SKIP_LINKS`被设置，命令行标志将被优先考虑。

通过环境变量设置的后端配置可以用`-vv`标志查看，例如`rclone about myRemote: -vv`。

对于非后端配置，顺序如下。

- 在命令行中提供的标志值，例如`--stats 5s`。
- 环境变量，例如：`RCLONE_STATS=5s`。
- 默认值，例如`1m`–这些不能改变。

### 其他环境变量

- `RCLONE_CONFIG_PASS`设置为包含你的配置文件密码（见[配置加密](https://rclone.cn/docs.html#configuration-encryption)部分） – `HTTP_PROXY`、`HTTPS_PROXY`和`NO_PROXY`（或其小写版本）。
    - `HTTPS_PROXY`优先于`HTTP_PROXY`用于https请求。
    - 环境值可以是一个完整的URL，也可以是一个 "host[:port]"，在这种情况下，会假定 "http "方案。
- `USER'和`LOGNAME’值被用来作为当前用户名的后备值。查询用户名的主要方法是针对操作系统的。Windows上的Windows API，Unix系统上/etc/passwd中的真实用户ID。在文档中，当前用户名被简单地称为`$USER`。
- `RCLONE_CONFIG_DIR` – rclone **设置**这个变量，在配置文件和子进程中使用，指向存放配置文件的目录。

环境变量设置的选项可以通过`-vv`和`-log-level=DEBUG`标志看到，例如`rclone version -vv`。