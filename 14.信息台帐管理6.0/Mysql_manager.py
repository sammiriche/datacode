# 数据库操作封装成类。 测试版
import pymysql

# 创建数据库和表写在类的外面import时就自动调用了。保证多个实例不影响，只调用一次
# 有个弊端，不能传参，但是一般这里数据库连接参数也不会修改
# conn = pymysql.connect(
#     host = 'localhost',
#     user = 'root',
#     passwd = 'root',
#     port = 3306,
# )
# cur = conn.cursor()
# #  数据库名称milkbottle
# sql = 'create database if not exists milkbottle default charset utf8mb4 collate utf8mb4_unicode_ci'
# cur.execute(sql)
# cur.execute('use milkbottle')
# # 创建员工信息表
# sql = '''
#     create table if not exists em_info(
#         em_name varchar(20),
#         em_dept varchar(20),
#         em_room_number int(4),
#         em_ip varchar(20),
#         em_mac varchar(20),
#         em_sw_ip varchar(20),
#         em_sw_port int(4)
#     )
# '''
# cur.execute(sql)

# # 创建用户管理表
# sql = '''
#     create table if not exists user_manager(
#         user_name varchar(20),
#         user_passwd varchar(20),
#         is_admin int(4)
#     )
# '''
# cur.execute(sql)
# cur.close()
# conn.close()

class Mysql_manager(object):
    # 构造时需传入相关数据库参数 自动构造不自动连接  在enter语句有调用连接，exit有调用关闭，配合with就好
    def __init__(self,host,user,passwd,port,db):
        print('测试自动构造')
        self.host = host
        self.user = user
        self.passwd = passwd
        self.port = port 
        self.db = db


    # 连接数据库
    # 实例化时已经保存了相关变量。这是类和函数的区别之一
    def connect(self):
        self.conn = pymysql.connect(
            host = self.host,
            user = self.user,
            passwd = self.passwd,
            port = self.port,
            db = self.db,
            charset = 'utf8mb4'
        )
        self.cur = self.conn.cursor() # 创建游标
    
    #该函数配合with方法在上下文完成时自动调用
    def __enter__(self): # 这两个都属于重写函数了
        print('测试开启连接')
        self.connect()
        # return self # 这句不加是否影响，后期测试？
        return None
    def __exit__(self,exc_type, exc_val, exc_tb):
        self.cur.close()
        self.conn.close()
        print('测试关闭连接')
    def __del__(self):
        print('测试删除函数执行时间')

if __name__ == '__main__':
    mm = Mysql_manager('localhost','root','root',3306,'milkbottle')
    with mm:
        print('数据库之间的操作')
    print('完全结束')

    

''' 测试自动构造
测试开启连接
数据库之间的操作
测试关闭连接
完全结束
测试删除函数执行时间 
'''