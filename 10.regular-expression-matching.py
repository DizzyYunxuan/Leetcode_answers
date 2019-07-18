#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         return self.myMatch(s, len(s)-1, p, len(p)-1)
    
#     def myMatch(self, s, i, p, j):
#         if j < 0:
#             if i < 0:
#                 return True
#             else:
#                 return False
        
#         if p[j] == '*':
#             if i >= 0 and (p[j-1] == '.' or p[j-1] == s[i]):
#                 if self.myMatch(s,i-1,p,j):
#                     return True
#             return self.myMatch(s,i, p, j-2)
        
#         if i>=0 and (p[j] == '.' or p[j] == s[i]):
#             return self.myMatch(s,i-1,p,j-1)
#         return False
        # ✔ Accepted
        #     ✔ 447/447 cases passed (88 ms)
        #     ✔ Your runtime beats 35.54 % of python3 submissions
        #     ✔ Your memory usage beats 27.37 % of python3 submissions (13.3 MB) 


# class Solution:
#     cache = {}
#     def isMatch(self, s, p):
#         if (s, p) in self.cache:
#             return self.cache[(s, p)]
#         if not p:
#             return not s
#         if p[-1] == '*':
#             if self.isMatch(s, p[:-2]):
#                 self.cache[(s, p)] = True
#                 return True
#             if s and (s[-1] == p[-2] or p[-2] == '.') and self.isMatch(s[:-1], p):
#                 self.cache[(s, p)] = True
#                 return True
#         if s and (p[-1] == s[-1] or p[-1] == '.') and self.isMatch(s[:-1], p[:-1]):
#             self.cache[(s, p)] = True
#             return True
#         self.cache[(s, p)] = False
#         return False
#     ✔ Accepted
#         ✔ 447/447 cases passed (44 ms)
#         ✔ Your runtime beats 96.41 % of python3 submissions
#         ✔ Your memory usage beats 5.11 % of python3 submissions (14.3 MB)


# Solution https://www.cnblogs.com/mfrank/p/10472663.html
class Solution:
    def isMatch(self, s, p):
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        dp[0][0] = True
        for i in range(1, len(p)):
            dp[i + 1][0] = dp[i - 1][0] and p[i] == '*'
        for i in range(len(p)):
            for j in range(len(s)):
                if p[i] == '*':
                    dp[i + 1][j + 1] = dp[i - 1][j + 1] or dp[i][j + 1]
                    if p[i - 1] == s[j] or p[i - 1] == '.':
                        dp[i + 1][j + 1] |= dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i][j] and (p[i] == s[j] or p[i] == '.')
        return dp[-1][-1]

    # ✔ Accepted
    #     ✔ 447/447 cases passed (56 ms)
    #     ✔ Your runtime beats 72.62 % of python3 submissions
    #     ✔ Your memory usage beats 34.03 % of python3 submissions (13.3 MB)

if __name__ == '__main__':
    res = Solution().isMatch('aab', 'c*a*b')
    print(res)
