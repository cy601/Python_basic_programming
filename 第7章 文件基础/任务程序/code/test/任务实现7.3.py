# -*- coding: utf-8 -*-
###############################################################################
####################              任务实现7.3               ####################
###############################################################################
import csv

squares = [value ** 2 for value in range(1, 101)]

file_name = 'C:\\Users\\cy601\\Desktop\\2019Spring-智能信息处理应用开发\\20190228Python编程基础-参考代码与习题参考答案\\第7章 文件基础\\实训数据\\squares.csv'
with open(file_name, 'w', newline='') as f:
    write_csv = csv.writer(f)
    for square in squares:
        write_csv.writerow([str(square)])

f.close()
