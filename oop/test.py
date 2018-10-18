## 学习 if语句
#用and和or

age_0 = 18
age_1 = 28
age_2 = 20
if (age_2 <= age_1) and (age_2 >=age_0):
    print(age_2)

age_0 = 18
age_1 = 28
age_2 = 20
if age_0 <= age_2 <= age_1:
    print(age_2)

age_0 = 18
age_1 = 28
age_2 = 15
if age_0 <= age_2 or age_2 <= age_1:
    print(age_2)

#最主要的用法，检查列表中是否包含某特定的值，利用关键字in
value = [1,2,3,4,5]
if 3 in value or 6 not in value:
    print("3在这个列表" + str(value[0:5]) + "中")
    print("6不在这个列表" + str(value[0:5]) + "中")

#if-else语句
values = [1,2,3,4,5]
if 7 in values:
    print("3在这个列表" + str(value[0:5]) + "中")
else:
    print("7不在这个列表" + str(value[0:5]) + "中")

#if-elif-else结构
#例子：6岁以下免票，6-18岁半票，18-65岁免票，65岁以上免票

#age = int(input())
age = 19
print("你今年" + str(age) + "岁")
if age <6 or age > 65:
    print("您是免票参观的")
elif age >=6 and age < 18:
    print("你是半票参观的")
else:
    print("你是全票参观")

#for循环与if语句搭配使用，
#for循环前，首先得确认这个列表是否为空，看例子

love_cars = ["奔驰","BMW"]

if love_cars:
    for love_car in love_cars:
        print("\n土豪，这辆" + love_car + "是你的了")
    print("\n土豪购物完毕")
else:
    print("穷鬼，你还没有车！")
print("\n")
print("*" * 50)

love_cars_have = ["奔驰","宝马","奥迪","劳斯莱斯"]
love_cars_want = ["宝马","劳斯莱斯","兰博基尼"]
print("你先看看")
for love_car in love_cars_want:

    if love_car in love_cars_have:
        print("\n土豪，这辆" + love_car + "是你的了")

    else:
        print("\n穷鬼，这个" + love_car + "你买不起")
print("\n土豪购物完毕")


##学习字典（注意关联性,搜索与键对应的值）
#举个例子作比较

sky_name = "小天"
sky_age = 18
sky_country = "china"
print(sky_name,sky_age,sky_country)

sky = {"name": "小天","age": 18 ,"country":"china"}
print(sky["name"],sky["age"],sky["country"])
print("love"+ sky["name"])

#添加键-值对
sky["tel"] = 13909388802
print(sky["tel"])
#修改字典中的值
sky['age'] = 28
print(sky['age'])

Dong = {}
Dong['age'] = 28
print(Dong["age"])

favorite_building = {
    '中国': '长城',
    '美国': '自由女神像',
    '法国': '埃菲尔铁塔',
    '英国': '伦敦桥'
}

print(favorite_building)

print("中国人最自豪的建筑是：" + favorite_building['中国']) # 类似查字典
print('美国人最喜欢的建筑是：'+ favorite_building['美国'])
print('*' * 40)

#遍历字典，使用.items()方法，申明两个变量，提取存储的键-值
for country, building in favorite_building.items():
    print(country + "人最自豪的建筑是：" + building)

#遍历字典的键，使用.keys()方法
for country in favorite_building.keys():
    print("\n以上的国家有：" + country)

#遍历字典的值，使用.values()方法
for building in favorite_building.values():
    print("\n以上的建筑有：" + building)


#关于字典的嵌套

alien_0 = {'color':'green','points':5}

#字典练习题（宠物）

tiantian = {"type":"dog","name":"张三"}
huihui = {"type":"cat","name":"李四"}
xiaoli = {"type":"dog","name":"王五"}

pets = [tiantian,huihui,xiaoli]
for pet in pets:
    print(pet)

favorite_places = {
    "alen":["beijing","shanghai","tianhui"],
    "lindy":["suzhou",'shanghai','hangzhou'],
    'harry':["lanzhou","xi\'an",'dongjin']
}
for names , places in favorite_places.items():
    print("\n" + names + "\'s favorite pleaces are :" )

    for place in places:
        print("\t" + place) #字典里面存储列表，和访问liebi8ao的值， 注意第二个for循环


#喜欢的数字
persons_numbers = {
            "zhangsan": ['110', '120', '119'],
            "lisi": ['111', '222', '333'],
            "wangwu": ['123', '456', '789'],
            "liuqi": ['123', '321', '213', '312'],
            "zhuba": ['7777', '8888', '9999']
        }
for names, numbers in persons_numbers.items():
    print(names + "\'s numbers are:")
    for number_A in numbers:
        print(number_A)

#演示一下多行字符
message = "yellow duck, yellow duck, what do you see ? "
message += "\n" + "I see a blue dog" # 用+=连接，第二句用\n
print("\n" + message)


#正式学习while循环，注意何时停止

tips = "\n 告诉我一些东西，我可以完整的复述出来，不信你试试："
tips += "想结束，可以打字符"+ "滚"
message = ""
while message != "滚":
    message = input(tips)
   # print(message)  #这个时候能看见滚，如何去掉
    if message != "滚":
        print(message)

tips = "\n 告诉我一些东西，我可以完整的复述出来，不信你试试："
tips += "想结束，可以打字符"+ "滚"
active = True

message = ""
while active:
    message = input(tips)
   # print(message)  #这个时候能看见滚，如何去掉
    if message == "滚":
        active = False
    else:
        print(message)

tips = "\n 告诉我一些东西，我可以完整的复述出来，不信你试试："
tips += "想结束，可以打字符"+ "滚"
message = ""
while True:
    message = input(tips)
   # print(message)  #这个时候能看见滚，如何去掉
    if message == "滚":
        break
    else:
        print(message)



#举例子学习
#结束while循环的三种方法（出口）
#while中使用if语句结束
#使用变量active控制结束
#使用break语句退出





