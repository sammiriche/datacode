import re
pattern = r'(25[0-5]\.)|(2[0-4]\d\.)|(1\d\d\.)|(\d\d\.)|(\d\.)'
pattern30 = r'((1\d\d\.)|(2[0-4]\d\.)|(25[0-5]\.)|([1-9]\d\.)|([1-9]\.)){3}'
pattern31 = r'((1\d\d\.)|(2[0-4]\d\.)|(25[0-5]\.)|([1-9]\d\.)|([1-9]\.)){3}((1\d\d)|(2[0-4]\d)|(25[0-5])|([1-9]\d))'
ip = '152.20.3.152'
a = re.search(pattern, ip)
b = re.search(pattern30, ip)
b = re.search(pattern31, ip)
print(a)
print(b)
