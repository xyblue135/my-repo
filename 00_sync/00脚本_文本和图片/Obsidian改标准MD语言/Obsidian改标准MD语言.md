# 为什么需要更改
众所周知,我们在使用obsidian编辑笔记的时候,如果我们需要粘贴图片,它所链接的并不是一个标准的MD语言的图片.
![image-202312115531544.png](00_sync/00脚本_文本和图片/Obsidian改标准MD语言/Obsidian改标准MD语言/image-202312115531544.png)
![image-20231211012958.png](00_sync/00脚本_文本和图片/Obsidian改标准MD语言/Obsidian改标准MD语言/image-20231211012958.png)
这就导致我们在如果需要需要在本地编辑笔记,或者typora用户感觉到不适应的话,以及上传到个人博客的时候还要改格式(改为标准MD语言以及删除空格等),这是非常难受的,即使使用py脚本进行更改也比较繁琐,那么还是建议在使用obsidian写笔记的时候就默认粘贴为标准的MD语言的格式就好了.
# 下载
所以我们借助开源obsidian插件来完成这个的更改
https://github.com/ostoe/Ob-ImagePastePlugin
# 使用
别忘记打开
![image-20231211212525.png](00_sync/00脚本_文本和图片/Obsidian改标准MD语言/Obsidian改标准MD语言/image-20231211212525.png)
然后我们使用snipaste软件的截图粘贴就可以是标准的md语言格式了
![image-20231211253294.png](00_sync/00脚本_文本和图片/Obsidian改标准MD语言/Obsidian改标准MD语言/image-20231211253294.png)
```
分割
```
![image-20231211726218.png](00_sync/00脚本_文本和图片/Obsidian改标准MD语言/Obsidian改标准MD语言/image-20231211726218.png)
# 特别注意
如果你的文档和附件是这样的链接格式,这是比较推荐的,这个时候我们修改文件夹名test为test55555的时候,相应的test.md里面的所链接的附件也会同步更改.
![image-202312111246331.png](00_sync/00脚本_文本和图片/Obsidian改标准MD语言/Obsidian改标准MD语言/image-202312111246331.png)
![image-20231211165696.png](00_sync/00脚本_文本和图片/Obsidian改标准MD语言/Obsidian改标准MD语言/image-20231211165696.png)
但相应的,如果直接修改文档的名字的话,我们再粘贴照片的话就又会创建一个文件夹来存储我们后面放入的图片.
![image-202312111945473.png](00_sync/00脚本_文本和图片/Obsidian改标准MD语言/Obsidian改标准MD语言/image-202312111945473.png)
也就是说,如果你感觉标题不对了,编辑好了想修改标题,建议文档和文件夹同时修改为一样的名字,以便于后续的更新以及其它操作.
# 个人推荐
而如果你是像我这样管理文件的话.
![image-202312112416273.png](00_sync/00脚本_文本和图片/Obsidian改标准MD语言/Obsidian改标准MD语言/image-202312112416273.png)
除了第一次需要创建文件夹繁琐一点?其它的我个人感觉挺舒服的,但也要考虑注意事项,但也算是不容易混的吧.我个人比较喜欢这种管理方式.
# 放入网站
有些博客是可以和obsidian的文件同步的,需要配置配置,我这边就不用了.大家知道就好.然厚找个文本编辑器ctrl+h替换掉你本地的路径和网站上的路径即可简略很多步骤了.
![image-20231211277321.png](00_sync/00脚本_文本和图片/Obsidian改标准MD语言/Obsidian改标准MD语言/image-20231211277321.png)
# 更改非标准MD语言
此插件还提供了可以将非标准的MD改为标准的MD语言的选项,我们在我们的文档页使用ctrl+p,然后搜
```
reconstrut-image
```
就可以非标准的MD语言改为标准的MD语言了.
![image-202312113026942.png](00_sync/00脚本_文本和图片/Obsidian改标准MD语言/Obsidian改标准MD语言/image-202312113026942.png)
![image-202312113042658.png](00_sync/00脚本_文本和图片/Obsidian改标准MD语言/Obsidian改标准MD语言/image-202312113042658.png)
![image-202312113124862.png](00_sync/00脚本_文本和图片/Obsidian改标准MD语言/Obsidian改标准MD语言/image-202312113124862.png)
不用在意这些乱七八操的字符,目前也不知道什么bug,手动改名上级文件夹,再改回来就会显示正常了,但不改也没事,可以看到vscode和typora都是可以正常加载的就没有问题.
![image-202312113552388.png](00_sync/00脚本_文本和图片/Obsidian改标准MD语言/Obsidian改标准MD语言/image-202312113552388.png)
![image-202312113625803.png](00_sync/00脚本_文本和图片/Obsidian改标准MD语言/Obsidian改标准MD语言/image-202312113625803.png)
