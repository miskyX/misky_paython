
import matplotlib.pyplot as plt
'''使用scatter绘制散点图'''

x_values = list(range(1,101))
y_values = [x_value **2 for x_value in x_values]

plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Reds,edgecolors='none') #输入坐标
#渐变色，cmap
#设置样式
plt.title("My Matplotlib(scatter)",fontsize=24) #标题
plt.xlabel("X:value",fontsize=14) #X轴
plt.ylabel("Y:square of value",fontsize=14) #Y轴
plt.tick_params(axis='both',which='major',labelsize=14) #刻度大小
plt.axis([0,110,0,11000]) #axis刻度的取值范围

#plt.show()
plt.savefig("spuares_plot.png",bbox_inches='tight')
