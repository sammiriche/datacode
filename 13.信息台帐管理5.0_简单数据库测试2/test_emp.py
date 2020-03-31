# 练习语法
'''5.0版本不需要员工类的功能。直接在数据库操作，随时操作，随时保存'''
class Employees(object):
    # 构造方法
    def __init__(self,name,dept,ip,mac):
        self.__name = name
        self.__dept = dept
        self.__ip = ip
        self.__mac = mac
    
    # get,set方法，旧式和新式都适用
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    # property方法 这样既保证了通过get，set方法限制获取属性。同时调用时语法也更加简洁
    name = property(get_name,set_name)
    # x.name x.name = xxx  两个语句执行就会分别调用get和set方法

    def get_dept(self):
        return self.__dept
    def set_dept(self,dept):
        self.__dept = dept
    dept = property(get_dept,set_dept)

    def get_ip(self):
        return self.__ip
    def set_ip(self,ip):
        self.__ip = ip
    ip = property(get_ip,set_ip)

    def get_mac(self):
        return mac
    def set_mac(self,mac):
        self.__mac = mac
    mac = property(get_mac,set_mac)

    def __str__(self):
        return f'修改默认返回值（内存对象）为指定元素，比如名字：{self.name}'

if __name__ == '__main__':
    em = Employees('kaka','renzi','192.168.1.1','ff')
    print(em)
    print('=====================')
    em.name = 'james'
    em.mac = 'new ff'
    print(em.name)
    print('她的ip' + em.ip)
    print(em)
