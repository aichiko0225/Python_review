from collections import namedtuple, defaultdict, OrderedDict
from tkinter import Frame, Button, Label

Point = namedtuple('Point', ['x', 'y'])

p = Point(11, 22)
print(p)

defalutD = defaultdict(lambda: 'N/A')

print(defalutD['key'])

# 如果要保持Key的顺序，可以用OrderedDict：

d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)

od = OrderedDict([('a', 1), ('c', 3), ('b', 2)])
print(od)

# 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：

# 图形界面
# Python支持多种图形界面的第三方库，包括：
# Tk
# wxWidgets
# Qt
# GTK
# 等等。

# 但是Python自带的库是支持Tk的Tkinter，使用Tkinter，无需安装任何包，就可以直接使用。本章简单介绍如何使用Tkinter进行GUI编程。
# Tkinter
# 我们来梳理一下概念：
# 我们编写的Python代码会调用内置的Tkinter，Tkinter封装了访问Tk的接口；
# Tk是一个图形库，支持多个操作系统，使用Tcl语言开发；
# Tk会调用操作系统提供的本地GUI接口，完成最终的GUI。
# 所以，我们的代码只需要调用Tkinter提供的接口就可以了。


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()


app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()
