# 数据库操作封装成类。 测试版
import pymysql

class Op_mysql(object):
    # 构造时需传入相关数据库参数
    def __init__(self,host,user,passwd,port,db):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.port = port 
        self.db = db

    # 单独写创建数据库和表的方法
    def create_db(self):
        pass
    def create_table(self):
        pass
    def 

    # 连接数据库
    # 实例化时已经保存了相关变量。这是类和函数的区别之一
    def connect(self):
        self.conn = pymysql.connect(
            host = self.host,
            user = self.user,
            passwd = self.passwd,
            port = self.port,
            charset = 'utf8mb4'
        )
        self.cur = self.conn.cursor() # 创建游标
        # 创建UTF8mb4类型数据库，如果不存在
        sql = 'create database if not exists %s DEFAULT CHARSET utf8mb4 COLLATE utf8mb4_unicode_ci'
        self.cur.execute(sql,self.db)
        # 使用指定数据库
        self.cur.execute('use %s',self.db)
    
    #该函数配合with方法在上下文完成时自动调用
    def __enter__(self): # 这两个都属于重写函数了
        self.connect()()
        return self # 这句不加是否影响，后期测试？
    def exit(self):
        self.cur.close()
        self.conn.close()
