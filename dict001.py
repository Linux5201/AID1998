import pymysql



fd = open('dict.txt')


# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')

# 获取游标（操作数据库，执行sql语句，承载执行结果）
cur = db.cursor()



row = fd.readline()


while row:
    row = row.decode()

    try:
        # 写sql语句，执行
        # 插入操作
        word = row.split(' ')[0]
        mean = str(row.split(' ')[1:])[1:-1]

        sql = "insert into words (word,mean) values" \
              "(%s,%s)"
        # 可以使用列表直接给sql语句的values传值
        cur.execute(sql, [word, mean])  # 执行语句
        db.commit()  # 将写操作提交，多次写操作一同提交


    except Exception as e:
        db.rollback()   # 退回到commit执行之前的数据库状态
        print(e)

    row = fd.readline()

fd.close()
# 关闭数据库
cur.close()
db.close()




























