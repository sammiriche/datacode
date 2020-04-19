import re
a = re.search(r'\.', 'hello world.tt')
# print(a)
pattern = r'([01]\d\d\.|2[0-4]\d\d\.|25[0-5]\.){3}([01]\d\d|2[0-4]\d\d|25[0-5])'
ip = '132.186.192.111'
ip2 = '232.22.22.22'
test = re.search(pattern, ip)
# print(test)

pattern2 = r'((1[0-9][0-9]\.)|(2[0-4][0-9]\.)|(25[0-5]\.)|([1-9][0-9]\.)|([0-9]\.)){3}((1[0-9][0-9])|(2[0-4][0-9])|(25[0-5])|([1-9][0-9])|([0-9]))'
pattern3 = r'((1\d\d\.)|(2[0-4]\d\.)|(25[0-5]\.)|([1-9]\d\.)|([1-9]\.)){3}((1\d\d)|(2[0-4]\d)|(25[0-5])|([1-9]\d)|([1-9]))'
test2 = re.search(pattern2, ip)
test3 = re.search(pattern3, ip)
print(test2)
print(test3)

