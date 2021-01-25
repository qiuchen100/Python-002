# 作业详情

### 作业文件夹：

### 作业一代码及文件：

### 作业二代码目录：



# 学习笔记


### 第一节
* 异常不完全等于错误：错误更多指程序错误，异常通常指因用户输出或者系统输入输出产生的意想不到结果
* 异常可以捕获，对异常对捕获可以提升程序对健壮性
* Traceback从上往下去找异常，最下边显示异常详情
* 异常可以嵌套，包住内部的except部分
* Exception和BaseException：所有的异常都继承自BaseException，自定义异常需要继承Exception

```bash
#  安装美化异常工具包
pip install pretty_errors 
```

### 第二节
```bash
#  安装Mysql连接器
pip install pymysql
```
* 学会F12进去看源码
* Type Hint
* 更好的操作数据库方式 ORM

### 第三节
* 爬虫做的事归根结底就说模拟浏览器
* 反爬虫比较简单的几种：（1）模拟器请求头的User-Agent和正常浏览器不一致；（2）和正常用户行为不一样。
```bash
# 安装fake-useragent 来提供随机的User-Agent
pip install fake-useragent
```
* 除了注意User-Agent，还需要注意Referer、Host的信息，爬虫的Header里面最好补全

### 第四节
* 爬虫做的事归根结底就说模拟浏览器，经常需要模拟用户登录。
* Post Cookies来完全模拟浏览器请求，所有的参数务必完整，避免被识别出爬虫。

### 第五节
* 使用webdriver来完整模拟浏览器行为
* 对于有些动态内容（JS加载）的内容，用requests无法解决，需要借助webdriver
```bash
# 安装selenium 完整模拟浏览器的行为
pip install selenium
# 然后下载chromedriver，存放到虚拟环境所在的bin目录即可
```

### 第六节
* 验证码识别
```bash
# 安装依赖库 libpgn, jpeg, libtiff, leptonica
brew install leptonica
# 安装tesseract
brew install tesseract
# 安装python对接需要安装的包
pip install Pillow
pip install pytesseract
```

### 第七节
* 代理IP
```bash
export http_proxy='http://52.179.231.206:80'
# setting 增加 scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware
# 通过Request.meta['proxy']读取http_proxy环境变量加载代理
```

### 第八节
* 随机代理IP
```bash
export http_proxy='http://52.179.231.206:80'
# setting 增加 scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware
# 通过Request.meta['proxy']读取http_proxy环境变量加载代理
```