import numpy as np
# softmax函数在计算机的运算中有一定的缺陷，缺陷就是溢出问题下面将要演示溢出和溢出解决方案
a = np.array([1000,2010,999])
print(np.exp(a) / np.sum(np.exp(a)))
# [nan nan nan]
# 解决方案
c = np.max(a)
print(np.exp(a - c) / np.sum(np.exp(a - c)))
# [0. 1. 0.]

# 完整的函数
def max_sof_function(a):
    c =np.max(a)
    exp_a = np.exp(a - c) # 溢出对策
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    print(y)
    return y

param = [1010,1000,990]
max_sof_function(param)
# [9.99954600e-01 4.53978686e-05 2.06106005e-09]

# softmax函数的特种就是输出的是0.0到1.0之间的实数，输出值的总和是1.
param1 = np.array([0.4,2.3,4.0])
y = max_sof_function(param1)
# [0.02258145 0.15097721 0.82644133]
print(np.sum(y))
# 1.0