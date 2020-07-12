# 从核心交换机获取接入交换机管理IP，并且进行分类
# 交换机名称 类型 地址 品牌 系统版本

import paramiko
from Re_manager import *
from Switch_db import *

# 单个交换机对象。保存交换机的各种属性值
class Switch(object):
    def __init__(self,name,ip,brand,version):
        self.name = name
        self.ip = ip
        self.brand = brand
        self.version = version

# 交换机管理类
class Switch_manager(object):
    def __init__(self):
        # 交换机对象列表
        self.sw_obj_list = []
        # 交换机ip地址列表
        self.sw_ip_list = []

    # 判断版本和品牌
    def judge_version(self, ip):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(
            hostname=ip,
            port=22,
            username='admin',
            password='xtgsywb6193',
            allow_agent=False,
            look_for_keys=False
        )
        cmd = 'display version'
        stdin, stdout, stderr = ssh.exec_command(cmd)
        result = stdout.read().decode()
        print('----------------')
        # 首先判断品牌
        if 'H3C' in result:
            self.brand = 'H3C'
        else:
            self.brand = 'Huawei'
        print(f'交换机品牌是 {self.brand}')
        # print(result)
        # 用Version分割。分隔符本身去除
        result_ls = result.split('Version')
        # print(type(result_ls))
        # print(len(result_ls))
        # print('---第一部分----')
        # print(result_ls[0])
        # print('---第二部分----')
        # print(result_ls[1])
        # print('----版本------')
        # # 取第二部分（字符串）去除空格等，取第一个元素,注意自动去除空格
        self.version = result_ls[1].split()[0]
        # print('**********')
        print(self.version)
        # 返回值 两个
        return self.brand, self.version

    # 从核心arp获取地址列表
    def collect_ip(self,core_ip):
        # 首先实例化连接
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(
            hostname= core_ip,
            port=22,
            username='admin',
            password='xtgsywb6193',
            allow_agent=False,
            look_for_keys=False
        )
        # cmd1 = r'''user-interface vty 0 4
        #         screen-length 100
        #         quit
        #         dis arp'''
        cmd1 = 'dis arp interface vlanif 1 ' # 实际当中需要加入管理vlan限制
        stdin, stdout, stderr = ssh.exec_command(cmd1)
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
        print('-----交换机列表')
        print(self.sw_ip_list)

        return self.sw_ip_list

    # 获取交换机名称,返回交换机IP列表
    def get_switch_name(self, ip):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(
            hostname=ip,
            port=22,
            username='admin',
            password='xtgsywb6193',
            look_for_keys=False,
            allow_agent=False
        )

        # ts = paramiko.Transport('192.168.209.2', 22)
        # ts.connect(username='admin', password='xtgsywb6193')
        # ssh = paramiko.SSHClient()
        # ssh._transport = ts
        cmd = 'display cur | include sysname'
        stdin, stdout, stderr = ssh.exec_command(cmd)
        result = stdout.read().decode()
        # 将字符串按照空格和回车切分成列表
        result = result.split('sysname')
        # 按照sysname做分割成两个元素的列表。列表2再按照默认切割，取第一个元素（空格自动去除）
        self.name = result[1].split()[0]
        print(self.name)
        return self.name

    # 更新交换机对象信息到数据库
    def update_switch_db(self,core_ip):
        # 传参的ip是三层核心的交换机IP,自动更新了相应的IP列表
        self.collect_ip(core_ip)
        # 通过循环，获取每一个交换机名称，品牌，版本信息
        for ip in self.sw_ip_list:
            self.get_switch_name(ip)
            self.judge_version(ip)
            self.sw = Switch(self.name,ip,self.brand,self.version)
            print('ceshi')
            # print(f'name:{self.name} \n ip:{ip} \n brand:{self.brand} \n version:{self.version}')
            print(f'ceshi:{self.sw.ip}')
            # 更新交换机对象列表
            self.sw_obj_list.append(self.sw)

        # 循环交换机对象列表。写入信息到数据库
        # 实例化数据库对象
        sw_db = Switch_db()
        with sw_db:
            for sw in self.sw_obj_list:
                sql = 'insert into jiguan_switch values(0,%s,%s,%s,%s)'
                sw_db.exe_db(sql,(sw.name,sw.ip,sw.brand,sw.version))
        

if __name__ == "__main__":
    sm = Switch_manager()
    # sm.collect_ip()
    # a,b = sm.judge_version('192.168.209.2')
    print('----------------------------------------------')
    # print(type(sm.judge_version('192.168.209.2')))
    # print(a)
    # print(b)
    # sm.get_switch_name('192.168.209.2')
    sm.update_switch_db('172.31.64.1')
