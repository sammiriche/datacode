# 管理系统模块，主要是封装增删查改的方法等功能
# 加载数据，显示功能，交互执行功能。保存数据
from student import *


class Manager(object):
    def __init__(self):
        # 存储学生信息，用列表存放。初始为空
        self.student_list = []

    # 入口函数，从这里开始执行。然后里面的功能分别调用模块
    def run(self):
        # 加载学生信息
        self.load_student()
        while True:
            # 显示功能面板，放在while循环。不然程序每次就运行结束。不能交互操作了。
            self.show_menu()
            # 用户输入功能菜单号
            num = int(input('请输入您要进行的菜单号：'))
            # 根据菜单号分别在if判断语句里面进行相关操作
            if num == 1:
                self.add_student()
            elif num == 2:
                self.del_student()
            elif num == 3:
                self.search_student()
            elif num == 4:
                self.modify_student()
            elif num == 5:
                self.show_all_student()
            elif num == 6:
                self.save_student()
            elif num == 7:
                break

    # 功能函数列表
    # 1显示功能菜单面板，不涉及变量。使用静态方法
    @staticmethod
    def show_menu():
        print('-----------------')
        print('1:添加学员')
        print('2:删除学员')
        print('3:查询学员')
        print('4:修改学员')
        print('5:显示所有学员')
        print('6:保存学员信息')
        print('7:退出系统')
        print('-----------------')

    # 2 加载学员信息
    # 打开文件，将文件数据转换到student_list后，就关闭文件。后面的增删查改全部针对student_list
    def load_student(self):
        try:
            f = open('D:\\pythoncode\\StudentsManager\\backup.data', 'r')
        except:
            f = open('D:\\pythoncode\\StudentsManager\\backup.data', 'w')
        else:
            # data是字符串，但是字符串里面看起来像是列表包含字典一样，实际上是字符串
            data = f.read()
            # [{}]转换成[]从列表包含字典转换成 列表包含对象，和以前的student_list保存一致（打印的是列表-对象内存地址）
            # 此时new_list是由字典组成的列表。每个字典就是一个学员，需要将字典转换成对象
            if len(data) != 0:
                new_list = eval(data)
                # print(new_list)
                # print(type(new_list))
                # new_dict = {}
                for i in new_list:  # 这里每个i就是一个字典了
                    student = Student(i['name'], i['gender'], i['tel'])
                    self.student_list.append(student)
        finally:
            f.close()
            print(self.student_list)

    # 3 添加学员函数 从输入获取信息，由此创建student对象。然后添加到列表
    def add_student(self):
        name = input('请输入学员姓名：')
        gender = input('请输入学员性别：')
        tel = input('请输入联系方式：')
        student = Student(name, gender, tel)
        self.student_list.append(student)
        print(self.student_list)
        # print(student)

    # 4删除学员函数。判断是否存在学员
    def del_student(self):
        name = input('请输入待删除学员姓名：')
        for i in self.student_list:
            if name == i.name:
                self.student_list.remove(i)
                print('用户删除成功')
                break
            else:
                print('查无此人')

    # 5 查询学员函数
    def search_student(self):
        name = input('请输入待查询学员姓名：')
        for i in self.student_list:
            if name == i.name:
                print(f'学员姓名：{i.name}学员性别：{i.gender}学员电话：{i.tel}')
                break
            else:
                print('查无此人')

    # 6 修改学员函数
    def modify_student(self):
        name = input('请输入待修改学员姓名：')
        for i in self.student_list:
            if name == i.name:
                i.name = input('请输入修改后姓名:')
                i.gender = input('请输入修改后性别:')
                i.tel = input('请输入修改后电话:')
                print(f'修改成功。。姓名：{i.name}性别：{i.gender}电话：{i.tel}')
                break
            else:
                print('该学员并不存在')

    # 7 显示所有学员，通过for循环
    def show_all_student(self):
        print('姓名\t性别\t电话')
        for i in self.student_list:
            print(f'{i.name}\t{i.gender}\t{i.tel}')

    # 8 保存学员信息
    def save_student(self):
        # 打开存档文件
        f = open('D:\\pythoncode\\StudentsManager\\backup.data', 'w')
        # self.student列表文件已经有数据 但是是个内存地址？重点在对__dict__函数的理解
        # 列表的每个子元素是个字典
        new_list = []
        for i in self.student_list:
            new_list.append(i.__dict__)  # student_list这个表格有问题。看添加里面最后的打印输出格式
        f.write(str(new_list))
        print('信息保存成功')
        f.close()
