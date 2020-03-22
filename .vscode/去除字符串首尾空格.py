#去除字符串首尾的空格
def trim(s):
    while s[:1] == ' ':  #while是循环语句，只要条件满足，就一直循环,这里就是0-1 只选0这个字符判断
        s = s[1:]
    while s[-1:] == ' ':  # 如果倒数第一个是空格，那么字符串到倒数第一（注意不包含倒数第一）
        s = s[0:-1]
    return s


print('  hello  world  ')
print(trim('  hello  world  '))
