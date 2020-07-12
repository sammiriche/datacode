# 保存交换机基本信息的数据库
# 在类外面写建表语句，一次调用

import pymysql
# # 创建数据库连接
# conn = pymysql.connect(
#     host='localhost',
#     user='root',
#     passwd='root',
#     port=12306
# )
# # 创建操作游标
# cur = conn.cursor()
# # 建立数据库
# sql = 'create database if not exists sgcc_switch default charset utf8mb4 collate utf8mb4_unicode_ci'
# cur.execute(sql)
# # 使用创建好的数据库
# cur.execute('use sgcc_switch')
# # 建表
# sql = '''
#     create table if not exists jiguan_switch(
#         switch_name varchar(20),
#         switch_ip varchar(20),
#         switch_brand varchar(20),
#         switch_version varchar(20)
#     )
# '''
# cur.execute(sql)
# # 关闭游标和连接
# cur.close()
# conn.close()

# 交换机数据库的操作管理
class Switch_db(object):
    def __init__(self):
        self.config = {
            'host':'127.0.0.1',
            'user':'root',
            'passwd':'root',
            'port':12306,
            'db':'sgcc_switch'
        }
    
    # 数据库连接函数
    def con_db(self):
        # 建立连接和游标,注意可选参数
        self.conn = pymysql.connect(**self.config)
        self.cur = self.conn.cursor()

    # 数据库关闭函数，配合with使用
    def close_db(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    # 重写enter方法
    def __enter__(self):
        print('with模块，调用with就运行该enter方法')
        self.con_db()
    def __exit__(self,exc_type, exc_val, exc_tb):
        print('---with end---')
        self.close_db()
    # 对象被删除时调用del
    def __del__(self):
        print('对象删除')


    # 查看所有数据
    def show_db(self):
        sql = 'select * from jiguan_switch'
        self.cur.execute(sql)
        # 取出所有数据，二维列表,下标获取值
        result = self.cur.fetchall()
        print(result)
        # print(result[1][1])

    # 增删改查调用下面函数。具体通过语句
    def exe_db(self,sql,*params):
        self.cur.execute(sql,*params)
        result = self.cur.fetchall()
        return result

if __name__ == "__main__":
    sd = Switch_db()
    with sd:
        sd.show_db()