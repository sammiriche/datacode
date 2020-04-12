# 封装对数据库的操作 配合with方法简化语句

import pymysql

# 函数外语句在import时执行一次。在实例类时不会再执行
# 函数外语句主要起初始化作用，建立数据库和表（空值）
# 连接数据库，创建连接对象
conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root',
    port = 3306
)
# 建立操作游标
cur = conn.cursor()
# 建立数据库
sql = 'create database if not exists milkbottle default charset utf8mb4 collate utf8mb4_unicode_ci'
cur.execute(sql)
# 使用数据库
cur.execute('use milkbottle')
# 建立员工表（主表） 三冒号里面原样输出
sql = '''
    create table if not exists em_info(
        em_name varchar(20),
        em_dept varchar(20),
        em_ip varchar(20),
        em_mac varchar(20)
    )
'''
cur.execute(sql)

#建立用户表，管理权限作用
sql = '''
    create table if not exists user_info(
        user_name varchar(20),
        user_passwd varchar(20),
        is_admin int(4)
    )
'''
cur.execute(sql)

# 初始化完毕关闭游标和连接
cur.close()
conn.close()


class Mysql_manager(object):
    def __init__(self,host,user,passwd,port,db):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.port = port
        self.db = db

    #数据库连接方法
    def connect_db(self): # 防止重名可能的问题
        self.conn = pymysql.connect(
            host = self.host,
            user = self.user,
            passwd = self.passwd,
            port = self.port,
            db = self.db
        )
        self.cur = self.conn.cursor() # 建立游标属性，对象属性，可以随对象保存

    #数据库关闭方法
    def close_db(self):
        # 先提交事务。再关闭游标和连接。注意顺序
        self.conn.commit()
        self.cur.close()
        self.conn.close()
    
    # 配合with使用，重写enter方法
    def __enter__(self):
        self.connect_db()
        # 测试语句
        print('with方法开始模块')
        return self # 不用return不影响正常使用
    # 配合with使用，退出with模块，重写exit方法
    def __exit__(self,exc_type, exc_val, exc_tb): # 括号的参数格式是固定的
        self.close_db()
        print('with方法结束模块')
        return self
    
if __name__ == "__main__":
    mm = Mysql_manager('localhost','root','root',3306,'milkbottle')
    with mm:
        print('test')
    
    print('end')
