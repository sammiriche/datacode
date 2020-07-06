class Sou(object):
    def test(self):
        self.number = 3
        number2 = 22


def test2():
    number2 = 22
    return(number2)

if __name__ == "__main__":
    sou = Sou()
    sou.test()
    print(sou.number)
    print(test2())

