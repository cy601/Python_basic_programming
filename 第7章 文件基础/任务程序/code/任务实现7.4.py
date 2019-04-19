# -*- coding: utf-8 -*-
###############################################################################
####################              任务实现7.4               ####################
###############################################################################

# 加载模块
import os
import shutil

# 文件路径
file_name1 = 'C:\\Users\\cy601\\Desktop\\2019Spring-智能信息处理应用开发\\' \
             '20190228Python编程基础-参考代码与习题参考答案\\第7章 文件基础\\实训数据\\squares.csv'
file_name2 = 'C:\\Users\\cy601\\Desktop\\2019Spring-智能信息处理应用开发\\20190228Python编程基础-参考代码与习题参考答案\\第7章 文件基础\\任务程序\\' \
             'code\\任务实现7.3.py'
# '\\第7章 Python文件基础\\02-代码\\1.任务案例\\任务实现7.3.py'

# 目标路径（当前工作目录 + test文件夹）
out_file = os.getcwd() + '\\test'

# 创建文件夹
# os.mkdir(out_file)

# 复制文件
shutil.copy(file_name1, out_file)
shutil.copy(file_name2, out_file)

# 压缩文件
shutil.make_archive('test7.4', 'zip', root_dir=out_file)
