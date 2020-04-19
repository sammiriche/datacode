import pymysql
config = {
    'host':'localhost',
    'user':'root',
    'passwd':'root',
    'port':3306,
    'db':'milkbottle'
}


connect = pymysql.connect(**config)

# connect = pymysql.connect(
#     # 'localhost','root','root',3306,'milkbottle'
#     'host':'localhost',
#     'user':'root',
#     'passwd':'root',
#     'port':3306,
#     'db':'milkbottle'
# )
cur = connect.cursor()
cur.execute('select * from em_info')
result = cur.fetchone()
print(result)

print(type(config))
def test(**kwgs):
    print('aaadfdf')
    print(kwgs)
test(**config)

# print(type(**config))