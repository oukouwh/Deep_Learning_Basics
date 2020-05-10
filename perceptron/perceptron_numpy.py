# 感知机导入权重和偏置与门
import numpy as np
x = np.array([0, 1])  # 输入信号
w = np.array([0.5, 0.5])  # 输入权重
b = -0.3  # 偏置
print(x*w)
print(np.sum(x*w))
print(np.sum(x*w) + b)
# [0.  0.5]
# 0.5
# 0.2

def AND(x1, x2):
    x = np.array([x1, x2])  # 输入信号
    w = np.array([0.5, 0.5])  # 输入权重
    b = -0.7  # 偏置
    temp = np.sum(x*w) + b
    if temp <= 0:
        return 0
    else:
        return 1

# 与非门实现代码
def NAND(x1, x2):
    x = np.array([x1, x2])  # 输入信号
    w = np.array([-0.5, -0.5])  # 输入权重
    b = 0.7  # 偏置
    temp = np.sum(x*w) + b
    if temp <= 0:
        return 0
    else:
        return 1

# 或门实现代码
def OR(x1,x2):
    x = np.array([x1, x2])  # 输入信号
    w = np.array([0.5, 0.5])  # 输入权重
    b = -0.3  # 偏置
    temp = np.sum(x*w) + b
    if temp <= 0:
        return 0
    else:
        return 1

# 异或门
#   x1      |      x2     |    y
#   0       |      0      |    0
#   0       |      1      |    1
#   1       |      0      |    1
#   1       |      1      |    0
# 当x1,x2中一方为1是输出才是1
# 设置权重参数(a,w1,w2)=(-0.5,1.0,1.0)
# y={ 0 (-0.5+x1+x2<=0)
#   { 1 (-0.5+x1+x2>0)
# 异或门表现
def XOR(x1,x2):
    rest1 = NAND(x1,x2)
    rest2 = OR(x1,x2)
    rest3 = AND(rest1,rest2)
    print(rest3)
    return rest3

XOR(0,0)
XOR(0,1)
XOR(1,0)
XOR(1,1)
# 0
# 1
# 1
# 0

