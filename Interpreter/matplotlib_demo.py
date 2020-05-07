# 绘制简单的图形
import matplotlib.pyplot as plt
import numpy as np
# 生成数据
x = np.arange(0,10,0.1) # 以0.1为单位生成0-10的数据
y = np.sin(x)
plt.plot(x,y)
plt.show()