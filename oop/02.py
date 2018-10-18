




##课本上的练习题

#列表的使用（修改，添加，删除，排序）

#创建一个宴会名单

mingdan = ["刘德华","郭富城","张学友","黎明"]
print(mingdan)

#打印出张学友因故不能参加
print("意外，张学友要开演唱会，无法参加，很遗憾")

#讲无法参加的张学友，更换为高圆圆
mingdan[2] = "G高圆圆"
print("正式宴会名单是：")
print(mingdan[0])
print(mingdan[1])
print(mingdan[2])
print(mingdan[3])

#现在还可以邀请一些朋友了
print("\n机会你难得，再邀请一些朋友吧")
mingdan.insert(0,"L刘若英") #利用insert方法，插入一个元素
mingdan.append("秦岚") #利用append方法，在最末尾插入一个元素
mingdan.insert(2,"P彭于晏")
print("增加人员后，现在正式名单为：")
print(mingdan)
#缩减名单
print("财力有限，有超标了，需要删除")
shanchu1 = mingdan.pop()  #利用pop方法，删除列表最后一个元素，调用暂存
print(shanchu1 + "先生/女士,非常抱歉，不能邀请阁下参加")
shanchu2 = mingdan.pop()
print(shanchu2 + "先生/女士，非常抱歉，不能邀请阁下参加")

for i in mingdan:
    print(i + ",先生/女士，恭喜你，您在最终名单")
del(mingdan[1]) #del函数，删除第二个明星
mingdan.remove("郭富城") #利用remove方法，直接寻找第一个郭富城，然后删除
print(mingdan)

mingdan.sort() #利用sort方法永久性排序，字母顺序
print(mingdan)

mingdan.sort(reverse=True) #加参数，倒排
print(mingdan)

mingdan.reverse() #直接用reverse方法，倒排
print(mingdan)

print(len(mingdan)) #len函数测量list长度，也就是元素的个数

##列表的操作
  # 遍历列表，常使用for循环
  #演示一个for循环
dogs = ["aqi","maomao","xiaoli","huihui"]
for dog in dogs:
    print(dog.title() + "是汪汪队成员")
    print("你是最棒的狗狗，" + dog.title() + "。\n") # 利用\n插入一个空行

  #用range函数生成一个数字列表

numbers = list(range(1,11))
print(numbers)
even_number = list(range(1,11,2)) # 指定数字的步长，步长为2
print(even_number)
    #引入临时变量，将计算的结果生成到列表中
squares = []  #一个空表
for value in range(1,11):  #1-10的数字
    square = value **2     # 按每个数字的平方，计算出临时变量square
    squares.append(square)   #把临时变量square添加的列表中去
print(squares)

# 用列表解析的方法，一行代码完成

squares = list(number ** 2 for number in range(1,11))
print(squares)

##练习几个例子
numbers = [number for number in range(1,1000001)] #直接生成一个1到1000000的数字列表
print(min(numbers))
print(max(numbers))
print(sum(numbers))

value1 = list(range(1,21,2))
for i in value1:
    print(str(i) + ",是个奇数")

value3 = []
value2 = list(range(3,31))
for j in value2:
    if j % 3 == 0:
        print(str(j) + ",是3的倍数！")
        value3.append(j)
print(value3)


##元组（只可访问，不可修改，但可以重新定义）
caidan = ('鱼香肉丝','宫保鸡丁','红烧带鱼','干煸豆角','肚丝汤')
print("本店提供的菜品有：\n")
for i in caidan:
    print(i)
new_caidan = ('鱼香茄子','宫保鸡丁','红烧带鱼','干煸豆角','酸辣肚丝汤')
print(new_caidan)





