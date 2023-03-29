"""

练习：在控制台中录入日期（年月），计算这是一年的第几天
例如：3月5日
1月天数+二月天数+5
"""
day_of_month = (0,31,28,31,30,31,30,31,31,30,31,30,31)
# month = int(input("请输入月份："))
# day = int(input("请输入具体是哪一天："))
while True:
    month = int(input("请输入月份："))
    day = int(input("请输入具体是哪一天："))
    sum01 = 0
    for i in range(0,month):
        sum01 += day_of_month[i]
    print(sum01+day)

