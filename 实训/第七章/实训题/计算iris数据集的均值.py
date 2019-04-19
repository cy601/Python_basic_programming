import csv


# https://blog.csdn.net/Allyli0022/article/details/79125672
Sepal_Length = []
file_name = 'iris.csv'
# with open(file_name, 'r') as f:
#     reader = csv.DictReader(f)
# for row in reader:
#     if row. ='Sepal.Length':
#     Sepal_Length = row['Sepal.Length']
#     comma = row['']
with open(file_name, 'r') as f:
    reader = csv.DictReader(f)
    Sepal_Length = [row['Sepal.Length'] for row in reader]

with open(file_name, 'r') as f:
    reader = csv.DictReader(f)
    comma = [row[''] for row in reader]

with open(file_name, 'r') as f:
    reader = csv.DictReader(f)
    Sepal_Width = [row['Sepal.Width'] for row in reader]
with open(file_name, 'r') as f:
    reader = csv.DictReader(f)
    Petal_Length = [row['Sepal.Length'] for row in reader]

with open(file_name, 'r') as f:
    reader = csv.DictReader(f)
    Petal_Width = [row['Petal.Length'] for row in reader]
with open(file_name, 'r') as f:
    reader = csv.DictReader(f)
    Species = [row['Species'] for row in reader]
    # print(Sepal_Length)
    # print(Sepal_Width)
    # print(Petal_Length)
    # f.close()


def get_average(array):
    sum = 0
    for i in array:
        sum += float(i)
    avg = sum / len(array)
    return avg


# print(get_average([1,23,4]))


Sepal_Length_avg = get_average(Sepal_Length)
Sepal_Width_avg = get_average(Sepal_Width)
Petal_Length_avg = get_average(Petal_Length)
Petal_Width_avg = get_average(Petal_Width)
print(Sepal_Length)
print(Sepal_Length_avg)
# print(type(Sepal_Length[1]))


Sepal_Length.append(Sepal_Length_avg)
Sepal_Width.append(Sepal_Width_avg)
Petal_Length.append(Petal_Length_avg)
Petal_Width.append(Petal_Width_avg)
comma.append(len(comma)+1)
Species.append(1)
import pandas as pd

# 字典中的key值即为csv中列名
dataframe = pd.DataFrame(
    {",": comma, "Sepal.Length": Sepal_Length, "Sepal_Width": Sepal_Width, "Petal_Length": Petal_Length,
     "Petal_Width": Petal_Width, "": Species})

# 将DataFrame存储为csv,index表示是否显示行名，default=True
dataframe.to_csv("my_iris.csv", index=False, sep=',')

# with open('my_iris.csv', 'w', newline='') as f:
#     write_csv = csv.writer(f)
#     for square in squares:
#         write_csv.writerow([str(square)])
#
# f.close()
