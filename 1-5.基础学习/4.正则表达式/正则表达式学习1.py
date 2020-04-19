import re
result = re.match(r'\d{3,4}\-\d{7,8}', '0715-8349609')
print(result)

test = '0715-1235893'
if re.match(r'\d{3,4}\-\d{7,8}', test):
    print('match')
else:
    print('not match')
