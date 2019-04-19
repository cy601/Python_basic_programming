# -*- coding: utf-8 -*-
###############################################################################
####################               正文代码                 ####################
###############################################################################

# 代码 6-17
class Cat():
    def __init__(self):
        self.name = '猫'
        self.age = 4
        self.info = [self.name, self.age]
        self.index = -1

    def run(self):
        print(self.name, '--在跑')

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def __iter__(self):
        print('名字 年龄')
        return self

    def next(self):
        if self.index == len(self.info) - 1:
            raise StopIteration
        self.index += 1
        return self.info[self.index]


class Bosi(Cat):
    def setName(self, newName):
        self.name = newName

    def eat(self):
        print(self.name, '--在吃')


# 创建对象
bs = Bosi()
# 继承父类的属性和方法
print('bs的名字为:', bs.name)
print('bs的年龄为:', bs.age)
print(bs.run())
# 子类的属性和方法

bs.setName('波斯猫')
bs.eat()
# 迭代输出父类的属性
iterator = iter(bs.next, 1)
for info in iterator:
    print(info)


# 代码 6-18
class animal():
    def __init__(self, age):
        self.__age = age

    def print2(self):
        print(self.__age)


class dog(animal):
    def __init__(self, age):
        animal.__init__(self, age)

    def print2(self):
        print(self.__age)


a_animal = animal(10)
a_animal.print2()
a_dog = dog(10)
a_dog.print2()  # 程序报错


# 代码 6-19
# 定义一个父类
class A(object):
    def __init__(self):
        print("   ->Input A")
        print("   <-Output A")


# 定义一个子类
class B(A):
    def __init__(self):
        print("  -->Input B")
        A.__init__(self)
        print("  <--Output B")


# 定义另一个子类
class C(A):
    def __init__(self):
        print(" --->Input C")
        A.__init__(self)
        print(" <---Output C")


# 定义一个子类
class D(B, C):
    def __init__(self):
        print("---->Input D")
        B.__init__(self)
        C.__init__(self)
        print("<----Output D")


d = D()  # python中是可以多继承的，父类中的方法、属性，子类会继承。

issubclass(C, B)  # 判断一个类是不是另一个类的子孙类
issubclass(C, A)


# 代码 6-20
class Cat:
    def sayHello(self):
        print("喵-----1")


class Bosi(Cat):
    def sayHello(self):
        print("喵喵----2")


bosi = Bosi()
bosi.sayHello()  # 子类中的方法会覆盖掉父类中同名的方法
