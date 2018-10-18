
import pygame.font

from pygame.sprite import Group

from ship import Ship

class Scoreboard():
    '''创建一个得分牌'''

    def __init__(self,ai_settings,screen,stats):
        '''初始化得分牌的各项属性'''
        self.ai_settings = ai_settings
        self.screen =screen
        self.stats = stats
        self.screen_rect = screen.get_rect()

        '''得分信息显示字体'''
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        '''初始得分图像'''
        self.prep_score()

        '''初始化等级图像'''
        self.prep_level()

        '''初始化飞船编组'''
        self.prep_ships()


    def prep_score(self):
        '''渲染图像'''
        #score_str = str(self.stats.score)
        '''学习将分数圆整'''
        rounded_score = int(round(self.stats.score,-1)) #学习使用round函数
        score_str = "{:,}".format(rounded_score)  #{：，}字符串格式设置命令

        self.score_image = self.font.render(score_str,True,self.text_color,
                                            self.ai_settings.bg_color)
        '''得分放在屏幕右上角，选位置的'''
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20 #设置边距为20
        self.score_rect.top = 20   #设置高度


    def prep_level(self):
        '''渲染图像'''
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color,
                                            self.ai_settings.bg_color)
        '''将等级图像放在屏幕正中，选位置的'''
        self.level_rect = self.level_image.get_rect()
        self.level_rect.centerx = self.screen_rect.centerx  # 居中
        self.level_rect.top = self.score_rect.top   # 设置高度

    def prep_ships(self):
        '''渲染飞船编组'''
        self.ships = Group()
        self.image = pygame.image.load('images/ship.png').convert_alpha()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings,self.screen)
            ship.image = pygame.transform.smoothscale(self.image, (50, 50))
            ship.color = (255,255,255)
            ship.rect.x = 10 + ship_number * ship.rect.width/3
            ship.rect.y = 0
            self.ships.add(ship)


    def show_score(self):
        '''在屏幕上显示相关信息'''
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen) #draw方法绘制
