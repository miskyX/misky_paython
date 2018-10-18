
# 使用API对数据可视化

# web api
  - web计算平台包含了广泛的功能，其中的大部分均可以通过API（应用程序编程接口）访问
  - 调用API ：使用具体的URL请求特性的信息程序交互,一般返回的是json和csv
  - xuexi :使用github的api来请求有关该网站中python项目的信息，然后使用pygal生成交互式可视化
  - 编程：让他自动下载github上星级最高的Python项目信息，并对这些信息进行可视化。
# github的api
  - http://api.github.com/search/repositories?q=language:python&sort=stars
  
# 安装requests包