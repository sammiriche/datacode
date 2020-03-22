# 杨辉三角第二种解法
# 规律。行标为i，列表为j
# j=1 则肯定为1 或者 i=j  也是1 其他项的规律  每一行是个具体对象
# 每一个数值都是函数的返回值
def lst(i, j):
    if i == j or j == 1:
        return 1
    else:
        return lst(i - 1, j) + lst(i - 1, j - 1)
        # return 2

# 这里循环要从1开始，不然 在调用函数会出现负数 ？为什么从0开始递归超过深度？
# 因为从0开始，那么第二次外循环，就会出现lst(1,0)这个无法递归了。 从1开始，j最小项是1 函数里有默认返回值1.所以不会报错
for i in range(1, 11):
    for j in range(1, i + 1):
        print(lst(i, j),end = ' ')
    print()
