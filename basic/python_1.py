#练习三;在控制台分别录入4个数字
#打印最大的数字
#将第一个数字记在心里，然后与第二个比较
#如果第二个大于心中的，则记录第二个，然后依次类推

number_one = float(input("请输入第一个数："))
number_two = float(input("请输入第二个数："))
if number_two > number_one:
    number_one = number_two
number_three = float(input("请输入第三个数："))
if number_three > number_one:
    number_one = number_three
number_four = float(input("请输入第四个数："))
if number_four > number_one:
    number_one = number_four
print(number_one)