
# -*- coding: utf-8 -*-
###############################################################################
####################               正文代码                 ####################
###############################################################################

# 代码 7-1
f = open('..\\data\\e_point.txt', 'r')

# 代码 7-2
# f = open((os.path.dirname(__file__) + '..//data/Walden.txt', 'r')

# 代码 7-3
f = open('C:\\Users\cy601\Desktop\\2019Spring-智能信息处理应用开发\\20190228Python编程基础-参考代码与习题参考答案\\第7章 文件基础\\任务程序\\data\\e_ point.txt', 'r')  # 打开e_point.txt文件并定义变量f
txt = f.read()  # 阅读文件e_point.txt的内容并赋值变量txt
print(txt)  # 输出文件e_point.txt的内容

# 代码 7-4
f.close()

# 代码 7-5
try:
    f = open('e_point.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

# 代码 7-6
with open('e_point.txt', 'r') as f:
    print(f.read())

# 代码 7-7
with open('text_file\e_point.txt', 'r') as f:
    print(f.read())

# 代码 7-8
with open(r'C:\Users\45543\Desktop\text_file\e_point.txt', 'r') as f:
    print(f.read())

# 代码 7-9
with open('C:\\Users\\45543\\Desktop\\text_file\\e_point.txt', 'r') as f:
    print(f.read())

# 代码 7-10
with open('C:/Users/45543/Desktop/text_file/e_point.txt', 'r') as f:
    print(f.read())

# 代码 7-11
with open('e_point.txt', 'r') as f:
    for line_t in f:
        print(line_t)

# 代码 7-12   
with open('e_point.txt', 'r') as f:
    for line_t in f:
        print(line_t.rstrip())

# 代码 7-13
with open('e_point.txt') as f:
    txts = f.read()
print(type(txt))
print(txt)

# 代码 7-14
with open('e_point.txt') as f:
    txts = f.readlines()
print(type(txts))
print(txts)

# 代码 7-15
with open('e_point.txt') as f:
    txts = f.readlines()
for txt in txts:
    print(txt.strip())

# 代码 7-16
with open('e_point.txt') as f:
    txt = f.readline()
print(type(txt))

print(txt)
