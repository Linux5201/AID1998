"""
字典内嵌字典：
{
  ”张无忌“：{"age":28,"score":100,"sex":男"}，
}

代码中重命名shift+f6
"""
dict_student_info = {}
dict_info = []
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    age = int(input("请输入年龄："))
    score = int(input("请输入成绩："))
    sex = str(input("请输入性别："))

    dict_student_info[name] = {"age": age, "score": score, "sex": sex}


for name, dict_info in dict_student_info.items():
    print("%s的年龄是%s,成绩是%d,性别是%s" % (name, dict_info["age"], dict_info["score"], dict_info["sex"]))