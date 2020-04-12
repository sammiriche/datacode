# 简化功能，传入参数，直接判断返回。不用等待输入。为gui版本输入检查做准备
import re

class Re_manager(object):

    # 判断是否是1-8的数字
    def is_num(self,num):
        self.num = num
        pattern = r'^[1-8}$'
        if re.match(pattern,self.num):
            # 匹配成功
            return int(self.num)  # 转换为整数型
        else:
            print('匹配失败')
            return None

    # 判断是否是用户名格式（注册用）
    def is_user(self,user):
        self.user = user:
        pattern = r'^[A-Za-z0-9_\-]{3,8}$'  # 匹配3-8位的英文字母和数字和横杠。不包括中文
        result = re.match(pattern,self.user)
        if result:
            return self.user
        else:
            print('匹配失败')
            return None

    # 判断是否是密码用格式
    def is_passwd(self,passwd):
        self.passwd = passwd
        pattern = r'^[A-Za-z0-9_\-\.]{1,8}$' #比用户名多了一个.的特殊字符 1-8位密码
        result = re.match(pattern,self.passwd)
        if result:
            return self.passwd
        else:
            print('匹配失败')
            return None
    
    # 判断是否是名字（信息管理系统员工姓名判断）
    def is_name(self,name):
        self.name = name
        pattern = r'^[\u4e00-\u9fa5]{2,4}$'
        result = re.match(pattern,self.name)
        if result:
            return self.name
        else:
            print('匹配失败')
            return None
    
    # 判断是否是部门
    def is_dept(self,dept):
        self.dept = dept
        pattern = r'^[\u4e00-\u9fa5]{2,6}$' # 2-6位中文字符
        result = re.match(pattern,self.dept)
        if result:
            return self.dept
        else:
            print('匹配失败')
            return None
    
    # 判断是否是IP
    def is_ip(self,ip):
        self.ip = ip
        pattern = r'^((25[0-4]|2[0-4]\d|1\d\d|\d?\d)\.){3}(25[0-4]|2[0-4]\d|1\d\d|\d?\d)$'
        result = re.match(pattern,self.ip)
        if result:
            return self.ip
        else:
            print('匹配失败')
            return None

    # 判断是否是mac
    def is_mac(self,mac):
        self.mac = mac
        pattern1 = r'^(([0-9a-fA-F]{4}-){2}[0-9a-fA-F]{4})$'  # xxxx-xxxx-xxxx 默认保存格式
        pattern2 = r'^(([0-9a-fA-F]{4}\.){2}[0-9a-fA-F]{4})$'  # xxxx.xxxx.xxxx
        pattern3 = r'^(([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2})$'  # xx:xx:xx:xx:xx:xx
        result1 = re.match(pattern1,self.mac) 
        result2 = re.match(pattern2,self.mac) 
        result3 = re.match(pattern3,self.mac)
        if result1 == None or result2 == None or result3 == None:
            print('匹配失败')
            return None
        elif result1:  # 如果三者都不为0.那么肯定有两个None，一个非None 只可能匹配一个
            return self.mac
        else:
            return self.trans_mac(self.mac)
    
    # mac格式转换,支持xxxx.xxxx.xxxx  xx:xx:xx:xx:xx:xx转换为 xxxx-xxxx-xxxx
    def trans_mac(self,mac):
        if '.' in mac:
            mac = mac.replace('.','-')
            return mac
        else: # 针对xx:xx:xx:xx:xx:xx转换
            # 先去掉冒号
            mac = mac.replace(':','')
            # 转换为列表插入连接符
            ls_mac = list(mac)
            ls_mac.insert(4,'-')
            ls_mac.insert(9,'-')
            mac = ''.join(ls_mac) # 列表转字符串
            return mac
            

