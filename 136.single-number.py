#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res
✔ Accepted
  ✔ 16/16 cases passed (92 ms)
  ✔ Your runtime beats 96.43 % of python3 submissions
  ✔ Your memory usage beats 6.56 % of python3 submissions (16.2 MB)

#     def singleNumber(self, nums: List[int]) -> int:
#         return 2 * sum(set(nums)) - sum(nums)
# ✔ Accepted
#   ✔ 16/16 cases passed (96 ms)
#   ✔ Your runtime beats 88.23 % of python3 submissions
#   ✔ Your memory usage beats 6.56 % of python3 submissions (16.1 MB)


#     def singleNumber(self, nums: List[int]) -> int:
#         s1 = set(nums)
#         for i in s1:
#             nums.remove(i)
#         s2 = set(nums)
#         return (s1-(s1&s2)).pop()
# ✔ Accepted
#   ✔ 16/16 cases passed (572 ms)
#   ✔ Your runtime beats 9.28 % of python3 submissions
#   ✔ Your memory usage beats 6.56 % of python3 submissions (16.8 MB)

