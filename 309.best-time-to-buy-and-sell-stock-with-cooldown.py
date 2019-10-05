#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) < 2:
            return 0

        dp = [[0] * 2 for _ in range(len(prices) + 1)]
        dp[0][0], dp[0][1] = 0, -float('inf')
        for i in range(1, len(prices)+1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i-1])
            if i >= 2:
                dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i-1])
            else:
                dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i-1])
        return dp[-1][0]

Accepted
211/211 cases passed (52 ms)
Your runtime beats 27.87 % of python3 submissions
Your memory usage beats 13.64 % of python3 submissions (14.3 MB)
        
# if __name__ == "__main__":
#     res = Solution().maxProfit([1,2,3,0,2])
# @lc code=end

