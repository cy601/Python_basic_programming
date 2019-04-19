# -*-coding:utf8-*-
###############################################################################
####################               正文代码                 ####################
###############################################################################
applePriceStr = 'Apple\'s unit price is 9 yuan.'
applePrice = applePriceStr[22]                                                     # 提取数值
print('提取了苹果的单价为：',applePrice,'。此刻他的数据类型为：',type(applePrice))
applePrice = int(applePrice)                                                       # 字符转数值
print('转换数据类型后：',type(applePrice))