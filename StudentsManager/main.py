# 导入管理系统模块
# import manager_system
from manager_system import *
# 启动管理系统。加入判断。保证在当前文件才能执行
if __name__ == '__main__':
    manager = Manager()
    # 调用manager的run方法
    manager.run()
