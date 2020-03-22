# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
# 反弹高度函数
def height(n):
    if n == 0:
        m = 100
    else:
        m = height(n-1)*0.5
    return m
# 第n次运行距离
def long(height,n):
    t = height(n-1)*1.5
    lista.append(t)
    return t


n = 10
lista =[]
for i in range(1,n+1):
    long(height,i)
print(height(n))
print(sum(lista))
