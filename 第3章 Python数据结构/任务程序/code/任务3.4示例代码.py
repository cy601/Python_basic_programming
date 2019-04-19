# -*-coding:utf-8-*-
###############################################################################
####################               正文代码                 ####################
###############################################################################
#代码 3-26
mydict1={'myint':1,'myfloat':3.1415,'mystr':'name',               # 使用花括号创建字典
         'myint':100,'mytuple':(1,2,3),'mydict':{}}               # 重复键采用最后出现的对应值
mydict1
empty_dict={}                                                     # 创建空字典
empty_dict

#代码 3-27
mydict1=dict([('myint',1),('myfloat',3.1415),('mystr','name'),    # 使用dict( )转换列表对象为字典
              ('myint',100),('mytuple',(1,2,3)),('mydict',{})])
mydict1
mydict2=dict(zero=0,one=1,two=2)
mydict2
empty_dict=dict()
empty_dict

#代码 3-28
mydict3={'spring':(3,4,5),'summer':(6,7,8),'autumn':(9,10,11),'winter':(12,1,2)}
mydict3['autumn']                                                 # 提取键为’autumn’的对应值
mydict3['Spring']                                                 # 提取字典中不存在的键’Spring’所对应的值

#代码 3-29
'Spring' in mydict3                                               # 使用in检查传入键是否存在

#代码 3-30
mydict3.get('summer')                                             # 传入存在的键并返回对应值
mydict3.get('Spring')                                             # 仅传入不存在的键，不显示任何东西
print(mydict3.get('Spring'))                                      # 打印函数返回的结果
mydict3.get('Spring','Not in this dict')                          # 传入不存在的键并返回代替值

#代码 3-31
country=dict(China='Beijing',                                     # 使用dict( )函数创建字典
America='Washington',
Britain='London',
French='Paris',
Canada='Ottawa')
country_copy=country.copy()                                       # 创建一个副本字典对象
country_copy['Russian']='Moscow'                                  # 增添元素
country_copy

#代码 3-32
others=dict(Australia='Canberra',
Japan='tokyo',
Canada='OTTAWA')
country.update(others)                                            # 使用update( )函数增添多个元素
country

#代码 3-33
country_copy=country.copy()
del country_copy['Canada']                                       # 使用del删除副本字典中的元素
country_copy

#代码 3-34
old_value=country.pop('Canada')                                  # 将键对应的值赋值给变量，并删除键值对
old_value
country

#代码 3-35
country_copy=country.copy()
country_copy.clear()                                             # 清空副本字典内容
country_copy

#代码 3-36
country['Japan']='Tokyo'                                         # 直接将新值赋值给对应元素
country

#代码 3-37
# 判断键是否存在于字典当中
'Canada' in country
# 获取所有键
all_keys=country.keys()                                          # 使用函数keys( )得到全部键
all_keys
# 判断值是否存在于字典当中
all_values=country.values()                                      # 使用函数values( )得到全部值
all_values
'Beijing' in all_values                                          # 判断字典是否包含值
list(all_values)                                                 # 将值的迭代形式转换为列表
# 判断键值对是否存在于字典当中
all_items=country.items()                                        # 使用函数items( )得到全部键值对
all_items
('America','Washington') in all_items                            # 判断字典是否包含键值对
list(all_items)                                                   # 将键值对迭代形式转换为列表

#代码 3-38
# 提取字典中值为True所对应的键
test={'A':100,'B':300,'C':True,'D':200}
keys=list(test.keys())                                            # 提取字典中所有键
values=list(test.values())                                        # 提取字典中所有值
keys
values
keys[values.index(True)]                                          # 故利用值True的索引来提取对应的键


