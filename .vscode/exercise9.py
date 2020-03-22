# 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5
num = int(input('请输入一个正整数:'))
print(f'{num} = ', end = ' ') 
while True:
    for i in range(2,num+1):
        # 取回除法余数，如果此时为0，i一定是最小的质因数，因为如果不是质因数，肯定在上一个循环就能等于0了
        if num%i ==0:
            # 方便和line3做衔接
            print(i, end = ' ')
            # num 变成除以i以后的数，再来循环，由于运算结果是浮点，需要转换
            num = int(num/i)
            # 下面的break只是跳出for循环，但是while循环依然在。这个时候又从while循环开始，i从2开始。这样就不会错。
            break
    if num == 1:
        # 到最后除干净了。再跳出外层循环
        break