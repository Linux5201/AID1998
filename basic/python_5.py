#练习：一张纸的厚度是0.01毫米，请计算对折多少次，超过8844.43米
number_one = float(input("输入纸的厚度(mm)："))
number_one = number_one/1000
number_tow = 8844.43
count = 0
while number_one<number_tow:
    count += 1
    number_one *= 2
    print(number_one)
print(count)