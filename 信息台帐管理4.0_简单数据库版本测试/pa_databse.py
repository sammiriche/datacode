# 数据库操作类
import pymysql


class Mydb(object):
    def __init__(self):
        # 创建好数据库和表
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            passwd='root',
            port=3306,
            # db = 'mk_database', # 选填
            charset='utf8')
        self.cur = self.conn.cursor()
        sql = 'use  myemployees'
        self.cur.execute(sql)
        value = 12000
        sql = 'select * from employees where salary > %s'
        self.cur.execute(sql,value)
        print(self.cur.rowcount)
        self.cur.close()
        self.conn.close()


if __name__ == '__main__':
    mydb = Mydb()
