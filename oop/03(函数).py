 #函数练习题目：

 #城市名

def city_country(city,country):
     city_country = city + "," + country
     return city_country
jieguo = city_country('北京','中国')
jieguo1 = city_country("洛杉矶","美国")
jieguo2 = city_country("伦敦","英国")
print(jieguo)
print(jieguo1)
print(jieguo2)

#可选形参,

def make_album(singer,album,number=''): # 注意这个可选形参，默认为空
     if number:
          make_album = singer + album +number
     else:
          make_album = singer +album
     return make_album
vlaue1 = make_album("刘欢"," 好汉歌"," 4")
vlaue2 = make_album("beyond"," 光辉岁月")
vlaue3 = make_album("ladygaga"," haha")

print(vlaue1)
print(vlaue2)
print(vlaue3)
#可选形参，返回为字典
def make_album(singer, album, number=''):  # 注意这个可选形参，默认为空
      if number:
           make_album = {"singer":singer ,"album": album ,"number":number}
      else:
           make_album = {"singer":singer ,"album": album}
      return make_album


vlaue1 = make_album("刘欢", " 好汉歌", " 4")
vlaue2 = make_album("beyond", " 光辉岁月")
vlaue3 = make_album("ladygaga", " haha")

print(vlaue1)
print(vlaue2)
print(vlaue3)

'''''# 用户输入信息，组合成字典显示
singer = input("输入歌手")
album = input("输入专辑")
def make_album(singer,album):
    make_album = {"singer": singer, "album": album}
    return make_album
value = make_album(singer , album)
print(value)

# 加入while循环，可以一直输入

def make_album(singer, album, number=''):  # 注意这个可选形参，默认为空
    if number:
        make_album = {"singer": singer, "album": album, "number": number}
    else:
        make_album = {"singer": singer, "album": album}
    return make_album

while True:
    singer = input("输入歌手:")
    if singer == "end":
        break
    album = input("输入专辑:")
    if album == "end":
        break
    vlaue = make_album(singer,album)  #注意这个缩进，因为singer和albue这两个变量实在while下面定义的，所以成为循环体的一部分
    print(vlaue)
'''

# 向函数传递列表

def show_magicians(names):
    for name in names:
        message = "hello," + name + "!"
        print(message)
names = ["孙悟空","白龙马","九头鸟","黑熊精"]
show_magicians(names)

# 学习如何用函数批量修改列表数据
def make_great(great_names):
    for great_name in great_names:
        great_name = "伟大的" + great_name
        print(great_name)
great_names = ["孙悟空","白龙马","九头鸟","黑熊精"]
make_great(great_names)

