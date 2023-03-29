"""
    使用property（读取方法，写入方法），封装变量
    封装就是对外提供必要的功能，不必要的功能就藏起来
"""
class Wife:
    def __init__(self,name,age,weight):
        # 第一步 藏数据
        self.name = name
        # 本质：障眼法 实际将变量名改为：_类名__age
        # self.__age = age
        self.age = age
        self.weight = weight



    @property  # 创建property对象，只负责拦截读取操作
    def age(self):
        return self.__age

    @age.setter # 只负责拦截写入操作
    def age(self,value):
        if 21 <= value <= 31:
            self.__age = value
        else:
            raise ValueError("我不要")

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self,value):
        if 40 <= value <= 60:
            self.__weight = value
        else:
            raise ValueError("我不要")



w01 = Wife("铁扇公主",28,50)
print(w01.age)
w01.age = 25
# w01.set_age(107)
print(w01.__dict__)
# print(w01.get_age())





















