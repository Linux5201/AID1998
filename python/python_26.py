# """
#
# 使用元组优化代码
# 用容器同一管理数据
# """
# month = int(input("请输入月份："))
# if month <1 or month>12:
#     print("输入有误")
# else:
#     day_of_month = (31,28,31,30,31,30,31,31,30,31,30,31)
#     print(day_of_month[month-1])
#     #每月天数存在元组中
import random

list01 = []
list02 = []
list01 = ['苹果','狗','猫','图片','大']
list02 = ['apple','dog','cat','picture','big']
i = random.randint(0,5)
str01 = str(input("请输入"+list01[i]+"的英语单词:"))
while(str01!=list02[i]):
    print("答错了！")
    str01 = str(input("请输入"+list01[i]+"的英语单词:"))
print("答对了！")












