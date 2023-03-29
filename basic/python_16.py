"""
练习3：
在控制台录入，所有学生姓名
如果姓名重复，则提示”姓名已经存在“，不添加到列表中
如果录入空字符串，则倒序打印所有学生
"""

student_name = str(input("输入学生姓名："))
list02 = []
while student_name != "":
    list02.append(student_name)
    for item in range(0,len(list02)-2):
        if student_name == list02[item]:
            print("姓名已经存在")
            del list02[len(list02)-1]
            break
    student_name = str(input("输入学生姓名："))
for i in range(-1,-len(list02)-1,-1):
    print(list02[i])