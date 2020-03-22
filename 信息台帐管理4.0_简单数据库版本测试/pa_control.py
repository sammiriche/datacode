# 每单独调用一个函数打开-关闭数据库连接。而不是一直保持连接状态
import mysql.connector
from pa_employees import Employees

class Control(object):
    def __init__(self):
        # 创建数据库连接，调用相关函数
        # 假设电脑本机安装有数据库管理软件DBMS
        pass


    


if __name__ == '__main__':
    co = Control()
    co.mydb()