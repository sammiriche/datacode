class Huashan(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def __print(self):
        print(self.name)
        print('测试私有方法调用成功')
        # print(self.___score)

    def get_socre(self):
        return self.__score

    def set_score(self, score):
        self.__score = score

    #  调用私有方法
    def get_print(self):
        self.__print()


yuebuqun = Huashan('yuebuqun2', 100)
#print(yuebuqun.name)
# print(yuebuqun.__score)
# yuebuqun.__print()
yuebuqun.set_score(200)
a = yuebuqun.get_socre()
print(a)
yuebuqun.get_print()
