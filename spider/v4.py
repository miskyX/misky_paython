
from urllib import request,parse
if __name__ == '__main__':

    url = 'http://www.baidu.com/s?'
    wd = input("Input your keyword:")

    #要使用data,需要使用字典结构
    qs = {"wd": wd}

    #转换url编码,这一句很重要，它把关键字通过转码，加到了url里面去，如果直接带，会不识别
    qs = parse.urlencode(qs)

    fullurl = url + qs
    print(fullurl)

    rsp = request.urlopen(fullurl)
    html = rsp.read()
    html = html.decode()

    print(html)

