# -*-coding:utf-8-*-
###############################################################################
####################               正文代码                 ####################
###############################################################################
set1=['apple','pear','watermelon','peach']
set2=list(('pear','banana','orange','peach','grape'))
set1=set(set1)                                           # 转换列表对象为集合类型
set2=set(set2)
type(set1);type(set2)                                    # 查看转换后数据类型
print(set1|set2 )                                              # 求出并集
print(set1&set2)                                               # 求出交集
print(set1-set2 )                                               # 求出差集set1-set2
print(set2.difference(set1) )                                   # 求出差集set2-set1