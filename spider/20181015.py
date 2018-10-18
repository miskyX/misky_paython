import requests

from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import os
import bs4

class Mzitu():

    def request(self, url):  # 这个函数访问初始地址，
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
        content = requests.get(url, headers=headers)
        return content




    def html(self, url):  # 这个函数是处理套图地址获得图片的页面地址
        html = self.request(url)
        print(html)
        get_a = BeautifulSoup(html.text, 'lxml').find('div', class_='mainleft').find_all('a',class_='zoom')

        for a in get_a[-2:-1]:
            if a == 508:
                continue
            title = a.get('title')
            if title == None:
                continue
            print(u'开始保存：', title)
            path = str(title).replace("?", '_')
            self.mkdir(path)  # 调用mkdir函数创建文件夹！这儿path代表的是标题title哦！

            page_url = a['href']
            self.img(page_url, path)



    def mkdir(self, path):  # 这个函数判断文件位置，并创建路径
        path = path.strip()
        file_path_yes = os.path.join('/home/tlxy/下载/tuku2/尤蜜荟/', path)
        isExists = os.path.exists(file_path_yes)
        if not isExists:
            print(u'建一个名字叫做', path, u'的文件夹')
            os.makedirs(file_path_yes)
            return True
        else:
            print(u'名字叫做', path, u'的文件夹已经存在了')
            return False

    def img(self, page_url,path):  # 这个函数处理图片页面地址获得图片的实际地址
        img_html = self.request(page_url)
        print(img_html)
        get_img_href = BeautifulSoup(img_html.text, 'lxml').find('div', id='post_content')
        if isinstance(get_img_href, bs4.element.Tag):
            img_href = get_img_href.find_all('img')
            x = 0
            for b in img_href[::2]:
                img_url = b.get('data-lazy-src')

                img_name = path[24:30] + str(x) +'.jpg'
                if img_url == None:
                    continue
                self.save(img_url, img_name, path)
                print(img_url)
                x = x + 1





    def save(self, img_url,img_name,path):  # 这个函数下载图片并保存本地
        img = self.request(img_url)

        image = Image.open(BytesIO(img.content))

        file_path = os.path.join('/home/tlxy/下载/tuku2/尤蜜荟/'+ path + '/' + img_name)

        image.save(file_path)




mzitu = Mzitu()

#for i in range(2,11):
    #pages = "http://www.k86066.com/ugirls/page/" + str(i)
mzitu.html('http://www.k86066.com/youmi')
