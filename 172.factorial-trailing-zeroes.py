#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#
class Solution:
    def trailingZeroes(self, n: int) -> int:
        r = 0
        while n > 0:
            n //= 5
            r += n
        return r
✔ Accepted
  ✔ 502/502 cases passed (40 ms)
  ✔ Your runtime beats 42.72 % of python3 submissions
  ✔ Your memory usage beats 10 % of python3 submissions (13.9 MB)
