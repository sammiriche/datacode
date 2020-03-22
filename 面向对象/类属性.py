class Animal(object):
    __tooth = 12
    @classmethod
    def get_tooth(cls):
        return cls.__tooth

    
    @staticmethod
    def info():
        print('静态方法')

class Dog(Animal):
    pass


kaka = Dog()
print(kaka.get_tooth())
kaka.info()
