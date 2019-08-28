#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
class Solution:
    def solveNQueens(self, n: int):
        res = []
        self.solver(n, [], res, [], [])
        return [['.'*i +'Q'+'.'*(n-i-1) for i in col] for col in res]

    def solver(self, n, queens,  res, xy_sum, xy_sub):
        p = len(queens)
        if p == n:
            res.append(queens)
            return
        for q in range(n):
            if q not in queens and p-q not in xy_sub and p+q not in xy_sum:
                    self.solver(n, queens+[q], res, xy_sum+[p+q], xy_sub+[p-q])
        
✔ Accepted
  ✔ 9/9 cases passed (56 ms)
  ✔ Your runtime beats 96.87 % of python3 submissions
  ✔ Your memory usage beats 5 % of python3 submissions (13.9 MB)
# if __name__ == "__main__":
#     # board = []
#     # for _ in range(4):
#     #     board.append('.' * 4)
#     # board[0] = '...Q'
#     # test = Solution().isOK(4, board, [1, 2])
#     res = Solution().solveNQueens(4)
#     print(res)
