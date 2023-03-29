"""

str --> list

"""
str01 = "张无忌-赵敏-周芷若"
list_result = str01.split("-")
print(list_result)

#练习英文单词反转
#"How are you" --->  "you are How"
str02 = "How are you"
list_result = str02.split(" ")
lisr_1 = list()
for item in range(-1,-len(list_result)-1,-1):
    lisr_1.append(list_result[item])
str02 = " ".join(lisr_1)
print(str02)