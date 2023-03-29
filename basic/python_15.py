"""

练习2：在控制台中录入，所有学生成绩
输入空字符串，打印（一行一个）所有成绩
打印最高分，打印最低分，打印平均分
内建函数
len(x)
max(x)
min(x)
sum(x)
"""
score = str(input("输入成绩："))
list01 = []
while score != "":
    score = float(score)
    list01.append(score)
    score = str(input("输入成绩："))
for item in list01:
    print(item)
print("最高分："+str(max(list01)))
print("最低分："+str(min(list01)))
print("平均分："+str(sum(list01)/len(list01)))
