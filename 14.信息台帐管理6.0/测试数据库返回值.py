# 测试python 查询数据库的返回值格式
from Mysql_manager import *

mm = Mysql_manager('localhost','root','root',3306,'milkbottle')
with mm:
    # mm.cur.execute('use milkbottle')
    # mm.cur.execute('select user_passwd from user_manager where user_name = "user2"')
    # result = mm.cur.fetchone()
    # print(result[0])
    sql = "delete from em_info where em_name = '咔咔'"
    # sql = 'select * from em_info'
    mm.cur.execute(sql)
    print(mm.cur.rowcount)
