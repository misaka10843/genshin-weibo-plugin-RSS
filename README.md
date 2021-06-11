# genshin-weibo-plugin-RSS
OPQBot的一个原神微博获取插件（RSS版）
## 前置
请按照以下命令安装python依赖（此仓库支持python2.7+）
```python
pip install beautifulsoup4
pip install lxml
pip install html5lib
```
如果还有提示比如```ModuleNotFoundError: No module named 'name'```这种的还请自行百度qwq
因为是使用的php来解析xml文件，所以还请安装php（版本最好是7.3-7.4）
如果是Windows系统还请安装wget并且配合系统变量（不是用户变量）
## 运行解析
首先运行```python main.py``` 后，python会使用wget拉取原神的RSS订阅，然后在使用os命令运行```php getRSS.php```来让php解析xml并且将数据分包，因为防止QQ因为文字过长无法发送，所以我们使用PIL来将文字转换成图片进行发送。

## 后言
此仓库还并未开发完成，还请不要提前拉取qwq，我们会使用lua作为发送的脚本，所以理应来说lua的脚本才是这个插件的本体qwq

### README统计
![统计](https://count.getloli.com/get/@misaka10843?theme=elbooru)
