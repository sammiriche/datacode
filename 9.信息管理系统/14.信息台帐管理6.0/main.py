# 程序入口，包括注册和登录

from User_manager import *
from Re_manager import *
from Em_manager import *
print('欢迎使用员工信息管理系统')
print('-'*32)
print('1:注册用户 | 2:登录用户')
um = User_manager()
re = Re_manager()
num = int(input(''))
if num == 1:
    user = re.is_user()
    passwd = re.is_passwd()
    um.register(user,passwd)
if num == 2:
    user = re.is_user()
    passwd = re.is_passwd()
    if um.verify(user,passwd):
        em = Em_manager()
        em.run()
    else:
        print('退出当前程序')