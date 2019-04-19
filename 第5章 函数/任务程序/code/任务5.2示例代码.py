# -*- coding: utf-8 -*-
###############################################################################
####################               正文代码                 ####################
###############################################################################

# 代码 5-22
lambda arguments: expression

example = lambda x : x**3
print(example)
example(2)

# 代码 5-23
from math import log     # 引入Python数学库的对数函数
# 此函数用于返回一个以base为底的匿名对数函数
def make_logarithmic_function(base):
    return lambda x : log(x,base)
# 创建一个以3为底的匿名对数函数，并赋值
my_log = make_logarithmic_function(3)
# 调用匿名函数my_log，底数已经设置为3，只需设置真数。如果用log函数需要同时设置真数和底数。
print(my_log(9))

# 代码 5-24
def add(x):
    x += 3
    return x
numbers = list(range(10))
num1 = list(map(add,numbers))
num2 = list(map(lambda x:x+3,numbers))    # 速度快，可读性强

# 代码 5-25
def fib(n):
    if n <=2 :
        return 2
    else:
        return fib(n-1)+fib(n-2)
f = fib(10)
print(f)

# 代码 5-26
list(filter(lambda x:x%2==1, [1, 4, 6, 7, 9, 12, 17]))

s = list(filter(lambda c:c!='o','i love python and R!'))
s = ''.join(s) #变为字符型
print(s)