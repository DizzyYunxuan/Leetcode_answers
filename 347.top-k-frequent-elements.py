#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         import collections
#         from heapq import nlargest
#         count = collections.Counter(nums)
#         return nlargest(k, count.keys(), count.get)

# Accepted
# 21/21 cases passed (104 ms)
# Your runtime beats 94.23 % of python3 submissions
# Your memory usage beats 6.25 % of python3 submissions (17.2 MB)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mem = {}
        for n in nums:
            mem[n] = 1 + mem.get(n, 0)
        
        frq = {}
        for key, v in mem.items():
            frq[v] = frq.get(v, []) + [key]
        
        res = []
        for i in range(len(nums), 0, -1):
            if i in frq:
                res += frq[i]
        return res[:k]
Accepted
21/21 cases passed (108 ms)
Your runtime beats 87.76 % of python3 submissions
Your memory usage beats 6.25 % of python3 submissions (17.1 MB)


# @lc code=end

