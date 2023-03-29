"""
练习;循环根据成绩判断等级，如果录入空字符串则退出程序
如果录入错误次数达到3，则退出成绩并提示”成绩错误过多“
"""
count = 0
while count<3:
    score = str(input("请输入成绩："))
    if score == '':
        break
    score = int(score)
    if score >= 90 and score <= 100:
        print("优秀")
    elif score >= 80 and score < 90:
        print("良好")
    elif score >= 60 and score < 80:
        print("及格")
    elif score < 60 and score >= 0:
        print("不及格")
    else:
        print("输入有误")
        count += 1
print("成绩错误过多")