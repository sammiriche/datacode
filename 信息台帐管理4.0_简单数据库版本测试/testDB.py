import pymysql

conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root',
    port = 3306,
    db = 'myemployees',
    charset = 'utf8'
)

cur = conn.cursor()
value = 12000
sql = 'select * from employees where salary >%s'
# cur.execute(sql,value)
cur.execute(sql %value) # 两种不同的写法
print(cur.fetchone())
print(cur.rowcount)
cur.close()
conn.close()