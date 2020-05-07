# 特别基础的东西，这里就简单写一下。加深自己印象。
# 算术计算
print(1+2)
print(2*7)
print(8/2)
print(2**3)
# 3
# 14
# 4.0
# 8
# 数据类型
print(type(9))
print(type(9.8))
print(type('hello'))
print(type([1,2,3,4]))
print(type((1,2,3,4)))
print(type({'A':1,'B':2}))
# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'list'>
# <class 'tuple'>
# <class 'dict'>
# 变量
a = 10
b = 2
print(a*b)
print(a+b)
print(a-b)
print(a/b)
# 20
# 12
# 8
# 5.0
# 列表List
a = [1,2,3,4,5,6,7]
print(len(a))
print(a)
print(a[3])
print(a[0:3])
print(a[:4:2])
print(a[1:])
print(a[:-1])
print(a[-1])
a[0] = 'start'
print(a)
# 7
# [1, 2, 3, 4, 5, 6, 7]
# 4
# [1, 2, 3]
# [1, 3]
# [2, 3, 4, 5, 6, 7]
# [1, 2, 3, 4, 5, 6]
# 7
# ['start', 2, 3, 4, 5, 6, 7]
# 字典dict Key Value 键值对
dic_test = {'a':1,'b':2,'c':3}
print(dic_test)
print(dic_test['a'])
# {'a': 1, 'b': 2, 'c': 3}
# 1
# 元组 tuple
tuple_test = (1,2,3,4,5)
print(tuple_test)
print(type(tuple_test))
print(len(tuple_test))
print(tuple_test[1])
tup_to_list=list(tuple_test)
tup_to_list[1] = 99
print(tup_to_list)
# (1, 2, 3, 4, 5)
# <class 'tuple'>
# 5
# 2
# [1, 99, 3, 4, 5]
# 布尔类型
a = True
b = False
print(type(a))
print(type(b))
print(not a)
print(not b)
# <class 'bool'>
# <class 'bool'>
# False
# True
# if 语句
a = True
if a:
    print('hello,python')
else:
    print('hello,world')
# hello,python
a = False
if a:
    print('hello,python')
else:
    print('hello,world')
# hello,world
# for 循环语句
for i in range(9):
    print(i)
list_num = [1,3,444,565,23,99]
for i in list_num:
    print(i)
tuple_num = (1,3,23,99)
for i in tuple_num:
    print(i)
dic_num = {'a':1,'v':2,'c':66}
for i in dic_num:
    print(i)
# 函数
def say():
    print('hello')

say()
# hello

def say_hello(param):
    print('hello '+param)

say_hello('Tom')
# hello Tom

# 类
class Name:
    def __init__(self,name):
        self.username = name
        print('haha')
    def say_hello(self):
        print('hello ' + self.username)
    def say_bye(self):
        print('good bye '+ self.username)

# 创建实例
user = Name('Jack')
user.say_hello()
user.say_bye()
# haha
# hello Jack
# good bye Jack
