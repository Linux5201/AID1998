"""
练习：定义在控制台中打印二维列表
例如：
[
[1,2,3,44],
[4,5,5,5,65,6,87],
[7,5]
]
"""
def print_list(list_target):
    """
    打印二维列表
    :param list_target: 需要打印的二维列表
    :return:
    """
    for i in range(len(list_target)):
        temp_list = list_target[i]
        for item in temp_list:
            print(item,end=" ")
        print("")

list01 = [
[1,2,3,44],
[4,5,5,5,65,6,87],
[7,5]
]
print_list(list01)