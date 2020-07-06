# 封装数据库操作类

import pymysql

class Mysql_manager(object):
    # 类属性，保存服务器IP地址
    server_ip = ''
    def __init__(self):
        self.config = {
            'host':'127.0.0.1',
            'user':'root',
            'passwd':'root',
            'port':3306,
            'db':'sgcc'
        }

    def con_db(self): # 数据库开启链接
        self.conn = pymysql.connect(**self.config) # 建立连接
        self.cur = self.conn.cursor() # 建立游标

    def close_db(self):
        self.conn.commit() # 先提交当前事务
        self.cur.close()
        self.conn.close()
    
    # 重写enter方法
    def __enter__(self):
        print('with开始模块，准备调用连接')
        self.con_db()

    def __exit__(self,exc_type, exc_val, exc_tb):
        print('with结束模块。关闭游标和连接')
        self.close_db()
    
    def __del__(self):
        print('数据库操作类对象删除')

    # 具体数据库操作函数
    # 显示所有数据
    def show_db(self):
        sql = 'select * from em_info'
        self.cur.execute(sql)
        result = self.cur.fetchall()
        print(result) # 打印出来是个二维数组，
        return result

    # 操作，包括增，删，改，查（指定）
    def exe_db(self,sql,*params):
        self.cur.execute(sql,*params)
        result = self.cur.fetchall()
        if self.cur.rowcount == 0:
            print('数据库执行空')
            return None
        else:
            print(result)
            return result

if __name__ == "__main__":
    mm = Mysql_manager()
    with mm:
        sql = "insert into em_info values(%s,%s,%s,%s,%s,%s,%s)"
        lista = ('袁心玥','体育部','192.168.3.3','1111-aaaa-cccc',301,'10.229.61.143','21')
        mm.exe_db(sql,lista)
    print('--end--')
