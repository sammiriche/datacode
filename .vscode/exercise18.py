# 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
a = input('请输入字符串：')
b = len(a)
t =[]
for i in range(0,b):
    t.append(a[b-1-i])
print(t)
# 将列表转换为字符串
print(''.join(t))
print(b)
# print(type(a))
