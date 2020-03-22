class Huashan(object):
    def __init__(self):
        self.book = '葵花宝典'

    def kongfu(self):
        print(f'一代修炼{self.book}')


class Huashan_Sword(Huashan):
    def __init__(self):
        self.book = '独孤九剑'

    def kongfu(self):
        print(f'二代修炼{self.book}')
        # super().__init__()
        # super().kongfu()


class Students(Huashan_Sword, Huashan):
    def __init__(self):
        self.book = '紫霞神功'

    def kongfu(self):
        # print(f'三代修炼{self.book}')
        super().__init__()
        super().kongfu()



founder = Huashan()
founder.kongfu()
fengqingyang = Huashan_Sword()
fengqingyang.kongfu()
linghuchong = Students()
linghuchong.kongfu()
print(Students.mro())
