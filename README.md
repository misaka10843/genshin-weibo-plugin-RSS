# genshin-weibo-plugin-RSS
OPQBot的一个原神（可以替换成其他人的微博RSS链接）微博获取插件（RSS版），但是核心文件是可以支持任何一个QQ机器人框架以及调用（因为核心文件是获取内容后文字转成图片），

这样只要框架能支持发送图片，即可使用本插件

## 使用语言及平台💭
<br>
<p align="center">
<img src="https://avatars.githubusercontent.com/u/69132853?s=120&v=4"/>
</p>

<p align="center">
  本仓库默认支持的OPQBot框架需要：<br><br>
  <img src="https://img.shields.io/badge/Python-2.7+-326c9c?logo=Python&logoColor=326c9c"/>
  <img src="https://img.shields.io/badge/PHP-7.3+-777bb3?logo=PHP&logoColor=777bb3"/>
  <img src="https://img.shields.io/badge/Lua-5.0-000080?logo=Lua&logoColor=000080"/>
  <img src="https://img.shields.io/badge/Shell(bash/sh)-1.0-3e484a?logo=GNU%20Bash&logoColor=ffffff"/>
  <br><br>
  如果使用其他的框架的话可以无视&nbsp&nbsp&nbsp<img src="https://img.shields.io/badge/Lua-5.0-000080?logo=Lua&logoColor=000080"/>&nbsp&nbsp&nbsp，但是需要您使用框架的插件语言qwq
</p>
 <hr>
 <br>
 <br>
 <p align="center">
其中，本仓库默认支持的OPQBot框架不支持以下系统：<br><br>
<img src="https://img.shields.io/badge/Android--0?style=social&logo=Android&logoColor=3DDC84"/>
<img src="https://img.shields.io/badge/Windows10--0?style=social&logo=Windows&logoColor=0078D6"/>
<img src="https://img.shields.io/badge/IOS--0?style=social&logo=IOS&logoColor=black"/>
</p>
 <p align="center">
但是支持&nbsp&nbsp&nbsp<img src="https://img.shields.io/badge/Android--0?style=social&logo=Android&logoColor=3DDC84"/><img src="https://img.shields.io/badge/Windows10--0?style=social&logo=Windows&logoColor=0078D6"/>&nbsp&nbsp&nbsp的Linux模拟器
</p>



## 前置💨
请按照以下命令安装python依赖（此仓库支持python2.7+）
```python
pip install beautifulsoup4
pip install lxml
pip install html5lib
```
如果还有提示比如```ModuleNotFoundError: No module named 'name'```这种的还请自行百度qwq

因为是使用的php来解析xml文件，所以还请安装php（版本最好是7.3-7.4，Windows请配置php的系统变量（不是用户变量））

如果是Windows系统还请安装wget并且配置系统变量（不是用户变量）

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
