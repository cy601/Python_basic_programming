# -*- coding: utf-8 -*-
###############################################################################
####################             任务实现5.1                ####################
###############################################################################

# 构建方差函数示例：


def var(*args):  # 主体方差函数
    def mean(z):  # 内建均值函数
        def sum(x):  # 内建求和函数
            sum1 = 0
            for i in x:
                sum1 += i
            return sum1

        return sum(args) / len(args)  # 直接返回sum函数的结果

    def sums(y):  # 内建求平方和函数
        sum2 = 0
        for i in y:
            sum2 += i ** 2
        return sum2

    return sums(args) / len(args) - mean(args) ** 2  # 返回sums函数及mean函数的结果并计算方差


print("4,6,8,10这组数的方差为：", var(4, 6, 8, 10))
