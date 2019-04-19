import os


# # print(os.name)
# # print(os.sep)
# # print(os.linesep)
# path=os.getcwd()
# # print(path)
# # print(os.listdir(path))
# # print(os.path.exists(".py"))
# os.path
# a=[os.listdir()]
# print(a)

def find_string(str):
    dir = []
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            # print(os.path.join(root, name))
            if os.path.join(root, name).find(str):
                dir.append(os.path.join(root, name))
        for name in dirs:
            # print(os.path.join(root, name))
            if os.path.join(root, name).find(str):
                dir.append(os.path.join(root, name))

    return dir


a = find_string(".py")
print(a)
