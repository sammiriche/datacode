class Empolyee(object):
    def __init__(self,name,dept,ip,mac):
        self.__name = name
        self.__dept = dept
        self.__ip = ip
        self.__mac = mac

    # 设置相关属性
    def setName(self,name):
        self.__name = name
    def setDept(self,dept):
        self.__dept = dept
    def setIp(self,ip):
        self.__ip = ip
    def setMac(self,mac):
        self.__mac = mac
    
    #获取相关属性

    def getName(self):
        return self.__name
    def getDept(self):
        return self.__dept
    def getIp(self):
        return self.__ip
    def getMac(self):
        return self.__mac

    # 修改内置方法，返回值由内存地址改为指定显示
    def __str__(self):
        return f'姓名：{self.__name} 部门：{self.__dept} IP：{self.__ip} MAC：{self.__mac}'


# 测试模块
if __name__ == "__main__":
    em = Empolyee('lilei','renzi','10','bac')
    print(em)   