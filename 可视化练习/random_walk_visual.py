
import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    #导入randomwalk类，然后创建一个实例，绘制所有随机点

    rw = RandomWalk(50000)

    rw.fill_walk()

    # 为方便观察，可以设置窗口尺寸
    plt.figure(figsize=(10,6))  #这个单位是英寸
    plt.title("random walking",fontsize=25)
    #给随机点着色，通过颜色映射
    point_numbers = list(range(rw.number_points))

    plt.scatter(rw.x_values,rw.y_values,
                c=point_numbers,cmap=plt.cm.Greens,edgecolors='none',s=2)

    # 突出放大起点和终点，当然还可以特殊化异常值
    plt.scatter(0,0,c="Red",edgecolors="none",s=50)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c="Blue",edgecolors='none',s=50)
    plt.scatter(max(rw.x_values),min(rw.y_values),c="Yellow",edgecolors='none',s=50)

    # 影藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False) #函数plt.axes()
    plt.show()

    keep_running = input("再来一发？(y/n):")
    if keep_running == "n":
        break
    plt.savefig("random_walking.png",bbox_inches='tight')
