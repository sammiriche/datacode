# 第七行不行，因为字符串是不可变量。必须赋值给其他变量才能相加
f2 = open('test00','r')
f3 = open('test01','r')
a = f2.read()
b = f3.read()
# print(f2.read()+f3.read())
c = a+b
ls=[]
for i in range(0,len(c)):
    ls.append(c[i])
print(sorted(ls))
print(''.join(ls))




