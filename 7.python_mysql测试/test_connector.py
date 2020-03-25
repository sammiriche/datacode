# import mysql.connector

# con  = mysql.connector.connect(
#     host = 'localhost',user = 'root',passwd = 'root',port = 3306,database = 'myemployees',charset='utf8'
# )
# cu = con.cursor(buffered=True)
# cu.execute('select first_name from employees')
# result = cu.fetchone()
# print(result)
# result = cu.fetchone()
# print(result)
# cu.close()
# con.close()

import mysql.connector
conn = mysql.connector.connect(
    host = 'localhost',port = 3306,user = 'root',passwd = 'root',database = 'myemployees',charset = 'utf8'
)

cu = conn.cursor(buffered = True)
# print(cu)
cu.execute('select department_id,salary from employees where salary >10000 order by salary')
for i in cu.fetchall():
    print(i)

cu.close()
conn.close()

