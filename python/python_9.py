"""
在控制台获取一个整数，判断是否为素数
"""
number_one = int(input("输入一个整数："))
for i in range(2,number_one):
    if number_one % i == 0:
        print("不是素数")
        break
print("是素数")

