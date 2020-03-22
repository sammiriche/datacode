# 求100之内的素数
# flag = 0
for i in range(2,101):
    for j in range(2,i):
        if i%j==0:
            break
    #for else用法 在不存在break的情况下，迭代完所有对象，再运行一遍else
    # 如果直接是顺序执行，那么break的情况下还会运行。简单说break能跳出else语句    
    else:
        print(i,end = ' ')


    
        
