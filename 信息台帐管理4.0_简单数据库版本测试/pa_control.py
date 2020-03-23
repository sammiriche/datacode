# 每单独调用一个函数打开-关闭数据库连接。而不是一直保持连接状态
import pymysql
from pa_employees import Employees
import re

class Control(object):
    def __init__(self):
        # 创建数据库连接，调用相关函数
        # 假设电脑本机安装有数据库管理软件DBMS
        self.run()

    def run(self):
        while True:
            print('*'* 39)
            print('1：添加员工信息'.ljust(9),end = '\t') # ljust补全8个字符（不是字节）
            print('2：删除员工信息')
            print('3：修改员工信息'.ljust(9),end = '\t')
            print('4：查询指定员工')
            print('5：显示所有员工'.ljust(9),end = '\t')
            print('6：退出当前系统')
            print('*'* 39)
            # num = input('请输入功能序号：')
            # 通过函数检查输入合法性
            num = self.is_num()
            if num == 1:
                self.add_em()
            if num == 2:
                self.del_em()
            if num == 3:
                self.modify_em()
            if num == 4:
                self.query_em()
            if num == 5:
                self.show_em()
            if num == 6:
                break  # 直接跳出最外层while循环
    def is_num(self): # 判断输入字符是否是1-6的数字
        while 1:
            num = input('请输入功能序号：')
            result = re.match(r'^[1-6]$',num)
            if not result:
                print('请输入1-6之间的正整数！')
            else:
                return int(num)
                break

    def is_name(self): # 判断名字合法，返回名字
        pass
    def is_dept(self):
        pass
    def is_ip(self):
        pass
    def is_mac(self):
        pass
    # 增删查改系列函数    
    def add_em(self):
        name = is_name()
        dept= is_dept()
        ip = is_ip()
        mac = is_mac()
        em = Employees(name,dept,ip,mac)
        # 连接数据库，需要提交事务
        conn = pymysql.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'root',
            port = 3306,
            charset = 'utf8mb4'
        )
        cur = conn.cursor()
        
    def del_em(self):
        pass
    def modify_em(self):
        pass
    def query_em(self):
        pass
    def show_em(self):
        pass

    


if __name__ == '__main__':
    co = Control()
    