"""
1、创建学生类
    ——数据：姓名，年龄，成绩，性别
    ——行为：在控制台打印个人信息的方法
2、在控制台中循环录入学生信息，如果名称是空字符，退出录入。
3、在控制台输出每个学生（调用打印学生类的打印方法）
4、打印第一个学生信息

"""



# class Student:
#     def __init__(self):
#         self.list_student_info = []
#         self.dict_info = {}
#
#     def print_first_people(self):
#         dict_info = self.list_student_info[0]
#         print("第一个录入的是：%s的年龄是%s,成绩是%d,性别是%s" % (dict_info["name"], dict_info["age"], dict_info["score"], dict_info["sex"]))
#
#     def input_student(self):
#         while True:
#             name = input("请输入姓名：")
#             if name == "":
#                 break
#             age = int(input("请输入年龄："))
#             score = int(input("请输入成绩："))
#             sex = str(input("请输入性别："))
#
#             self.dict_info = {"name": name, "age": age, "score": score, "sex": sex}
#             self.list_student_info.append(self.dict_info)
#
#     def output_student(self):
#         for dict_info in self.list_student_info:
#             print("%s的年龄是%s,成绩是%d,性别是%s" % (dict_info["name"], dict_info["age"], dict_info["score"], dict_info["sex"]))
#
# student = Student()
# student.input_student()
# student.output_student()
# student.print_first_people()

class Student:
    def __init__(self,name,age,score,sex):
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex

    def print_self_info(self):
        print("%s的年龄是%s,成绩是%d,性别是%s" % (self.name, self.age, self.score, self.sex))

list_student_info = []

while True:
    name = input("请输入姓名：")
    if name == "":
        break
    age = int(input("请输入年龄："))
    score = int(input("请输入成绩："))
    sex = str(input("请输入性别："))

    stu = Student(name,age, score, sex)
    list_student_info.append(stu)

for stu in list_student_info:
    stu.print_self_info()

# 获取第一个学生信息
info  = list_student_info[0]
info.print_self_info()

 







