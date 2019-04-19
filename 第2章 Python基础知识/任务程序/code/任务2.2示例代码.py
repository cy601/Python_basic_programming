# -*-coding:utf-8-*-
###############################################################################
####################               正文代码                 ####################
###############################################################################
#代码 2-12
# 1.创建变量x
x = 4
id(x)                     # 查看变量x指向的内存地址
# 2.将变量x重新赋给另一个新变量y
y = x
id(y)
# 3.对变量x重新赋值
x = 2
x,y                      # 同时输出变量x和变量y的值
id(x)
id(y)

#代码 2-13
# 1.保留字做变量名时
import keyword                         # 加载keyword库
keyword.iskeyword("and")                # 判断“and”是否为保留字
and = "我是保留字"                      # 以保留字作为变量名
# 2.特殊字符串做变量名时
strExample = "我是一个字符串"            # 创建一个字符串变量
len(strExample)                          # 使用len()查看字符串长度
len = "特殊字符串命名"                   # 使用len()作为变量名
len
len(strExample)                          # len()查看字符串长度出错

#代码 2-14
a = b = c = 1                            # 一个值赋给多给变量
a
b
c

#代码 2-15
a,b ,c = 1,2,"abc"                        # 多个变量同时赋值
a
b
c

#代码 2-16
# 其他类型数据转成整型int
int(1.56) ;  int(0.156) ;  int(-1.56) ;  int()         # 浮点数转整型
int(True) ;  int(False)                          # 布尔型转整型	
int(1+23j)                                    # 复数转整型

#代码 2-17
#  其他类型转成布尔型bool
bool(1) ;   bool(2) ;   bool(0)                          # 整型转布尔型
bool(1.0) ;   bool(2.3) ;   bool(0.0)                     # 浮点数转布尔型
bool(1+23j) ;   bool(23j)                               # 复数转布尔型
bool();bool("") ;   bool([]);   bool(());   bool({})         # 各种类型的空值转布尔型

#代码 2-18
'This is a sentence.'                    # 单引号标识字符串

#代码 2-19
"This is a sentence."                    # 双引号标识字符串

#代码 2-20
# 三个单引号标识的一段字符串
paragraph = '''\
This is the first sentence.
   This is the second sentence.
   This is the third sentence.'''
print(paragraph)

#代码 2-21
'What's happened'                          # 单引号标识的字符串中含有单引号
'What\'s happened'                         # 反斜杠（\）转义单引号

#代码 2-22
"What's happened"                        # 双引号标识含有单引号的字符串
" Double quotes(\")"                       # 双引号标识的字符串里面的双引号需要转义
print('Backslash(\\)')                       # 转义反斜杠

#代码 2-23
print('D:\name\python')                    # 以反斜杠开头的特殊字符
print(r'D:\name\python')                   # 用r(或者R)指定原始字符串

#代码 2-24
word = 'Python'
word[1]                              # 提取第二个字符
word[0]                              # 提取第一个字符
word[-1]                             # 提取最后一个字符

#代码 2-25
word[0:3]                                # 截取第一到第三个字符
word[:3]                                 # 截取第一到第三个字符
word[4:]                                 # 截取第五到最后一个字符

#代码 2-26
word[3:52]                            # 第二个索引越界
word[52:]                              # 第一个索引超出字符串长度
word[-1:3]                              # 第一个索引为负，第二个索引正常
word[5:3]                               # 第一个索引大于第二个索引

#代码 2-27
word[0] = 'p'                             # 字符不可被修改

#代码 2-28
'Python is' + 3 *  ' good'                     #  加号拼接字符串
'Python is' ' good'                           #  相邻字符串自然拼接

#代码 2-29
sentence = 'Life is short,you need something.'
sentence[:23] + 'Python.'

