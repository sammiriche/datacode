# 测试读取linux文件目录信息

import paramiko


class SSH_client(object):
    def __init__(self):
        pass

    def SSH_cmd(self):
        #  创建SSH连接对象
        ssh = paramiko.SSHClient()
        # 允许连接不在信任主机列表，不用理解
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接到指定服务器,寻找key设置为假
        ssh.connect(
            hostname='192.168.10.41',
            port=22,
            username='root',
            password='sgcc.0527',
            allow_agent=False,
            look_for_keys=False
        )
        # 使用terminal 发送命令，SSH通道运行命令后不会关闭
        # cmd = 'df'
        # chanel = ssh.invoke_shell()
        # chanel.send(cmd + '\n')
        # result = chanel.recv(5000).decode()
        # print(type(result))
        # print(result)
        # print('============================')
        # chanel.send('ifconfig' + '\n')
        # result = chanel.recv(5000).decode()
        # print(result)

        # 使用SSHClient单次连接
        # cmd1 = 'll'
        # stdin, stdout, stderr = ssh.exec_command('ifconfig')
        # result = stdout.read().decode()
        # print(result)
        # print('----------------')
        # stdin, stdout, stderr = ssh.exec_command('ls -al')
        # result = stdout.read().decode()
        # print(result)

        # 使用transport
        ts = paramiko.Transport('192.168.10.41', 22)
        ts.connect(username='root', password='sgcc.0527')
        ssh = paramiko.SSHClient()
        ssh._transport = ts
        stdin, stdout, stderr = ssh.exec_command('df')
        result = stdout.read().decode()
        print(result)
        print('------')
        stdin, stdout, stderr = ssh.exec_command('ls -al')
        result = stdout.read().decode()
        print(result)


if __name__ == "__main__":
    new_ssh = SSH_client()
    new_ssh.SSH_cmd()
