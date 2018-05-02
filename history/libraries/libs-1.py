# 常用第三方模块

# 除了内建的模块外，Python还有大量的第三方模块。

# 基本上，所有的第三方模块都会在PyPI - the Python Package Index上注册，只要找到对应的模块名字，即可用pip安装。

# 此外，在安装第三方模块一节中，我们强烈推荐安装Anaconda，安装后，数十个常用的第三方模块就已经就绪，不用pip手动安装。

# 本章介绍常用的第三方模块。

# Pillow

# PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库了。PIL功能非常强大，但API却非常简单易用。

# 由于PIL仅支持到Python 2.7，加上年久失修，于是一群志愿者在PIL的基础上创建了兼容的版本，名字叫Pillow，支持最新Python 3.x，又加入了许多新特性，因此，我们可以直接安装使用Pillow。

# 安装Pillow
# 如果安装了Anaconda，Pillow就已经可用了。否则，需要在命令行下通过pip安装：

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# WechatIMG10.jpeg

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('libraries/WechatIMG10.jpeg')
# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
# im2.save('weixin.jpg', 'jpeg')


# 随机字母:
def randomChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 60 * 4
height = 60

image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())

# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), randomChar(), font=font, fill=rndColor2())

# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')




