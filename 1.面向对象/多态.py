class Animals(object):
    def speak(self):
        print('speaking')


class Dog(Animals):
    # pass
    def speak(self):
        print('wang wang')


class Cat(Animals):
    def speak(self):
        print('mi-ao miao')


class Person(object):
    def work(self, dog):
        dog.speak()


kaka = Dog()
lily = Cat()
james = Person()
james.work(kaka)
james.work(lily)
# kaka.speak()
# lily.speak()
