# 有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中
a = [3,1,8,2,6,5,9,0,16,21]
# a.append(7)
# print(a)
# a.sort()
# print(a)

# 另外一种方法
# t = 7
# a.sort()
# print(a)
# for i in a:
#     if a[i]<t<a[i+1]:
#         a.insert(i+1, t)
#         break
# print(a)

# b = a[-1:0:-1]
# print(b)
# print(a)
# a.reverse()
# print(a)
b = []
for i in range(0,len(a)):
    b.append(a[len(a)-1-i])
print(b)
