# 求1+2!+3!+...+20!的和
# 递归，每一项是前面的一项乘以n
def digui(n):
    if n == 1:
        return 1
    else:
        return digui(n - 1) * n


sumall = 0
for i in range(1, 21):
    sumall = digui(i) + sumall
print(sumall)
print(digui(5))
