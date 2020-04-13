# 主窗口的命令行形式
# 主要用来练习语法，为GUI版本做准备
from Re_manager import *
from Mysql_manager import *

class Em_manager_cmd(object):
    def __init__(self):
        # 实例正则类。方便调用，肯定用的到
        self.rem = Re_manager()
        self.run()

    # 入口，实例化自动调用到会运行
    def run(self):
        while 1:
                # 显示操作界面
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

            # 输入判断和跳转
            num = input('请输入功能序号：')
            # 配合continue语句跳转到while开始
            num = self.rem.is_num(num) # 先执行后面语句，再返回实际值给左侧num。所以没问题
            if num == None:
                continue  # 终止当前循环，重新开始循环，
            elif num == 1:
                self.add_em()
            elif num == 2:
                self.del_em()
            elif num == 3:
                self.modify_em()
            elif num == 4:
                self.query_em()
            elif num == 5:
                self.show_em()
            elif num == 6:
                pass
            elif num == 7:
                pass
            else:
                break

    def add_em(self):
        name = input('请输入员工姓名：')
        dept = input('请输入员工部门：')
        ip = input('请输入员工IP：')
        mac = input('请输入员工MAC：')

        # 传入正则类做比较
        name = self.rem.is_name(name)
        dept = self.rem.is_dept(dept)
        ip = self.rem.is_ip(ip)
        mac = self.rem.is_mac(mac)

        if name == None or dept == None or ip == None or mac == None:
            print('输入格式不正确。返回主菜单')  # 如果想返回子菜单，需要添加子循环
            print(name)
            print(dept)
            print(ip)
            print(mac)
        else:
            mm = Mysql_manager('localhost','root','root',3306,'milkbottle')
            with mm:
                sql = 'insert into em_info values(%s,%s,%s,%s)'
                mm.cur.execute(sql,(name,dept,ip,mac)) # 第二个参数一个元祖，字符串都行，多个就用元祖
                print(f'{name}的个人信息添加成功')
    def del_em(self):
        name = input('请输入员工姓名：')
        name = self.rem.is_name(name)
        if name == None:
            print('输入格式不正确')
        else:
            mm = Mysql_manager('localhost','root','root',3306,'milkbottle')
            with mm:
                sql = 'delete from em_info where em_name = %s'
                mm.cur.execute(sql,name)
                if mm.cur.rowcount == 0: # 代表上条语句执行后受影响条数。如果影响行数为1.代表成功
                    print('没有当前员工信息')
                else:
                    print('当前员工信息删除成功')
    def modify_em(self): # 注意用的都是临时变量
        name = input('请输入准备修改的员工的姓名：')
        name = self.rem.is_name(name)

        dept = input('部门：')
        dept = self.rem.is_dept(dept)
        ip = input('ip：')
        ip = self.rem.is_ip(ip)
        mac = input('mac：')
        mac = self.rem.is_mac(mac)
        if dept == None or ip == None or mac == None or name == None:
            print('需要修改的信息格式不正确。')
        else:
            mm = Mysql_manager('localhost','root','root',3306,'milkbottle')
            with mm: # 判断是否存在和修改一条过。通过rowcount判断是否修改了数据
                sql = 'update em_info set em_dept = %s,em_ip = %s,em_mac = %s where em_name = %s'
                mm.cur.execute(sql,(dept,ip,mac,name))
                print('信息修改成功')
            
    def query_em(self):
        print('按1通过姓名查询 | 按2通过ip查询')
        num = int(input(''))
        if num == 1:
            name = input('请输入员工姓名：')
        if num == 2:
            ip = input('请输入IP地址：')
        name = self.rem.is_name(name)
        ip = self.rem.is_ip(ip)
        if name == None or ip == None:  # 注意这里的逻辑关系为什么是or 因为前面两个if只会执行一个
            print('输入格式不正确')
        else:
            mm = Mysql_manager('localhost','root','root',3306,'milkbottle')
            with mm:
                # sql = 'select * from em_info where em_name = %s or em_ip =%s' # 这条语句可行，但是不好传参
                sql1 = 'select * from em_info where em_name = %s'
                sql2 = 'select * from em_info where em_ip = %s'
                pass


    def show_em(self):
        # 先打印输出抬头
        print('姓名'.ljust(8),end = '\t')
        print('部门'.ljust(8),end = '\t')
        print('ip'.ljust(8),end = '\t')
        print('mac'.ljust(8))


        mm = Mysql_manager('localhost','root','root',3306,'milkbottle')
        with mm:
            sql = 'select * from em_info'
            mm.cur.execute(sql)
            result = mm.cur.fetchall() # result 是个二维元祖
            # 方法一
            # for i in result: # 每个元祖对每个元素取值
            #     print(i[0].ljust(8),end = '\t')
            #     print(i[1].ljust(8),end = '\t')
            #     print(i[2].ljust(8),end = '\t')
            #     print(i[3].ljust(8))

            #方法2 
            for i in result:
                for j in i:
                    print(j.ljust(8),end = '\t')
                print()
if __name__ == '__main__':
    em = Em_manager_cmd()
