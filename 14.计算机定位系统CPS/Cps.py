# 通过mac地址或者IP地址查找所在具体位置

# 交换机信息类
''''
管理交换机所有信息
从核心交换机获取接入层交换机IP列表
通过类别对接入层交换机收集信息并且保存到数据库
数据实现自增，去重等基本功能
在通过for循环收集信息时考虑到paramiko连接失败的可能性以及二次收集问题
'''
import time
import paramiko
from Re_manager import *
from Mysql_manager import *


class SW_info(object):
    # 初始化信息，保存交换机IP列表
    def __init__(self):
        self.sw_list = []
        self.sw_obj = []

    # 从核心收集接入交换机IP信息,注意考虑到修改显示行数问题
    def get_ip_list(self, core_ip):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(
            hostname=core_ip,
            port=22,
            username='admin',
            password='xtgsxxyjb.520',
            allow_agent=False,
            look_for_keys=False
        )
        cmd = r'''
            system
            user-interface vty 0 4
            screen-length 100
            quit
            display arp int vlan 1
            user-interface vty 0 4
            screen-length 20
            quit
        '''
        # cmd = 'display arp int vlan 1 \n'
        channel = ssh.invoke_shell()
        channel.send(cmd)
        time.sleep(1)
        result = channel.recv(5000).decode()
        print(result)

        # 将结果按照空格回车切片，正则判断ip地址。提取出来添加到列表
        result = result.split()  # 转换成列表
        for ip in result:
            re = Re_manager()
            ip = re.is_ip(ip)
            if ip:
                self.sw_list.append(ip)
                print(ip)

    # 首先删除核心交换机
    # 然后while循环，循环一定条件，防止部分交换机连接失败
    # for循环收集所有交换机版本，品牌等信息，并且写入到数据库
    def get_sw_info(self):
        # 先删除核心交换机
        if '172.31.64.1' in self.sw_list:
            self.sw_list.remove('172.31.64.1')

        flag = 0  # 最多循环三次 列表为空，自动跳出
        while flag < 3:
            for ip in self.sw_list:
                try:
                    # 使用transport多个命令操作 固定写法
                    # 首先获取交换机名称
                    ts = paramiko.Transport(ip, 22)
                    ts.connect(username='admin', password='xtgsyjb.6193')
                    ssh = paramiko.SSHClient()
                    ssh._transport = ts
                    cmd = 'display cur | in sysname'
                    stdin, stdout, stderr = ssh.exec_command(cmd)
                    # 将结果分解成列表
                    # 取得sysname的下标，下标+1就是交换机名称

                    result = stdout.read().decode().split()
                    num = 0
                    for i in result:
                        if i == 'sysname':
                            break  # 跳出循环num不再累加
                        else:
                            num += 1
                    name = result[num+1]
                    print(f'交换机名称{name}')

                    # 获取交换机名称和版本
                    ts = paramiko.Transport(ip, 22)
                    ts.connect(username='admin', password='xtgsyjb.6193')
                    ssh = paramiko.SSHClient()
                    ssh._transport = ts
                    cmd = 'display version'  # 注意大小写
                    stdin, stdout, stderr = ssh.exec_command(cmd)
                    result = stdout.read().decode()
                    if 'H3C' in result:
                        brand = 'H3C'
                    else:
                        brand = 'Huawei'
                    version = result.split('Version')[1].split()[0]
                    print(f'交换机品牌{brand}')
                    print(f'交换机版本{version}')

                    # 将IP,名称，品牌，版本写入数据库
                    mm = Mysql_manager()
                    sql = 'insert ignore into jiguan_switch values(0,%s,%s,%s,%s)'
                    with mm:
                        mm.exe_db(sql, (name, ip, brand, version))
                    self.sw_list.remove(ip)
                except:
                    print('连接当前服务器失败')
            if self.sw_list == []:
                break
            flag += 1
        if self.sw_list:
            print(f'下列交换机无法连接上{self.sw_list}')
        else:
            print('交换机信息更新成功')


if __name__ == "__main__":
    sw = SW_info()
    sw.get_ip_list('192.168.209.2')
    sw.get_sw_info()
