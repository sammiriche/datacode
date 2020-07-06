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
            mm.cur.execute('use milkbottle') #这里mm.cur之所以存在，因为它是方法变量，伴随实例走，方法消失依然保存
            sql = 'insert into user_manager values(%s,%s,%s)'
            mm.cur.execute(sql,(self.name,self.passwd,1))
            mm.conn.commit()
        print(f'{self.name}注册成功')
    # 验证帐号密码，先验证帐号是否存在。注意fetchone的返回值
    def verify(self,name,passwd):
        self.name = name
        self.passwd = passwd
        mm = Mysql_manager('localhost','root','root',3306,'milkbottle')
        with mm:
            sql = 'select * from user_manager where user_name = %s and user_passwd = %s'
            mm.cur.execute(sql,(self.name,self.passwd))
            if mm.cur.rowcount:
                print('验证成功，欢迎使用')
                return True
            else:
                print('帐号或者密码不正确')
                return False
              

if __name__ == '__main__':
    um = User_manager()
    # um.register('user','mima')
    result = um.verify('user2','mima1')
    print(result)