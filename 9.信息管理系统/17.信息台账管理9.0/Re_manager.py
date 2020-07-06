# 主要用作输入判断，不需要循环等待

import re

class Re_manager(object):
    # 判断是否是登录帐号类型
    def is_account(self,account):
        pattern = r'^[A-Za-z0-9_\-]{3,10}$'
        result  = re.match(pattern,account)
        if result:
            print('匹配成功')
            return account
        else:
            print('匹配失败')
            return None

    # 判断是否是密码类型
    def is_passwd(self,passwd):
        pattern = r'^[A-Za-z0-9_\-\.]{1,10}$'
        result = re.match(pattern,passwd)
        if result:
            print('匹配成功')
            return passwd
        else:
            print('匹配失败')
            return None
    
    # 判断是否是员工姓名
    def is_name(self,name):
        pattern = r'^[\u4e00-\u9fa5]{2,4}$' # 2-4位中文字符
        result = re.match(pattern,name)
        if result:
            print('匹配成功')
            return name
        else:
            print('匹配失败')
            return None

    def is_dept(self,dept):
        pattern = r'^[\u4e00-\u9fa5]{2,6}$' # 2-6位中文字符
        result = re.match(pattern,dept)
        if result:
            print('匹配成功')
            return dept
        else:
            print('匹配失败')
            return None

    # 判断是否是IP格式
    def is_ip(self,ip):
        pattern = r'^((25[0-4]|2[0-4]\d|1\d\d|\d?\d)\.){3}(25[0-4]|2[0-4]\d|1\d\d|\d?\d)$'
        result = re.match(pattern,ip)
        if result:
            print('匹配成功')
            return ip
        else:
            print('匹配失败')
            return None

    # 判断是否是mac格式
    def is_mac(self,mac):
        pattern1 = r'^(([0-9a-fA-F]{4}-){2}[0-9a-fA-F]{4})$'  # xxxx-xxxx-xxxx 默认保存格式
        pattern2 = r'^(([0-9a-fA-F]{4}\.){2}[0-9a-fA-F]{4})$'  # xxxx.xxxx.xxxx
        pattern3 = r'^(([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2})$'  # xx:xx:xx:xx:xx:xx
        result1 = re.match(pattern1,mac)
        result2 = re.match(pattern2,mac)
        result3 = re.match(pattern3,mac)
        if result1:
            print('匹配成功')
            return mac
        elif result2:
            print('转换成功2')
            return(self.trans_mac(mac)) # 把mac传递进函数，返回来再赋值给自己
        elif result3:
            print('转换成功3')
            return(self.trans_mac(mac)) 
        else:
            print('匹配失败')
            return None
    
    def trans_mac(self,mac):
        if '.' in mac:
            mac = mac.replace('.','-')
            return mac
        else:
            # 先去掉冒号
            mac = mac.replace(':','')
            # 转换为列表进行添加操作
            ls_mac = list(mac)
            ls_mac.insert(4,'-')
            ls_mac.insert(9,'-') # 列表是可变类型，不用赋值给变量
            
            # 再从列表转换回来
            mac = ''.join(ls_mac)
            return mac # 注意不要忘记
            


if __name__ == '__main__':
    rem = Re_manager()
    result = rem.is_mac('a2:b3:c4:d6:e5:f8')
    print(result)

