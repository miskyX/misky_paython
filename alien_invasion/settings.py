
class Settings():
    '''存储《外星人入侵》这个游戏所有设置的类'''

    def __init__(self):
        '''初始化游戏的设置（类的初始化）--静态组'''

        # 默认的数值

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255,240,245)

        # 飞船设置
        #self.ship_speed_factor = 10 把这些动态的数据拿走，分为动态组
        self.ship_limit = 3

        #子弹设置

        self.bullet_width = 10
        self.bullet_height = 20
        self.bullet_color = 80,80,80
        self.bullets_allowed = 10

        #外星人设置

        self.fleet_drop_speed = 10 #撞到边缘是，下降的速度


        #记分牌设置
        self.alien_points = 50

        # 提升性能，增加难度
        self.speedup_scale = 1.1
        # 增加分值
        self.score_scale = 1.5
        self.initialize_dynamic_settings()  #再次初始化随游戏进行而变化的属性

    def increase_speed(self):
        '''提高速度设置和分数设置'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points *= int(self.score_scale)
        print("飞升一级！\n"
              "你当前的分数是："+ str(self.alien_points))

    def initialize_dynamic_settings(self):
        '''初始化岁游戏变化的属性设置--动态组'''
        self.ship_speed_factor = 10
        self.bullet_speed_factor = 4
        self.alien_speed_factor = 2
        self.fleet_direction = 1  # 实现方向改变，1为右，-1为左

