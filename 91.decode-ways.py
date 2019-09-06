#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#s
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = dp[1] = 1
        for i in range(2, len(s)+1):
            if 9 < int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
            if int(s[i-1]) > 0:
                dp[i] += dp[i-1]
        return dp[-1]
✔ Accepted
  ✔ 258/258 cases passed (40 ms)
  ✔ Your runtime beats 63.89 % of python3 submissions
  ✔ Your memory usage beats 16 % of python3 submissions (13.8 MB)
# if __name__ == "__main__":
#     res = Solution().numDecodings('12')

