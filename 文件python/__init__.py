
#学习如何读取文件
with open('learning_python.txt') as file_object: #这个文档在当前程序中,文件夹中
    contens = file_object.read()
    print(contens)  #注意这种read()方式读取后，会存在一个空行的字符串
    print(contens.rstrip()) #使用rstrip（）方法可以删除字符串后面空白

with open('/home/tlxy/tulingxueyuan/oop/1234') as hell: #绝对路径，Linux使用/，而windows使用\
    conets = hell.read()
    print(conets)

file_path = '/home/tlxy/tulingxueyuan/oop/1234' #绝对路径很长，经常使用file_path变量存储它的路径，然后引入
with open(file_path) as file_object:
   contes = file_object.read()
   print(conets.rstrip())

# 实现逐行打印
file_name = 'learning_python.txt'
with open (file_name) as file_object:
    for line in file_object:  #利用for循环逐行打印
        print(line.rstrip())

# 实现模块外调用
file_name = 'learning_python.txt'
with open (file_name) as file_object:
    lines = file_object.readlines()  #使用方法readlines()方法逐行读取内容,并存在一个列表中
    print(lines)  #打印出来后是一个列表
for line in lines:  #我们在with外实现了调用
    print(line.rstrip())


# 文件读取后进行数据更改（替换）—使用方法replace()
file_name = 'learning_python.txt'
with open (file_name) as file_object:
    lines = file_object.readlines()  #使用方法readlines()方法逐行读取内容,并存在一个列表中
    #print(lines)  #打印出来后是一个列表
for line in lines:  #我们在with外实现了调用
    line = line.replace("Python","Java")
    print(line.rstrip())

# 写入文件

file_name = 'creat_learning_python.txt'
with open(file_name,"w") as file_object:
    file_object.write("我们用Python命令创建了一个文本!恭喜你！，GGG")   #write（）方法一定要慎用，因为如果存在同名文件，则直接清空原有内容，
with open(file_name) as GG: #再次打开看一下
    juzi = GG.read()
    print(juzi)
## 写入多行数据 （write不添加换行符，我们要分开的话要在后面加\n)
file_name = 'creat_learning_python.txt'
with open(file_name,"w") as file_object:
    file_object.write("我们用Python命令创建了一个文本!恭喜你！，GGG")   #write（）方法一定要慎用，因为如果存在同名文件，则直接清空原有内容，
    file_object.write("\n一行测试！\n")
    file_object.write("二行测试！")
with open(file_name) as GG: #再次打开看一下
    juzi = GG.read()
    print(juzi)

## 写入文件，增加数据，而不是覆盖原有内容
file_name = 'learning_python.txt'
with open(file_name,"a") as file_object:
    file_object.write("\n我们用Python命令增加一段数据，而不是覆盖\n")
    file_object.write("承接上面，学Python是为了打发时间。\n")
with open(file_name) as GG: #再次打开看一下,我们每运行一次文件里面都会增添一遍，这是个问题
    juzi = GG.read()
    print(juzi)

# 文件操作的几个例子学习

#访客
name = input('请输入你的姓名：')
file_name = 'guest.txt'
with open('file_name','w') as file_object:  #注意生成的文件名是file_name而不是guest.txt
    file_object.write(name)

#访客名单
tips = "请输入你的访客姓名："
tips += "(若要退出，可输入Q)\n"
name =""
while True:
    name = input(tips)
    if name == "Q":
        break
    else:
        with open('guest_book.txt','a') as file_object:
            file_object.write(name + "\n")
            print(name + "您的信息已经录入成功！")
with open('guest_book.txt') as GG:
    dis = GG.read()
    print(dis)




