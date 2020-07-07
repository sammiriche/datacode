# 对输入格式进行判断和返回
import re

class Re_manager(object):
    # 判断管理员账号格式
    def is_user(self,user):
        pattern = r'^[A-Za-z0-9_\-]{3,10}$' # 3-10位英文字符包括下划线
        result = re.match(pattern,user)
        if result:
            return user
        else:
            print('账号格式不匹配')
            return None

    # 判断管理员密码格式
    def is_passwd(self,passwd):
        pattern = r'^[A-Za-z0-9_\-\.]{3,10}$' # 密码可以包含英文句号
        result = re.match(pattern,passwd)
        if result:
            return passwd
        else:
            print('密码不符合要求')
            return None

    # 判断中文姓名格式
    def is_name(self,name):
        pattern = r'^[\u4e00-\u9fa5]{2,4}$' # 2-4位中文字符
        result = re.match(pattern,name)
        if result:
            return name
        else:
            print('姓名格式不对')
            return None

    # 判断部门格式
    def is_dept(self,dept):
        pattern = r'^[\u4e00-\u9fa5]{2,6}$' # 2-6位中文字符
        result = re.match(pattern,dept)
        if result:
            return dept
        else:
            print('请输入正确的部门')
            return None

    # 判断IP格式
    def is_ip(self,ip):
        pattern = r'^((25[0-4]|2[0-4]\d|1\d\d|\d?\d)\.){3}(25[0-4]|2[0-4]\d|1\d\d|\d?\d)$'
        result = re.match(pattern,ip)
        if result:
            return ip
        else:
            # print('请输入正确的IP格式')
            return None
    
    # 判断mac格式
    def is_mac(self,mac):
        pattern1 = r'^(([0-9a-fA-F]{4}-){2}[0-9a-fA-F]{4})$'  # xxxx-xxxx-xxxx 默认保存格式
        pattern2 = r'^(([0-9a-fA-F]{4}\.){2}[0-9a-fA-F]{4})$'  # xxxx.xxxx.xxxx
        pattern3 = r'^(([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2})$'  # xx:xx:xx:xx:xx:xx
        result1 = re.match(pattern1,mac)
        result2 = re.match(pattern2,mac)
        result3 = re.match(pattern3,mac)
        if result1:
            return mac
        elif result2 or result3:
            mac = self.trans_mac(mac)
            print('转换mac格式成功')
            return mac
        else:
            print('mac格式不符合要求')
            return None

    # 判断房间号3位数字
    def is_room(self,room):
        pattern = r'^[1-9][0-9]{2}$' # 必须3位数字,从100开始
        result = re.match(pattern,room)
        if result:
            return room
        else:
            print('房间编号错误')
            return None
        
    # 判断交换机地址
    def is_switch(self,switch):
        return self.is_ip(switch) # 直接调用判断IP
    
    # 判断端口格式
    def is_port(self,port):
        pattern = r'^[1-9][0-9]{0,1}$' # 大括号对后面方框有效，所以数字范围是1-99
        result = re.match(pattern,port)
        if result:
            return port
        else:
            print('端口格式不正确')
            return None
    

    # mac格式转换
    def trans_mac(self,mac):
        if '.' in mac:
            mac = mac.replace('.','-')
            return mac
        else:
            # 先去掉冒号
            mac = mac.replace(':','')
            ls_mac = list(mac)
            ls_mac.insert(4,'-')
            ls_mac.insert(9,'-')
            mac = ''.join(ls_mac)
            return mac
    

        