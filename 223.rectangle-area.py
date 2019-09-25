#
# @lc app=leetcode id=223 lang=python3
#
# [223] Rectangle Area
#
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        sq = (C - A)*(D - B) + (G - E)*(H - F)
        if E >= C or G <= A or H <= B or F >= D:
            return sq
        else:
            l, r = max(A, E), min(C, G)
            b, t = max(B, F), min(D, H)
            sq -= (r-l)*(t-b)
            return sq
✔ Accepted
  ✔ 3082/3082 cases passed (68 ms)
  ✔ Your runtime beats 28.09 % of python3 submissions
  ✔ Your memory usage beats 12.5 % of python3 submissions (13.9 MB)
