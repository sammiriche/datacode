with open('c:\\2.reg','r',encoding='utf-8') as f:
    result = f.read()
    print(type(result))

print(result)

with open('c:\\1.reg','w',encoding='utf-8') as f2:
    f2.write(result)
