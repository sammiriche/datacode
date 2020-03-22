# 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
a = input('请输入第一个字母：')
# b = 0
if a =='m':
    print('星期一')
elif a == 't':
    b = input('请输入第二个字母：')
    if  b=='u':
        print('星期二')
    else:
        print('星期四')
elif a == 'w':
    print('星期三')
elif a == 'f':
    print('星期四')
elif a == 's':
    b = input('请输入第二个字母：')
    if b == 'a':
        print('星期六')
    else:
        print('星期天')
