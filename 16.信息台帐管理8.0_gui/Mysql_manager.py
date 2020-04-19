# 假设已经通过其他办法建立好类（简化语句和输出）

import pymysql

class Mysql_manager(object):
    # 初始化数据库。
    def __init__(self):
        # config不用传参。麻烦。以后可以通过从文件读取的方式写入config
        self.config = {
            'host':'localhost',
            'user':'root',
            'passwd':'root',
            'port':3306,
            'db':'milkbottle'
        }
    
    # 连接数据库
    def connect_db(self):
        self.conn = pymysql.connect(**self.config)  # 还要深刻理解运行过程
        # 定义游标
        self.cur = self.conn.cursor()
    
    def close_db(self):
        # 提交事务
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    # 查询所有方法
    def query_db(self): # 因为查询条件不同，参数数量不一,params是个元组参数
        sql = 'select * from em_info'
        self.cur.execute(sql)
        return self.cur.fetchall()

    # 其他增删改和单个查询方法通过传入sql语句来分开实现
    def exe_db(self,sql,*params): # 这里也许不用可变参数，因为参数数量变化体现在元组里面了
        self.cur.execute(sql,*params)
        num = self.cur.rowcount
        if num == 0:
            print('执行失败')
            return self.cur.fetchall()  # 查询单个数据时起作用
        else:
            print('执行成功')
            return self.cur.fetchall()
    
    
    def __enter__(self): # with  begin
        self.connect_db()
        print('with开始在此')

    def __exit__(self,exc_type, exc_val, exc_tb): # 前后下划线都属于重写方法
        self.close_db()
        print('with语句结束')

    def __del__(self):
        print('实例内存回收')


if __name__ == '__main__':
    mm = Mysql_manager()
    with mm:
        # sql = 'select * from em_info where em_name = %s'
        # sql = 'insert into em_info values(%s,%s,%s,%s)'
        # sql = 'select * from em_info where em_name = %s'
        sql = 'delete from em_info where em_name = %s and em_dept = %s'
        params = ('刘嗯','甜甜')
        result = mm.exe_db(sql,params)
        print(result)
        # result = mm.query_db(sql,params)
        # print(result)