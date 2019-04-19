# -*- coding: utf-8 -*-
###############################################################################
####################              任务实现5.3               ####################
###############################################################################

import var  # 导入封装好的函数模块var

var1 = var.var(1, 3, 5, 7, 9, 11, 13)
print(var1)


from var import var  # 导入模块中的函数var.var
var2 = var(5, 6, 7, 8, 9)
print(var2)


from var import var as fangcha  # 给函数指定别名fangcha
var3 = fangcha(1, 2, 3, 4, 5, 6)
print(var3)


import var as V  # 给函数模块指定别名V
var4 = V.var(8, 9, 10, 11)
print(var4)


from var import *  # 导入模块中的所有函数
