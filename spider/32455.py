import urllib
import urllib.request
import random
from bs4 import BeautifulSoup
import os
import bs4
from PIL import Image
from io import BytesIO
class TT:
    def request(self, url, headers):  # 这个函数访问初始地址，


        req = urllib.request.Request(url)

        req.add_header("User-Agent", headers)
        req.add_header("GET", url)

        content = urllib.request.urlopen(req).read()
        # headers = {
        # 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        # req = request.Request(url=url,headers=headers)
        # content = request.urlopen(req)
        return content


    def save(self, img_url, headers):  # 这个函数下载图片并保存本地

        img = self.request(img_url, headers)

        image = Image.open(BytesIO(img.content))
        image.save('/home/tlxy/下载/tu3/'+ '123' +'.jpg','jpeg')
        # f = open('/home/tlxy/下载/tu2/'+ name +'.jpg','ab')
        # f.write(img.content)
        # f.close()

tt = TT()
tt.save(img_url = 'http://i.meizitu.net/2018/10/11c05.jpg',headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'})