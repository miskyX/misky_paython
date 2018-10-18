import pygame

from pygame.sprite import Sprite #导入了sprite让ship继承Sprite，创建飞船组

class  Ship(Sprite):

    def __init__(self,ai_settings,screen):
        '''初始化飞船，并设置其初始位置'''
        super(Ship,self).__init__() #继承属性

        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/ship.png').convert_alpha()
        self.image =pygame.transform.smoothscale(self.image,(150,150))
        # 导入图像，并设置了大小
        self.rect = self.image.get_rect()
        #get_rect()方法处理图像，获取图像的矩形坐标
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom =self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        #增加一个移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''根据移动标志来调整飞船的位置,通过更新飞船的center'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        '''通过self.center更新rect对象'''
        self.rect.centerx = self.center


    def blitme(self):
        '''在刚才指定的位置，绘制飞船'''
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        '''让飞船在屏幕上居中'''
        self.center = self.screen_rect.centerx
