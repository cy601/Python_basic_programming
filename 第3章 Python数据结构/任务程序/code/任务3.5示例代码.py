# -*-coding:utf-8-*-
###############################################################################
####################               正文代码                 ####################
###############################################################################
#代码 3-39
# 使用花括号创建可变集合
myset1={'A','C','D','B','A','B'}
myset1
# 使用函数set( )创建可变集合
myset2=set([2,3,1,4,False,2.5,'one'])
myset2
empty_set=set()                                                  # 创建空可变集合
empty_set
type(empty_set)

#代码 3-40
myset3=frozenset([3,2,3,'one',frozenset([1,2]),True])            # 使用函数frozenset( )创建不可变集合
myset3
empty_frozenset=frozenset()                                       # 创建空不可变集合
empty_frozenset
type(empty_frozenset)

#代码 3-41
A={'足球','游泳','羽毛球','乒乓球'}
B={'篮球','乒乓球','羽毛球','排球'}
A|B                                                               # 使用符号’|’获取并集
A.union(B)                                                        # 使用集合方法union( )函数获取并集

#代码 3-42
A&B                                                               # 使用符号’&’获取交集
A.intersection(B)                                                 # 使用集合方法intersection( )函数获取交集

#代码 3-43
A-B                                                               # 使用减号’-’来获取差集
A.difference(B)                                                   # 使用集合方法difference( )函数获取差集

#代码 3-44
A^B                                                               # 使用符号” ^ ”获取异或集
A.symmetric_difference(B)                                         # 使用集合方法symmetric_difference( )函数获取异或集

#代码 3-45
C={'足球','乒乓球','游泳'}
# 判断子集
C<=A                                                              # 使用符号’ <= ’判断子集
C.issubset(A)                                                     # 使用函数issubset( )判断子集
# 判断真子集
C<A;A<A                                                           # 使用符号’ < ’判断真子集
# 判断超集
A>=C                                                              # 使用符号’ >= ’判断超集
A.issuperset(C)                                                   # 使用函数issuperset( )判断超集
# 判断真超集
A>C;C>C                                                           # 使用符号’ > ’判断真超集

#代码 3-46
myset4={'red','green','blue','yellow'}
myset4_copy=myset4.copy()                                         # 创建一个集合副本对象
others={'black','white'}
# 可变集合增添元素
myset4.add('orange')                                              # 使用集合方法add( )函数增添元素
myset4.update(others)                                             # 使用集合方法update( )函数合并两个集合
myset4
# 可变集合删除元素
myset4.pop()                                                      # 使用pop( )函数从集合中抽离出一个元素
myset4                                                            # 查看抽离元素后的集合内容
myset4.remove('yellow')                                           # 使用remove( )删除指定元素
myset4_copy.clear()                                               # 使用clear( )将副本集合内容清空
myset4_copy
# 使用in查看集合是否包含指定元素
'green' in myset4
# 使用len( )函数获取集合元素个数
len(myset4)
