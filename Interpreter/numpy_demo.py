import numpy as np
# 数组和矩阵计算用numpy
# 生成numpy数组
a = np.array([1.3, 3, 4, 5])
print(a)
print(type(a))
# [1.3 3.  4.  5. ]
# <class 'numpy.ndarray'>
# numpy的算术运算
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print(x + y)
print(x * y)
print(x / y)
print(x - y)
# [5 7 9]
# [ 4 10 18]
# [0.25 0.4  0.5 ]
# [-3 -3 -3]
# numpy的N维数组进行计算
arr = np.array([[1, 2], [3, 5]])
print(arr)
print(arr.shape)
# [[1 2]
#  [3 5]]
# (2, 2)得到的是一个二维数组
arr_num = np.array([[12, 34], [45, 43]])
arr_num1 = np.array([[1, 3], [5, 9]])
print(arr_num + arr_num1)
print(arr_num - arr_num1)
print(arr_num * arr_num1)
print(arr_num / arr_num1)
# [[13 37]
#  [50 52]]
# [[11 31]
#  [40 34]]
# [[ 12 102]
#  [225 387]]
# [[12.         11.33333333]
#  [ 9.          4.77777778]]
# 广播
arr_num1 = np.array([[1, 3], [5, 9]])
print(arr_num1 * 10)
# 标量10被扩展成了2x2的形状，然后在和arr_num1矩阵进行乘法运算
# [[10 30]
#  [50 90]]
A = np.array([[1, 3], [5, 9]])
B = np.array([10, 20])
print(A * B)
# [[ 10  60]
#  [ 50 180]]
# 访问元素
print(A)
print(A[0])
print(A[0][1])
# [[1 3]
#  [5 9]]
# [1 3]
# 3
# 二维数组转为一维数组
two_to_one = arr_num1.flatten()
print(two_to_one)
# [1 3 5 9]
print(two_to_one>3)
# [False False  True  True]
print([two_to_one>3])
# [array([False, False,  True,  True])]
print(two_to_one[two_to_one>3])
# [5 9]


