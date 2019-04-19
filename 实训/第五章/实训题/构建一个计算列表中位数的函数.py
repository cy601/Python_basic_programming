def sort(*data):
    data = sorted(data)
    size = len(data)
    if size % 2 == 0:  # 判断列表长度为偶数
        median = (data[size // 2] + data[size // 2 - 1]) / 2
        print("中位数为：", median)
    if size % 2 == 1:  # 判断列表长度为奇数
        median = data[(size - 1) // 2]
        print("中位数为：", median)

    return


sort(1, 1, 342, 34, 535, 11)
