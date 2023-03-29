"""
给定一个字符串s,请你找出其中不含有重复字符的最长子串的长度。
"""
# ls = []
# ls.append()


class Solution:
    def lengthOfLongestSubstring(self, s):
        m = 0
        ls = []
        if len(s) == 0:
           return 0
        elif len(s) == 1:
           return 1
        else:
            for i in s:
                if i not in ls:
                    ls.append(i)
                    l = len(ls)
                    m = max(l,m)
                else:
                    ls.append(i)
                    while len(ls)!=0:
                        if ls[0] != i:
                            ls.pop(0)
                        else:
                            ls.pop(0)
                            break
        return m



class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s)==0:
            return 0
        if len(set(s))==1:
            return 1
        dic=[]
        l=0
        maxl=0
        for i in range(len(s)):
            if s[i] not in dic:
                dic.append(s[i])
                l=len(dic)
                maxl=max(l,maxl)
            else:
                tmp=None
                while tmp !=s[i]:
                    tmp=dic.pop(0)
                dic.append(s[i])
                l=len(dic)
                maxl=max(l,maxl)
        return maxl


import re
print(re.findall('[0-9]*', 'Words and 987')[0])   # ^匹配字符串开头位置