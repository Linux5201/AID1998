"""
定义列表升序排列的函数
"""
def sort(list01):
    """
    满足以下条件，就无需通过返回值传递结果。
    1、传入的是可变对象
    2、函数体修改的是传入的对象
    排序函数
    :param list01: 目标列表
    :return:
    """
    for r in range(len(list01)-1):
        for c in range(r+1,len(list01)):
            if list01[r]>list01[c]:
                temp = list01[r]
                list01[r] = list01[c]
                list01[c] = temp

list01 = [5,1,3,5,8,7]
sort(list01)
print(list01)