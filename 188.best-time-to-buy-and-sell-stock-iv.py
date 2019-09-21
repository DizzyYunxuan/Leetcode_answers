#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#
class Solution:
    def maxProfit(self, k: int, prices) -> int:
        if not prices or not k:
            return 0
        n = len(prices)

        if k > n//2:
            return self.greedy(prices)

        dp = [[[0]*2 for _ in range(k+1)] for __ in range(n)]
        
        for i in range(k+1):
            dp[0][i][0], dp[0][i][1] = 0, -prices[0]
        
        for i in range(1, n):
            for j in range(k+1):
                if j == 0:
                    dp[i][j][0] = dp[i-1][j][0]
                else:
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j-1][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j][0] - prices[i])
        res = []
        for m in range(k+1):
            res += [dp[n-1][m][0]]
        return max(res)

    def greedy(self, prices):
        res = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                res += prices[i] - prices[i-1]
        return res
✔ Accepted
  ✔ 211/211 cases passed (184 ms)
  ✔ Your runtime beats 5.5 % of python3 submissions
  ✔ Your memory usage beats 16.67 % of python3 submissions (23.6 MB)

# if __name__ == "__main__":
#     test = Solution().maxProfit(2, [3,2,6,5,0,3])

