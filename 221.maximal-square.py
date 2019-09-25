#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        maxsq = 0
        dp = [[0] * (len(matrix[0])+1) for _ in range(len(matrix)+1)]
        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                else:
                    dp[i][j] = 0
                maxsq = max(maxsq, dp[i][j]**2)
        return maxsq
✔ Accepted
  ✔ 68/68 cases passed (224 ms)
  ✔ Your runtime beats 45.09 % of python3 submissions
  ✔ Your memory usage beats 9.09 % of python3 submissions (14.8 MB)

