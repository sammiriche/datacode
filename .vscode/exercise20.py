# 一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同
a = input('请输入五位数：')
print(type(a))
flag = 0
for i in range(0,5):
    if a[i]!=a[4-i]:
        # print('不是回文数')
        flag = 1
        break
    # print('OK')

if flag ==0:
    print('是回文数')
else:
    print("不是回文数")