# 公路 属性 名称，长度
# 汽车 属性 车名，时速
# 方法 1 获取汽车在哪条公路上以什么速度行驶
#      2 初始化属性信息
#      3  修改str方法
class Road(object):
    def __init__(self,name,length):
        self.__name = name 
        self.__length = length
    
    def __str__(self):
        return self.__name + '--' + self.__length

    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name
class Car(object):
    def __init__(self,brand,speed):
        self.__brand = brand
        self.__speed = speed
    
    def __str__(self):
        return f'汽车品牌是{self.__brand},速度是{self.__speed}。'

    def run(self,road):
        info = road.get_name()
        print(f'在{info}上行驶')


road317 = Road('road317','1000km')
road317.set_name('g107')
benz = Car('benz','180km/h')
benz.run(road317)
print(benz)


