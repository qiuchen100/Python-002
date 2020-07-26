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
```python
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
```python
import requests
from bs4 import BeautifulSoup
'''
拿到网页html源代码
'''
resp = requests.get(url, headers=header)
'''
对html源码内容做解析，提取需要对信息
'''
content_parse_info = BeautifulSoup(resp.text, 'html.parser')
movies = content_parse_info.find_all('div', attrs={'class': 'hd'})
```

### 第三节
* XPath也是一种解析并提取html源代码的工具包，它比beautifulsoup要高效。
```bash
#  安装依赖包
pip install lxml
```
* 具体用法
```python
import requests
import lxml.etree
'''
拿到网页html源代码
'''
resp = requests.get(url, headers=header)
'''
对html源码内容做解析，提取需要对信息
'''
selector = lxml.etree.HTML(resp.text)
# xpath的路径可以在浏览器按F12，鼠标选择需要提取的元素，并右键得到。
film_name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
```

### 第四节
* 翻页关键代码
```python
items_per_page = 25
urls = tuple(f'https://movie.douban.com/top250?start={items_per_page * page}' for page in range(10))
```

### 第五节
* 数据结构：字符串，元组，列表，字典，集合
* 流程控制：if--else--； for .. in, 包括break和continu还有else字句
* 类和实例的关系
* 函数

### 第六节 & 第七节
* HTTP协议与浏览器的关系
  1. 重要的两个协议HTTP协议和TCP协议
  2. 浏览器通过解析HTTP协议的内容，来给用户呈现信息。
  3. HTML CSS JS这三个部分组成了网页的基本元素，分别表示结构，样式和行为。
* Request Header
  1. 客户端（浏览器）可以对web server发起请求，请求的相关信息可以放在Request Header中。
  2. 与爬虫相关: Request URL, Status Code, Request Method
  3. 具体头部: cookies, User-Agent
* 请求方式get post
  1. 点击页面 get
  2. 登录 post
* HTTP状态码
  1. 2xx 成功
  2. 5xx 4xx 失败
* W3C标准
* HTML常用标签和属性
  1. span a img
* CSS，JS和JSON

### 第八节
* Scarpy是一个流行的，成熟的，并集成了满足爬虫各种功能的框架。
* Scrapy核心组件
  1. 引擎（无需修改）
  2. 调度器（无需修改）
  3. 下载器（无需修改）
  4. 爬虫（按需开发）
  5. 项目管道（按需开发）
  6. 下载器中间件
  7. 爬虫中间件

### 第九节
```bash
#  安装依赖包
pip install scrapy
#  构建项目
scrapy startproject crawler
cd crawler
scrapy genspider movies douban.com
```
* 目录结构
  1. 实现爬虫的Python文件：spiders目录
  2. 项目的设置文件：setting.py
  3. 项目的配置文件：scrapy.cfg
  4. 定义所爬去记录的数据结构：items.py
  5. 编写爬虫逻辑：moives.py
  6. 设置保持位置：pipelines.py

### 第十节
* 重要逻辑
  1. settings.py打开USER_AGENT，并设定好DOWNLOAD_DELAY
  2. 爬虫代码设定好起始url，并设定好允许爬取的域名范围（一定不能出错）。重写parse方法，返回items即可。这里只是提取信息交给下游管道处理，其本身并不直接对爬取内容做处理
  3. items.py设定好爬取的每一项信息字段。
  4. pipelines.py负责具体对爬取结果对处理逻辑。
  5. 运行爬虫命令：<code>scrapy crawl movies</code>

### 第十一节
* 重要逻辑
  1. 如果还需要对爬取到对信息进一步深层爬取提取内容，那就在process方法中不返回item，而是发给下游对parse方法来解决，如：
  ```python
  yield scrapy.Request(link, meta={'item': item}, callback=self.parse2)
  ```
  2. 在pipelines中对item做处理，比如保存到文件中。但是需要同时主要两点
     1. 方法最后必须返回item，否则程序会抛异常。
     2. 需要在settings中打开pipelines的注册信息，并确保该pipeline注册进去了。

### 第十二节
* 重要逻辑

## 第十三节
* yield和return都可以做为函数都返回语句，yield可以根据需要一个一个值单独返回。
* 推导式一般用于生成一个新的列表，字典，集合。创建方式非常简洁。