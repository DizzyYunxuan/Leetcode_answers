#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        thresh = len(nums) // 3
        res = []
        l = Counter(nums)
        for i in l:
            if l[i] > thresh:
                res.append(i)
        return res
✔ Accepted
  ✔ 66/66 cases passed (128 ms)
  ✔ Your runtime beats 97.36 % of python3 submissions
  ✔ Your memory usage beats 5.88 % of python3 submissions (14.9 MB)
