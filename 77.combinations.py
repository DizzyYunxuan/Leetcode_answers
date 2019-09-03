#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
class Solution:
    def combine(self, n, k):
        from itertools import combinations
        return list(combinations(range(1, n+1), k))
✔ Accepted
  ✔ 27/27 cases passed (84 ms)
  ✔ Your runtime beats 99.65 % of python3 submissions
  ✔ Your memory usage beats 23.33 % of python3 submissions (15.4 MB)
#     def combine(self, n: int, k: int):
#         nums = [i+1 for i in range(n)]
#         res = []
#         self.solver(nums, [], res, k)
#         return res
#     def solver(self, nums, path, res, k):
#         if len(path) == k:
#             res.append(path)
#             return
#         else:
#             for i in range(len(nums)):
#                 self.solver(nums[i+1:], path+[nums[i]], res, k)
# ✔ Accepted
#   ✔ 27/27 cases passed (744 ms)
#   ✔ Your runtime beats 12.78 % of python3 submissions
#   ✔ Your memory usage beats 36.67 % of python3 submissions (15.1 MB)
