## 重构 ，把代码划分为具体的函数

import json
# 如果以前有存储，我们就加载数据
#如果没有，就提示用户输入，并存储
def love_numbers(): #创建一个函数，把后面的代码封装起来
    '''注释：表明这个函数是干啥的。问候老用户并指出他喜欢的数字'''

    file_name = 'love_numer1.json'

    try:
        with open('love_number1.json') as file_object:
            my_love_number = json.load(file_object)

    except FileNotFoundError:
        love_number = input("请输入你最喜欢的数字：\n")
        with open('love_number1.json', 'w') as file_object:
            json.dump(love_number, file_object)
            print("I will remember you when you come back!")

    else:
        print("Welcome back," + "I know your favorite number! It\'s" + str(my_love_number))
love_numbers()
