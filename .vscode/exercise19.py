# 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

a = str(input('请输入正整数：'))
print(type(a))
length = (len(a))
print(length)
t = []
for i in range(0,length):
    t.append(a[length-1-i]) 
t1 = ''.join(t)
print(t1)
