#
# @lc app=leetcode id=132 lang=python3
#
# [132] Palindrome Partitioning II
#
class Solution:
    def minCut(self, s: str) -> int:
        if s == s[::-1]: return 0
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        dp = [0] * (len(s)+1)
        dp[0] = -1
        for i in range(1, len(s)+1):
            curmin = dp[i-1]
            for j in range(1, i):
                if s[i-j-1:i] == s[i-j-1:i][::-1]:
                    curmin = min(curmin, dp[i-j-1])
            dp[i] = curmin+1
        return dp[-1]
✔ Accepted
  ✔ 29/29 cases passed (156 ms)
  ✔ Your runtime beats 87.75 % of python3 submissions
  ✔ Your memory usage beats 90 % of python3 submissions (13.7 MB)
# if __name__ == "__main__":
#     res = Solution().minCut('abcdcba')
