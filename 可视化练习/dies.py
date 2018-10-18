import pygal
from die import Die

'''学习同时扔出两个骰子，加起来的值'''
# 创建两个骰子
die_1 = Die()
die_2 = Die()

results = []
for roll_number in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
print(results)

# 分析结果
pinlvs = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1,max_result+1): #意思是1-12之间
    pinlv = results.count(value) #统计每个值出现的次数
    pinlvs.append(pinlv)

print(pinlvs)

# 对结果进行可视化
hist = pygal.Bar()

hist.title ="Results of rolling TWO D6 1000 times"
hist.x_labels = ['1','2','3','4','5','6','7','8','9','10','11','12']
hist.x_title = "results"
hist._y_title = 'pinlv'
hist.add('D6+D6',pinlvs)
hist.render_to_file('die_TWO_visual.svg')


