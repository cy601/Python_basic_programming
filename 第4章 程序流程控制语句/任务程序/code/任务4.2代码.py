# -*- coding: utf-8 -*-
###############################################################################
####################               正文代码                 ####################
###############################################################################
#代码 4-3
# 对列表和字符串进行迭代
for a in ['e','f','g']:
    print(a)

for a in 'string':
    print(a)

#代码 4-4
s = 0
while(s <= 1):
    print('计数：', s)
    s = s + 1

#代码 4-5
s = 1
while(s <= 1):
    print('无限次循环')

#代码 4-6
for i in range(0,5):
    print(i)

for i in range(0,6,2):
    print(i)
    
#直接使用for循环难以改变序列元素
L = [1,2,3]
for a in L:
    a+=1                      #a不是引用，L中对应的元素没有发生改变
print(L)

# range与len函数遍历序列并修改元素
for i in range(len(L)):
    L[i]+=1                    #通过索引访问
print(L)

#代码 4-7
s = 0
while True:
    s+=1
    if s == 6:                     #满足s等于6的时候跳出循环
	break
s

for i in range(0,10):
    print(i)
    if i == 1:                     #当i等于1的时候跳出循环
	break

#代码 4-8
s = 3
while s > 0:
    s = s - 1
    if s == 1:                    #当s等于1时跳出循环
	continue
    print(s)

for i in range(0,3):
    if i == 1:                    #当i等于1时跳出循环
	continue
    print(i)

#代码 4-9
for i in range(0,3):
    if i == 1:
	pass
	print('pass块')
    print(i)



