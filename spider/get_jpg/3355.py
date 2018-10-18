import requests
from bs4 import BeautifulSoup
import lxml
import os
import bs4

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}#浏览器请求头
all_url = 'http://www.meizian.com/' ##开始的URL地址
start_html = requests.get(all_url,headers = headers)##使用requests中的get方法来获取all_url(就是：http://www.mzitu.com/all这个地址)的内容 headers为上面设置的请求头、请务必参考requests官方文档解释
#print(start_html.text) ##打印出start_html (请注意，concent是二进制的数据，一般用于下载图片、视频、音频、等多媒体内容是才使用concent, 对于打印网页内容请使用text)

soup = BeautifulSoup(start_html.text, 'lxml') ##使用BeautifulSoup来解析我们获取到的网页 lxml’是指定的解析器

all_a = soup.find('div', class_='all')
if isinstance(all_a,bs4.element.Tag):
    all_a = all_a.find_all('a')  ##意思是先查找 class为 all 的div标签，然后查找所有的<a>标签。 ##使用BeautifulSoup解析网页过后就可以用找标签呐！（find_all是查找指定网页内的所有标签的意思，find_all返回的是一个列表。）


    for a in all_a:
        title = a.get_text() #取出a标签的文本
        href = a['href'] #取出a标签的href 属性
        html = requests.get(href, headers=headers) ##上面说过了
        html_Soup = BeautifulSoup(html.text, 'lxml') ##上面说过了
        get_span = html_Soup.find('div', class_='pagenavi')

        if isinstance(get_span,bs4.element.Tag):
            max_span = get_span.find_all('span')[-2].get_text() ##查找所有的<span>标签获取第十个的<span>标签中的文本也就是最后一个页面了。
            print(max_span)
            '''for page in range(1, int(max_span)+1): ##不知道为什么这么用的小哥儿去看看基础教程吧
                page_url = href + '/' + str(page) ##同上

                        ##这个page_url就是每张图片的页面地址啦！但还不是实际地址！我们需要的地址在<div class=”main-image”>中的<img>标签的src属性中
                img_html = requests.get(page_url, headers=headers)
                img_Soup = BeautifulSoup(img_html.text, 'lxml')
                img_url = img_Soup.find('div', class_='main-image').find('img')['src']
                name = img_url[-9:-4] ##取URL 倒数第四至第九位 做图片的名字
                print(img_url)'''
