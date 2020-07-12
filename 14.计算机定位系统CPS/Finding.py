# 寻找给定mac地址或者IP所在具体端口
# 通过mac查找，遍历核心交换机列表，查找具体在哪个核心交换机
# 通过ip查找，类似。
# 搜索出可能存在的交换机列表。根据版本分成几个大类。分别使用dis mac搜索
# 判断依据。交换机存在该mac。mac所在端口是access端口。（该端口如果有多个mac。则下面有傻瓜交换机）

# 注意每次执行命令先运行sys到全局模式

import time
import paramiko
import pymysql
from Re_manager import *
from Switch_db import *
from Switch_ip_statis import Switch_manager, Switch


class Finding(object):
    def __init__(self):
        pass
        # 测试阶段一个核心
        # self.core_switch_list = []
        # self.core_switch_list.append('172.31.64.1')
        # print(self.core_switch_list)

    # 通过MAC查找
    def find_by_mac(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(
            hostname='172.31.64.1',
            port=22,
            username='admin',
            password='xtgsywb6193',
            look_for_keys=False,
            allow_agent=False
        )

        # terminal连接
        # 这种方法执行慢，最好加上time sleep
        channel = ssh.invoke_shell()
        cmd = 'sys \n'
        channel.send(cmd)
        time.sleep(1)
        cmd = 'dis arp \n'
        channel.send(cmd)
        time.sleep(1)
        result = channel.recv(5000).decode()
        print(type(result))
        print(result)
        # cmd = r'''
        #     user-interface vty 0 4 \n
        #     screen-length 512 \n
        #     quit \n
        #     dis cur \n

        # '''
        # channel.send(cmd)
        # time.sleep(3)
        # result = channel.recv(5000).decode()
        cmd = 'user-interface vty 0 4 \n'
        channel.send(cmd)
        time.sleep(1)
        cmd = 'screen-length 512 \n'
        channel.send(cmd)
        time.sleep(1)
        cmd = 'dis cur \n'
        channel.send(cmd)
        time.sleep(1)
        result = channel.recv(5000).decode()
        print(result)

    def find_by_ip(self):
        pass


if __name__ == "__main__":
    fd = Finding()
    fd.find_by_mac()
