import requests
from bs4 import BeautifulSoup
import os
import bs4

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}#浏览器请求头
all_url = 'http://www.k86066.com/' ##开始的URL地址
start_html = requests.get(all_url,headers = headers)##使用requests中的get方法来获取all_url(就是：http://www.mzitu.com/all这个地址)的内容 headers为上面设置的请求头、请务必参考requests官方文档解释
#print(start_html.text)
##打印出start_html (请注意，concent是二进制的数据，一般用于下载图片、视频、音频、等多媒体内容是才使用concent, 对于打印网页内容请使用text)

soup = BeautifulSoup(start_html.text, 'lxml') ##使用BeautifulSoup来解析我们获取到的网页 lxml’是指定的解析器
all_a = soup.find_all('a',attrs={'class':'zoom'})##意思是先查找 class为 all 的div标签，然后查找所有的<a>标签。 ##使用BeautifulSoup解析网页过后就可以用找标签呐！（find_all是查找指定网页内的所有标签的意思，find_all返回的是一个列表。）
#get_all_a = get_div.fine_all('a')
for a in all_a:
    title = a.get_text()
    href = a['href']
    #print(href)
    img_html = requests.get(href, headers=headers)
    img_Soup = BeautifulSoup(img_html.text, 'lxml')
    get_img_url = img_Soup.find('div',class_='post_content')
    if isinstance(get_img_url, bs4.element.Tag):
        img_url = get_img_url.find_all('img')['src']
        for b in img_url:
            print(b)
        '''name = img_url[-9:-4]  ##取URL 倒数第四至第九位 做图片的名字
        img = requests.get(img_url)
        f = open('/home/tlxy/下载/tu2/' + name + '.jpg', 'ab')
        f.write(img.content)
        f.close()'''
