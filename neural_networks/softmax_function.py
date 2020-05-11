import numpy as np
# softmax函数解决分类问题


def soft_max_fun(param):
    exp_parm = np.exp(param)
    sum_parm = np.sum(exp_parm)
    y = exp_parm / sum_parm
    print(y)
    return y


param = [0.4, 2.7, 4.8]
soft_max_fun(param)
# [0.01081958 0.10791644 0.88126398]
