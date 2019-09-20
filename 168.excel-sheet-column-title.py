#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#
class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ''
        while n >= 1:
            cur = (n-1) % 26
            res = chr(65+cur) + res
            n = (n - 1) // 26
        return res
✔ Accepted
  ✔ 18/18 cases passed (40 ms)
  ✔ Your runtime beats 20.5 % of python3 submissions
  ✔ Your memory usage beats 6.25 % of python3 submissions (13.7 MB)
