

'''学习类和实例'''

#餐馆属性

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type): #__int__初始化描述餐馆的全部属性
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):  #创建一个描述方法
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self): #创建一个营业方法
        print("餐厅正在营业")

restaurant = Restaurant("川香渔府","川菜") # 实例化一个餐厅，并且给他的属性赋值
restaurant.describe_restaurant() #调用方法1
restaurant.open_restaurant()    #调用方法2

#修改属性的值

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):  # __int__初始化描述餐馆的全部属性
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 # 添加一个属性，默认值为0

    def describe_restaurant(self):  # 创建一个描述方法
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):  # 创建一个营业方法
        print("餐厅正在营业")
        print("在这家餐厅就餐的人数是:" + str(self.number_served))

    def set_number_severd(self):
        '''可以设置就餐人数'''
        self.number_served = int(input("输入就餐人数"))

    def print_number_served(self):
        print("在这家餐厅就餐的人数修改后是:" + str(self.number_served))

    def increament_number_served(self,mile):
        self.number_served += mile

restaurant = Restaurant("川香渔府", "川菜")  # 实例化一个餐厅，并且给他的属性赋值
restaurant.describe_restaurant()  # 调用方法1
restaurant.open_restaurant()  # 调用方法2
restaurant.set_number_severd() #调用设置就餐人数的方法
restaurant.increament_number_served(101) #调动步长累进的方法，同事设置值为12，如果不设置就缺少参数而报错
restaurant.print_number_served() #调用打印就餐人数的方法



#关于继承的练习题

#冰激凌店是一种特殊的餐馆

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type): #__int__初始化描述餐馆的全部属性
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

class IceCreamStand(Restaurant): #冰激凌店是餐馆的子类
    def __int__(self,restaurant_name,cuisine_type):  #初始化父类的属性
        super().__init__(restaurant_name,cuisine_type) #super关联
        self.flavors = "caomei"

    def print_icecream(self):

        for icecream in self.flavors:
            print("本店出售的冰激品种有："+ icecream)

my_icecreamstand = IceCreamStand("极速冷冻","nice")
my_icecreamstand.print_icecream()

