# 个人信息类，包含姓名，部门，ip，mac,全部为字符串
# 在部门里建立好子菜单选择
class Info(object):
    def __init__(self, name, dept, ip, mac):
        self.__name = name
        self.__dept = dept
        self.__ip = ip
        self.__mac = mac

    # 通过setget来体验封装的好处。检查输入合法性。
    # 通过判断语句，正则表达式等等
    def set_name(self, name):
        self.__name = name

    def set_dept(self, dept):
        self.__dept = dept

    def set_ip(self, ip):
        self.__ip = ip

    def set_mac(self, mac):
        self.__mac = mac

    def get_name(self):
        return self.__name

    def get_dept(self):
        return self.__dept

    def get_ip(self):
        return self.__ip
    
    def get_mac(self):
        return self.__mac
    
    def __str__(self):
        return f'姓名：{self.__name} 部门：{self.__dept} IP：{self.__ip} MAC：{self.__mac}'

if __name__ == '__main__':
    info = Info("lile",'to','fa','ta')
    print(info.get_name())
    print(type(info.get_name()))
    print(type(info.get_name))
    print(info.get_name)
