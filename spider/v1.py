
'''
使用urllib.request请求一个网页，并把内容打印出来
'''

from urllib import request

if __name__ == '__main__':

    url = 'http://www.runoob.com/w3cnote/python-spider-intro.html'
    # 打开相应的url，并把相应的页面作为返回
    rsp = request.urlopen(url)

    html = rsp.read()
    print(type(html))
    html = html.decode()
    print(html)

if __name__ == '__main__':

    url = 'http://war.163.com/photoview/4T8E0001/2296852.html#p=DTJ9IBA64T8E0001NOS'
    # 打开相应的url，并把相应的页面作为返回
    rsp = request.urlopen(url)

    html = rsp.read()
    print(type(html))
    html = html.decode()
    print(html)

