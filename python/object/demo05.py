"""
实例变量
1、语法
    （1）定义：对象.变量名
    （2）调用：对象.变量名
练习1：定义函数，在list01中查找name是“苏大强”的对象，将名称与年龄打印在控制台中
"""
class Student:
    def __init__(self,name,age,score,sex):
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex

    def print_self_info(self):
        print("%s的年龄是%s,成绩是%d,性别是%s" % (self.name, self.age, self.score, self.sex))

list01 = [
    Student("赵敏",28,100,"女"),
    Student("苏大强",68,62,"男"),
    Student("明玉",30,95,"女"),
    Student("无忌",29,70,"男"),
    Student("张三丰",130,96,"男")
]

def seek01():
    for item in list01:
        if item.name == "苏大强":
            return item
        # 如果没有找到，则返回空。而函数返回默认就是空，所以可以不写
        # return None

# stu = seek01()
# print(stu.name,stu.age)  #*values 可以把多个实参转换为元组

"""
练习2：定义函数，在list01中查找所有女同学，将名称与年龄打印在控制台
"""

def seek02():
    list02 = []
    for item in list01:
        if item.sex == "女":
            list02.append(item)
    return list02

# list02 = seek02()
# for item in list02:
#     print(item.name,item.age)

"""
练习3：定义函数，查找年龄>=30的学生数量
"""
def seek03():
    count = 0
    for item in list01:
        if item.age >= 30:
            count += 1
    return count
# count = seek03()
# print(count)

"""
练习4：定义函数，将list01中所有学生的成绩归零
"""
def zero():
    for item in list01:
        item.score = 0

# zero()
# for item in list01:
#     item.print_self_info()

"""
练习5：获取list01中所有学生的名字
"""
def get_name():
    list02 = []
    for item in list01:
        list02.append(item.name)
    return list02

# list02 = get_name()
# for item in list02:
#     print(item)

"""
练习6:定义函数：在list01中查找年龄最大的学生对象
"""

def seek04():
    max = list01[0].age
    for item in list01:
        if item.age > max:
            max = item.age
            obj = item
    return obj

stu = seek04()
stu.print_self_info()





