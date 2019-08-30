#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(m+1)] for __ in range(n+1)]
        dp[1][1] = 1
        for i in range(2, n+1):
            dp[i][1] = 1
        for i in range(2, m+1):
            dp[1][i] = 1
        for i in range(2, n+1):
            for j in range(2, m+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
✔ Accepted
  ✔ 62/62 cases passed (32 ms)
  ✔ Your runtime beats 93.93 % of python3 submissions
  ✔ Your memory usage beats 5.77 % of python3 submissions (14 MB)
# if __name__ == "__main__":
#     res = Solution().uniquePaths(7, 3)



