# 主窗口的命令行形式
# 主要用来练习语法，为GUI版本做准备
from Re_manager import *
from Mysql_manager import *

class Em_manager_cmd(object):
    def __init__(self):
        # 实例正则类。方便调用，肯定用的到
        rem = Re_manager()
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
            num = input(print('请输入功能菜单序号：'))
            # 配合continue语句跳转到while开始
            num = rem.is_num(num) # 先执行后面语句，再返回实际值给左侧num。所以没问题
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
        pass
    def del_em(self):
        pass
    def modify_em(self):
        pass
    def query_em(self):
        pass
    def show_em(self):
        pass

