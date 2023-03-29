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

def register():
    name = input("请输入用户名：")
    password = input("请输入密码：")
    while True:
        # 获取数据库数据
        sql = "select * from user1 where name=%s;"
        # 执行正确后cur调用函数获取结果
        cur.execute(sql, [name])
        # 获取一个查询结果
        one_row = cur.fetchone()
        if one_row is None:
            name = input("该用户名不存在，请重新输入用户名：")
            password = input("请输入密码：")
        elif one_row[2] != password:
            password = input("密码错误，请重新输入密码：")
        else:
            print("登录成功！")
            break
    # 关闭数据库
    cur.close()
    db.close()

def login():
    # 获取数据库数据
    while True:
        name = input("请输入用户名：")
        password = input("请输入密码：")
        try:
            # 获取数据库数据
            sql = "select * from user1 where name=%s;"
            # 执行正确后cur调用函数获取结果
            cur.execute(sql, [name])
            # 获取一个查询结果
            one_row = cur.fetchone()
            if one_row:
                print("该用户名已存在，请重新输入用户名密码")
            else:
                sql = "insert into user1 (name,password) values" \
                      "(%s,%s)"
                # 可以使用列表直接给sql语句的values传值
                cur.execute(sql, [name, password])  # 执行语句
                db.commit()  # 将写操作提交，多次写操作一同提交
                print("注册成功！")
                break
        except Exception as e:
            db.rollback()  # 退回到commit执行之前的数据库状态
            print(e)
    # 关闭数据库
    cur.close()
    db.close()

if __name__ == '__main__':
    while True:
        print("""====================
1、登录    2、注册
====================""")
        order = input("请输入命令：")

        if order == '1':
            register()

        if order == '2':
            login()









