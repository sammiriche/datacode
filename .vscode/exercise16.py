# 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和
# 分子，分母都是斐波拉契数列数列，先定义斐波拉契数列数列函数
# 第一项  分子为feibo3 分母为feibo2
def feibo(n):
    if n ==1 or n == 2:
        t = 1
    else:
        t = feibo(n-1)+feibo(n-2)
    return t
a = []
for i in range(1,21):
    r = feibo(i+2)/feibo(i+1)
    # print(r)
    a.append(r)
print(a)
print(sum(a))


