#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
class Solution:
    def minPathSum(self, grid) -> int:
        h, w = len(grid), len(grid[0])
        dp = [[0 for i in range(w+1)] for j in range(h+1)]
        dp[1][1] = grid[0][0]
        for i in range(2, h+1):
            dp[i][1] += dp[i-1][1] + grid[i-1][0]
        for i in range(2, w+1):
            dp[1][i] += dp[1][i-1] + grid[0][i-1]
        for i in range(2, h+1):
            for j in range(2, w+1):
                dp[i][j] += min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]
        return dp[-1][-1]
✔ Accepted
  ✔ 61/61 cases passed (116 ms)
  ✔ Your runtime beats 50.88 % of python3 submissions
  ✔ Your memory usage beats 22.81 % of python3 submissions (15.3 MB)
# if __name__ == "__main__":
#     a = [[1,2,5],[3,2,1]]
#     res = Solution().minPathSum(a)


