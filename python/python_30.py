"""
练习1：在控制台中循环录入学生信息（姓名，年龄，成绩，性别）。
#   如果名称输入空字符，则停止录入
#   将所有信息逐行打印出来
    字典内嵌列表
    数据结构：
    {
    “张无忌”：[28，100，“男”]
    }
"""
dict_student_info = {}
list_info = []
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    age = int(input("请输入年龄："))
    score = int(input("请输入成绩："))
    sex = str(input("请输入性别："))

    dict_student_info[name] = [age,score,sex]

print(dict_student_info)
# for name,list_info in dict_student_info.items():
#     print("%s的年龄是%s,成绩是%d,性别是%s"%(name,list_info[0],list_info[1],list_info[2]))


        
