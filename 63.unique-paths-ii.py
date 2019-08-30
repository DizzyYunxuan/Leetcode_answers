#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        dp = [[0 for _ in range(m+1)] for __ in range(n+1)]
        if obstacleGrid[0][0] != 1:
            dp[1][1] = 1
        for i in range(2, m+1):
            if obstacleGrid[0][i-1] != 1:
                dp[1][i] = dp[1][i-1] + dp[0][i]
        for i in range(2, n+1):
            if obstacleGrid[i-1][0] != 1:
                dp[i][1] = dp[i-1][1] + dp[i][0]
        for i in range(2, n+1):
            for j in range(2, m+1):
                if obstacleGrid[i-1][j-1] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
✔ Accepted
  ✔ 43/43 cases passed (56 ms)
  ✔ Your runtime beats 58.69 % of python3 submissions
  ✔ Your memory usage beats 8.89 % of python3 submissions (13.9 MB)
# if __name__ == "__main__":
# #     obstacleGrid = \
# # [
# #   [0,0,0],
# #   [0,1,0],
# #   [0,0,0]
# # ]
#     obstacleGrid = [[1,0]]
#     res = Solution().uniquePathsWithObstacles(obstacleGrid)
