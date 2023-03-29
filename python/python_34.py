"""

1、存储全国各个城市的景区与美食，在控制台显示出来
北京：
    景区：故宫、天安门、天坛。
    美食：烤鸭、炸酱面、豆汁、卤煮。
四川：
    景区：九寨沟、峨眉山、春熙路。
    美食：火锅、串串香、兔头

{
”北京“：{
”景区“：[故宫，天安门，天坛],
“美食”：[烤鸭，炸酱面，豆汁，卤煮]
}
}

2、计算一个字符串中的字符以及出现的次数

"""
dic_adress = {}
list_scenic = []
list_food = []
while True:
    name = input("请输入城市：")
    if name == "":
        break
    dic_adress[name] = {}
    dic_adress[name] = {"景区":list_scenic,"美食":list_food}
    while True:
        scenic = input("请输入景区：")
        if scenic == "":
            break
        dic_adress[name]["景区"].append(scenic)
    while True:
        food = input("请输入美食：")
        if food == "":
            break
        dic_adress[name]["美食"].append(food)

for name,dic_info in dic_adress.items():
    print("城市：%s"%name)
    print("景区：")
    print(dic_info["景区"])
    print("美食：")
    print(dic_info["美食"])
    # for item,list_item in dic_info:
    #     print("%s:"%item)
    #     print(list_item)