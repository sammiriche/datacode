# 学生类 学生有书本，多本书。和电脑 姓名 三个属性  方法 借书
# 书本类 属性  书名 作者 编号 方法。。
# 电脑类 品牌，型号 
# 都修改str方法

class Student(object):
    def __init__(self,name,computer,book):
        self.name = name
        self.computer = computer
        self.books = []  # 初始藏书为0 列表保存
        self.books.append(book)

    # 购买藏书

    def buy_book(self,book):
        self.books.append(book)

    #借书函数
    def borrow_book(self,book):
        # pass
        if len(self.books)==0:
            print('藏书为0')
        else:
            for i in self.books:
                if i.name == book.name:
                    print('借书成功')
                    self.books.remove(i)
                    break
            
    def __str__(self):
        return '{}的电脑品牌是{},共有{}本书'.format(self.name,self.computer.brand,len(self.books))

class Computer(object):
    def __init__(self,brand,typed):
        self.brand = brand
        self.type = typed
    
    def __str__(self):
        return f'电脑品牌是{self.brand},型号是{self.typed}'

class Book(object):
    def __init__(self,name,author,number):
        self.name = name
        self.author = author
        self.number = number
    
    def __str__(self):
        return f'书名：{self.name} 作者：{self.author}编号：{self.number}'

book1 = Book('活着','余华',1)
book2 = Book('平凡的世界','路遥',2)
print(book1)
print(book2)
computer = Computer('lenovo','E420')
leifeng = Student('leifeng',computer,book1)
leifeng.buy_book(book2)
leifeng.borrow_book(book1)
print(leifeng)
