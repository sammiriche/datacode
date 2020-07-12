class Employees(object):
    def __init__(self, name, dept, ip, mac):
        self.__name = name
        self.__dept = dept
        self.__ip = ip
        self.__mac = mac


    # 类属性方式设置get set方法，支持新式类和旧类
    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name 
    # 方法属性化
    # 方法就是对象，prpoerty 有四个参数。如果你使用instance.name就自动调用第一个参数，使用instance.name= XXX, 自动调用第二个参数
    # 以后在其他地方获取或者设置该属性值，写法相对简单一点，同时同样受set_name这些方法语句的约束
    name = property(get_name,set_name) # 两个方法顺序不能变动，因为分别调用对应位置参数的方法

    def set_dept(self,dept):
        self.__dept = dept
    def get_dept(self):
        return self.__dept
    dept= property(get_dept,set_dept)

    def set_ip(self,ip):
        self.__ip = ip
    def get_ip(self):
        return self.__ip
    ip = property(get_ip,set_ip)

    def set_mac(self,mac):
        self.__mac= mac
    def get_mac(self):
        return self.__mac
    mac = property(get_mac,set_mac)



    def __str__(self):  # 字符串运算组合
        return '姓名：'.ljust(16) + self.__name + '\n' + '部门：'.ljust(16) + \
            self.__dept + '\n' + 'IP：'.ljust(16) + self.__ip + '\n' + 'MAC：'.ljust(16) + self.__mac


if __name__ == '__main__':
    em = Employees('mark', '人资', '192.168.1.1', 'aaaa-bbbb-cccc')
    print(em)
    em.name = 'tony'
    print(em.name)
