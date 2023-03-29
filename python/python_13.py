"""

列表list
str:由一系列字符组成的不可变序列容器
list:由一系列变量组成的不可变序列容器
创建一个空的列表
list01 = []
list01 = list()
"""
list01 = []
list01 = list()

#默认值
list02 = ["悟空",100,True]   #根据一些数据构建列表
list02 = list("我是齐天大圣")             #根据另外一个容器构建列表

#2、获取元素
#索引
print(list02[2])
#切片
print(list02[-4:])

#3、添加元素
#在末尾添加
list02.append("八戒")
print(list02)
#插入，在指定位置添加
list02.insert(1,True)
print(list02)


#4、删除元素
#根据元素删除，根据位置删除
list02.remove("是")
print(list02)
del list02[0]
print(list02)



#5、定位元素可以进行增删改查
#切片
del list02[0:3]
print(list02)

# del list02[0:2]
# print(list02)
list02[0:2] = ["a","b"]
print(list02)

#遍历列表
#获取列表中所有元素
for item in list02:
    print(item)

#倒序获取所有元素
#不建议使用，通过切片拿元素，会重新创建新列表，浪费内存
for item in list02[::-1]:
    print(item)

#0 1 2
#-1 -2 -3
for i in range(2,-1,-1):
    print(list02[i])

for i in range(len(list02)-1,-1,-1):
    print(list02[i])

for i in range(-1,-len(list02)-1,-1):
    print(list02[i])





