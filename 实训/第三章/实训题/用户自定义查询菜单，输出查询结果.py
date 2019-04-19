hamburger = (
    "香辣鸡腿堡",
    "劲脆鸡腿堡",
    "新奥尔良烤鸡腿堡",
    "半鸡半虾米堡"
)
snacks = (
    "薯条",
    "黄金鸡块",
    "香甜栗米棒",

)
beverage = (
    "可口可乐",
    "九珍果汁",
    "经典咖啡"
)
s = int(input("查询汉堡类菜单请输入1\n查询小食类菜单请输入2\n查询饮料类菜单请输入3\n若不查询请输入0\n请选择需要进行操作的对应数字:\n"))
if s == 1:
    for i in hamburger:
        print(i)
elif s == 2:
    for i in snacks:
        print(i)
elif s == 3:
    for i in beverage:
        print(i)
elif s == 0:
    exit()
