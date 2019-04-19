# -*- coding: utf-8 -*-
###############################################################################
####################              任务实现5.2               ####################
###############################################################################

# 正常方式


def add(x):
    x += 3
    return x


new_numbers = []
for i in range(10):
    new_numbers.append(add(i))  # 调用add()函数，并append到list中
print(new_numbers)


# lambda函数方式（匿名函数）
lam = lambda x: x + 3
n2 = []
for i in range(10):
    n2.append(lam(i))
print(n2)


# 或者
lam = lambda x: x + 3
n1 = []
[n1.append(lam(i)) for i in range(10)]
print(n1)

# map函数方式
numbers = list(range(10))
map(add, numbers)
aa = list(map(lambda x: x + 3, numbers))
print(aa)
print([aaa ** 2 for aaa in aa])  # 速度快，可读性强
