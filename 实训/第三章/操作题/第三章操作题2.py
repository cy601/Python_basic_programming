dict = {'小明': '4月1日', '老王': '4月1日', '小强': '9月10日'}
print(dict)
dict['小明'] = '5月1日'
dict.pop('老王')
dict['小王'] = '10月1日'
print("修改后的字典", dict)
