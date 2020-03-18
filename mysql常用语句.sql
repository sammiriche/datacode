# 查看所有数据库
SHOW DATABASES;
# 打开指定库
USE myemployees;
# 查看库中所有表,两种方法
SHOW TABLES;
SHOW TABLES FROM sys;
# 创建表，注意表和库的区别
CREATE TABLE test1(
bname VARCHAR(20),
priche INT,
publish_date VARCHAR(20)
)

# 查看指定表的结构
DESC employees;
# 显示表中所有数据
SELECT * FROM employees;

# DQL 基础查询部分
# 查询指定字段(列),并且给字段重新命名
SELECT last_name AS 名 FROM employees;
SELECT first_name,salary FROM employees WHERE salary >10000 AND salary <15000;
# 模糊查询 a% a开头 后面接0或者多个任意字符
SELECT first_name,last_name FROM employees WHERE last_name LIKE 'a%';
# 排序查询，asc/desc 升降序,默认asc升序从小到大
SELECT first_name,salary FROM employees ORDER BY salary DESC;

# 常见函数
SELECT CONCAT(first_name,'__',last_name) FROM employees WHERE salary >10000;
SELECT UPPER(first_name) FROM employees;

# DML 以test1表为例
# 增加列
SELECT * FROM test1;
ALTER TABLE test1 ADD COLUMN author VARCHAR(20) NOT NULL;
# 插入数据和修改数据
ALTER TABLE test1 DROP COLUMN publish_date; -- 删除列
ALTER TABLE test1 CHANGE priche price VARCHAR(20); -- 修改列名
INSERT INTO test1(bname,price,author) VALUES('朝花夕拾',30,'鲁迅');
INSERT INTO test1(bname,price,author) VALUES('呐喊',12,'鲁迅'); -- 字符加引号
DELETE FROM test1 WHERE price = 12; -- 修改行数据
UPDATE test1 SET bname = '纪念刘和珍君' WHERE price = 30; -- 修改数据
