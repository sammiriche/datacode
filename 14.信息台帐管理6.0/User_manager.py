# 用于管理登录用户以及权限的管理
# from Re_manager import Re_manager
# 暂时放在主程序做输入检查
from Mysql_manager import Mysql_manager
class User_manager(object):
    def register(self,name,passwd):
        # 注册用户,采用正则表达式判断是否符合要求
        self.name = name
        self.passwd = passwd
        mm = Mysql_manager('localhost','root','root',3306,'milkbottle')
        with mm: # 自动调用enter方法
            mm.cur.execute('use milkbottle')
            sql = 'insert into user_manager values(%s,%s,%s)'
            mm.cur.execute(sql,(self.name,self.passwd,1))
            mm.conn.commit()

if __name__ == '__main__':
    um = User_manager()
    um.register('user','mima')
