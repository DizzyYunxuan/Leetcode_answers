#
# @lc app=leetcode id=292 lang=python3
#
# [292] Nim Game
#
class Solution:
    def canWinNim(self, n: int) -> bool:
        return False if not n % 4 else True 
✔ Accepted
  ✔ 60/60 cases passed (36 ms)
  ✔ Your runtime beats 62.64 % of python3 submissions
  ✔ Your memory usage beats 14.29 % of python3 submissions (13.8 MB)
