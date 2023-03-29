#在控制台中录入一个乘积，判断等级(优秀/良好/及格/不及格/输入有误)
score = int(input("请输入成绩："))
if score>=90 and score<=100:
    print("优秀")
elif score>=80 and score<90:
    print("良好")
elif score>=60 and score<80:
    print("及格")
elif score<60 and score>=0:
    print("不及格")
else:
    print("输入有误")