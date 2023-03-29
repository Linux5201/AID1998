"""
pymysql使用流程
    1、建立数据库连接（db=pymysql.connect(....)）
    2、创建游标对象（c=db.cursor()）
    3、游标方法:c.execute("insert....")
    4、提交到数据库:db.commit()   针对于写操作
    5、关闭游标对象:c.close()
    6、断开数据库连接:db.close()
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


# 执行sql语句
sql = "insert into class_1 values" \
      "(7,'Emma',17,'w',76.5,'2019-8-8');"

cur.execute(sql)         # 执行语句
db.commit()              # 将写操作提交，多次写操作一同提交

# 关闭数据库
cur.close()
db.close()
















