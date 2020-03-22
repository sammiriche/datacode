a = 'abcde'
b = 'adegh'
c = 'dgghjk'
d = 'fdkk'
e ='fabb'
lt = []
lt.append(a)
lt.append(b)
lt.append(c)
lt.append(d)
lt.append(e)
for i in range (len(lt)):
    for j in range(1,len(lt)):
        if lt[i]<=lt[j]:
            # lt[i],lt[j] = lt[j],lt[i]
            t = lt[i]
            lt[i] = lt[j]
            lt[j] = t
for i in range(len(lt)):
    print(lt[i], end = ' ')

lt.sort()
print(lt)
