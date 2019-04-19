# -*- coding: utf-8 -*-
###############################################################################
####################               正文代码                 ####################
###############################################################################
#代码 4-10
num = zeros(shape=(3,3))
num

for i in range(0,3):
    for j in range(0,3):
        num[i,j] = i * j
num

#代码 4-11

for i in range(0,11):
    while(i > 8):
        print(i*10)
        break

#代码 4-12
for x in range(10,15):                  # 迭代 10 到 15 之间的数字
    for i in range(2,x):                    # 根据因子迭代
        if x%i == 0:                     # 确定第一个因子
            j=x/i                       # 计算第二个因子
            print('%d 等于 %d * %d' % (x,i,j))
            break                         # 跳出当前循环
        else:                              # 循环的 else 部分
            print(x, '是一个质数')
            break                         # 跳出当前循环

#代码 4-13
count = 0
while count < 5:
    if count > 3:
        print(count**2)
    else:
        print(count)
    count = count + 1


