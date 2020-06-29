import paramiko


# 封装类，用于SSH连接交换机，控制交换机，通过paramiko类实现
class SSH_switch(object):
    def __init__(self):
        pass

    def ssh_cmd(self):
        # 创建SSH连接客户端对象的实例
        ssh = paramiko.SSHClient()
        # 理解成自动添加信任，忽略安全检查
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 注意后面两个参数对连接的实质影响
        ssh.connect('192.168.10.41',22,'root','sgcc.0527',allow_agent=False,look_for_keys=False)
        # ssh.connect('172.31.64.28',
        #             22,
        #             'admin',
        #             'xtgsywb6193',
        #             allow_agent=False,
        #             look_for_keys=False)
        # 命令字符串
        cmd = 'll'
        # 接收输出结果
        # stdin 标准输入 用户交互使用，比如修改密码
        # stdout 标准输出 正常输出结果在此
        # stderr 标准错误输出

        stdin, stdout, stderr = ssh.exec_command(cmd)
        # 接收输出结果 本身是bytes类型 decode方法的含义注意理解，相当于以UTF8读取输出内容
        # self.result = str(stdout.read().decode(encoding = 'UTF-8'))
        self.result = stdout.read().decode(encoding='UTF-8')  # 这样也不用转换文件类型
        # print(type(self.result))
        print(self.result)
        print('-------------------')
        # 按照回车换行将字符串转换成列表。这样方便以后对单行数据进行处理
        self.result = self.result.splitlines()
        print(type(self.result))
        num = 1
        for i in self.result:
            print(f'输出数据第{num}行：'.ljust(16), end='\t\t')
            print(i)
            num += 1

    # 对输出结果做处理
    def convert(self):
        pass


if __name__ == "__main__":
    s = SSH_switch()
    s.ssh_cmd()
