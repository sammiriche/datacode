# 每单独调用一个函数打开-关闭数据库连接。而不是一直保持连接状态
import pymysql
from pa_employees import Employees
import re


class Control(object):
    def __init__(self):
        # 建立好本机的数据库
        conn = pymysql.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'root',
            port = 3306
        )
        cur = conn.cursor()
        sql = 'create database if not exists info'
        cur.execute(sql)
        cur.execute('use info')
        sql = '''create table if not exists emp(
            user_name varchar(20),
            user_dept varchar(20),
            user_ip varchar(20),
            user_mac varchar(20)
        )ENGINE=INNODB DEFAULT CHARSET=utf8mb4
        '''
        cur.execute(sql)
        cur.close()
        conn.close()
        # 假设电脑本机安装有数据库管理软件DBMS
        self.run()

    def run(self):
        while True:
            print('*' * 39)
            print('1：添加员工信息'.ljust(9), end='\t')  # ljust补全8个字符（不是字节）
            print('2：删除员工信息')
            print('3：修改员工信息'.ljust(9), end='\t')
            print('4：查询指定员工')
            print('5：显示所有员工'.ljust(9), end='\t')
            print('6：退出当前系统')
            print('*' * 39)
            # num = input('请输入功能序号：')
            # 通过函数检查输入合法性
            num = self.is_num()
            if num == 1:
                self.add_em()
            if num == 2:
                self.del_em()
            if num == 3:
                self.modify_em()
            if num == 4:
                self.query_em()
            if num == 5:
                self.show_em()
            if num == 6:
                break  # 直接跳出最外层while循环

    def is_num(self):  # 判断输入字符是否是1-6的数字
        while 1:
            num = input('请输入功能序号：')
            result = re.match(r'^[1-6]$', num)
            if not result:
                print('请输入1-6之间的正整数！')
            else:
                return int(num)

    def is_name(self):  # 判断名字合法，返回名字
        while True:
            name = input('请输入姓名：')
            result = re.match(r'^[\u4e00-\u9fa5]{2,4}$',name) # 匹配2到4位中文字符
            if not result:
                print('请输入正确的姓名格式')
            else:
                return name

    def is_dept(self):
        while True:
            dept = input('请输入部门名称：')
            result = re.match(r'^[\u4e00-\u9fa5]{2,6}$',dept)
            if not result:
                print('请输入正确的部门名称')
            else:
                return dept # return 会跳出函数
    def is_ip(self):
        while True:
            ip = input('请输入IP地址：')
            result = re.match(r'^((25[0-4]|2[0-4]\d|1\d\d|\d?\d)\.){3}(25[0-4]|2[0-4]\d|1\d\d|\d?\d)$',ip)
            if not result:
                print('请输入正确的IP地址格式')
            else:
                return ip
    def is_mac(self):
        while True:
            mac = input('请输入mac地址：')
            result1 = re.match(r'^(([0-9a-fA-F]{4}\.){2}[0-9a-fA-F]{4})$',
                           mac)  # 格式1 xxxx.xxxx.xxxx
            result2 = re.match(r'^(([0-9a-fA-F]{4}-){2}[0-9a-fA-F]{4})$',
                           mac)  # 格式2 xxxx-xxxx-xxxx
            result3 = re.match(r'^(([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2})$',
                           mac)  # 格式3 xx:xx:xx:xx:xx:xx
            if result1 == None and  result2 == None and result3 == None: # 注意none和0的区别
                print('请输入正确的mac地址格式')
            elif result2 == None: # 如果过了第一步，又不属于result2，那么肯定是result1和3，再调用转换函数
                mac2 = self.trans_mac(mac)
                return mac2
            else:
                return mac
    def trans_mac(self,mac):
        if '.' in mac:
            mac = mac.replace('.','-')
            return mac  # 记得要返回值
        else:
            # 是多个冒号的形式。先去掉冒号
            mac = mac.replace(':','')
            # 然后转换列表进行切片操作
            ls_mac = list(mac)
            ls_mac.insert(4,'-')
            ls_mac.insert(9,'-')
            mac = ''.join(ls_mac)
            return mac
    # 增删查改系列函数
    def add_em(self):
        name = self.is_name()
        dept = self.is_dept()
        ip = self.is_ip()
        mac = self.is_mac()
        # 实例化员工类
        em = Employees(name, dept, ip, mac)
        # 连接数据库，需要提交事务
        conn = pymysql.connect(host='localhost',
                               user='root',
                               passwd='root',
                               port=3306,
                               charset='utf8mb4')
        cur = conn.cursor()
        # 创建数据库
        # sql = 'create database if not exists info'
        # cur.execute(sql)
        # cur.execute('use info')
        # sql_create = '''
        #     CREATE TABLE if not exists emp(
        #             user_name VARCHAR(20),
        #             user_dept VARCHAR(20),
        #             user_ip VARCHAR(20),
        #             user_mac VARCHAR(20)
        #             )ENGINE=INNODB DEFAULT CHARSET=utf8
        #                     '''
        # cur.execute(sql_create)
        cur.execute('use info')
        sql_insert = 'INSERT INTO emp VALUES(%s,%s,%s,%s)'
        cur.execute(sql_insert, (em.name, em.dept, em.ip, em.mac))
        conn.commit()
        cur.close()
        conn.close()

    def del_em(self):
        # 代码类似添加步骤 
        name = self.is_name()
        # 判断数据库中是否有当前名字
        conn = pymysql.connect(host='localhost',
                               user='root',
                               passwd='root',
                               port=3306,
                               charset='utf8mb4')
        cur = conn.cursor()
        cur.execute('use info')
        sql = 'select * from emp where user_name = %s'
        cur.execute(sql,name)
        if cur.rowcount:
            sql = 'delete from emp where user_name = %s'
            cur.execute(sql,name)
            print(name+'的个人数据删除完毕！')
        else:
            print('数据库中没有此人记录')
            # 除了查询，其他都需要提交事务。最后记得关闭cur和conn
        conn.commit()
        cur.close()
        conn.close()

    def modify_em(self):
        name = self.is_name()
        conn = pymysql.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'root',
            port = 3306,
            charset = 'utf8mb4'
        )
        cur = conn.cursor()
        cur.execute('use info')
        sql = 'select * from emp where user_name = %s'
        cur.execute(sql,name)
        if cur.rowcount: # 代表查询有数据出来
            print('请依次输入需要修改的部门，ip和mac地址')
            dept = self.is_dept()
            ip = self.is_ip()
            mac = self.is_mac()
            sql = 'update emp set user_dept = %s,user_ip = %s,user_mac = %s' # 代码错误
            cur.execute(sql,(dept,ip,mac))
            conn.commit()
        else:
            print('数据库中没有该员工信息')
            cur.close()
            conn.close()  
    def query_em(self):
        print('按1，根据姓名查询 | 按2，根据IP地址查询')
        conn = pymysql.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'root',
            port = 3306
        )
        cur = conn.cursor()
        num = int(input('press 1 or 2 \n'))
        if num == 1:
            name = self.is_name()
            cur.execute('use info')
            sql = 'select * from emp where user_name = %s'
            cur.execute(sql,name)
            if cur.rowcount:
                result = cur.fetchone()
                print(result)
            else:
                print('没有当前员工信息')
        elif num == 2:
            ip = self.is_ip()
            cur.execute('use info')
            sql = 'select * from emp where user_ip = %s'
            cur.execute(sql,ip)
            if cur.rowcount:
                result = cur.fetchone()
                print(result)
            else:
                print('没有当前员工信息')

        # 最后无论如何，关闭连接。查询不需要提交事务
        cur.close()
        conn.close()


    def show_em(self):
        while True:
            conn = pymysql.connect(
                host = 'localhost',
                user = 'root',
                passwd = 'root',
                port = 3306,
                charset = 'utf8mb4'
            )
            cur = conn.cursor()
            cur.execute('use info')
            cur.execute('select * from emp')
            result = cur.fetchall()
            # 先打印抬头
            print('姓名'.ljust(8),end = '\t')
            print('部门'.ljust(8),end = '\t')
            print('IP'.ljust(8),end = '\t')
            print('MAC'.ljust(8))
            print('-'*54)
            # print(result)
            for i in result:
                for j in i:
                    print(j.ljust(8),end = '\t')
                print()
            cur.close()
            conn.close()
            num = input('按任意键返回主菜单')
            if num:
                break


if __name__ == '__main__':
    co = Control()
 