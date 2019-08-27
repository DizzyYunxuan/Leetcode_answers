#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[0] * (len(s)+1) for _ in range(len(p)+1)]
        dp[0][0] = 1
        for i in range(1, len(p)+1):
            if p[i-1] == '*':
                dp[i][0] = dp[i-1][0]
            
        for i in range(1, len(p)+1):
            for j in range(1, len(s)+1):
                if p[i-1] == '*':
                    dp[i][j] = dp[i][j-1] | dp[i-1][j]
                elif p[i-1] == s[j-1] or p[i-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]
✔ Accepted
  ✔ 1809/1809 cases passed (788 ms)
  ✔ Your runtime beats 50.83 % of python3 submissions
  ✔ Your memory usage beats 50 % of python3 submissions (22 MB)
# if __name__ == "__main__":
#     # res = Solution().isMatch('adceb', '*a*b')
#     res = Solution().isMatch('aa', '*')
#     # res = Solution().isMatch('acdcb', 'a*c?b')
#     # res = Solution().isMatch('aab', 'c*a*b')
#     # res = Solution().isMatch('abefcdgiescdfimde', 'ab*cd?i*de')
#     # res = Solution().isMatch('mississippi', 'm??*ss*?i*pi')
