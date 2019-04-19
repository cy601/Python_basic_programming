name = input('请输入你的名字:')
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
constellations = ['水瓶',
                  '双鱼',
                  '白羊',
                  '金牛',
                  '双子',
                  '巨蟹',
                  '狮子',
                  '处女']
datas = ['1月20日-2月18日',
         '2月20日-3月20日',
         '3月21日-4月19日',
         '4月20日-5月20日',
         '5月21日-6月21日',
         '6月21日-7月22日',
         '7月23日-8月22日',
         '8月23日-9月22日']
print('编号  星座     日期')
for number, constellation, data in zip(numbers, constellations, datas):
    print(str(number) + '     ' + constellation + '     ' + data)
number1 = input('请根据如上提示选择对应编号：')
print('{}您好！您星座分析结果为：'.format(name) + datas[int(number1) - 1])
