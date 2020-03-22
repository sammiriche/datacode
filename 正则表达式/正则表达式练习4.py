import re
str1 = 'hellopython'
# msg = re.compile('hello')
# a = msg.match(str1)
# print(a)

a = re.match('hello',str1)
print(a)
a = re.search('ello',str1)
print(a)
print(a.group())