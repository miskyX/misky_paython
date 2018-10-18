
import sys  #导入sys模块

import pygame # 导入pygame模块，它包含开发游戏需要的功能
from pygame.sprite import Group

'''我们的setting文件里面，创建了一个类，现在实例化'''

from settings import Settings

from game_stats import GameStats

from button import Button

from ship import Ship

from alien import Alien

from scoreboard import Scoreboard

import game_functions as gf



def run_game():   #定义函数，
    #初始化游戏并创建一个屏幕对象
    pygame.init()   #初始化

    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))

    #pygame.display.set_mode()创建一个显示窗口
    pygame.display.set_caption("打倒特朗普，中国人民万岁！")
    # display.set_caption()窗口标题

    #创建一个统计游戏信息的实例
    stats = GameStats(ai_settings)
    #创建一个记分牌的实例
    scoreboard = Scoreboard(ai_settings,screen,stats)

    #实例化一艘飞船
    ship = Ship(ai_settings,screen)
    #实例化子弹
    bullets = Group()
    #实例化外星人
    alien = Alien(ai_settings,screen)
    # 创建一群外星人
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #创建一个开始按钮
    play_button = Button(ai_settings,screen,"Play")


    '''开始游戏的循环'''
    while True:
        #监视键盘和鼠标事件,调用check_events函数
        gf.check_events(ai_settings,screen,stats,scoreboard,play_button,
                        ship,aliens,bullets)

        if stats.game_active:

            #调用update方法
            ship.update()

            #调用子弹,重绘，实现移动
            gf.update_bullets(ai_settings,screen,stats,scoreboard,ship,aliens,bullets)

            #调用外星人，重绘，实现移动
            gf.update_aliens(ai_settings,stats,screen,scoreboard,ship,aliens,bullets)

        #重绘图像，调用update_screen函数
        gf.update_screen(ai_settings,stats,screen,scoreboard,ship,aliens,bullets,play_button)


run_game()


'''我们的setting文件里面，创建了一个类'''


