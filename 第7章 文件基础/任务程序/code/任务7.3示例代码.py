# -*- coding: utf-8 -*-
###############################################################################
####################               正文代码                 ####################
###############################################################################

# 代码 7-17
squares = [value ** 2 for value in range(1, 101)]
print(squares)
print(type(squares))

# 代码 7-18
file_name = 'words.txt'
f = open(file_name, 'w', )
f.write('Hello, world!')

# 代码 7-19
file_name = 'words.txt'
f = open(file_name, 'w', )
data = list(range(1, 11))
f.write(str(data))
f.close()

# 代码 7-20
file_name = 'words.txt'
f = open(file_name, 'w', )
f.write('Hello, world!')
f.write('I love Python!')
f.close()

# 代码 7-21
file_name = 'words.txt'
f = open(file_name, 'w', )
f.write('Hello, world!\n')
f.write('I love Python!\n')
f.close()

# 代码 7-22
file_name = 'words.txt'
with open(file_name, 'w') as f:
    f.write('Hello, world!\n')
    f.write('I love Python!\n')

# 代码 7-23
file_name = 'words.txt'
f = open(file_name, 'w', encoding='gbk')
f.write('Hello, world!')

# 代码 7-24
file_name = 'words.txt'
with open(file_name, 'a') as f:
    f.write("What's your favourite language?\n")
    f.write('My favourite language is Python too.\n')

# 代码 7-25
# csv.reader 函数
import csv

file_name = 'C:\\Users\\cy601\\Desktop\\2019Spring-智能信息处理应用开发\\20190228Python编程基础-参考代码与习题参考答案\\第7章 文件基础\\实训数据\\iris.csv'
with open(file_name, 'r') as f:
    reader = csv.reader(f)
    iris = [iris_item for iris_item in reader]
print(iris)

# 代码 7-26
# csv.DictReader 函数
import csv

file_name = 'C:\\Users\\cy601\\Desktop\\2019Spring-智能信息处理应用开发\\20190228Python编程基础-参考代码与习题参考答案\\第7章 文件基础\\实训数据\\iris.csv'
with open(file_name, 'r') as f:
    reader = csv.DictReader(f)
    iris1 = [iris_item for iris_item in reader]
print(iris1)

# 代码 7-27
# 读取Sepal.Length列的内容
with open(file_name, 'r') as f:
    reader = csv.DictReader(f)
    column = [iris_item['Sepal.Length'] for iris_item in reader]
print(column)

# 代码 7-28
# 写入csv文件（列表）
file_name = 'C:\\Users\\cy601\\Desktop\\test.csv'
with open(file_name, 'w', newline='') as f:
    write_csv = csv.writer(f)
    write_csv.writerow(iris)

# 代码 7-29
## 写入字典数据
file_name = 'C:\\Users\\45543\\Desktop\\test.csv'
# 键的集合
my_key = []
for i in iris1[0].keys():
    my_key.append(i)
with open(file_name, 'w', newline='') as f:
    write_csv = csv.DictWriter(f, my_key)
    write_csv.writeheader()  # 输入标题
    write_csv.writerows(iris1)  # 输入数据
