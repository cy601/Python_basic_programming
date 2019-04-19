# -*- coding: utf-8 -*-
###############################################################################
####################              任务实现6.2               ####################
###############################################################################

class Car():
    """一次模拟汽车的简单尝试"""
    # 属性
    wheelNum = 4
    color = 'red'

    # 方法
    def getCarInfo(self, name):
        self.name = name
        print(self.name, '有%d个车轮, 颜色是%s。' % (self.wheelNum, self.color))

    def run(self):
        print('车在行驶在学习的大道上。')


new_car = Car()
(new_car.getCarInfo('Land Rover'))
(new_car.run())
