# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 17:39:11 2017

@author: Dell
"""


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
