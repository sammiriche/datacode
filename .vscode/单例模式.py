# 重写new方法
# new方法首先开辟内存空间给新建对象，然后将该对象的内存地址返回给init 
# 创建对象时，自动调用了new方法和init方法

# class Musicplayer(object):
#     def __new__(self):
#         print('new方法显示出来')
#         return super().__new__(self)
    
#     def __init__(self):
#         self.a = 3
#         print('调用init方法')

# mp = Musicplayer()

# 单例模式实现代码。单个类的多个对象地址指向同一个
class Musicplayer(object):
    # 定义一个类变量，记录对象的内存地址 如果没有新建对象，这里就是none
    instance = 0
    # 如果有了一个对象，在new方法里记录下返回值，并且赋值给__instance 
    # 下次再建立对象，只要判断__instance不为空，那么直接把当前__instance返回给init，这样第二次的对象的内存地址就和第一次一样了
    def __new__(self):
        if self.instance == 0:
            self.instance = super().__new__(self)  #调用父类方法获取的准备返回的对象内存地址，
            return self.instance
        else:
            return self.instance # 如果不为空，说明建立过对象，有内存地址值，那么直接返回他的地址值，这样两个对象内存地址一样了

    def __init__(self):
        print('证明new传递到init成功')

mp1 = Musicplayer()
print(Musicplayer.instance)
mp2 = Musicplayer()
print(mp1)
print(mp2)

"""
在开发时，如果碰到单例模式，只需要构造函数运行一次。可以用类似方法
先定义类变量init_flag = False 在类函数里面可以用Musicplayer.init_flag或者self.init_flag访问（init构造 参数是self）
然后在构造函数加上判断语句
if init_flag = False:
    这里填写构造函数语句
else:
    return （不做任何构造动作了）

"""


