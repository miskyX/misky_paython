
class GameStats():
    '''统计游戏各类信息'''
    def __init__(self,ai_settings):
        '''初始化统计信息'''
        self.ai_settings = ai_settings
        self.reset_stats()  #定义一个方法，reset.stats()
        #游戏启动后，正常状态
        self.game_active = False


    def reset_stats(self):
        '''初始化在游戏运行期间可能变化的统计信息'''
        self.ships_left = self.ai_settings.ship_limit
        #飞船数量存储在sittings里
        self.score = 0
        self.level = 1