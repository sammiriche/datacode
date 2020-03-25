"""
首先建表
1开始事务
2检测账户A和B是否是可用账户
3检测账户A余额是否充足，如果不足，直接退出
4进行转账操作
5提交事务
中间有任何异常，回滚事务

"""
import mysql.connector

# 完整思路
# 首先编写脚本入口
class Transfer(object):
    def __init__(self,conn):
        self.conn = conn

    def run(self,source_id,destinantion_id,money):
        try:
            # 先检查两个账户是否正常可用，定义函数检查
            self.check(source_id)
            self.check(destinantion_id)
            # 检查是否有足够的钱
            self.has_enough_money(source_id,money)
            # 付款人减去金额
            self.reduce_money(source_id)
            # 收款人加上金额
            self.add_money(destinantion_id)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e

    def check(id):
        # 获取游标
        cur = self.conn.cursor()
        
if __name__ == '__main__':
    # 首先在实例对象之前建立起数据连接
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'root',
        port = 3306,
        database = 'test1'
    )
    try:
        tr = Transfer(conn)
        tr.run(source_id,destinantion_id,money)
    except Exception as e:
        print('转账错误' + str(e))
    finally:
        conn.close()
     