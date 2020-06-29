# 脚本修改360配置文件当中的服务器更新地址选项

import os
def alter_360(file, old_ip, new_ip):
    # 读取配置文件，保存进列表
    with open(file, 'r', encoding='utf-8') as f_r:
        content = f_r.readlines()  # 结果是列表类型

    # 更改文件
    with open(file, 'w', encoding='utf-8') as f_w:
        # 定位到服务器地址所在行，进行修改
        for i in content:
            if old_ip in i:
                i = i.replace(old_ip, new_ip)
                print(i)

            # w模式第一次清空所有内容，在没有关闭情况下，从指针处再写入
            f_w.write(i)
        f_w.write('modify by milkbottle 20200609')


# 定义路径，旧服务器地址和新服务器地址
file_64bit = 'C:\\Program Files (x86)\\360\\360Safe\\deepscan\\smart.dat'
file_32bit = 'C:\\Program Files\\360\\360Safe\\deepscan\\smart.dat'
str1 = 'sev=10.229.241.38:18000'
str2 = 'sev=xnfbd.hb.sgcc.com.cn:80'

# 程序入口
if 'PROGRAMFILES(X86)' in os.environ:
    print('64位系统')
    alter_360(file_64bit,str1,str2)
else:
    alter_360(file_32bit,str1,str2)

