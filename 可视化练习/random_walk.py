

from random import choice
'''学习随机漫步'''

class RandomWalk():
    '''生成一个随机漫步数据的类'''

    def __init__(self,number_points=5000):
        '''初始化属性'''
        self.number_points = number_points

        #所有随机漫步都开始与（0,0）
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        # 向左走还是向右走,向上还是向下
        direction = choice([1, -1])
        # 沿方向走多远
        distance = choice([0, 1, 2, 3, 4])
        # 走多少距离
        step = direction * distance
        return step

    def fill_walk(self):
        '''计算随机漫步的所有点'''
        # 不断漫步，直到到达指定的长度（5000个）
        while len(self.x_values) < self.number_points:
            x_step = self.get_step()
            y_step = self.get_step()

            #不能原地不动
            if x_step == 0 and y_step == 0:
                continue

            #计算随机点的坐标
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step  #让X和Y坐标的最后一位（就是最后一个点的坐标值更新）

            self.x_values.append(next_x)
            self.y_values.append(next_y)



