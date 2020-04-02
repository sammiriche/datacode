# 正则类主要封装 判断输入合法性问题,合法直接返回输入值，不合法则提示
# 循环判断暂时不放到这里面看看
import re
class Re_manager(object):
    # 判断是否是用户名
    def is_user(self,user):
        self.user = user
        pattern = r'^[A-Za-z0-9_\-]{3,8}$'  # 匹配3-8位的英文字母和数字和横杠。不包括中文
        result = re.match(pattern,self.user)
        if result:
            return self.user
        else:
            print('不符合用户名规则')
    # 判断是否是密码
    def is_passwd(self,passwd):
        self.passwd = passwd
        pattern = r'^[A-Za-z0-9_\-\.]{1,8}$' #比用户名多了一个.的特殊字符 1-8位密码
        result = re.match(pattern,self.passwd)
        if result:
            return self.passwd
        else:
            print('密码设置不符合规则')
    # 判断是否是姓名
    def is_name(self,name):
        self.name = name
        pattern = r'^[\u4e00-\u9fa5]{2,4}$'
        result = re.match(pattern,self.name)
        if result:
            return self.name:
        else:
            print('名字设置不符合规则')
    # 判断是否是部门
    def is_dept(self,dept):
        self.dept = dept
        pattern = r'^[\u4e00-\u9fa5]{2,6}$'
        result = re.match(pattern,self.dept)
        if result:
            return self.dept
        else:
            print('部门设置不符合规则')
    # 判断是否是IP
    def is_ip(self,ip):
        self.ip = ip
        pattern = r'^((25[0-4]|2[0-4]\d|1\d\d|\d?\d)\.){3}(25[0-4]|2[0-4]\d|1\d\d|\d?\d)$'
        result = re.match(pattern,self.ip)
        if result:
            return self.ip
        else:
            print('ip格式不正确')
    # 判断是否是mac
    def is_mac(self,mac):
        self.mac = mac
        pattern1 = r'^(([0-9a-fA-F]{4}\.){2}[0-9a-fA-F]{4})$'  # xxxx.xxxx.xxxx
        pattern2 = r'^(([0-9a-fA-F]{4}-){2}[0-9a-fA-F]{4})$'  # xxxx-xxxx-xxxx
        pattern3 = r'^(([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2})$'  # xx:xx:xx:xx:xx:xx
        result1 = re.match(pattern1,self.mac)
        result2 = re.match(pattern2,self.mac)
        result3 = re.match(pattern3,self.mac)
        if result1 or result2 or result3:
            return self.mac
        else:
            print('mac格式不正确')