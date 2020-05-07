import numpy as np
import matplotlib.pyplot as plt
# python -m pip install matplotlib
x = np.arange(0,10,0.1)
y1 = np.sin(x)
y2 = np.cos(x)
# 绘制图形
plt.title('sin or cos')
plt.plot(x,y1,label='sin')
plt.plot(x,y2,label='cos',linestyle="--")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()