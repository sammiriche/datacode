class Animal(object):
    a = 10
    def __init__(self):
        self.b = 1


aa = Animal()
print(Animal.__dict__)
print(aa.__dict__)
