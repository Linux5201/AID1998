"""
read_db.py
pymysql 读操作示例（select）
"""

import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')

# 获取游标（操作数据库，执行sql语句，承载执行结果）
cur = db.cursor()

# 获取数据库数据
sql = "select * from class_1 where gender='w';"

# 执行正确后cur调用函数获取结果
cur.execute(sql)

# 获取一个查询结果
one_row = cur.fetchone()
print(one_row)   # 元组

# # 获取多个查询结果
# many_row = cur.fetchmany(2)
# print(many_row)   # 元组
#
# # 获取所有查询结果
# all_row = cur.fetchall()
# print(all_row)

# 关闭数据库
cur.close()
db.close()

