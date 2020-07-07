# 从核心交换机获取接入交换机管理IP，并且进行分类
# 交换机名称 类型 地址 品牌 系统版本

import paramiko
from Re_manager import *

# 交换机对象。保存交换机的各种属性值
class Switch(object):
    def __init__(self):
        self.name = ''
        self.sw_type = ''
        self.address = ''
        self.brand = ''
        self.version = ''

# 交换机管理类
class Switch_manager(object):
    def __init__(self):
        # 交换机对象列表
        self.sw_obj_list = []
        # 交换机ip地址列表
        self.sw_ip_list = []
    
    # 判断版本
    def judge_version(self,ip):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(
            hostname=ip,
            port = 22,
            username='admin',
            password='xtgsywb6193',
            allow_agent=False,
            look_for_keys=False
        )
        cmd = 'dis ver'
        stdin,stdout,stderr = ssh.exec_command(cmd)
        result = stdout.read().decode()
        print('----------------')
        # print(result)
        result_ls = result.split('Version')
        # print(type(result_ls))
        # print(len(result_ls))
        print(result_ls[1])
        self.version = result_ls[1].split()[0]
        print('**********')
        print(self.version)

    # 从核心arp获取地址列表
    def collect_ip(self):
        # 首先实例化连接
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(
            hostname='192.168.209.2',
            port = 22,
            username='admin',
            password='xtgsywb6193',
            allow_agent=False,
            look_for_keys=False
        )
        # cmd1 = r'''user-interface vty 0 4
        #         screen-length 100
        #         quit
        #         dis arp'''
        cmd1 = 'dis arp'
        stdin,stdout,stderr = ssh.exec_command(cmd1)
        result = stdout.read().decode()
        print(result)
        result_ls = result.split()
        print(result_ls)
        # 正则判断IP地址
        re = Re_manager()
        for ip in result_ls:
            if re.is_ip(ip):
                # 判断为IP地址，将其添加到地址列表
                self.sw_ip_list.append(ip)
        print(self.sw_ip_list)


if __name__ == "__main__":
    sm = Switch_manager()
    # sm.collect_ip()
    sm.judge_version('192.168.209.2')