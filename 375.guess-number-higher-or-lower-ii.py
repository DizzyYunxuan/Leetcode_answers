#
# @lc app=leetcode id=375 lang=python3
#
# [375] Guess Number Higher or Lower II
#

# @lc code=start
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n+1) for i in range(n+1)] 
        
        for window in range(2, n + 1):
            for start in range(1, n - window + 2):
                minres = float('inf')
                for piv in range(start + (window - 1) // 2, start + window - 1):
                    res = piv + max(dp[start][piv-1], dp[piv+1][start + window - 1])
                    minres = min(res, minres)
                dp[start][start + window - 1] = minres
        
        return dp[1][n]

Accepted
13/13 cases passed (412 ms)
Your runtime beats 85.15 % of python3 submissions
Your memory usage beats 100 % of python3 submissions (13.3 MB)
# if __name__ == "__main__":

#     res = Solution().getMoneyAmount(5)

# @lc code=end

