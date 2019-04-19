List = [5, 8, -7, 4, 6, 2, -3, 0]
print("列表中的最大元素为：", max(List))
print("列表中的最小元素为：(已删除)", min(List))
List.remove(min(List))

for i in range(len(List)):
    if List[i] < 0:
        List[i] = abs(List[i])
print(List)
