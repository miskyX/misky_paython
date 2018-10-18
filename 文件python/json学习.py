
#练习使用json存储数据

##存数据
import json  #导入模块json

numbers = [110,120,119,999,"kitty","misky"] #定义要存储的数据为列表
file_name = "number.json"   #指定存储数据的json文件名
with open(file_name,'w') as file_object:  #打开文件并写入数据
    json.dump(numbers,file_object)   #利用json.dump()保存数据

##读取数据

import json

file_name = 'number.json'  #说明要找的文件
with open(file_name) as file_object:  #打开文件，并读取数据到file_name
    numbers = json.load(file_object)  #调用json.load()提取数据，存储到变量中
print(numbers)

##练习题

import json

love_number = input("请输入你最喜欢的数字：\n")
file_name = 'love_numer.json'
with open('love_number.json','w') as file_object:
    json.dump(love_number,file_object)

import json

with open('love_number.json') as file_object:
    my_love_number = json.load(file_object)
print("I know your favorite number! It\'s" + str(my_love_number))


##练习题

import json
# 如果以前有存储，我们就加载数据
#如果没有，就提示用户输入，并存储
file_name = 'love_numer1.json'

try:
    with open('love_number1.json') as file_object:
        my_love_number = json.load(file_object)
    print("I know your favorite number! It\'s" + str(my_love_number))
except FileNotFoundError:
    love_number = input("请输入你最喜欢的数字：\n")
    with open('love_number1.json', 'w') as file_object:
        json.dump(love_number, file_object)

else:
    print("Welcome back," + "I know your favorite number! It\'s" + str(my_love_number))


