# 乘法口诀表，i控制行，j控制列

i = 1
for i in range (1, 10):
    for j in range (1,i+1):
        # 通过end 取消末尾默认的换行符
        print (f'{i}*{j}={i*j}',end = ' ')
    #打印空白时里面自动包含换行符
    print()
