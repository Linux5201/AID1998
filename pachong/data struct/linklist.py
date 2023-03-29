# 创建节点类
class Node:
    def __init__(self, val, next=None):
        self.val = val    # 有用数据
        self.next = next   # 循环下一个节点关系


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
        p = self.head   # p作为移动变量
        for item in list_:
            p.next = Node(item)
            p = p.next

    # 遍历链表
    def show(self):
        p = self.head.next  # 第一个有效节点
        while p is not None:
            print(p.val)
            p = p.next

    # 判断链表为空
    def is_empty(self):
        if self.head.next is None:
            return True
        else:
            return False

    # 清空链表
    def clear(self):
        self.head.next = None

    # 尾部插入
    def append(self, val):
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(val)

    # 头部插入
    def head_inser(self, val):
        node = Node(val)
        node.next = self.head.next
        self.head.next = node



import time
l = []
for i in range(99999):
    l.append(i)
link = LinkList()
link.init_list(l)

tm = time.time()
l.insert(0, 8866)
# link.head_inser(8866)
print(tm)
print(time.time())

