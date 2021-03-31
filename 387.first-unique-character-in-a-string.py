#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         d = {}
#         for i in range(len(s)):
#             c = s[i]
#             d[c] = d.get(c, []) + [i]
        
#         res = len(s)
#         for k, v in d.items():
#             if len(v) == 1:
#                 res = min(res, v[0])
#         return -1 if res == len(s) else res

# Accepted
# 104/104 cases passed (1632 ms)
# Your runtime beats 6.45 % of python3 submissions
# Your memory usage beats 5 % of python3 submissions (15.2 MB)

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for l in s:
            if l not in d: d[l] = 1
            else: d[l] += 1
        
        index = -1
        for i in range(len(s)):
            if d[s[i]] == 1:
                index = i
                break
        
        return index
Accepted
104/104 cases passed (160 ms)
Your runtime beats 35.28 % of python3 submissions
Your memory usage beats 29.29 % of python3 submissions (14 MB)
# @lc code=end

