import os

# print(os.listdir())
# list = os.listdir()
import shutil


def get_file(string):
    list = os.listdir()
    for i in range(len(list)):
        if (str(list[i]).find(string)) == -1:
            list.pop(i)
    # return list

    # 目标路径（当前工作目录 + test文件夹）
    out_file = os.getcwd() + "\\my python"
    # 创建文件夹

    os.mkdir(out_file)

    for i in range(len(list)):
        shutil.copy(list[i], out_file)

    # 压缩文件
    shutil.make_archive('allpython', 'zip', root_dir=out_file)


get_file("py")
