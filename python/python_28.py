"""

字典
1、由一系列键值对组成的可变映射容器
2、映射：一对一的对应关系，且每条记录无序。
3、键必须惟一且不可变（字符串/数字/元组)

1、创建
#空  默认值
2、查找元素
3、修改元素
4、添加元素
5、删除元素
6、遍历
"""
# 创建
dict01 = {"wj":100,"zm":80,"zr":90}
print(dict01)
dict01 = dict([("a","b"),("c","d")])     # 里面放容器
print(dict01)
#查找元素（根据key查找value）
print(dict01["a"])
#如果key不存在，查找时会报错
#如果存在key
if "qtx" in dict01:
    print(dict01["qtx"])

#修改元素（之前存在key)
dict01["a"] = "BB"
print(dict01["a"])

#添加（之前不存在key）
dict01["e"] = "f"
print(dict01)

#删除
print(dict01)
del dict01["a"]
print(dict01)

#遍历（获取字典中所有元素）
#遍历字典，得到的是key
for item in dict01:
    print(item)
    print(dict01[item])

#遍历字典，得到的是value
for key in dict01.values():
    print(key)

#遍历字典，获取键值对key value（元组）
for item in dict01.items():
    print(item)

#遍历字典，分别获取键和值
for k,v in dict01.items():
    print(k)
    print(v)


