#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(n+1):
            dp[0][i] = i
        for j in range(m+1):
            dp[j][0] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        return dp[-1][-1]
# ✔ Accepted
#   ✔ 1146/1146 cases passed (176 ms)
#   ✔ Your runtime beats 72.33 % of python3 submissions
#   ✔ Your memory usage beats 15.38 % of python3 submissions (17.5 MB)
if __name__ == "__main__":
    res = Solution().minDistance('FreshMeat', 'FishAndMeat')      

