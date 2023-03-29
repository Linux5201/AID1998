# 使用方法封装变量
class Wife:
    def __init__(self,name,age,weight):
        # 第一步 藏数据
        self.name = name
        # 本质：障眼法 实际将变量名改为：_类名__age
        # self.__age = age
        self.set_age(age)
        self.__weight = weight


    # 第二步 提供公开的读和写
    def get_age(self):
        return self.__age

    def set_age(self,value):
        if 21 <= value <= 31:
            self.__age = value
        else:
            raise ValueError("我不要")
w01 = Wife("铁扇公主",87,87)
w01.set_age(107)
print(w01.get_age())


"""
    w01 = Wife("铁扇公主",87,87)
    # 重新创建了新变量
    w01._Wife__age = 107  # (修改了类中定义的私有变量）
    # print(w01.name)
    # print(w01.age)
    # python内置变量，存储对象的实例变量
    print(w01.__dict__)
    # print(w01.weight)
"""














