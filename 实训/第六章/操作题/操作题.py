class Student:
    name = ''
    age = 0
    course = []

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_course(self):
        return max(self.course)

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.course.append(score[0])
        self.course.append(score[1])
        self.course.append(score[2])


zm = Student('zhangming', 20, [69, 88, 100])

print(zm.get_course())