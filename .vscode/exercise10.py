# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字
a = int(input('请输入a的数值：'))
n = int(input('请输入个数：'))
# 递归求取第n项的值
def digui(n, a):
    if n == 1:
        t = a
        return t
    else:
        t = digui(n-1,a)*10 + a
        return t
num = 0
for i in range(1,n+1):
    num = num +digui(i, a)
    # if i == n:
        # print(num)
print(num)

