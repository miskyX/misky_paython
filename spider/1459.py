import requests
from bs4 import BeautifulSoup
import os
import bs4

def all_url(self,url):
        html = self.request(url)##调用request函数把套图地址传进去会返回给我们一个response
        get_a = BeautifulSoup(html.text, 'lxml').find('div',class_='image')
        if isinstance(get_a,bs4.element.Tag):
            all_a = get_a.find_all('a')
            for a in all_a[1:4]:
                title = a.get_text()
                print(u'开始保存：', title)
                path = str(title).replace("?",'_')
                self.mkdir(path) #调用mkdir函数创建文件夹！这儿path代表的是标题title哦！
                href = a['href']
                self.html(href)#调用html函数把href参数传递过去！href是啥还记的吧？ 就是套图的地址哦！