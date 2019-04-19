# -*- coding: utf-8 -*-
###############################################################################
####################              任务实现6.5               ####################
###############################################################################

class Car():
    def __init__(self, brand, newWheelNum, newColor, T):
        self.brand = brand
        self.wheelNum = newWheelNum
        self.color = newColor
        self.T = T  # T为废气涡轮增压
        self.info = [self.brand, self.wheelNum, self.color, self.T]
        self.index = -1

    def getBrand(self):
        return self.brand

    def getNewheelnum(self):
        return self.wheelNum

    def getNewcolor(self):
        return self.color

    def getT(self):
        return self.T

    def __iter__(self):
        print('品牌 车轮数 颜色 废气涡轮增压')
        return self

    def next(self):
        if self.index == 3:
            raise StopIteration
        self.index += 1
        return self.info[self.index]


class Land_Rover(Car):
    def __init__(self, brand, newColor):
        self.brand = brand
        self.wheelNum = 4
        self.color = newColor
        self.T = 3
        Car.__init__(self, self.brand, self.wheelNum, self.color, self.T)


# 创建对象
Luxury_car = Land_Rover('Land_Rover', 'black')
# 访问属性
print(Luxury_car.getNewcolor())
# 迭代输出对象的属性
iterator = iter(Luxury_car.next, 1)
for info in iterator:
    print(info)
