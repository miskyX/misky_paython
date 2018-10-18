'''
定义一个学生类，用来形容学生
'''


# 定义一个空的类
class Student():
    # 此处的pass必须有，不然报错，它是一个空类，pass代表直接跳过
    pass


# 定义一个对象
sky = Student()


# 定义一个类，用来描述听python课的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"

    # 注意事项：
    # 我们定义这个函数，要注意层级
    # 系统默认有一个self参数
    def doHomework(self):
        print("i am doing")
        return None
    # 创造一个实例化，misky也是一个学Python的学生


misky = PythonStudent()

# 这个点号，就可以调用类的属性，
print(misky.name)
print(misky.age)
print(misky.course)
misky.doHomework()
print(PythonStudent.__dict__)  # 显示PythonStudent这个类的所有成员
print(misky.__dict__)  # 显示这个类下面misky这个对象的所有成员，显然没有继承到属性


# 2018-09-19
# 举例1.

class A():
    name = "sky"
    age = 28

    def say(self):
        self.name = "sky02"
        self.age = 280


print(A.name)  # 显示类的实例A的成员
print(A.age)

print("*" * 20)

print(id(A.name))  # 显示类的实例A的成员内存地址
print(id(A.age))

print("*" * 20)

a = A()  # a是类的实例A的一个对象
print(a.name)  # 对象a的成员
print(a.age)

print("*" * 20)

print(id(a.name))
print(id(a.age))
print("*" * 20)  # 经过比对，发现这两个变量为同一个


##这个案例说明：类实例的属性和其对象的属性，如果不给对象属性赋值的情况下，指向同一个变量。

#例子2 （实验self)

class Student():
    name = misky
    age = 18
    def say(self):  #封装一个函数，打印Student这个类实例的属性
        self.name = "misky02"
        self.age = 280
        print("My name is {0}".format(self.name))
        print("My age is {0}".format(self.age))

sky = Student() # sky是一个对象
sky.say()   #调用函数（在这里也就是打印信息） ,把sky这个变量传入到say这个函数肚饿第一个参数里

print("*" * 10,"华丽分割线","*" * 10)

#例子3 （让self作为形参的比较）

class Teacher():
    name = None
    age = 18
    country = None
    def introduce(self):
        self.name = "小天"
        self.age = 21
        self.country = "美国"
        print("hello，我叫{0}，今年{1}岁，来自{2},".format(self.name,self.age,self.country))

    def again():
        print(__class__.name)# __class__,注意是两个—— ——
        print(__class__.age) #访问类本身的成员
        print("我还没有准备好自我介绍，sorry")
sky = Teacher()
sky.introduce()
  #调用绑定类函数，使用类名
Teacher.again()
print("*" * 20,"华丽分割线","*" * 20,"上例结束end")
# 例子3 关于self

class A():
    name = "sky"
    age = 18
    country = "china"

    def __init__(self):  #构造函数__int__，还没学习，意义何在？主要是对象的初始化，刷新上面的定义值
        self.name = "小天"
        self.age = 21
        self.country = "美国"
        print("hello，我叫{0}，今年{1}岁，来自{2},".format(self.name,self.age,self.country))

    def say(self):
        print(self.name)
        print(self.age)
        print(self.country)
        print("输出已结束，下面我不管")
a = A()
a.say() #对象a得到了类A被构造函数后，得到的值
## A.say()报错，因为有self,所以不能绑定调用
A.say(a) #我们把a给传递进去，得到也是构造函数的值
A.say(A) #我们把A给传递进去,返回的是A的初始值
## 注意上面三个的结果
class B():
    name = "sky02"
    age = 28
    country = "tianshui"
A.say(B) #我们又把类B的初始值给传递进SAY这个函数里面去了，显然只要它认为我们满足了所有参数要求，我们就能带进去
        # 这个被成为”鸭子模型“

# 举个例子：私有变量

class Person():
    # name是共有的成员
    name = "liuying"
    # __age就是私有成员
    __age = 18


p = Person()
# name是公有变量
print(p.name)
# __age是私有变量
#print(p.__age) # 不能访问age,报错
print(Person.__dict__)

print(p._Person__age)# 查询出了私有变量age的实际地址



