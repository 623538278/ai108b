import random as r

'''

S = NP VP
NP = DET N
VP = V NP
N = dog | cat
V = chase | eat
DET = a | the

'''

A=['张三', '李四', '王五' , '德萊厄斯']
B=['想', '不想']
C=['在你嘴裡种水稻', '請你吃飯', '外圈刮','皮一哈']

def S():

    return N() + V() + DET()

def N():

    return r.choice(A)

def V():

    return r.choice(B)

def DET():

    return r.choice(C)

for a in range(3):

    print(S())
