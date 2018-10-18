import csv

import matplotlib.pyplot  as plt

from datetime import datetime

filename = 'sitka_weather_2014.csv'

'''打开源数据文件'''
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader) #读取文件头
    '''
    我们为了方便查看文件头，用此方法
        for index, column_hearder in enumerate(header_row):  #调用enumerate获取每个元素的索引值和值
            print(index,column_hearder)
    '''
    # 读取最高气温，最低气温和日期
    highs = []
    lows = []
    dates = []
    for row in reader: # 逐行读取
        high = int(row[1])
        highs.append(high) # 我们从第二行开始读取数据的第二列，并添加到highs末尾
        low = int(row[3])
        lows.append(low)
        current_date = datetime.strptime(row[0],"%Y-%m-%d")
        # 转换日期，注意Y字母大写代表4位数的年份
        dates.append(current_date)
    print(highs)

# 可视化数据
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5) # alpha参数指定颜色的透明度
plt.plot(dates,lows,c="green",alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor="yellow",alpha=0.1)
# fill_betweeen()填充区域
plt.title("daily high_low temperatures, 2014",fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
#利用autofmt_xdate()来绘制斜的日期标签
plt.ylabel('temperatures',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=5)

plt.show()

