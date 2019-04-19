n = int(input("请输入要参与计算的数字的个数:"))
n1 = 0
n2 = 1

List = []
List.append(n1)
List.append(n2)
print(List)

# for i in range(2, n):
#     print(i)
for i in range(2, n):
    List.append(List[i - 2] + List[i - 1])

List.pop(2)
print("斐波那契数列为：", List)
sum = 0
for i in List:
    sum += i

print(sum)
