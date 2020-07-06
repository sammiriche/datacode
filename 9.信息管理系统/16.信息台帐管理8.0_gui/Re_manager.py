# 主要对输入是否符合规范做检查，以及对mac格式做转换
# 注意解决self乱用的问题
# 连续按两下跳出引号
# 无论真实是数字还是字符串。用来匹配的格式必须是字符串 '123'

import re

class Re_manager(object):

    # 判断是否是注册账号名
    def is_user(self,user):
        # 正则表达式
        pattern = r'^[A-Za-z0-9_\-]{3,8}$'  # 匹配3-8位的英文字母和数字和横杠。不包括中文
        if re.match(pattern,user):
            print('匹配成功') # 基本上print语句用来检查错误使用
            return user
        else:
            print('匹配失败')
            return None
    
    # 判断是否是密码字符串
    def is_passwd(self,passwd): # 比用户名多了一个.
        pattern = r'^[A-Za-z0-9_\-\.]{1,10}$' # 1到10位数密码
        if re.match(pattern,passwd):
            print('匹配成功')
            return passwd

    # 判断是否是中文名字
    def is_name(self,name):
        pattern = r'^[\u4e00-\u9fa5]{2,4}$' # 2-4位中文字符
        if re.match(pattren,name):
            print('匹配成功')
            return name
        else:
            print('匹配失败')
            return None
    
    # 判断是否是中文部门
    def is_name(self,dept):
        pattern = r'^[\u4e00-\u9fa5]{2,6}$' # 2-6位中文字符
        if re.match(pattren,dept):
            print('匹配成功')
            return dept
        else:
            print('匹配失败')
            return None

    # 判断是否是IP格式
    def is_ip(self,ip):
        pattern = r'^((25[0-4]|2[0-4]\d|1\d\d|\d?\d)\.){3}(25[0-4]|2[0-4]\d|1\d\d|\d?\d)$'
        if re.match(pattern,ip):
            print('匹配成功')
            return ip
        else:
            print('匹配失败')
            return None # 其实不写这句默认返回就是None

    # 判断是否是mac格式
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
            return self.trans_mac(mac)
        else:
            print('匹配失败')

    # 转换mac格式
    def trans_mac(self,mac):
        if '.' in mac:
            mac = mac.replace('.','-')
            return mac
        else:
            # 先去掉冒号
            mac = mac.replace(':','')
            # 转换为列表
            ls_mac = list(mac)
            ls_mac.insert(4,'-')
            ls_mac.insert(9,'-')
            # 再转换回字符串
            mac = ''.join(ls_mac)
            return mac
            
if __name__ == '__main__':
    rem = Re_manager()
    result = rem.is_mac('1122-3211-abcd')
    print(result)