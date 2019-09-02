#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0] * n
        dp[0], dp[1] = 1, 2
        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]
    ✔ Accepted
  ✔ 45/45 cases passed (32 ms)
  ✔ Your runtime beats 89.16 % of python3 submissions
  ✔ Your memory usage beats 5.97 % of python3 submissions (13.8 MB)
# if __name__ == "__main__":
#     res = Solution().climbStairs(6)
