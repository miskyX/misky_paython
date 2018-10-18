# coding:utf-8
from urllib import request
import re

def get_html(url):
    page = request.urlopen(url)
    html = page.read()
    return html



def get_img(html):

    html = html.decode('utf-8')
    reg = r'src="(http:[^"]+?\.jpg)"'  # 正则表达式
    img_re = re.compile(reg)  # 编译一下，运行更快
    img_list = re.findall(img_re,html)  # 进行匹配
    print(type(img_list))
    n = 0
    for img_url in img_list:
        request.urlretrieve(img_url, '/home/tlxy/下载/tu/%s.jpg' % n)
        n += 1
    return img_list

ht = get_html("http://www.umei.cc/p/gaoqing/xiuren_VIP/119332.htm")
for i in get_img(ht):
    print(i)
