#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [[0]*2 for _ in range(len(nums)+1)]
        for i in range(1, len(nums)+1):
            for j in range(2):
                if j == 0:
                    dp[i][j] = max(dp[i-1][0], dp[i-1][1])
                else:
                    dp[i][j] = dp[i-1][0]+nums[i-1]
        return max(dp[-1])
✔ Accepted
  ✔ 69/69 cases passed (32 ms)
  ✔ Your runtime beats 95.42 % of python3 submissions
  ✔ Your memory usage beats 9.09 % of python3 submissions (13.7 MB)
