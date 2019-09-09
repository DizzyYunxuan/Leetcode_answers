#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(t)+1) for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][0] = 1
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if i >= j:
                    if s[i-1] == t[j-1]:
                        dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                    else:
                        dp[i][j] =  dp[i-1][j]       
        return dp[-1][-1]
# ✔ Accepted
#   ✔ 63/63 cases passed (160 ms)
#   ✔ Your runtime beats 45.35 % of python3 submissions
#   ✔ Your memory usage beats 57.14 % of python3 submissions (18.8 MB)
# if __name__ == "__main__":
#     res = Solution().numDistinct('babgbag', 'bag')
