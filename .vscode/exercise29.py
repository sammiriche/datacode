dict1 = {'tom':88,'kaka':61,'lucy':61,'mane':0,'crespo':100}
dict1['james'] = 99
print(dict1)
print(dict1['lucy'])
print(dict1.get('tom'))
a = []
for k,v in dict1.items():
    if v == 61:
        a.append(k)
print(a)
