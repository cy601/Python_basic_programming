import math

n = int(input("请输入要参与计算的数字的个数:"))
num = [int(input('请输入第 %d 个数字:\n' % i)) for i in range(1, n + 1)]
print(num)
# a = float(input("please input the first number"))
# b = float(input("please input the second number"))
# c = float(input("please input the third number"))
sum = 0
for i in range(n):
    sum += num[i]
average = sum / n
power = 0
for i in range(n):
    power = power + pow(num[i], 2)
power /= n
sd = math.sqrt(power)
print("The average is: %d" % average)
print("The square error is: %f" % average)
print("The standard deviation is: %f" % sd)
