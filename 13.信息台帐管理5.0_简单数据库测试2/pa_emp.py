# 测试语法
class Emp(object):
    # 构造方法，设定属性
    def __init__(self,name,dept,ip,mac):
        self.__name = name
        self.__dept = dept
        self.__ip = ip
        self.__mac = mac

    # get，set方法 限定获取和更改属性的方法
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    # property方法  在不同语句（xx.name,  xx.name = name）分别调用1，2 位置的函数  
    name = property(get_name,set_name)

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
        return self.__mac
    def set_mac(self,mac):
        self.__mac = mac
    mac = property(get_mac,set_mac)

    # 修改默认返回函数值（原始是内存对象地址）
    def __str__(self):
        return f'测试返回函数{self.mac}' #  注意这里没有下划线 自动调用property里的第一个参数

if __name__ == "__main__":
    emp = Emp('liu','hengsheng','192','aaa')
    print(emp)  # 调用str函数
    print(emp.ip)
    emp.dept = '鼎立'
    print(emp.dept)
    # print(emp.__dept) 加这行会提示没有相关属性。因为它是类属性
