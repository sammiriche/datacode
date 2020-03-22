# 输入三个整数x,y,z，请把这三个数由小到大输出 一定注意下标起始是0 所以range起始从0开始
a = [12,3,9,6,2,7,3]
b = len(a)
for i in range(0,b):
    for j in range(i,b):
        if a[i]>=a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
print(a)
