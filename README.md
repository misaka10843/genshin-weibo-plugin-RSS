# genshin-weibo-plugin-RSS
OPQBot的一个原神微博获取插件（RSS版）

## 前置💨
请按照以下命令安装python依赖（此仓库支持python2.7+）
```python
pip install beautifulsoup4
pip install lxml
pip install html5lib
```
如果还有提示比如```ModuleNotFoundError: No module named 'name'```这种的还请自行百度qwq

因为是使用的php来解析xml文件，所以还请安装php（版本最好是7.3-7.4）

如果是Windows系统还请安装wget并且配合系统变量（不是用户变量）

## 运行解析💬
首先运行```python main.py``` 后，python会使用wget拉取原神的RSS订阅，

然后在使用os命令运行```php getRSS.php```来让php解析xml并且将数据分包，

因为防止QQ因为文字过长无法发送，

所以我们使用PIL来将文字转换成图片进行发送。

## 文件生成👀
我们会生成一些文件来供解析以及消息发送
下面是文件生成的列表
```
rss.out
time.out
url.out
txt.png
```
## 文件用途😺

```
bg.png
font.ttf
```
这两个文件是python的文字转图片用到的字体文件和背景图片，你可以修改或替换这些文件来个性化

但是需要注意的是，图片的分辨率虽然不需要注意，但是如果分辨率过小的话可能不会显示全部文字，

而且请注意，替换了图片后还请将图片分辨率-80px（比如```1200px(原图片宽度)-80px=1120px(实际文字一行的宽度)```）

并且记住得到的分辨率后修改main.py中```self.width = 1100```的1100（无须填写单位）

<hr>

```
main.py
getRSS.php
```
这两个文件是核心文件，如果没有必要请不要修改，

如果想个性化生成的图片的话也最好只修改main.py，并且按照文件中的注解来修改对应的参数（小白的话还请不要随便改qwq）

## 后言✨
此仓库还并未开发完成，还请不要提前拉取qwq，我们会使用lua作为发送的脚本，所以理应来说lua的脚本才是这个插件的本体qwq


## README统计🎶
![统计](https://count.getloli.com/get/@misaka10843?theme=elbooru)
