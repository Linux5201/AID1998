"""
    2048游戏核心算法
    1、零元素移至末尾
        [2,0,2,0] --> [2,2,0,0]
        [2,0,0,2] --> [2,2,0,0]
        [2,4,0,2] --> [2,4,2,0]
"""
def zero_to_end():
    list_temp1 = []
    list_temp2 = []
    for item in list_merge:
        if item == 0:
            list_temp1.append(item)
        else:
            list_temp2.append(item)
    for item in list_temp1:
        list_temp2.append(item)
    for i in range(len(list_temp2)):
        list_merge[i] = list_temp2[i]

list_merge = [2,4,4,0]
"""
练习2、将相同数字合并
    [2,2,0,0] --> [4,0,0,0]
    [2,0,0,2] --> [4,0,0,0]
    [2,0,4,0] --> [2,4,0,0]
    [2,2,2,2] --> [4,4,0,0]
    [2,2,2,0] --> [4,2,0,0]
"""

def merge():
    """
    合并相邻相同元素
    :return:
    """
    zero_to_end()
    for i in range(len(list_merge)-1):
        if list_merge[i] == list_merge[i+1]:
            list_merge[i] += list_merge[i+1]
            del list_merge[i+1]
            list_merge.append(0)

"""
练习3：地图向左移动
"""
map = [
    [2,0,0,2],
    [4,4,2,2],
    [2,4,0,4],
    [0,0,2,2]
]
def move_left():
    """
    向左移动
    思想：将二维列表中每行交给merge函数进行操作
    :return:
    """
    for line in map:
        global list_merge
        list_merge = line
        merge()
# move_left()
# print(map)  # [[4, 0, 0, 0], [8, 4, 0, 0], [2, 8, 0, 0], [4, 0, 0, 0]]

def move_right():
    """
    向右移动
    思想：将二维列表中每行（从右向左）交给merge函数进行操作
    :return:
    """
    for line in map:
        global list_merge
        # 从右向左取出数据，形成新列表
        list_merge = line[::-1]  # 切片产生新列表
        merge()
        line[::-1] = list_merge

"""
练习4、向上移动、向下移动
先对矩阵进行转置，然后再进行左移，或者右移
转置后，向上移动相当于左移，向下移动相当于右移
完成后，再对map进行转置
"""

def transpose_map():
    """
    对map进行转置操作
    :return:
    """
    global map
    for i in range(len(map)):
        for j in range(i,len(map[0])):
            temp = map[i][j]
            map[i][j] = map[j][i]
            map[j][i] = temp
def move_up():
    transpose_map()
    move_left()
    transpose_map()

def move_down():
    transpose_map()
    move_right()
    transpose_map()






