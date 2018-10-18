import requests ##导入requests
from bs4 import BeautifulSoup ##导入bs4中的BeautifulSoup
import os
import bs4
from urllib import request

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}#浏览器请求头
all_url = 'http://www.mzitu.com/all' ##开始的URL地址
req = request.Request(url=all_url, headers=headers)
start_html = request.urlopen(req).read().decode('utf-8')
##使用requests中的get方法来获取all_url(就是：http://www.mzitu.com/all这个地址)的内容 headers为上面设置的请求头、请务必参考requests官方文档解释
#print(start_html) ##打印出start_html (请注意，concent是二进制的数据，一般用于下载图片、视频、音频、等多媒体内容是才使用concent, 对于打印网页内容请使用text)

soup = BeautifulSoup(start_html, 'lxml') ##使用BeautifulSoup来解析我们获取到的网页 lxml’是指定的解析器
get_a = soup.find('div', class_='all')

if isinstance(get_a,bs4.element.Tag):
    all_a = get_a.find_all('a')

    for a in all_a:
        title = a.get_text()  # 取出a标签的文本
        href = a['href']  # 取出a标签的href 属性
        html = request.urlopen(request.Request(url= href, headers=headers)).read()  ##上面说过了
        html_Soup = BeautifulSoup(html, 'lxml')  ##上面说过了
        get_span = html_Soup.find('div', class_='pagenavi')
        #print(get_span)

        if isinstance(get_span,bs4.element.Tag):

            max_span = get_span.find_all('span')[-2].get_text()  ##查找所有的<span>标签获取第十个的<span>标签中的文本也就是最后一个页面了。
            for page in range(1, int(max_span) + 1):  ##不知道为什么这么用的小哥儿去看看基础教程吧
                page_url = href + '/' + str(page)
                #print(page_url)

img_html = request.urlopen(request.Request(url=page_url, headers=headers)).read()
#print(img_html)
img_Soup = BeautifulSoup(img_html, 'lxml')
img_url = img_Soup.find('div', class_='main-image').find('img')['src']
name = img_url[-9:-4] ##取URL 倒数第四至第九位 做图片的名字
print(name)
'''img =  requests.get(img_url, headers=headers)
f = open('/home/tlxy/下载/tu/'+name+'.jpg', 'ab')##写入多媒体文件必须要 b 这个参数！！必须要！！
f.write(img.content) ##多媒体文件要是用conctent哦！
f.close()'''