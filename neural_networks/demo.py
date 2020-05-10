import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1/(1+np.exp(-x))

def identity_function(x):
    return x

def init_network():  # 此函数提供权重和偏置的初始化
    network = {}
    network['w1'] = np.array([[0.2,0.3,0.5],[0.2,0.3,0.5]])
    network['b1'] = np.array([0.1,0.2,0.3])
    network['w2'] = np.array([[0.1,0.3],[0.2,0.5],[0.4,0.6]])
    network['b2'] = np.array([0.1,0.2])
    network['w3'] = np.array([[0.1,0.3],[0.3,0.4]])
    network['b3'] = np.array([0.1,0.3])
    return network

def forward(network,x):
    w1,w2,w3 = network['w1'],network['w2'],network['w3']
    b1,b2,b3 = network['b1'],network['b2'],network['b3']

    sum1 = np.dot(x,w1) + b1
    s1 = sigmoid(sum1)
    sum2 = np.dot(s1,w2) + b2
    s2 = sigmoid(sum2)
    sum3 = np.dot(s2,w3) + b3
    y = identity_function(sum3)

    return y

network = init_network()
x = np.array([1.0,0.5])
y = forward(network,x)
print(y)
# [0.39227535 0.79683545]
