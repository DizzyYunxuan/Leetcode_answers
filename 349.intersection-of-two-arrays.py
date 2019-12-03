#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         return set(nums1) & set(nums2)
# Accepted
# 60/60 cases passed (48 ms)
# Your runtime beats 83.97 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = {}
        for i in nums1:
            d1[i] = 1
        res = []
        for k in d1:
            if k in nums2:
                res.append(k)
        return res
Accepted
60/60 cases passed (60 ms)
Your runtime beats 29.77 % of python3 submissions
Your memory usage beats 100 % of python3 submissions (12.9 MB)
# @lc code=end

