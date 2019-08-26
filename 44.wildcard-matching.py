#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not s or not p:
            return False
        dp = [[0] * len(s) for _ in p]
        if p[0] == '?' or p[0] == s[0]:
            dp[0][0] = 1
        elif p[0] == '*':
            for i in range(len(s)):
                dp[0][i] = 1
        
        for i in range(1, len(p)):
            if p[i] == s[0] and p[i-1] == '*':
                dp[i][0] = dp[i-1][0]
            if p[i] == '*':
                dp[i][0] = dp[i-1][0]

        for i in range(1, len(p)):
            for j in range(1, len(s)):
                if p[i] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                elif p[i-1] == '*' and (p[i] == s[j] or p[i] == '?'):
                    dp[i][j] = dp[i-1][j]
                elif p[i] == s[j] or p[i] == '?':
                    dp[i][j] = dp[i-1][j-1]

        return dp[-1][-1]

# if __name__ == "__main__":
#     # res = Solution().isMatch('adceb', '*a*b')
#     # res = Solution().isMatch('aa', '*')
#     # res = Solution().isMatch('acdcb', 'a*c?b')
#     # res = Solution().isMatch('aab', 'c*a*b')
#     res = Solution().isMatch('abefcdgiescdfimde', 'ab*cd?i*de')
