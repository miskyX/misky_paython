import pygal
from die import Die

'''学习同时扔出两个骰子，数字相同的频率'''
# 创建两个骰子
die_1 = Die()
die_2 = Die()

results = []
'''如果出现相同面值，则记录下这个值'''
for roll_number in range(100000):

    if die_1.roll() == die_2.roll():
        result = die_1.roll()
        results.append(result)

# 分析结果
pinlvs = []
'''统计记录中每个相同值的次数'''
for value in range(1,7): #意思是1-12之间
    pinlv = results.count(value) #统计每个值出现的次数
    pinlvs.append(pinlv)

# 对结果进行可视化
hist = pygal.Bar()

hist.title ="Results of rolling Same_D6 1000 times"
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "results"
hist._y_title = 'pinlv'
hist.add('D6=D6',pinlvs)
hist.render_to_file('same_dice_visual.svg')


