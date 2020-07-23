# 学习笔记

### 基础环境准备
```bash
# 安装python虚拟环境
pip3 install virtualenv
virtualenv ~/venv
# 激活python虚拟环境
source ~/venv/bin/activate
#  安装依赖包
pip install requests 
```

### 第一节
* requests是一个很方便的发起HTTP请求，并获得响应的Python工具包
``` python
url = 'https://movie.douban.com/top250?start=0'
header = {}
header['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
resp = requests.get(url, headers=header)
```
如上所示，它可以让我们的python程序伪装成一个浏览器，去访问网站，并获得响应。

### 第二节
* requests可以获取网页的html源代码，beautifulsoup可以对html源代码进行解析来获取我们需要的信息。
```bash
#  安装依赖包
pip install beautifulsoup4
```
* 采用如下方式解析html
``` python
import requests
from bs4 import BeautifulSoup
'''
拿到网页html源代码
'''
resp = requests.get(url, headers=header)
'''
拿到网页html源代码
'''

```

### 第三节
```bash
#  安装依赖包
pip install lxml
```