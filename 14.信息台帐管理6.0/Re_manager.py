# 正则类主要封装 判断输入合法性问题,合法直接返回输入值，不合法则提示
# 为了方便简化语句。循环还是放在正则类里面
import re
class Re_manager(object):
    # 判断是否是用户名
    def is_user(self):
        while 1:
            self.user = input('请输入用户名：')
            pattern = r'^[A-Za-z0-9_\-]{3,8}$'  # 匹配3-8位的英文字母和数字和横杠。不包括中文
            result = re.match(pattern,self.user)
            if result:
                return self.user # 因为函数就一个循环，这里不需要break了直接return就跳出函数了
            else:
                print('不符合用户名规则')
    # 判断是否是密码
    def is_passwd(self):
        while 1:
            self.passwd = input('请输入用户密码：')
            pattern = r'^[A-Za-z0-9_\-\.]{1,8}$' #比用户名多了一个.的特殊字符 1-8位密码
            result = re.match(pattern,self.passwd)
            if result:
                return self.passwd
            else:
                print('密码设置不符合规则')
    # 判断是否是姓名
    def is_name(self):
        while 1:
            self.name = input('请输入员工姓名：')
            pattern = r'^[\u4e00-\u9fa5]{2,4}$'
            result = re.match(pattern,self.name)
            if result:
                return self.name
            else:
                print('姓名输入不符合规则')
    # 判断是否是部门
    def is_dept(self):
        while 1:
            self.dept = input('请输入部门名称：')
            pattern = r'^[\u4e00-\u9fa5]{2,6}$'
            result = re.match(pattern,self.dept)
            if result:
                return self.dept
            else:
                print('部门设置不符合规则')
    # 判断是否是IP
    def is_ip(self):
        while 1:
            self.ip = input('请输入IP格式地址：')
            pattern = r'^((25[0-4]|2[0-4]\d|1\d\d|\d?\d)\.){3}(25[0-4]|2[0-4]\d|1\d\d|\d?\d)$'
            result = re.match(pattern,self.ip)
            if result:
                return self.ip
            else:
                print('ip格式不正确')
    # 判断是否是mac
    def is_mac(self):
        while 1:
            self.mac = input('请输入mac地址：')
            pattern1 = r'^(([0-9a-fA-F]{4}\.){2}[0-9a-fA-F]{4})$'  # xxxx.xxxx.xxxx
            pattern2 = r'^(([0-9a-fA-F]{4}-){2}[0-9a-fA-F]{4})$'  # xxxx-xxxx-xxxx
            pattern3 = r'^(([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2})$'  # xx:xx:xx:xx:xx:xx
            result1 = re.match(pattern1,self.mac)
            result2 = re.match(pattern2,self.mac)
            result3 = re.match(pattern3,self.mac)
            if result1 or result2 or result3:
                self.mac = self.trans_mac(self.mac) # 直接在判断之后转换再返回
                return self.mac
            else:
                print('mac格式不正确')

    # 判断输入是否是指定范围数字
    def is_num(self):
        while 1:
            self.num = input('请输入1-8之间的数字：')
            pattern = r'^[1-8]$'
            result = re.match(pattern,self.num)
            if result:
                return int(self.num)
            else:
                print('请输入正确的数字范围')

    def trans_mac(self,mac): # 转换mac格式
        if '-' in mac:   # 传参后，函数里就用了mac这个变量了
            return mac
        elif '.' in mac:
            mac = mac.replace('.','-') # 注意字符串不可变变量
            return mac
        else:
            mac = mac.replace(':','') #  先去掉冒号
            # 然后转换成列表操作
            ls_mac = list(mac)
            ls_mac.insert(4,'-')
            ls_mac.insert(9,'-')
            # 然后重新转成字符串
            mac = ''.join(ls_mac)
            return mac