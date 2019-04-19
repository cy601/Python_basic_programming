# -*-coding:utf-8-*-
###############################################################################
####################               正文代码                 ####################
###############################################################################
task_tuple=['pen','paper',10,False,2.5]
type(task_tuple)
task_tuple=tuple(task_tuple)                 # 转换列表对象为元组类型
type(task_tuple)                             # 查看对象的数据类型
Index=task_tuple.index(False)                # 查询元素位置索引
bool=task_tuple[Index]                       # 提取元组元素
print(bool)                                  # 查看提取元素

