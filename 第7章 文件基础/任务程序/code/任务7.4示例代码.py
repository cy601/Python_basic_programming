# -*- coding: utf-8 -*-
###############################################################################
####################               正文代码                 ####################
###############################################################################

# 代码 7-30
import os
os.name  #查询操作系统名称
os.sep  #查询文件路径的分割符
os.linesep  #查询当前平台使用的行终止符

# 代码 7-31
path = os.getcwd()  # 查询当前工作目录，并赋值给path
print(path)

# 代码 7-32
os.listdir(path)

# 代码 7-33
os.remove('C:\\Users\\45543\\Desktop\\test.csv')

# 代码 7-34
file_name = 'C:\\Users\\45543\\Desktop\\my_file'
os.mkdir(file_name)  # 创建文件夹
os.rmdir(file_name)  # 删除文件夹

# 代码 7-35
import os
system = os.name  # 获取操作系统名称
if system == 'nt':
    print('当前的操作系统是Windows.')
else:
    print('当前的操作系统是Linux.')
print('本系统表示路径的分隔符是：' + os.sep) 
print('本系统中使用的行终止符为：' , [os.linesep])

path=os.getcwd()  #获得当前目录
print('运行本程序所在目录是:' + path)

print('电脑的Path环境变量如下所示：\n' + os.getenv("Path"))  
#获取环境变量的值os.putenv(key,value)可以设置环境变量的值

os.mkdir("test")        # 创建空文件夹
print('当前文件夹中的文件有：\n' , os.listdir(path))  #获取文件夹中的所有文件
if(os.path.exists("test")):   #判断文件是否存在
    os.rmdir("test")   #删除指定文件
    print('删除成功夹')
else:
    print('文件夹不存在')
print('删除后的结果：\n' , os.listdir(path))
 
filepath1="Python7"
if(os.path.isfile(filepath1)):    #判断是不是文件
    print(filepath1 + "是一个文件")
else:
    print(filepath1 + "不是一个文件")
 
name="Ch7.py"
print("本程序的大小为" , os.path.getsize(name))   #获取文件大小
name=os.path.abspath(name);     #获取文件的绝对路径
print("本程序的绝对路径是" + name)               

print("本程序的路径的文件名分别为：", os.path.split(name)) #将文件名和路径分开
 
files=os.path.splitext(name)  #将文件名和扩展分开
print("本程序的扩展为" + files[1])
 
print("本程序的文件名为" + os.path.basename(name))#获取文件的名字
print("本程序的路径为" + os.path.dirname(name))#获取文件的路径


# 代码 7-36
import shutil
# 复制文件，没有则新建
shutil.copyfile('Ch7.py', 'Ch7.py.copy')
shutil.copy('C:\\Users\\45543\\Desktop\\程序\\pi_digits.txt', 'C:\\Users\\45543\\Desktop\\MyFile.txt')

# 代码 7-37
# 移动文件
shutil.move('C:\\Users\\45543\\Desktop\\程序\\pi_digits.txt', 'C:\\Users\\45543\\Desktop')
shutil.move('C:\\Users\\45543\\Desktop\\程序\\pi_digits.txt', 'C:\\Users\\45543\\Desktop\\MyText.txt')

# 代码 7-38
import shutil
shutil.copyfile('Ch7.py', 'Ch7.py.copy')

# 代码 7-39
import shutil
shutil.copy('C:\\Users\\45543\\Desktop\\pi_digits.txt', 'C:\\Users\\45543\\ MyFile.txt')

# 代码 7-40
import shutil
shutil.copytree('C:\\Users\\45543\\Desktop\\程序', 'C:\\Users\\45543\\test')

# 代码 7-41
# 删除文件夹
import os
os.unlink('C:\\Users\\45543\\Desktop\\Delect')
os.rmdir('C:\\Users\\45543\\Desktop\\Delect')
shutil.rmtree('C:\\Users\\45543\\Desktop\\Delect')

# 代码 7-42
# 压缩与解压文件
shutil.make_archive("C:\\Users\\45543\\Desktop\\test", 'zip', root_dir='C:\\Users\\45543\\Desktop\\程序')

# 代码 7-43
shutil.unpack_archive('C:\\Users\\45543\\Desktop\\test.zip')
