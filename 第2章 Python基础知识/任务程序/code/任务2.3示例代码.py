# -*-coding:utf-8-*-
###############################################################################
####################               正文代码                 ####################
###############################################################################
#代码 2-30
2 / 1 ;  type(2 / 1)                                               # 单斜杠除法
2 // 1 ;  type(2 // 1)                                              # 双斜杠除法
print(1 + 2,'and',1.0 + 2) ;  print(1 * 2,'and',1.0 * 2)                  # 加法和乘法
print('23除以10，商为：',23 // 10,'，余数为：',23 % 10)            # 商和余数
3 * 'Python'                                                    # 字符串的n次重复

#代码 2-31
1 == 2 ;  1 != 2                                               # 数值的比较
print('a' == 'b', 'a' != 'b') ;  print( 'a' < 'b','a' > 'b')               # 字母的比较
print(ord('a'),ord('b'))                                         # 查看字母编码
print(chr(97),chr(98))                                          # 查看编码对应的字符
'# ' < '$'                                                      # 符号的比较

#代码 2-32
a = 1 + 2 ;  print(a)                                                 # 简单赋值运算
print('a：',a) ;   a += 4 ;  print('a += 4特殊赋值运算后，a：',a)        # 特殊赋值运算
f += 4                                                   # 未定义变量不能进行特殊赋值运算

#代码 2-33
a = 60 ;  b = 13 ;  print('a = 60,b =13')                                     # 初始赋值
print('a & b =',a & b) ;   print('a | b =',a | b) ;   print('a ^ b =',a ^ b)          # 或、与、异位运算
print('~a =',~a) ;   print('a << 2 =', a << 2) ;   print('a >> 2 =', a >> 2)        # 取反和位移运算

#代码 2-34
a = 11;b = 22;print('a = 11,b =22')                                             # 初始赋值
print('a and b =',a and b); print('a or b =',a or b); print('not(a and b) =', not(a and b));    # and、or、not运算
print('a and b =',a and b); print('a or b =',a or b); print('not(a and b) =', not(a and b));    # and、or、not运算

#代码 2-35
True & True ;   True and True                     # 按位&、逻辑and 
True | False ;   True or False;                      # 按位|、逻辑or
True & False ;   True and False;                                        
False | False ;  False or False;   

#代码 2-36
List = [1,2,3.0,[4,5],'Python3']                     # 初始化列表List
1 in List                                       # 查看1是否在列表内
[1] in List                                      # 查看[1]是否在列表内   
3 in List                                       # 查看3是否在列表内
[4,5] in List                                     # 查看[4,5]是否在列表内
'Python' in List                                 # 查看字符串’Python’是否在列表内
'Python3' in List                                # 查看字符串’Python3’是否在列表内

#代码 2-37
a = 11 ;  b = 11 ;  print('a = 11,b = 11')                     # 初始化a、b
a is b ;  a is not b                                       # 身份运算
id(a) ;  id(b)                                            # 查看id地址   
a = 11 ;  b = 22 ;  print('a = 11,b = 22')                     # 重新赋值b
a is b ;  a is not b                                       # 身份运算
id(a) ;  id(b)                                            # 查看id   

#代码 2-38
24 + 12 / 6 ** 2 * 18                            # 24+12/36*18 → 24+(1/3)*18 → 24+6
24 + 12 / ( 6 ** 2 ) * 18                          # 24+12/36*18 → 24+(1/3)*18 → 24+6
24 + ( 12 / ( 6 ** 2 ) ) * 18                        # 24+(12/36)*18 → 24+(1/3)*18 → 24+6   
24 + ( 12 / 6 ) ** 2 * 18                          # 24+2**2*18 → 24+4*18 → 24+72
( 24 + 12 ) / 6 ** 2 * 18                          # 36/6**2*18 → 36/36*18 → 1*18
- 4 * 5 + 3                                     # -20+3    
4 * - 5 + 3                                     # -20+3  
