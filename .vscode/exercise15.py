# 打印图案
# 类似习题一般都用两个循环，分别控制行和列
for i in range(1,5):
    print((' ')*(4-i),end = '')
    for j in range (1,i*2):
        print('*', end ='')
    print()
# -1为步长，就是倒着数的意思
for i in range(4,1,-1):
    print(' '*(4-i+1), end ='')
    for j in range(1,2*i-2):
        print('*', end ='')
    print()
