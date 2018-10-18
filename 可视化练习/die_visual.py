import pygal
from die import Die

die = Die()

results = []
for roll_number in range(1000):
    result = die.roll()
    results.append(result)
print(results)

# 分析结果
pinlvs = []

for value in range(1,die.num_sides+1): #意思是1-6之间
    pinlv = results.count(value) #统计每个值出现的次数
    pinlvs.append(pinlv)

print(pinlvs)

# 对结果进行可视化
hist = pygal.Bar()

hist.title ="Results of rolling one D6 1000 times"
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "results"
hist._y_title = 'pinlv'
hist.add('D6',pinlvs)
hist.render_to_file('die_visual.svg')


