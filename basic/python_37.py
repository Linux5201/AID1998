"""
练习2：经理：曹操、刘备、孙权
      技术：曹操，刘备、张飞、关羽
请计算：
      （1）是经理也是技术的有谁？
      （2）是经理不是技术的有谁？
      （3）是技术，不是经理的有谁？
      （4）张飞是经理吗？
      （5）身兼一职的有谁？
      （6）经理和技术总共有多少人？
"""
set00 = set()
set01 = set()
set02 = set()
set01 = {"曹操","刘备","孙权"}
set02 = {"曹操","刘备","张飞","关羽"}
print(set01 & set02)

print(set01 - (set01 & set02))

print(set02 - (set01 & set02))

set00 = {"张飞"}
print(set01 > set00)

list_temp1 = list(set01 - (set01 & set02))
list_temp2 = list(set02 - (set01 & set02))
list_temp1 = list_temp1 + list_temp2
set03 = set(list_temp1)
print(set03)

list01 = list(set01)
list02 = list(set02)
list01 = list01 + list02
set04 = set(list01)
list_1 = list(set04)
print(len(list_1))