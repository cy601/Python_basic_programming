# -*- coding: utf-8 -*-
###############################################################################
####################               正文代码                 ####################
###############################################################################

# 代码 6-1
class Cat():
    """一次模拟猫咪的简单尝试"""
    # 属性
    name = 'tesila'
    age = 3

    # 方法
    def sleep(self):
        """模拟猫咪被命令睡觉"""
        print('%d岁的%s正在沙发上睡懒觉。' % (self.age, self.name))

    def eat(self, food):
        """模拟猫咪被命令吃东西"""
        self.food = food
        print('%d岁的%s在吃%s' % (self.age, self.name, self.food))


new_cat = Cat()
print(new_cat.sleep())
print(new_cat.eat('fish'))


# 代码 6-2
class Cat():
    def sleep(self):
        print(self)


new_cat = Cat()
print(new_cat.sleep())


# 代码 6-3
class Test:
    def prt(my_address):
        print(my_address)
        print(my_address.__class__)


t = Test()
t.prt()


# 代码 6-4
class Example():
    pass


example = Example()
dir(example)
