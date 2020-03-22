# 斐波拉契数列 1 1 2 3 5
def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n-1) + f(n-2)
num = int(input('请输入长度：'))
for i in range(1,num+1):
    print(f(i),end = ' ')
