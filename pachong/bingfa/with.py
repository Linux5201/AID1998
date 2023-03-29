"""
使用with语句打开文件
"""

with open("E:\DK\Project\learn_torch\pachong\\bingfa\day02") as f:  # 生成对象
    data = f.read()
    print(data)

#with语句结束，f销毁


