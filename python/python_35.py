"""
计算一个字符串中的字符以及出现的次数
1、逐一判断字符出现的次数
2、如果统计过则增加一，如果没统计过则等于一
"""
list_char = []
dict_count = {}
list_char = str(input("请输入字符串："))
for item in list_char:
    if item not in dict_count:
        dict_count[item] = 1
    elif item in dict_count:
        dict_count[item] = dict_count[item] + 1
print(dict_count)
for key,value in dict_count.items():
    print("%s出现%d次"%(key,value))

