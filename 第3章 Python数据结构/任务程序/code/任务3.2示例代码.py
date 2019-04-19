# -*-coding:utf-8-*-
###############################################################################
####################               正文代码                 ####################
###############################################################################
#代码 3-1
mylist1=[1,2.0,['three','four',5],6.5,True]            # 创建包含混合数据类型的嵌套列表
mylist1                                                # 查看列表内容
empty_list=[]                                          # 创建空列表
empty_list

#代码 3-2
mylist1=list((1,2.0,['three','four',5],6.5,True))     # 向list( )函数传入一个元组对象
mylist1
type(mylist1)                                          # 查看对象类型
empty_list=list()                                      # 创建空列表
empty_list
mylist2=list(['one','two','three'])                    # 向list( )函数传入一个列表对象
mylist2

#代码 3-3
list('hello world!')                                   # 向函数list( )传入一个字符串

#代码 3-4
mylist3=['Sunday','Monday','Tuesday',
         'Wednesday','Thursday','Friday']
mylist3[1]                                             # 提取列表中第2个元素
mylist3[-3]                                            # 提取列表中倒数第3个元素

#代码 3-5
mylist3[7]                                             # 传入索引大于最后一个元素的正索引
mylist3[-10]                                           # 传入索引小于第一个元素的负索引

#代码 3-6
# 步长为正数时的切片操作
mylist4=[10,20,30,40,50,60,70,80,90,100]
mylist4[2:7]                                           # 提取从第3个元素到第8个元素前的所有元素
mylist4[1:9:2]                                         # 提取从第2个元素到第10个元素前的所有元素，步长为2
# 步长为负数时的切片操作
mylist4[-2:-8:-2]                                      # 提取从倒数第2个元素到倒数第8个元素前的所有元素，步长为2
mylist4[1:4:0]                                         # 步长为0时会报错

#代码 3-7
# 省略起始索引
mylist4[:-7:-2]                                        # 提取从结尾向左到倒数第7个元素前的所有元素，步长为2
mylist4[6:]                                            # 提取从第7个元素到列表右端最后一个元素之间的所有元素
mylist4[::-2]                                          # 提取从右端开始到左端之间的全体元素，步长为2
mylist4[::-1]                                          # 提取从右端开始到左端之间的全体元素，步长为1，即列表反转

#代码 3-8
# 传入索引超出列表索引范围
mylist4[3:100:2]                                       # 提取从第4个元素到右端之间的全体元素，步长为2
mylist4[-5:-20:-1]                                     # 提取从倒数第5个元素到左端之间的全体元素
# 起始索引无法达到终止索引
mylist4[6:2]                                           # 提取从第7个元素向右到第3个元素之间的所有元素

#代码 3-9
month=['January','February','March','April','May','June']
month.append('July')                                   # 使用append( )函数向列表尾部追加元素
month                                                  # 查看列表内容

#代码 3-10
month_copy= month.copy()                               # 创建一个列表对象month的副本，理由稍后解释
month_copy
others=['August','September','November','December']
month.extend(others)                                   # 使用extend( )函数将两个列表进行合并
month
month_copy+=others                                     # 对副本进行自增运算
month_copy

#代码 3-11
month.insert(9,'October')                              # 在列表第10个位置上插入元素
month
month.insert(20,'None')                                # 插入位置超出列表尾端
month

#代码 3-12
month_copy=month.copy()                                # 创建一个列表对象month副本
del month_copy[-1]                                     # 删除副本中最后一个元素
month_copy

#代码 3-13
month_copy=month.copy()                                # 创建一个列表对象month副本
month_copy.pop(3)                                      # 获取并删除第4个元素
del_element=month_copy.pop()                           # 将最后一个元素赋值给一个变量并在副本中删除
del_element                                            # 查看删除元素
month_copy                                             # 查看副本

#代码 3-14
month.remove('None')                                   # 删除列表中的元素’None’
month

#代码 3-15
month[0]='Jan'                                         # 将第一个元素改为缩写形式
month

#代码 3-16

a=[1,2,3,4]                                            # 变量名a指向列表对象[1,2,3,4]
b=a                                                    # 变量名b也指向列表对象[1,2,3,4]
a.append(5)                                            # 列表尾端追加元素5
a
b                                                      # 通过变量名b查看列表
b[2]='three'                                           # 修改副本第3个元素
b
a                                                      # 列表并没有发生变化
c
d

#代码 3-17
a=[10,20,30,40,50]
b=a.copy()                                             # 使用copy( )函数创建副本
c=a[:]                                                 # 使用切片操作创建副本
d=list(a)                                              # 使用list( )函数创建副本
id(a),id(b),id(c),id(d)                                # 查看各变量对象id

#代码 3-18
# index( )方法查询元素位置
letter=['A','B','A','C','B','B','C','A']
letter.index('C')                                      # 查询元素’C’在列表中第一次出现的位置
# 使用in判断列表是否包含元素
'A' in letter

#代码 3-19
# 使用count( )函数进行元素计数
letter=['B','A','C','D','A','C','D','A']
letter.count('A')                                      # 获取元素’A’在列表中出现的次数
# 使用sort( )函数和sorted( )函数对列表进行排序
sorted(letter)                                         # 使用sorted( )函数对列表进行排序，不改变列表
letter
letter.sort()                                          # 使用列表方法sort( )进行排序，改变列表内容
letter
letter.sort(reverse=True)                              # 对列表进行倒序排序
letter
# 使用reverse( )函数反转列表
season=['spring','summer','autumn','winter']
season.reverse()                                        # 反转列表
season
# 使用函数len( )获取列表长度
len(season)
# 使用列表加法合并两个列表
[1,2,3]+[4,5,6]
# 使用列表乘法重复合并列表
[10,20,30,40]*3



