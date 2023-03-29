"""
选择策略：根据需求，结合优缺点，综合考虑
字典：
    优点：根据键获取，读取速度快
    代码可读性相对列表更高
    缺点：内存占用大；
列表：
    优点：根据索引/切片,获取元素更灵活
    相比于字典占内存更小
    缺点：通过索引获取，如果信息较多，可读性不高。
"""
"""
在控制台中录入多个人的多个喜好
例如：请输入姓名：
     请输入第一个喜好：
     请输入第二个喜好：
     ~
     请输入姓名：
     ~
     输入空字符停止
     最后在控制台打印所有人的所有喜好

{
"无忌“：[赵敏，周芷若，小昭]
}

"""
dic_person_hobby = {}
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    dic_person_hobby[name] = []
    while True:
        hobby = input("请输入喜好：")
        if hobby == "":
            break
        dic_person_hobby[name].append(hobby)

for name,list_hobby in dic_person_hobby.items():
    print("%s喜欢"% name)
    for item in list_hobby:
        print(item)


# for name,list_info in dict_student_info.items():
#     print("%s的爱好是%s"%(name,list_info))