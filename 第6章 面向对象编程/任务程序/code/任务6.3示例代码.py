# -*- coding: utf-8 -*-
###############################################################################
####################               正文代码                 ####################
###############################################################################

# 代码 6-5
class Cat():
    """再次模拟猫咪的简单尝试"""

    # 构造器方法
    def __init__(self, name, age):
        # 属性
        self.name = name
        self.age = age

    def sleep(self):
        """模拟猫咪被命令睡觉"""
        print('%d岁的%s正在沙发上睡懒觉。' % (self.age, self.name))

    def eat(self, food):
        """模拟猫咪被命令吃东西"""
        self.food = food
        print('%d岁的%s在吃%s' % (self.age, self.name, self.food))


# 代码 6-6
class Animal():
    # 构造方法
    def __init__(self):
        print('---构造方法被调用---')
        # 析构方法

    def __del__(self):
        print('---析构方法被调用---')


cat = Animal()
print(cat)
# 删除对象
del cat
# print(cat)


# 代码 6-7
class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        """模拟猫咪被命令睡觉"""
        print('%d岁的%s正在沙发上睡懒觉。' % (self.age, self.name))

    def eat(self, food):
        """模拟猫咪被命令吃东西"""
        self.food = food
        print('%d岁的%s在吃%s。' % (self.age, self.name, self.food))


# 创建对象
cat1 = Cat('Tom', 3)
cat2 = Cat('Jack', 4)
# 访问对象的属性
print('Cat1的名字为:', cat1.name)
print('Cat2的名字为:', cat2.name)
# 访问对象的方法
print(cat1.sleep())
print(cat2.eat('fish'))

# 代码 6-8
cat1 = Cat('Tom', 3)
sleep = cat1.sleep
print(sleep())
cat2 = Cat('Jack', 4)
eat = cat2.eat
print(eat('fish'))

# 代码 6-9
print(cat1.age)
print(cat2.name)


# 代码 6-10
class Cat():
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def sleep(self):
        """模拟猫咪被命令睡觉"""
        print('%d岁的%s正在沙发上睡懒觉。' % (self.__age, self.__name))

    def eat(self, food):
        """模拟猫咪被命令吃东西"""
        self.__food = food
        print('%d岁的%s在吃%s。' % (self.__age, self.__name, self.__food))

    def getAttribute(self):
        return self.__name, self.__age


# 创建对象
cat1 = Cat('Tom', 3)
cat2 = Cat('Jack', 4)
# 访问对象的属性
print('Cat1的名字为:', cat1.name)
print('Cat2的名字为:', cat2.name)
# 访问对象的方法
print(cat1.sleep())
print(cat2.eat('fish'))
print(cat1.getAttribute())

# 代码 6-11
print(cat1._Cat__name)
print(cat1._Cat__age)
