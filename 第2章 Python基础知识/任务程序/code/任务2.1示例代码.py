# -*-coding:utf-8-*-
###############################################################################
####################               正文代码                 ####################
###############################################################################
#代码 2-1
# 这是一个单独成行的注释
print("Hello,World!")                   # 这是一个在代码后面的注释

#代码 2-2
# 这是一个使用# 号的多行注释
# 这是一个使用# 号的多行注释
# 这是一个使用# 号的多行注释
print("Hello,World!")

#代码 2-3
'''
该多行注释使用的是三个单引号
该多行注释使用的是三个单引号
该多行注释使用的是三个单引号
'''
print("Hello,World!")

#代码 2-4
"""
该多行注释使用的是三个双引号
该多行注释使用的是三个双引号
该多行注释使用的是三个双引号
"""
print("Hello,World!")


#代码 2-5
# 使用反斜杠（\）的多行一个语句
total = applePrice +\
      bananaPrice + \
      pearPrice

#代码 2-6
# []中的多行语句只需要回车即可
total = [applePrice ,
      bananaPrice ,
      pearPrice]

#代码 2-7
# 使用分号（;）的一行多语句
applePrice = 8;  bananaPrice = 3.5;  pearPrice = 5     

#代码 2-8
# 代码块包含相同的空格数
if True :
    print('我的行缩进空格数相同')
else :
    print('我的缩进空格数不同')
	
#代码 2-9
# 代码块包含的空格数不同
if True :
       print('我的行缩进空格数相同')
else :
       print('错误示范')
   print('我的缩进空格数不同')
   
   
#代码 2-10
import keyword
keyword.iskeyword("and")         # 查看“and”是否为保留字
keyword.kwlist                   # 查看Python3中所有的保留字
	
#代码 2-11
print "Hello,World!"            #缺少括号
print(‘Hello,World!’)          #引号为中文输入引号
print（'Hello,World!'）        #括号为中文输入括号
