# 编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
def tns(n):
    if n == 1:
        return 1/2
    return tns(n-1) + 1/(2*n)

def tnd(n):
    if n == 1:
        return 1
    return tnd(n-1) + 1/(2*n-1)

n = int(input('请输入正整数：'))
if int(n%2) == 1:
    print(tnd(n))
elif int(n%2)==0:
    print(tns(n))

