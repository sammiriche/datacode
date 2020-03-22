# 职员类，每个对象就是一个职员
class Empo(object):
    # 构造函数，包含姓名，部门，IP，MAC
    def __init__(self,name,dept,ip,mac):
        self.__name = name
        self.__dept = dept
        self.__ip = ip
        self.__mac = mac

    #私有属性的get，set方法，装饰器暂时不用
    def set_name(self,name):
        self.__name = name
    def set_dept(self,dept):
        self.__dept = dept
    def set_ip(self,ip):
        self.__ip = ip
    def set_mac(self,mac):
        self.__mac = mac
    
    def get_name(self):
        return self.__name
    def get_dept(self):
        return self.__dept
    def get_ip(self):
        return self.__ip
    def get_mac(self):
        return self.__mac

    # 修改str方法，打印对象直接打印返回内容
    def __str__(self):
        return f'姓名：{self.__name} 部门：{self.__dept} IP：{self.__ip} MAC：{self.__mac}'