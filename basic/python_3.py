#在控制台获取一个月份
#打印天数
month = int(input("输入一个月份："))
max = 31
min = 30
if month<1 or month>12:
    print("输入有误")
elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print(max)
elif month==2:
    print(28)
else:
    print(min)