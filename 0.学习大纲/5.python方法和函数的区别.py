'''
python中函数和方法是有区别的。
比如函数中的变量 在函数运行完成后会回收内存空间。
方法中定义的变量则会伴随实例或者类

与类和实例无绑定关系的function都属于函数（function）；
与类和实例有绑定关系的function都属于方法（method）。
给段代码演示
'''
class Example(object):
    def test(self):
        self.number = 3

# 注意下面这个函数是在类外面，没有和类或者实例绑定
def test2():
    number2 = 22
if __name__ == "__main__":
    ex = Example()
    ex.test()
    print(ex.number)  # 输出为3.即使这个变量是在'test'这个function中定义的。但是test运行完毕依然有内存空间占用
    # 因为test和实例（self）绑定了。这个时候的test其实就是方法
    
    print(number2)  # 这个就会报错，因为number2 在'test2'这个function定义的。没有和任何类，实例绑定，运行完function就退出内存了
    # 再执行下面的print语句就会提示找不到变量

'''
最大的结论可以推倒出 类和函数的区别。类可以保存变量（通过self），即使只是在类里面的function定义的变量也可以保存
这样在多个py之间引用时就不存在作用域问题了
函数只能通过return返回变量

paramiko 连接电脑，如果使用invoke_shell  注意最好延时。因为执行较慢，另外注意连接交换机注意需要先sys切换全局模式
'''

