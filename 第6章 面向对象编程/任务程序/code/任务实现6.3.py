# -*- coding: utf-8 -*-
###############################################################################
####################              任务实现6.3               ####################
###############################################################################

class Car():
    # 构造器方法
    def __init__(self, newWheelNum, newColor):
        self.wheelNum = newWheelNum
        self.color = newColor

    # 方法(函数)
    def run(self):
        print('车在跑，目标:夏威夷。')

    # 析构方法
    def __del__(self):
        print('---析构方法被调用---')


# 创建对象
BMW = Car(4, 'green')
# 访问属性
print('车的颜色为:', BMW.color)
print('车轮子数量为:', BMW.wheelNum)
# 调用对象的run方法
BMW.run()
# 删除对象
del BMW
# 查看是否删除
print(BMW)
