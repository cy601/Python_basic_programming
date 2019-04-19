# -*- coding: utf-8 -*-
###############################################################################
####################               正文代码                 ####################
###############################################################################

# 代码 6-12
for element in [1,2,3]:
    print(element)
for element in (1,2,3):
    print(element)
for key in {'one':1,'two':2}:
    print(key)
for char in '123':
    print(char)
for line in open('myfile.txt'):
    print(line)
    
# 代码 6-13
L = [1,2,3]
it = iter(L)
it
next(it)
next(it)
next(it)
next(it)

# 代码 6-14
class Cat():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.info = [self.name,self.age]
        self.index = -1
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def __iter__(self):
        print('名字 年龄')
        return self
    def next(self):
        if self.index == len(self.info)-1:
            raise StopIteration
        self.index += 1
        return self.info[self.index]

# 创建对象
newcat = Cat('coffe', 3)
# 访问对象的属性
print(newcat.getName())
# 迭代输出对象的属性
iterator = iter(newcat.next,1)
for info in iterator:
    print(info)

# 代码 6-15
import sys
def fibonacci(n,w=0): # 生成器函数——斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        print('%d,%d' % (a,b))
        counter += 1
f = fibonacci(10,0) # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print (next(f), end=" ")
    except :
        sys.exit()

# 代码 6-16
import sys
def fibonacci(n,w=0): # 生成器函数——斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        # yield a        # 不执行yield语句
        a, b = b, a + b
        print('%d,%d' % (a,b))
        counter += 1
f = fibonacci(10,0) # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print (next(f), end=" ")
    except :
        sys.exit()
