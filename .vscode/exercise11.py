# 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数
# 首先求出它的因子。即可以整除

#首先循环出1000以内所有的整数
for i in range(1, 1001):
    sum = 0
    for j in range(1, i):
        if i % j == 0:
            sum = sum + j
    if sum == i:
        print(i)


# for i in range(1, 1001):
#     sum = 0
#     for j in range(1, i):
#         if i % j == 0:
#             sum += j
#     if sum == i:
#         print(i)