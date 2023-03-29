"""
1、自学字符串/列表/字典常用函数方法，实现如下：
字符串：” 校 训：自 强不息、厚德载物 “
    1、查找空格的数量
    2、删除字符串前后空格
    3、删除字符串所有空格
    4、查找”载物“的位置
    5、判断字符串是否以”校训开头“
2、定义函数，计算指定范围内的素数
3、is与==的区别
4、玩2048游戏
5、重构shopping.py程序
"""
str01 = " 校 训：自 强不息、厚德载物 "
def str_count(str01,char01):
    """
    查找空格的数量
    :param str01: 目标字符串
    :param char01: 目标字符
    :return: 目标字符计数
    """
    count = 0
    for item in str01:
        if item == char01:
            count += 1
    return count
print(str_count(str01,' '))

str01 = " 校 训：自 强不息、厚德载物 "
print(str01[0])
print(str01[-1])
def str_delete01(str01):
    """
    删除字符串前后空格
    :param str01: 目标字符串
    :return: 修改字符串
    """
    str01 = str01.strip()
    return str01
print(str_delete01(str01))

str01 = " 校 训：自 强不息、厚德载物 "
print(str01.replace(' ',''))
str01 = " 校 训：自 强不息、厚德载物 "
print(str01.find("厚德"))

def str_judge(str01,char01):
    temp = str01.find(char01)
    return temp == 1
print(str01.replace(' ',''))
print(str01.find("校训:"))
print(str_judge(str01,"校训"))