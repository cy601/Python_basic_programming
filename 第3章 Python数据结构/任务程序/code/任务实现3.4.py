# -*-coding:utf-8-*-
###############################################################################
####################               正文代码                 ####################
###############################################################################
score={'Math':96,'English':86,
       'Chinese':95.5,'Biology':86,
       'Physics':None}
score['History']=88                               # 增添键值对
del score['Physics']                              # 删除键值对
new_value=round(score['Chinese'])                 # 将成绩进行四舍五入取整
score['Chinese']=new_value                        # 修改对应值
print(score['Math'] )                              # 查看键的对应值
print(score )                                           # 查看处理后的字典
