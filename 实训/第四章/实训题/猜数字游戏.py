import random

number = random.randint(1, 20)
guess = 0
while 1:
    i = (input("输入你猜的数字:"))
    if i.isdigit():
        guess += 1
        i = int(i)
        if i > number:
            print("猜大了")
        elif i < number:
            print("猜小了")
        else:
            print("恭喜你，猜对了")
            print("一共猜了%d次" % guess)
            exit()
    else:
        print("必须输入数字，请重新输入")
