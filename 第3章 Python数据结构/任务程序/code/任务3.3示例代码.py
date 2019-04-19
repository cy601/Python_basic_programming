# -*-coding:utf-8-*-
###############################################################################
####################               正文代码                 ####################
###############################################################################
#代码 3-20
mytuple1=(1,2.5,('three','four'),[True,5],False)            # 使用圆括号( )创建元组
mytuple1
mytuple2=2,True,'five',3.5                                  # 省略圆括号
mytuple2
empty_tuple=()                                              # 创建空元组
empty_tuple

#代码 3-21
mytuple1=tuple([1,2.5,('three','four'),[True,5],False])    # 使用函数tuple( )将列表转换为元组
mytuple1
mytuple2=tuple((2,True,'five',3.5))
mytuple2
empty_tuple=tuple()
empty_tuple

#代码 3-22
mytuple3=('China','America','England','France')
mytuple3[0]                                                 # 提取元组第1个元素
mytuple3[10]                                                # 传入索引超出元组索引范围

#代码 3-23
mytuple3[-2::-1]                                            # 提取元组倒数第２个元素到左端之间所有元素
mytuple3[1:10]                                              # 超出元素索引范围

#代码 3-24
A,B,C,D=mytuple3                                            # 将元组中各元素分别赋值给对应变量
A
C
x,y,z=1,True,'one'                                          # 利用元组解包进行多个变量赋值
x
z

#代码 3-25
# 使用count( )函数进行元素计数
mytuple4=('A','D','C','A','C','B','B','A')
mytuple4.count('B')
# 使用index( )函数获取元素在元组中第一次出现的位置索引
mytuple4.index('C')
# 使用sorted( )对元组元素进行排序
sorted(mytuple4)
# 使用len( )函数获取元组长度
len(mytuple4)
# 使用元组加法合并两元组
(1,2,3)+(4,5,6)
# 使用元组乘法重复合并元组
(10,20,30,40)*3


