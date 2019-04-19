intCount = 0
strCount = 0
otherCount = 0
v = input("请输入语句:")

for i in range(0, len(v)):
    if v[i].isdigit():
        intCount += 1
    elif v[i].isalpha():
        strCount += 1
    else:
        otherCount += 1
print("整型有%d个" % intCount)
print("字符串有%d个" % strCount)
print("其他类型有%d个" % otherCount)
