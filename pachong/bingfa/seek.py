"""
seek.py 文件偏移量实例


注意：1、每次open打开文件，文件偏移量都在开头
    2、以a方式打开时，文件偏移量在结尾
    3、读写操作共用一个文件偏移量
"""

# f = open('day02', "r+")    # 读写
#
# data = f.read(5)
# print("文件偏移量：",f.tell())
# f.write("aaa")
# f.close()

# Definition for singly-linked list.
class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkList:
    """
    思路： 单链表类，生成对象可以进行增删改查操作
          具体操作通过调用具体方法完成
    """

    def __init__(self):
        """
        初始化链表，标记一个链表开端，以便获取后续节点
        """
        self.head = Node(None)

    # 通过list_为链表添加一组节点
    def init_list(self, list_):
        p = self.head  # p作为移动变量
        for item in list_:
            p.next = Node(item)
            p = p.next

    # 头部插入
    def head_inser(self, val):
        node = Node(val)
        node.next = self.head.next
        self.head.next = node


# 两个字符串（合法的数字字符串）相加，不能用内置库
# 算竖式的思想，个位对齐，相加，并把进位传递到下一位
def add_strings1(a, b):
    i = len(a)
    j = len(b)
    carry = 0  # 进位
    res = ''
    while i > 0 or j > 0 or carry:  # 对于不确定在哪里停止的循环，就用while，用i来控制循环次数
        x = a[i - 1] if i > 0 else '0'
        y = b[j - 1] if j > 0 else '0'
        sum_x_y = (ord(x) - ord('0')) + (ord(y) - ord('0'))
        res = str((sum_x_y + carry) % 10) + res
        carry = int((sum_x_y + carry) / 10)
        i -= 1
        j -= 1
    return res


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        link1 = LinkList()
        link2 = LinkList()
        reslink = LinkList()
        link1.init_list(l1)
        link2.init_list(l2)
        s1 = "".join(map(str, l1))
        s2 = "".join(map(str, l2))
        s3 = add_strings1(s1, s2)
        b = list(s3)
        c = list(map(int, b))
        for item in c:
            reslink.head_inser(item)

        return reslink.head.next










