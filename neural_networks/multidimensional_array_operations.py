# 多维数组的运算
import numpy as np
A = np.array([1,2,3,4,5])
print(A)
print(np.ndim(A))
print(np.shape(A))
# [1 2 3 4 5]
# 1
# (5,)
B = np.array([[1,2],[3,4],[5,6]])
print(B)
print(np.ndim(B))
print(np.shape(B))
# [[1 2]
#  [3 4]
#  [5 6]]
# 2
# (3, 2) 3代表第一个维度有3个元素，2代表第二个维度有2个元素
a = np.array([[1,2],[3,4]])  #a 为 2x2的矩阵
b = np.array([[5,6],[7,8]])  #b 为 2x2的矩阵
print(np.dot(a,b))
print(np.dot(b,a)) # 参数位置不一样得到的矩阵结果也会不一样
# [[19 22]
#  [43 50]]
# [[23 34]
#  [31 46]]
# 2x3的矩阵和3x2的矩阵运算
c = np.array([[1,2,3],[4,5,6]]) # 2x3
d = np.array([[1,2],[3,4],[5,6]]) # 3x2
print(np.dot(c,d))
# [[22 28]
#  [49 64]]
# 用c 2x3的矩阵乘以 e 2x2的矩阵会报错
e = np.array([[1,2],[3,4]])
print(np.dot(c,e))
# Traceback (most recent call last):
#   File "c:\py_vscod\Deep_Learning_Basics\neural_networks\multidimensional_array_operations.py", line 35, in <module>
#     print(np.dot(c,e))
# 矩阵c的第一维度和矩阵c的第0维度的元素个数不一致导致，在矩阵的运算中，必须使两个矩阵中的对应维度的元素个数保持一致否则无法计算
