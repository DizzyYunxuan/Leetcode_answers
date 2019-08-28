#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#
class Solution:
    def totalNQueens(self, n: int) -> int:
        res = []
        self.solver(n, [], res, [], [])
        return len(res)

    def solver(self, n, queens,  res, xy_sum, xy_sub):
        p = len(queens)
        if p == n:
            res.append(queens)
            return
        for q in range(n):
            if q not in queens and p-q not in xy_sub and p+q not in xy_sum:
                    self.solver(n, queens+[q], res, xy_sum+[p+q], xy_sub+[p-q])
        
✔ Accepted
  ✔ 9/9 cases passed (48 ms)
  ✔ Your runtime beats 93.69 % of python3 submissions
  ✔ Your memory usage beats 7.69 % of python3 submissions (13.8 MB)
