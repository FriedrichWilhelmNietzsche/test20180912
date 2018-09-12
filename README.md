# test20180912
python3+selenium+autoit


dediprog.py

Selenium 的定位元素操作:

Selenium 提供了 8 种的定位元素方法，百度首页作为例子

1 find_element_by_id()         通过 ID 查找元素，也就是使用页面里的 id 属性:id = “”

2 find_element_by_name()                 通过查找名字的方式，属性:name=””

3 find_elements_by_class_name()            通过查找 class_name 的方式

4 find_element_by_tag_name()                 通过元素的标签属性对元素进行定位，在检查元素的时候查看元素的最前面的 input，很多页面都有同样的标签存在,不推荐使用

5 find_element_by_link_text()              通过查找页面的文本信息进行定位 

6 find_element_by_partial_link_text()        通过模糊文本信息查找元素

7 find_element_by_xpath()                 通过查找元素的路径去查找元素

8 find_element_by_css_selector()             通过复制粘贴的方式进行定位


upload

打开 Autolt Window Info(x64)

pycharm 里创建一个命名为 “upload” 的 HTML

使用 autolt 工具来定位窗口的位置，拖动Finder Tool圆点

将移动到的位置的信息记录下来，点击 Control 可以看到信息窗口的 title 为 “打开”，标题的 Class 为 “#32770”。

文件名输入框的 class 为 “Edit”，Instance 为 “1” ，所以 ClassnameNN 为 “Edit1”。打开按钮的 class 为 “Button”，Instance 为 “1” ，所以 ClassnameNN 为 “Button1”

打开 SciTE Script Editor 编辑脚本信息

将 upload.txt 文件放在我们的自动化测试脚本里面，再去修改我们脚本的路径 ControlSetText(“ 打开 “, “”, “Edit1”, @WorkingDir & “ \file\upload.txt”)

编辑好了脚本信息了，保存我们的文件，会生成 .au 的文件，但是这个文件不是我们想要的，我们要得到的是 .exe 的文件，打开 Compile Script to .exe(x64) 文件，将 .au 的文件转换成 .exe 文件就可以了

点击 Convert 就 ok 了，在当前文件夹下我们就可以看到生成的 .exe 文件

新建命名为 uploadfile 的 python 文件


