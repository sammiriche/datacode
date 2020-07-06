#控制面板，增删查改这些功能都在这里体现？
"""
测试代码
# import infomation
from infomation import Info
# employ = infomation.Info('黎明','人资部','10.228.198.1','00-0c-2a-5a-4a-20')
employ = Info('黎明', '人资部', '10.228.198.1', '00-0c-2a-5a-4a-20')
print(employ.get_name())
"""

# 控制面板也是一个类
from infomation import Info
import os
import pickle
import re

class Control(object):
    # 这个类应该把员工类组合进来。那么所有员工应该保存在一个表里面，初始表格为空
    def __init__(self):
        self.employee_list = []

    #类的静态方法，不调用任何属性参数
    @staticmethod
    def show():
        print('*'*24)
        print('欢迎使用员工信息系统')
        print('-'*24)
        print('1：显示所有员工信息')  # 在子菜单实现排序功能
        print('2：查询员工信息')  # 实现模糊查询功能
        print('3：添加员工信息')
        print('4：删除员工信息')
        print('5：修改员工信息')
        print('6：保存员工信息')
        print('7：退出当前系统')
        print('*'*24)

    # 各个子菜单函数
    def show_info(self):
        if self.employee_list:
            print('请先保存信息') # 如果保存了还是会提示
        else:
            if os.path.exists(('empolyee.data')):
                if os.path.getsize('empolyee.data'):
                    f = open('empolyee.data','rb')
                    self.employee_list = pickle.load(f)
                    f.close()
                    print('姓名',end = '\t\t')
                    print('部门',end = '\t\t')
                    print('IP',end = '\t')
                    print('MAC')
                    for i in self.employee_list:
                        print(i.get_name(),end = '\t\t')
                        print(i.get_dept(),end = '\t\t')
                        print(i.get_ip(),end = '\t')
                        print(i.get_mac())

                

    def search_em(self):
        pass
    def add_em(self):
        # 每次新增一个。相当于新增一个员工类对象
        # 首先加载存储文件，将其读取到内存，保存信息到list
        # 判断文件是否存在。并且是否为空
        if os.path.exists('empolyee.data') :
            if os.path.getsize('empolyee.data'):
                f = open('empolyee.data','rb')
                self.employee_list = pickle.load(f)
                f.close()
        name = input('请输入新员工姓名：')
        dept = input('请输入新员工部门：')
        ip = input('请输入新员工IP地址：')
        mac = input('请输入新员工MAC地址：')
        info = Info(name,dept,ip,mac)
        self.employee_list.append(info)
        print('员工信息更新成功')
        #下面这里可以直接打印对象是因为对应类修改了str函数
        for i in self.employee_list:
            print(i)
    def del_em(self):
        if len(self.employee_list) == 0:
            print('当前没有任何员工信息')
        # 暂时通过姓名来删除  
        name = input('请输入需要删除的员工的姓名')
        for i in self.employee_list:
            # 如果get_name不带括号，她就是一个变量名字。变量类型是方法。。返回是方法的内存地址。带括号她的类型就是方法的返回值。
            if name == i.get_name():
                self.employee_list.remove(i)
                print(f'{name}信息删除成功')
                break
            else:
                print('系统不存在当前员工信息')

    def modify_em(self):
        name = input('请输入需要修改的员工姓名')
        for i in self.employee_list:
            if name == i.get_name():
                i.set_dept(input('请输入新的部门名称：'))
                i.set_ip(input('请输入新的IP地址：'))
                i.set_mac(input('请输入新的MAC地址：'))
                print('信息修改成功')
                print(i)
                break
            else:
                print('系统不存在当前员工信息')
    def save_em(self):
        # if not os.path.exists('empolyee.data'):
        # 文件操作三部曲 打开-编辑-关闭 打开默认模式就是r
        f = open('empolyee.data','wb') # 文件作为一个对象加载到内存,wb模式
        # 文件全部重新写入，旧的覆盖，因为在前面读取信息时里面的文件已经读取在内存了。旧信息其实没用
        # 将列表（对象也行）序列化后可以保存到文件，注意格式。
        pickle.dump(self.employee_list,f)
        print('信息保存成功')
        f.close()
        self.employee_list = []  # 保存好清空列表方便功能1模块的判断。以后想其他办法改进
        # 下面测试代码通过
        # print('打开测试看看')
        # f = open('empolyee.data','rb') # 文件作为一个对象加载到内存,wb模式
        # a = pickle.load(f)
        # print(type(a))
        # for i in a:
        #     print(i)
    #类的入口方法，从这里开始执行（面向过程来理解）
    def run(self):
        Control.show()
        while True:
            num = input('请输入您需要的功能模块：')
            # ^字符串开始 $字符串结束 r前缀代表raw原样输出
            pattern = re.compile(r'^[1234567]$')
            # pattern = re.compile(r'\b[a-zA-Z\']+\b')
            if re.match(pattern,num) == None:
                print('请输入正确的序号: 数字1-7')
            else:
                num = int(num)
            if num == 1:
                self.show_info()
            if num == 2:
                self.search_em()
            if num == 3:
                self.add_em()
            if num == 4:
                self.del_em()
            if num == 5:
                self.modify_em()
            if num == 6:
                self.save_em()
            if num == 7:
                break
        
                

if __name__ == '__main__':
    cr = Control()
    cr.run()