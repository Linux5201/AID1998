"""
sstack.py 栈模型的顺序存储

思路总结：
1、列表即顺序存储，但功能多，不符合栈的模型特征
2、利用列表将其封装，提供接口方法
"""

# 自定义异常
# 异常分为三大类：1、keyboard interapution 2、系统异常 3、继承异常

class StackError(Exception):
    pass


# 顺序栈类
class SStack:
    def __init__(self):
        # 空列表是栈的存储空间
        # 列表的最后一个元素作为栈顶
        self._elems = []


    # 判断列表是否为空
    def is_empty(self):
        return self._elems == []    # python最大的哲学是优雅

    # 入栈
    def push(self,val):
        self._elems.append(val)

    # 出栈
    def pop(self):
        if not self._elems:
            raise StackError("Stack is empty")
        return self._elems.pop()   # 弹出最后一个


    # 查看栈顶元素
    def top(self):
        if self._elems:
            raise StackError("Stack is empty")
        return self._elems[-1]






if __name__ == "__main__":
    st = SStack()      # 初始化栈




