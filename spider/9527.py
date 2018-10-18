import urllib
import urllib.request
import random
from bs4 import BeautifulSoup
import os
import bs4
from PIL import Image
from io import BytesIO

class Mzitu():

    def all_url(self,url,headers): #这个函数获取页面列表
        html = self.request(url,headers)##调用request函数把套图地址传进去会返回给我们一个response
        get_a = BeautifulSoup(html, 'lxml').find('div',class_='all')
        if isinstance(get_a,bs4.element.Tag):
            all_a = get_a.find_all('a')
            for a in all_a[1:4]:
                title = a.get_text()
                print(u'开始保存：', title)
                path = str(title).replace("?",'_')
                self.mkdir(path) #调用mkdir函数创建文件夹！这儿path代表的是标题title哦！
                href = a['href']
                self.html(href,headers)#调用html函数把href参数传递过去！href是啥还记的吧？ 就是套图的地址哦！
    '''观察一下网页你会发现图片页面的地址全部都在 li 标签中，点开li标签你会发现图片页面的地址在a标签的href属性中、主题在a标签中。 
实现逻辑就是：先找到页面中的全部 li标签、然后提取出中间a标签的href属性值与a标签的内容，前者我们用来继续请求html看看会不会有我们需要的图片下载地址，后者我们存储的时候给文件夹命名使用。 
下面用beautifulsoup 提取　ｌｉ标签中的内容
从途中发现提取了多余的li标签。我们推翻上面的思路 
现在我们先找到 div class=”all”这个标签 ， 
然后直接找a标签！在div class=”all”/div 这个模块里面的a标签的全是我们需要的东西，
就不需要li标签来限制提取范围啦！'''

    def html(self,href,headers):#这个函数是处理套图地址获得图片的页面地址
        html = self.request(href,headers)
        max_span = BeautifulSoup(html,'lxml').find('div',class_='pagenavi').find_all('span')[-2].get_text()
        for page in range(1,int(max_span)+1):
            page_url = href +'/' +str(page)
            self.img(page_url,headers)

    def img(self,page_url,headers):#这个函数处理图片页面地址获得图片的实际地址
        img_html = self.request(page_url,headers)
        img_url = BeautifulSoup(img_html,'lxml').find('div',class_ ='main-image').find('img')['src']
        #print(img_url)
        self.save(img_url,headers)

    def save(self,img_url,headers): #这个函数下载图片并保存本地
        name = img_url[-9:-4]
        img = self.request('http://i.meizitu.net/2018/10/11c04.jpg',headers)
        #print(type(img.content))

        #image = Image.open(BytesIO(img.content))
        #image.save('/home/tlxy/下载/tu3/'+ name +'.jpg','jpeg')
        #f = open('/home/tlxy/下载/tu2/'+ name +'.jpg','ab')
        #f.write(img.content)
        #f.close()

    def request(self, url,headers): #这个函数访问初始地址，


        randdom_header=random.choice(headers)
        req = urllib.request.Request(url)

        req.add_header("User-Agent", randdom_header)
        req.add_header("GET", url)

        content = urllib.request.urlopen(req).read()
        #headers = {
            #'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        #req = request.Request(url=url,headers=headers)
        #content = request.urlopen(req)

        return content

    def mkdir(self, path): #这个函数判断文件位置，并创建路径
        path = path.strip()
        isExists = os.path.exists(os.path.join('/home/tlxy/下载/tu3/', path))
        if not isExists:
            print(u'建一个名字叫做', path, u'的文件夹')
            os.makedirs(os.path.join('/home/tlxy/下载/tu3/', path))
            return True
        else:
            print(u'名字叫做', path, u'的文件夹已经存在了')
            return False
my_headers = [
            "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"
]
mzitu = Mzitu()
mzitu.all_url('http://www.mzitu.com/all',my_headers)##给函数all_url传入参数  你可以当作启动爬虫（就是入口）