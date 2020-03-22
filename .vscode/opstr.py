# 字符串操作从文件读取并且再分割好再写入
# class Opstr(object):
#     with open('字符串操作.txt','r') as f:
#         content = f.read()
#         a = content.split()
#         # a = content.splitlines()
#         for i in  a:
#             print(i)


# if __name__ == '__main__':
#     opstr = Opstr()

#  去掉每一行的前面多余的空格以及多余的空行
class Opstr(object):
    with open('字符串操作.txt','r') as f:
        # content = f.read()
        content = f.readlines()
    with open('字符串操作修改.txt','w') as f2:
        for i in content:
            t = i.strip() # 去除每一行首尾的空格
            if len(t)!=0: # 判断行长度（因为每一行是字符串），注意一定要去除首尾空格后再判断长度，不然有空格的字符串长度不为0. 保证空行不写入新字符串
                f2.write(t + '\n') # 每一行后面跟上回车符。跟原来一致
            
        


if __name__ == '__main__':
    opstr = Opstr()