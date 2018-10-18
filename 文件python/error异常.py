#print(10/0)

'''Traceback (most recent call last):
  File "/home/tlxy/tulingxueyuan/文件python/error异常.py", line 1, in <module>
    print(10/0)
ZeroDivisionError: division by zero'''
##这就是一个异常，ZeroDivisionError: division by zero

try:
    print(5/0)
except ZeroDivisionError:
    print('division by zero')
    print('大哥0不能做为除数')   #相当于把大家看不懂的错误给翻译一下，同时让程序不要终止

## 学习分析文本
file_name = '/home/tlxy/下载/all.txt'
try:
    with open(file_name,'r') as book:
        contents = book.read()
except FileNotFoundError:
    msg = "大哥，没找到！"
    print(msg)
else:
    # 我们来分析文本，计算文件包含多少个字
        words = contents.count("刘备")
        print("这本小说里‘刘备’一共出现了" + str(words) + "次")
        num_words = contents.count("")
        print("这本小说一共有" + str(num_words) + "字")
##
