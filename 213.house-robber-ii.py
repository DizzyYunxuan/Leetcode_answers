#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        return max(self.dp(nums[1:]), self.dp(nums[:-1]))

    def dp(self, nums):
        dp = [[0]*2 for _ in range(len(nums))]
        dp[0][0], dp[0][1] = 0, nums[0]
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = max(dp[i-1][0] + nums[i], dp[i-1][1])
        return max(dp[-1])
✔ Accepted
  ✔ 74/74 cases passed (40 ms)
  ✔ Your runtime beats 52.38 % of python3 submissions
  ✔ Your memory usage beats 5.56 % of python3 submissions (13.8 MB)
