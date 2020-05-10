# ReLU(Rectified Linear Unit)函数，在输入值大于0时，直接输出该值，在输入值小于0时，输出0
import numpy as np
import matplotlib.pyplot as plt

def relu(x):
    print(np.maximum(0,x))
    return np.maximum(0,x)

relu(2) # 2
relu(-0.9) # 0.0
