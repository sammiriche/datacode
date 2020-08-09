# 封装数据库操作类
import pymysql

class Mysql_manager(object):
    def __init__(self):
        self.config = {
            'host':'127.0.0.1',
            'user':'root',
            'passwd':'root',
            'port':12306,
            'db':'sgcc_switch'
        }
    
    # 数据库开始连接
    def con_db(self):
        self.conn = pymysql.connect(**self.config)
        self.cur = self.conn.cursor()

    # 数据库关闭连接和游标
    def close_db(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    #重写enter方法和exit方法
    def __enter__(self):
        print('with开始,调用连接函数')
        self.con_db()
    def __exit__(self,exc_type, exc_val, exc_tb):
        # 注意参数是固定写法
        print('连接提交和关闭')
        self.close_db()
    def __del__(self):
        print('数据库操作对象删除')

    # 数据库操作函数
    def show_db(self):
        sql = 'select * from jiguan_switch'
        self.cur.execute(sql)
        result = self.cur.fetchall() # 注意返回的二维元祖
        print(result)
        return result 
    def exe_db(self,sql,*params):
        self.cur.execute(sql,*params)
        result = self.cur.fetchall()
        if self.cur.rowcount == 0:
            print('执行为空')
            return None
        else:
            print(f'影响行数{self.cur.rowcount}')
            return result

if __name__ == "__main__":
    mm = Mysql_manager()
    with mm:
        sql = 'insert ignore into jiguan_switch values(0,%s,%s,%s,%s)'
        temp = ('wenbishan','172.31.64.151','HUAWEI','7.20')
        mm.exe_db(sql,temp)
    print('---end---')
    