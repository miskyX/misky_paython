
import matplotlib.pyplot as plt
'''导入plplot模块，并指定为plt别名'''

'''使用plot绘制曲线图'''
input_values = [1,2,3,4,5,6]
squares = [1,4,9,16,25,36]

plt.plot(input_values,squares,linewidth=2)
# 函数plot用来绘制图形


# 设置标题，XY轴添加标签
plt.title("My Matplotlib",fontsize=24)
plt.xlabel("X:value",fontsize=14)
plt.ylabel("Y:square of value",fontsize=14)

# 设置刻度大小
plt.tick_params(axis="both",labelsize=14)
plt.show()
#用来打开图形查看器
