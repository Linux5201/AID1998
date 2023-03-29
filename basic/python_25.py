"""
元组 tuple
由一系列变量组成的不可变序列容器
不可变是指一旦创建，不可以再添加/删除/修改元素
列表扩容原理：
预留空间
1、列表都会预留空间
2、当列表预留空间不足时，会再创新列表（开一个更大的空间）
3、将原有数据拷贝到新列表当中
4、替换引用
变量-->表头-->表身

元组：
按需分配
1、创建元组
空、具有默认值
不增加

2、获取元素
3、遍历元素
"""
tuple01 = (1,2,3)
print(tuple01)
#列表--->元组
tuple01 = tuple(["a","b"])
#元组--->列表
list01 = list(tuple01)
print(list01)
print(type(tuple01))

#获取元素（索引，切片）
tuple03 = ("a","b","c","d")
e01 = tuple03[2]
print(type(e01))
e01 = tuple03[-2:]
print(type(e01))

tuple04 = (100,200)
#可以直接将元组赋值给多个变量
a,b = tuple04
print(a)
print(b)

#遍历元素
#正向
for item in tuple04:
    print(item)

#反向
for item in range(len(tuple04)-1,-1,-1):
    print(tuple04[item])


