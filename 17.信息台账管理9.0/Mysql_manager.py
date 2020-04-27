# 在python中对mysql数据库进行操作封装的类
# 研究从登陆窗口获取到数据库IP和端口信息

import pymysql

class Mysql_manager(object):
    def __init__(self):
        self.config = {
            'host':'localhost',
            'user':'root',
            'passwd':'root',
            'port':3306,
            'db':'milkbottle'
        }

    def db_connect(self):
        self.conn = pymysql.connect(**self.config)
        self.cur = self.conn.cursor()

    def db_close(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def __enter__(self):
        print('with模块开始')
        self.db_connect()

    def __exit__(self,exc_type, exc_val, exc_tb):
        print('with结束模块')
        self.db_close()

    def __del__(self):
        print('对象删除')

    # 显示所有 和其他语句函数
    def db_show(self):
        sql = 'select * from em_info'
        self.cur.execute(sql)
        # print(self.cur.fetchall()) # 注意这条语句不是属性，执行一次，第二次执行就是空白了
        # print('')
        # print(self.cur.fetchall())
        # 返回二维数组集合
        return self.cur.fetchall()
    
    def db_exe(self,sql,*params):
        self.cur.execute(sql,*params)
        if self.cur.rowcount == 0:
            print(self.cur.rowcount)
            print('没有任何信息')
            return self.cur.fetchall()
        else:
            print(self.cur.rowcount)
            print('执行成功')
            return self.cur.fetchall()

if __name__ == '__main__':
    mm = Mysql_manager()
    with mm:
        # mm.db_show()
        print('=============')
        mm.db_exe('select * from em_info where em_ip = %s and em_name = %s',('192.168.1.1','刘继平'))