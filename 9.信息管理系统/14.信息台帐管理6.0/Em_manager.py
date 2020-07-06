# 程序的主体部分，从这里显示管理页面，实现主要功能
from Mysql_manager import *
from Re_manager import *
from Excel_manager import *

class Em_manager(object):
    # 正则类可以一直存在。避免生成多个实例
    def __init__(self):
        self.rm = Re_manager()


    def run(self):
    # 显示操作界面
        while True:
            print('*' * 62)
            print('1:添加员工信息'.ljust(8), end='\t')
            print('2:删除员工信息'.ljust(8), end='\t')
            print('3:修改员工信息'.ljust(8), end='\t')
            print('4:查询员工信息')
            print('5:显示所有员工'.ljust(8), end='\t')
            print('6:表格批量导入'.ljust(8), end='\t')
            print('7:表格批量导出'.ljust(8), end='\t')
            print('8:退出当前系统')
            print('*' * 62)

            self.flag = self.rm.is_num()
            # 下面这些语句不用再在while循环了。
            if self.flag == 1:
                self.add_em()
            if self.flag == 2:
                self.del_em()
            if self.flag == 3:
                self.modify_em()
            if self.flag == 4:
                self.query_em()
            if self.flag == 5:
                self.show_em()
            if self.flag == 6:
                ex = Excel_manager()
                ex.import_excel()
            if self.flag == 7:
                ex = Excel_manager()
                ex.export_excel()
            if self.flag == 8:
                break

    def add_em(self):
        # 首先建立数据库连接。实例数据库操作类,属性没必要保存，一般变量即可
        name = self.rm.is_name()
        dept = self.rm.is_dept()
        ip = self.rm.is_ip()
        mac = self.rm.is_mac()
        mm = Mysql_manager('localhost','root','root',3306,'milkbottle')
        with mm:
            sql = 'insert into em_info values(%s,%s,%s,%s)'
            mm.cur.execute(sql,(name,dept,ip,mac))
        print(f'{name}的信息添加成功')

    # 函数里不需要返回的变量不用加self，self后面的变量通过实例可以保存
    def del_em(self): # 在这里顺便测试try语法
        print('支持通过姓名删除相关信息。')
        name = self.rm.is_name()
        mm = Mysql_manager('localhost','root','root',3306,'milkbottle') #  实例化并不会连接数据库，enter方法才调用连接
        with mm:
            sql = 'delete from em_info where em_name = %s'
            mm.cur.execute(sql,name)
            if mm.cur.rowcount == 0:
                print('没有相关员工信息')
            else:
                print('信息删除成功')
    def modify_em(self):
        name = self.rm.is_name()
        mm = Mysql_manager('localhost','root','root',3306,'milkbottle')
        with mm:
            sql = 'select * from em_info where em_name = %s'
            mm.cur.execute(sql,name)
            if mm.cur.rowcount == 0:
                print('没有当前员工信息')
            else:
                dept = self.rm.is_dept()
                ip = self.rm.is_ip()
                mac = self.rm.is_mac()
                sql = 'update em_info set em_dept = %s,em_ip = %s,em_mac = %s where em_name = %s'
                mm.cur.execute(sql,(dept,ip,mac,name)) # 注意参数顺序
                print(f'{name}的个人信息更新成功')
    def query_em(self):  # 假设有重名，怎么输出返回值测试 综合了ljust方法的应用
        print('按1通过姓名查询 | 按2通过IP地址查询')
        mm = Mysql_manager('localhost','root','root',3306,'milkbottle')
        num = int(input('请输入选择序号：'))
        if num == 1:
            name = self.rm.is_name()
            with mm:
                sql = 'select * from em_info where em_name = %s'
                mm.cur.execute(sql,name)
                if mm.cur.rowcount>1:
                    print('姓名'.ljust(8),end = '\t')
                    print('部门'.ljust(8),end = '\t')
                    print('ip'.ljust(8),end = '\t')
                    print('mac'.ljust(8))
                    for i in range(0,mm.cur.rowcount):
                        result = mm.cur.fetchone()
                        for j in result:
                            print(j.ljust(8),end = '\t')
                        print() # 每个员工信息之间回车，而不是制表符
                elif mm.cur.rowcount == 1:
                    result = mm.cur.fetchone()
                    print('姓名'.ljust(8),end = '\t')
                    print('部门'.ljust(8),end = '\t')
                    print('ip'.ljust(8),end = '\t')
                    print('mac'.ljust(8))
                    for j in result:
                        print(j.ljust(8),end = '\t')
                    print() # 接着mac后面打印空白后然后回车了
                else:
                    print('查无此人')

                            
    def show_em(self): # 这里验证fetchall的用法。就是个二维元组（列表），双循环打印出来
        mm = Mysql_manager('localhost','root','root',3306,'milkbottle')
        with mm:
            sql = 'select * from em_info'
            mm.cur.execute(sql)
            # 先打印表头
            print('姓名'.ljust(8),end = '\t')
            print('部门'.ljust(8),end = '\t')
            print('ip'.ljust(8),end = '\t')
            print('mac'.ljust(8))
            result = mm.cur.fetchall()
            for i in result:
                for j in i:
                    print(j.ljust(8),end = '\t')
                print()
            

if __name__ == '__main__':
    em = Em_manager()
    em.run()


