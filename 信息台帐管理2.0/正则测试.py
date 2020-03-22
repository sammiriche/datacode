# import re
# string = '刘a屏'
# t = re.match(r'^[\u4e00-\u9fa5]{1,3}$',string)
# print(t)

# # t2 = re.search(r'((25[0-4]|2[0-4]\d|1\d\d|\d?\d)\.){3}(25[0-4]|2[0-4]\d|1\d\d|\d?\d)','254.188.120.09111')
# # print(t2)

# # ((25[0-4]|24\d|1\d\d|\d?\d)\.){3}(25[0-4]|24\d|1\d\d|\d?\d)
# # ([0-9a-fA-F]{4}\.){2}[0-9a-fA-F]{4}
# # ([0-9a-fA-F]{4}-){2}[0-9a-fA-F]{4}
# # ([0-9a-fA-F]{2}:){5}[0-9a-fA-F]

# pattern = re.compile(r'^([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}$')
# t3 = re.search(pattern,'cd:ab:eA:11:3f:22')
# print(t3)

import pickle
from empolyee2 import Empolyee
empolyee = Empolyee('lilei','renzi','11','22')
# ls = ['1','abc',3]
ls = []
ls.append(empolyee)
with open('data3','wb') as f:
    pickle.dump(ls,f)
