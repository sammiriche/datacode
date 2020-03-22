"""
工资管理程序 
所有员工都有员工号，姓名，工资，有私有属性 计算工资方法
工人worker 额外属性:工时，时薪，
销售员saleman 销售额和提成比例属性，工资计算，相乘
经理manager 固定月薪属性，
销售经理sale_manager 工资计算 销售额*提成比例+固定月薪属性。

显示出所有人薪资情况。详细员工信息
"""
# 新建父类
class Person(object):
    def __init__(self,number,name,salary):
        self.__number = number
        self.__name = name
        self.__salary = salary
    
    def set_number(self,number):
        self.__number = number
    def set_name(self,name):
        self.__name = name
    def set_salary(self,salary):
        self.__salary = salary
    
    def get_number(self):
        return self.__number
    def get_name(self):
        return self.__name
    def get_salary(self):
        return self.__salary
    # 工资计算方法 calculation
    def salary_cal(self):
        pass

class Worker(Person):
    # 构造方法重写，并且调用super方法
    def __init__(self,number,name,salary,hour,hourly_salary):
        super().__init__(number,name,salary)
        self.__hour = hour
        self.__hourly_salary = hourly_salary
    
    def set_hour(self,hour):
        self.__hour = hour
    def set_hourly_salary(self,hourly_salary):
        self.__hourly_salary = hourly_salary
    def get_hour(self):
        return self.__hour
    def get_hourly_salary(self):
        return self.__hourly_salary

    # 重写月薪计算方法
    def salary_cal(self):
        return self.__hour * self.__hourly_salary

    def __str__(self):
        return f'员工工号：{self.get_number}姓名：{self.get_name}工资：{self.get_salary}'

class saleman(Person):
    pass
worker = Worker(1,'mini',1000,3,80)
worker.set_number(2)
print(worker.get_number())
