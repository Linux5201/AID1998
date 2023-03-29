class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dic = dict()
        res = list()

        for i in nums:
            dic[i] = dic.get(i, 0) + 1      # 统计一个数组中元素出现个数，放入字典构成哈希表

        n1 = [n for n in dic.keys() if n < 0]   # 放入小于0的数
        n2 = [n for n in dic.keys() if n > 0]   # 放入大于0的数

        if 0 in dic and dic[0] >= 3:
            res.append([0, 0, 0])

        for i in n1:
            for j in n2:
                k = -i-j
                if k in dic:
                    if i < k < j:
                        res.append([i, k, j])
                    elif i <= k < j:
                        if dic[i] >= 2:
                            res.append([i, i, j])
                    elif i < k <= j:
                        if dic[j] >= 2:
                            res.append([i, j, j])
        return res



