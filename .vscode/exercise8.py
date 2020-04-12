class Example():
    a = 1
    cc = 12
    def test(self):
        a = 3
        self.c = 22

def outside():
    b = 22

ex = Example()
ex.test()
# print(ex.a)
print(ex.c)
print(Example().cc)