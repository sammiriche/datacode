# 注意观察输入值为什么不变
dict1 = {'tom':90, 'lily':62, 'kaka':62,'frame':100}
test = dict1['tom']
print(test)
dict1['tom'] = 88
print(test)
print(dict1)
