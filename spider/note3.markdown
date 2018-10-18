

# 学习爬虫 Spite

# 参考资料
 - 《Python网络数据采集》
 - 精通Python爬虫框架Scrapy
 - python网络爬虫 CSDN

# 前提知识
 - URL
 - HTTP协议
 - WEB前端技术：HTML CSS JS XML
 - ur

# 1.爬虫简介
- 是一种按照一定的规则，自动地抓取万维网信息的程序或者脚本
- 两大特性
    - 能够按照作者的要求，下载特定的数据或者内容
    - 能自动在网络上流窜 
- 三大步骤
    - 下载网页
    - 提取正确信息
    - 根据一定的规则自动跳转到另外的网页上执行上面两个步骤
- 爬虫的分类
    - 通用爬虫：爬行对象从一些种子 URL 扩充到整个 Web，主要为门户站点搜索引擎和大型 Web 服务提供商采集数据。
              各大搜索引擎把全网信息存储到自己的服务器，提供链接信息给用户。
    - 聚焦爬虫：专用爬虫，选择性地爬行那些与预先定义好的主题相关页面。
- Python网络包简介

    - Python3.x : urllib , urllib3 ,httplib2 ,requests
    
# 2.urllib（URL lib)
- 包含模块：
  - urllib.request:打开和读取URL
  - urllib.error:包含产生的错误，使用try捕捉
  - urllib.robotparse:解析robots.txt
- 网页编码问题的解决
  - chardet 可以自动检测页面文件的编码格式
- urlopen 的返回对象
  - geturl:返回请求对象的url
  - info:请求反馈对象的meta信息
  - getcode:返回的http code
- request.date 的使用
  - 访问网络的两种方法:往服务器扔数据
    - get：
       - 利用参数给服务器传递数据，
       - 参数为字典dict
       - 要使用parse进行转码，不然服务器拒绝，即便看起来一样
    - post：
       - 一般向服务器传递参数使用post方法
       - post是把信息自动加密处理
       - 如果使用post信息，需要用到data参数
       - 使用post，意味着http的请求头可能需要更改：
          ① content-type：application/x-www.form-urlencode
          ② content-length:数据长度
       - urllib.parse.urlencode可以讲字符串自动转换成上面识别的