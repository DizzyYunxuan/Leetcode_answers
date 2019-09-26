#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#
class Solution:
    def isPowerOfTwo(self, n):
        return (n>0) and (n & (n-1))==0
✔ Accepted
  ✔ 1108/1108 cases passed (32 ms)
  ✔ Your runtime beats 95.44 % of python3 submissions
  ✔ Your memory usage beats 9.52 % of python3 submissions (14.1 MB)
    
#     def isPowerOfTwo(self, n: int) -> bool:
#         p, res = 0, 1
#         while res < n:
#             res = 2**p
#             p += 1
#         return res == n
# ✔ Accepted
#   ✔ 1108/1108 cases passed (40 ms)
#   ✔ Your runtime beats 57.95 % of python3 submissions
#   ✔ Your memory usage beats 9.52 % of python3 submissions (13.6 MB)
