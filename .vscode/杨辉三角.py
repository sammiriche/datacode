# 杨辉三角 首先排成直角三角形找规律。从第三行开始，每一项的值都是上+上左。
# 把整个杨辉三角看成一个大的列表。列表的每个元素就是每一行的子列表。通过每次打印一个子列表再换行就可以了。
# 所以首先建立一个列表。将第一行包裹进去，因为没规律，不参与循环
def yanghui(n):
    ls = [[1]]
    print(ls[0])
    # i控制行，j控制列，记得下标是从0开始。最后一位不算
    for i in range(1,n):
        # 每一行的首尾都是1,同时也为这一行建立了子列表
        # 注意是从第二列开始循环
        # 由于下标从0开始，所以这里的i正好就是第i行。0，1，2。。i这样数
        ls.append([1])
        # 列循环只需要在每一列循环中间的非1项
        for j in range(1,i):
            # 子列表开始添加元素，注意规律
            ls[i].append(ls[i-1][j-1]+ls[i-1][j])
        ls[i].append(1)
        # 每一行循环完打印一次，
        print(ls[i])
    return ls 

yanghui(10)
print(yanghui(10))


# 一定注意合起来是个总列表,最后就是打印这一个整个列表


