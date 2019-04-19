# -*- coding: utf-8 -*-
###############################################################################
####################               正文代码                 ####################
###############################################################################

# 代码 5-1
def my_function(parameter):
    '''打印任何传入的字符串'''
    print(parameter);  # print与return没有关系，也不会相互影响
    return 'parameter is ' + parameter  # 分号与C语言中一样是断句，但在R语言中不行


# 代码 5-2
def interest(money, day=1, interest_rate=0.05):
    income = 0
    income = money * interest_rate * day / 365
    print(income)


# 代码 5-3
interest(5000)  # 本金为5000，年化利率为默认值0.05时的单日利息

interest(10000)  # 本金为10000，年化利率为默认值0.05时的单日利息


# 代码 5-4
def exp(x, y, *args):
    print('x:', x)
    print('y:', y)
    print('args:', args)


exp(1, 5, 66, 55, 'abc')


# 代码 5-5
def exp(x, y, *args, **kwargs):
    print('x:', x)
    print('y:', y)
    print('args:', args)
    print('kwargs:', kwargs)


exp(1, 2, 2, 4, 6, a='c', b=1, ss=5)


# 代码 5-6
def interest_r(money, day=1, interest_rate=0.05):
    income = 0
    income = money * interest_rate * day / 365
    return income


# 代码 5-7
x = interest(1000)

y = interest_r(1000)
y

# 代码 5-8
list(range(0, 10, 2))  # 按start=0,stop=10,step=2的顺序传入

list(range(10, 0, 2))  # 调转strart和stop的顺序传入

list(range(10, 2, 0))  # 调转全部参数的顺序传入

# 代码 5-9
list(range(0, 10, 1))

list(range(10))

# 代码 5-10
interest(money=5000, day=7, interest_rate=0.06)

interest(day=7, money=5000, interest_rate=0.06)

# 代码 5-11
interest(10000, day=7, interest_rate=0.06)

interest(10000, interest_rate=0.06, day=7)

interest(7, interest_rate=0.06, money=10000)  # 位置参数必须在关键字参数前面，否则会报错

# 代码 5-12
arg = [0, 10, 2]
list(range(*arg))


# 代码 5-13
def user(username, age, **kwargs):
    print('username:', username,
          'age:', age,
          'other:', kwargs)


user('john', 27, city='guangzhou', job='Data Analyst')

kw = {'age': 27, 'city': 'guangzhou', 'job': 'Data Analyst'}
user('john', **kw)


# 代码 5-14
def mean(*args):  # 定义求均值函数
    m = 0

    def sum(x):  # 内建求和函数
        sum1 = 0
        for i in x:
            sum1 += i
        return sum1

    m = sum(args) / len(args)
    return m


# 代码 5-15
def means(*args):
    def sum(x):
        sum1 = 0
        for i in x:
            sum1 += i
        return sum1

    return sum(args) / len(args)  # 直接返回sum函数的结果


# 代码 5-16
def sum(*arg):
    sum1 = 0
    for i in range(len(arg)):
        sum1 += arg[i]
    return sum1


# 代码 5-17
sum(1, 2, 3, 4, 5)

sum1

# 代码 5-18
sum0 = 10


def fun():
    sum_global = sum0 + 100
    return sum_global


fun()

# 代码 5-19
sum1 = 0


def sum(*arg):
    for i in range(len(arg)):
        sum1 += arg[i]
    return sum1


sum(1, 2, 3, 4)

# 代码 5-20
sum1 = 10


def sum(*arg):
    sum1 = 0
    for i in range(len(arg)):
        sum1 += arg[i]
    return sum1


sum(1, 3, 4, 5)

# 代码 5-21
sum1 = 0


def sum(*arg):
    global sum1
    for i in range(len(arg)):
        sum1 += arg[i]
    return sum1


sum(1, 3, 5, 7)

sum1

sum(1, 3, 5, 7)
