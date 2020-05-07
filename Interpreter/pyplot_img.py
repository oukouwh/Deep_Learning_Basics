# 图像显示
import matplotlib.pyplot as plt
from matplotlib.image import imread
img = imread('testimg.jpg')
plt.imshow(img)
plt.show()