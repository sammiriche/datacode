str_ver = r'''H3C Comware Software, Version 7.1.042, ESS 0006P05
Copyright (c) 2004-2013 Hangzhou H3C Tech. Co., Ltd. All rights reserved.
H3C MSR56-60'''

# 第一种方法，假设前面输出固定，获取版本
# 首先按照换行切片，不保留换行符
# 然后按照空格切片
# 最后去列表第四个元素（字符串）的第一个字符转换为数字，作为判断版本依据

# list_ver = str_ver.splitlines(keepends=False)
# print(list_ver)
# list_ver2 = list_ver[0].split(' ')
# print(list_ver2)
# version_num = int(list_ver2[4][0])
# # version_num = version_num[0:3]
# print(version_num)

# 第二种方法，按照version切片，第二个元素首先去掉头部空格，然后截取第一个元素
# 注意大小写
list_ver = str_ver.split('Version')
print(len(list_ver))
# 列表元素2去掉空格的字符串取第一个字符，然后转成
version_num = list_ver[1].strip()
print(version_num)
if version_num == '7':
    print('版本7')
else:
    print('错误')
