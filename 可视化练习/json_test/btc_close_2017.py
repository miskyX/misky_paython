import json
import pygal

#将数据加载到一个列表中
filename = 'btc_close_2017.json'

with open(filename) as f:
    btc_data = json.load(f)

# 提取每一天的数据
dates = []
months = []
weeks = []
weekdays = []
closes =[]


for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    closes.append(int(float(btc_dict['close'])))

# 可视化数据
line_chart = pygal.Line(x_label_rotation=20,show_minor_x_labels=False)
#让X轴标签值倾斜20度
line_chart.title = "收盘价（¥）"
line_chart.x_labels = dates
N = 20
line_chart.x_labels_major = dates[::N]
# X轴数值每隔20天显示，刻度
line_chart.add('收盘价',closes)
line_chart.render_to_file("收盘价折线图（¥）.svg")



