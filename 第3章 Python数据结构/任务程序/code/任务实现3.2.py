# -*-coding:utf-8-*-
###############################################################################
####################               正文代码                 ####################
###############################################################################
task_list=[110,'dog','cat',120,'apple']
task_list.insert(2,[])                       # 插入空列表
task_list.remove('apple')                    # 删除元素
num_index=task_list.index(110)               # 查询元素位置
task_list[num_index]*=10                     # 将查询出来的元素进行自乘运算赋值修改
num_index=task_list.index(120)
task_list[num_index]*=10
print(task_list)                             # 查看修改后的列表对象
