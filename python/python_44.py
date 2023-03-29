"""
需求：定义两个数字相加的函数
三件事：
1、获取数据  调用者提供数据
2、逻辑运算  定义方法所做的事
3、显示结果  调用者负责显示结果
"""
def add(number01,number02):
    return number01 + number02

number01 = int(input("请输入第一个数字："))
number02 = int(input("请输入第二个数字："))
result = add(number01,number02)
print("结果是："+str(result))






