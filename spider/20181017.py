

import requests

from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import os
import bs4
#import urllib.request
import random

class Meitu():


    def request(self, url):  # 这个函数访问初始地址，

        headers = {"Accept": "text/html,application/xhtml+xml,application/xml;",
                   "Referer": "https://www.meitulu.com/",
                   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"}


        #headers = {
            #'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
        content = requests.get(url, headers=headers)
        content.encoding = 'utf-8'
        return content


    def html(self, url):  # 这个函数是处理套图地址获得图片的页面地址封面页
        html = self.request(url)
        print(html)
        get_li = BeautifulSoup(html.text, 'lxml').find('ul',class_='img').find_all('li')

        for li in get_li[:]:
            a = li.find('a')
            t = a.find('img')
            title = t.get('alt')
            print(u'开始保存：', title)
            path = str(title).replace("?", '_')
            self.mkdir(path)  # 调用mkdir函数创建文件夹！这儿path代表的是标题title哦！
            html_url = a['href']
            print(html_url)
            self.page(html_url,path)


    def page(self, html_url,path):  # 这个函数处理图片页面的逐个地址
        img_html = self.request(html_url)
        print(img_html)
        self.img(html_url,path)
        max_span = BeautifulSoup(img_html.text, 'lxml').find('div',id='pages').find_all('a')[-2].get_text()
        for page in range(2,int(max_span)+1):
            page_html =html_url.split('.html')[0] +'_{}' .format(str(page)) + '.html'
            # 涉及到字符串指定位置插入
            print(page_html)
            self.img(page_html,path)


    def img(self,page_html,path):  #逐个函数处理每个页面的图片真实地址
        page_url = self.request(page_html)
        get_img_href = BeautifulSoup(page_url.text, 'lxml').find('center')

        if isinstance(get_img_href, bs4.element.Tag):
            img_href = get_img_href.find_all('img')

            for b in img_href[:]:
                img_url = b.get('src')
                print(img_url)
                img_name = b.get('alt')  + '.jpg'
                self.save(img_url, img_name, path)



    def mkdir(self, path):  # 这个函数判断文件位置，并创建路径
        path = path.strip()
        file_path_yes = os.path.join('/home/tlxy/下载/tuku4/', path)
        isExists = os.path.exists(file_path_yes)
        if not isExists:
            print(u'建一个名字叫做', path, u'的文件夹')
            os.makedirs(file_path_yes)
            return True
        else:
            print(u'名字叫做', path, u'的文件夹已经存在了')
            return False

    def save(self, img_url,img_name,path):  # 这个函数下载图片并保存本地


        img = self.request(img_url)
        image = Image.open(BytesIO(img.content))

        file_path = os.path.join('/home/tlxy/下载/tuku4/' + path + '/' + img_name)
        image.save(file_path)



meitu = Meitu()

#for i in range(2,11):
    #pages = "http://www.k86066.com/ugirls/page/" + str(i)

meitu.html('https://www.meitulu.com/t/sisy-si/')