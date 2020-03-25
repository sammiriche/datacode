# 学生类。保存学生个人信息，并且提供str查询后的返回信息
# vscode init函数自动补全有点问题。注意！


class Student(object):
    def __init__(self, name, gender, tel):
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f'{self.name},{self.gender},{self.tel}'

if __name__ == '__main__':
    aa = Student('tom', 'female', 138)
    print(aa)
