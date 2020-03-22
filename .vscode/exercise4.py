# 输入某年某月某日，判断这一天是这一年的第几天？
# 逻辑 能被400整除，或者能被4整除但是不能被100整除的是闰年
# 通过列表循环加月的天数
year = int(input('请输入年份：'))
month = int(input('请输入月份：'))
day = int(input('请输入日期：'))
list_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    list_month[2] = 29
sum = 0
for i in range(1, month):
    sum += list_month[i]

print(sum+day)
list_month[2] = 100
print(list_month[2])