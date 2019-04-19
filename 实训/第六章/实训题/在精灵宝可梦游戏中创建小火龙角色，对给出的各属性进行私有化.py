class pokemon:
    name = ""
    gender = ""
    level = 0
    type = ""
    index = -1

    def __init__(self, n, gender, level, type):
        self.name = n
        self.gender = gender
        self.level = level
        self.ability = {"status": level + 5, "HP": level * 2 + 10, "attack": level + 5, "defence": level + 5,
                        "speed": level + 5}
        self.type = type
        self.info = [self.name, self.type, self.gender, self.level, self.ability]

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

    def GetStatus(self):
        return self.ability

    def GetType(self):
        return self.type

    def level_up(self):
        self.level += 1
        self.ability['HP'] += 2
        self.ability['status'] += 1
        self.ability['attack'] += 1
        self.ability['defence'] += 1

    def __iter__(self):
        print('名字 属性 性别 等级 能力')
        return self

    def next(self):
        if self.index > 10:
            raise StopIteration
        self.index += 1
        return self.info[self.index]


class Charmander(pokemon):
    name = ""
    gender = ""
    level = 0
    type = ""
    index = -1

    # def __init__(self, n, gender, level, type):
    #     self.name = n
    #     self.gender = gender
    #     self.level = level
    #     self.ability = {"status": level + 5, "HP": level * 2 + 10, "attack": level + 5, "defence": level + 5,
    #                     "speed": level + 5}
    #     self.type = type
    #     self.info = [self.name, self.type, self.gender, self.level, self.ability]
    #
    # def getName(self):
    #     return self.name
    #
    # def getGender(self):
    #     return self.gender
    #
    # def GetStatus(self):
    #     return self.ability
    #
    # def GetType(self):
    #     return self.type
    #
    # def level_up(self):
    #     self.level += 1
    #     self.ability['HP'] += 2
    #     self.ability['status'] += 1
    #     self.ability['attack'] += 1
    #     self.ability['defence'] += 1
    #
    # def __iter__(self):
    #     print('名字 属性 性别 等级 能力')
    #     return self
    #
    # def next(self):
    #     if self.index > 10:
    #         raise StopIteration
    #     self.index += 1
    #     return self.info[self.index]


# 创建对象
pokemon1 = Charmander('pokemon', 'male ', 1, 'yes')
# 访问属性
# print(pokemon1.GetStatus())

# 迭代输出对象的属性
iterator = iter(pokemon1.next, 1)
for info in iterator:
    print(info)

# print(pokemon1.ability)
print(pokemon1.info)
