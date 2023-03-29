"""
1、利用python的max()和min()，在Python里字符串是可以比较的，
按照ascII值排，举例abb， aba，abac，最大为abb，最小为aba。
所以只需要比较最大最小的公共前缀就是整个数组的公共前缀
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        s1 = min(strs)
        s2 = max(strs)
        for i,x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1


"""
利用python的zip函数，把str看成list然后把输入看成二维数组，左对齐纵向压缩，
然后把每项利用集合去重，之后遍历list中找到元素长度大于1之前的就是公共前缀
"""
def longestCommonPrefix(self, strs):
    if not strs:
        return ""
    ss = list(map(set, zip(*strs)))
    res = ""
    for i, x in enumerate(ss):
        x = list(x)
        if len(x) > 1:
            break
        res = res + x[0]
    return res